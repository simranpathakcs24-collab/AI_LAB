import random
import time

class CombinedVacuumAgent:
    def __init__(self,totalrooms):
        self.goalstate={rooms: 'clean' for rooms in totalrooms}
        self.model={rooms:"unkonown" for rooms in totalrooms}
    def act(self,location,status):
        self.model[location]=status
        if status=="Dirty":
            return "Suck"
        if self.model== self.goalstate:
            return "Shutdown"
        for room, roomstatus in self.model.items():
            if roomstatus != "Clean":
                if room=='B' and location =='A':
                    return "right"
                else: 
                    return "left"
        return "Shutdown"

def vacuum():
    totalrooms=['A','B']
    environment={'A':"Clean", 'B':"Dirty"}
    agent=CombinedVacuumAgent(totalrooms)
    agentlocation='A'
    step=1
    while True:
        print(f"step {step}")
        status=environment[agentlocation]
        action=agent.act(agentlocation,status)
        if action=="Suck":
            environment[agentlocation]='Clean'
            print("room cleaned")
        elif action == "right":
            agentlocation='B'
            print("travelled to b")
        elif action== "left":
            agentlocation ='A'
            print("travelled to a")
        elif action== "Shutdown":
            print("goal reached")   
            break
        step+=1
    
vacuum()   

