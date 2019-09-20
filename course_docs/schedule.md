---
title: Schedule
keywords: documentation theme, jekyll, technical writers, help authoring tools, hat replacements
last_updated: August 26, 2019
#tags: [course_docs]
summary: "The schedule for this semester."
sidebar: mydoc_sidebar
permalink: schedule.html
folder: course_docs
---

Below you will find a description for each day of the semester.  

Note: For the first few days (probably into the second week) of the semester, we will be having a review/summary of the main concepts in Quantum Mechanics.  I will provide some suggestions for reading for these days, but you are encouraged to look at the topic and search out your own reading material on that topic.  Quantum Mechanics is not that challenging.  Don't let the name psyche you out... you can do this.
  
## Day 1 (Monday September 16)
   - Topic:  After the course overview/introductions we will have a short discussion on the history of quantum mechanics, what a wave-function is, it's stastical interpretation, and how to normalize it.  We'll also discuss how to find average values(typically called expectation values in quantum mechanics) from the wavefunction.

   - Suggested Reading: Griffiths [1.1 - 1.4][griffiths_chp_1]
   - Additional/Alternative suggestions for reading:  
     - Liboff pg 55 - 56 (If you have already taken Quantum, you should have the Liboff text)
     - Your modern physics textbook covers this topic.
     - Use Google.  There is plenty of reading out there on this topic.

   - Homework: [here][day_1_hw]

## Day 2 (Wednesday September 18)  

   - Topic:  Today we will discuss all but the last postulate of quantum mechanics.  The idea that every observable has a corresponding operator in QM will be discussed.    Expectation values will be defined and examples will be given so you can see how to calculate them. 
   - Reading: Griffiths [1.5,1.6][griffiths_chp_1]
   - Alternative/Supplemental reading: Liboff ch 3.1 - 3.4

   - Description (instructor notes): The main postulates of quantum mechanics are:
     1. **The state of a quantum mechanical system is completely specified by the wavefunction.**  We learned a little about the wavefunction last time, but we still might not be completely certain how it can possibly contain all of the information we could ever ask for.
     2. **For every observable in classical physics (position, momentum, energy, etc.) there exists a linear, Hermitian operator in quantum mechanics.**  We'll see examples of the momentum operator and kinetic energy operator and maybe even the total energy operator for some simple choice of potential.  P
     3. **Measurement of the observable corresponding to operator A will only yield a_i, where a_i are the eigenvalues associated with opertor A.**  Also, this measurement causes a change in the state of the particle to the eigenstate corresponding to the measured eigenvalue.
     4. **The average (aka expectation) value of any physical observales is set forth.**  Should have already seen this with position, but to get to anything other than position, we have a little calculus to do.  Griffiths does a good job of deriving it.  In the end, the result is simple, the expectation value of any opertor is <n\|A\|n>, where n is the state and A is the operator.
     5. **The wavefunction evolves in time according the the time-dependent Schrodinger equation.**  Here we should show the separable solution to the time-**dependent** Schrodinger equation.  Then we should go back to the solution to the time-**independent** Schrodinger equation and show how we can time evolve the wavefunction.

     Note:  This day may end up spilling over into the next.

   - Homework: [here][day_2_hw]


## Day 3 (Friday September 20)
   - Topic: Properties of Eigenfunctions, Superposition, Basis Sets, Completeness, Orthonormality.

   - Reading: Griffiths  2.1 - 2.3
   - Alternative/Supplemental reading: Krane 4.5

   - Description: So far we have learned what the wavefunctin is, how to normalize it, and how to calculate expectation values for any observable.  Today we will solve the time-independent Schrodinger equation and discuss the unique properties that these functions possess.  The homework problems have been carefully selected to help you see the critical principles in action.  We will also discuss the time evolution of the wavefunction.

   - Homework: [here][day_3_hw]


## Day 4 (Monday September 23)

   - Topic: Dirac Notation, Matrix Representation of Operator
   - Reading: Griffiths  3.6
   - Alternative/Supplemental reading: Sutton 2.1 (Section entitled "Reviews of bras, kets, and all that.")

   - Description: Today we will introduce Dirac notation and show how the matrix representation emerges.  We will modify our infinite square well potential to have a "bump" in the bottom of the well and then use the ideal well eigenfunctions as a basis to solve this problem.

   - Homework: [here][day_4_hw]


## Day 5 (Wednesday September 25)

   - Reading: Krane 7.3 (Review of Hydrogen Atom) and Sutton 2.1 ("A homonuclear diatomic molecule: the hydrogen molecule.")

   - Description: Diatomic molecule.  Discuss the analytical treatment from Sutton.  Solve computationally using plane wave basis.

   - Class Time:  We will have some discussion about the math used in this section and then we will work on a numerical solution to this problem.

## Day 6 (Wednesday September 25)

   - Reading: Krane 7.3 (Review of Hydrogen Atom) and Sutton 2.1 ("A homonuclear diatomic molecule: the hydrogen molecule.")

   - Description: Time-development of hydrogen molecule.  Analytical treatment.

   - Class Time:  We will have some discussion about the math used in this section and then we will work on a numerical solution to this problem.





[griffiths_chp_1]: https://content.byui.edu/file/51c6f2c7-d1f2-4716-9674-c3bc2de5a273/1/Intro%20to%20Quantum%20Mechanics%20Chapter%201.pdf
[griffiths_chp_2]: https://content.byui.edu/file/51c6f2c7-d1f2-4716-9674-c3bc2de5a273/1/Intro%20to%20Quantum%20Mechanics%20Chapter%202.pdf
[day_1_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day1.pdf
[day_2_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day2.pdf
[day_3_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day3.pdf
[day_4_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day4.pdf