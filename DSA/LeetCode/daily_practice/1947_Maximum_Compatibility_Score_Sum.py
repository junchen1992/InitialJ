class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        self.max_score = 0
        self.scores = self.pre_compute_score(students, mentors)
        self.back_tracking(students, mentors, set(range(len(students))), [None] * len(students), 0)
        
        return self.max_score
        
    def back_tracking(self, students, mentors, mentors_set, cur_idxes, start_index):
        """Generate permutations of indices of mentors."""
        m = len(students)
        
        if start_index == m:
            self.max_score = max(self.max_score, self.compute_score(students, mentors, cur_idxes))
        else:
            for nxt_mentor_idx in mentors_set:
                cur_idxes[start_index] = nxt_mentor_idx
                self.back_tracking(students, mentors, mentors_set - {nxt_mentor_idx}, cur_idxes, start_index + 1)
                cur_idxes[start_index] = None
            
        
    def compute_score(self, students, mentors, mentors_indices):
        """Compute the compatibility score for an arrangement of students and mentors."""
        m = len(students)
        n = len(students[0])
            
        return sum([self.scores[idx, mentors_indices[idx]] for idx in range(m)])
    
    def pre_compute_score(self, students, mentors):
        m = len(students)
        n = len(students[0])
        scores = {}
        for s_idx in range(m):
            for m_idx in range(m):
                score = sum([students[s_idx][ans_idx] == mentors[m_idx][ans_idx] for ans_idx in range(n)])
                scores[(s_idx, m_idx)] = score
                
        return scores
