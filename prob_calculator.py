
import random
import copy

#CLASS


class Hat :

    def __init__(self,**contents):

        self.contents = contents
        
        contents_list = []

        for color, count in self.contents.items():
            contents_list.extend([color]*count)

        self.contents = contents_list


    def draw (self,nb_draw):
        
        if len(self.contents) < nb_draw :
            return self.contents

        else:
            
            timer_draw = 1
            draw_list = []
            
            while timer_draw <= nb_draw :

                draw_choice = random.choice(self.contents)
                idraw_choice=self.contents.index(draw_choice)
                
                draw_list.append(draw_choice)
                del self.contents [idraw_choice]

                timer_draw += 1

            return draw_list


# Experiment

def experiment(hat,expected_balls,num_balls_drawn,num_experiments) :

    count_experiment = 0

    for i in range(num_experiments) :
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)

        expected_balls_draw = all(balls_drawn.count(ball) >= count for ball, count in expected_balls.items())

        if expected_balls_draw :
            count_experiment += 1
    

    proba_experiments = count_experiment / num_experiments

    return proba_experiments

