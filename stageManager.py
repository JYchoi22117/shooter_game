
class StageManager:
    """Stage Manager : Manages stages and stores them"""
    def __init__(self, stages=[]): 
        self.stages = stages
        if len(self.stages) == 0:
            self.active = None
        else:
            self.active = self.stages[0]

        self.stage_names = []

    def append(self, stage, name):
        self.stages.append(stage)
        self.stage_names.append(name)

        if len(self.stages) == 1:
            self.active = self.stages[0]

    def get_stage_by_name(self, name):
        return self.stages[self.stage_names.index(name)]


