from ps9pr3 import *
import random  


class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        indices = []
        max_score = scores[0]

        for i in range(len(scores)):
            if scores[i] > max_score:
                indices = [i]
                max_score = scores[i]
            elif scores[i] == max_score:
                indices += [i]
        
        if self.tiebreak == 'LEFT':
            return indices[0]
        elif self.tiebreak == 'RIGHT':
            return indices[-1]
        else:
            return random.choice(indices)
    
    def scores_for(self, b):
        scores = [50] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker):
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opponent_scores = opponent.scores_for(b)
                if max(opponent_scores) == 100:
                    scores[col] = 0
                elif max(opponent_scores) == 0:
                    scores[col] = 100
                elif max(opponent_scores) == 50:
                    scores[col] = 50
                
                b.remove_checker(col)
        
        return scores
    
    def next_move(self, b):
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
        