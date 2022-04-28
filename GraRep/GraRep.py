from BaseAlgorithm import BaseAlgorithm


class GraRep(BaseAlgorithm):
    """
    Main class for GraRep algorithm model.
    """

    def __init__(self,
                 max_transition_step: int):
        """
        GraRep constructor
        @param max_transition_step: Maximum number of steps to collect structural data
         """
        self.K = max_transition_step
        super().__init__()

    def create_embedding(self):
        """
        Creates embedding from a graph based on GraRep algorithm
        """
