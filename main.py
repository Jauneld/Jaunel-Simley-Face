#Jaunel Deans
#October 6, 2023

import simpleplot
import matplotlib
leftEye = [(-4,5), (-6,4), (-6,1),(-4,0),(-2,1),(-2,4),(-4,5)]
leftIris = [(-4,0),(-2,1),(-2,2.5),(-4,2.5),(-4,0)]
leftPupil = [(-2.5,2),(-3.25,2),(-3.25,1),(-2.5,1.25),(-2.5,2)]
rightEye = [(4,5), (6,4), (6,1),(4,0),(2,1),(2,4),(4,5)]
rightIris = [(4,0),(6,1),(6,2.5),(4,2.5),(4,0)]
rightPupil = [(5.5,2),(5.5,1.25),(4.75,1),(4.75,2),(5.5,2)]
mouth = [(-5,-3),(0,-4),(5,-3),(4,-5),(3,-6),(-3,-6),(-4,-5),(-5,-3)]
headOutline = [(0,8) , (-8,6), (-8,-6), (0,-8), (8,-6),(8,6),(0,8)]
simpleplot.plot_lines("Simley Face",300,300,"World","Hello",[headOutline,mouth,leftEye,leftIris,leftPupil,rightEye,rightIris,rightPupil,],True,["Head Outline","Mouth","Left Eye","Left Iris","Left Pupil","Right Eye", "Right Iris","Right Pupil"])
