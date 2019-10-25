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

   - Description: Today we will introduce Dirac notation and show how the matrix representation emerges.  We will modify our infinite square well potential to have a "bump" in the bottom of the well and then use the ideal well eigenfunctions as a basis to solve this problem.  Mathematica will be used.

   - Homework: [here][day_4_hw]


## Day 5 (Wednesday September 25)

   - Reading: Sutton pgs 10-17 (section on hydrogen atom)

   - Description: Review day.  Last time we worked on a Mathematica notebook together and used a new method (basis expansion) to solve Schrodinger's equation.  For the first part of today, we'll let you breathe and catch up, making sure you understand what we did last time and to feel prepared to move forward.  If we have time, we'll solve Schroding'er equation for the one-dimensional Hydrogen atom using a plane wave basis.
 
   - Homework: [here][day_5_hw]


## Day 6 (Friday September 27)

   - Reading: Sutton Chapter 2 section entitled "A homonuclear diatomic molecule: the hydrogen atom"

   - Description: Today we will step through the analytic solution to Schrodinger's equation for the diatomic molecule.  Then we will solve the problem numerically and see that the solutions match.

   - Homework: None 

## Day 7 (Monday September 30)

   - Reading: None

   - Description: The code we wrote together last time was challenging for some students.  Let's take today and make sure we understand everything that we did.  Once we do understand everything, work on the homework problems.

   - Homework: [here][day_6_hw]

## Day 8 (Wednesday October 2)

   - Reading: Sutton Chapter 2, section entitled "Heteronuclear diatomic molecule"

   - Description: Today we will finish up our discussion of the homonuclear diatomic nuclear, talking about the time dependence of the coefficients.  The idea of a "hopping integral" emerges.  Then we will discuss the heteronuclear diatomic molecule and give time to work on the homework assignment.  Specifically, students will be given time to "fill in the details" on the heteronuclear solution.

   - Homework: [here][day_8_hw]

## Day 9 (Friday October 4)

   - Reading: Sutton Chapter 3, section entitled "Chain molecules and k-space"

   - Description: Today we will step through the mathematical derivation of the finite linear chain to see what the coefficients look like.  Then students will be given time to work on their homework.  The homework today asks them to modify their diatomic molecule code to consider any number of identical, even-spaced atoms in a chain.  Begin to see energy bands emerge.

   - Homework: [here][day_9_hw]

## Day 10 (Monday October 7)

   - Reading: Sutton Chapter 3, section entitled "Chain molecules and k-space".  Reread if necessary, but we will pick up on page 44 where we do the infinite chain and discover bloch functions.

   - Description: Extend the finite linear chain to an infinite linear chain and see what the coefficients look like.  Then talk about bloch functions.

   - Homework: None

## Day 11 (Wednesday October 9)

   - Reading: Reread Sutton chapter 3 up through page 55. Also read through the derivation located [here][bloch_atomic_basis].

   - Description: Today we will continue building our code for modeling an infinite linear chain of atoms using a 1s,2s atomic orbital basis.  Our goal is to understand energy bands, Brillioun zones, and k-space.

   - Homework: [here][day_11_hw]

## Day 12 (Friday October 11)

   - Reading: Stokes section 1.1 - 1.8

   - Description: Lattices and Unit cells is the topic

   - Homework: Stokes problems 1.1,1.3,1.4,1.7

## Day 13 (Monday October 14)

   - Reading: Stokes sections 1.9 - 1.12

   - Description: Crystal Structure

   - Homework: Stokes problems 1.14, 1.15,1.16, 1.18


## Day 14 (Wednesday October 16)

   - Reading: Stokes sections 1.13 - 1.16

   - Description: Symmetry

   - Homework: Stokes problems 1.21, 1.22, 1.24

## Day 15 (Friday October 18)

   - Reading: Stokes sections 1.17 - 1.20

   - Description: Symmetry part II, Bonding

   - Homework: Stokes problems 1.26, 1.29, 1.30

## Day 16 (Monday October 21)

   - Reading: Stokes sections 2.1 - 2.7

   - Description: X-Ray diffraction.  Note: Section 1-3 should be very familiar to you and only needs a brief skim.  2.4-2.7 is where you should focus your attention

   - Homework: Stokes problems 2.7,2.10, 2.12, 2.14

## Day 17 (Wednesday October 23)

   - Reading: Stokes sections 2.8 - 2.9

   - Description: X-ray diffraction in real crystals

   - Homework: Stokes problems 2.17,2.18

## Day 18 (Friday October 25)

   - Reading: Re-read Stokes sections 2.8 - 2.9

   - Description: X-ray diffraction in real crystals

   - Homework: No new

## Day 19 (Monday October 28)

   - Reading: Stokes Sections 3.1-3.3

   - Description: Lattice Vibrations: One-D monatomic lattice

   - Homework: 3.3


[griffiths_chp_1]: https://content.byui.edu/file/51c6f2c7-d1f2-4716-9674-c3bc2de5a273/1/Intro%20to%20Quantum%20Mechanics%20Chapter%201.pdf
[griffiths_chp_2]: https://content.byui.edu/file/51c6f2c7-d1f2-4716-9674-c3bc2de5a273/1/Intro%20to%20Quantum%20Mechanics%20Chapter%202.pdf
[day_1_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day1.pdf
[day_2_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day2.pdf
[day_3_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day3.pdf
[day_4_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day4.pdf
[day_5_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/quantumReview.pdf

[day_6_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day6.pdf
[day_8_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day8.pdf
[day_9_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day9.pdf
[day_11_hw]: https://lancejnelson.github.io/PH323/course_docs/homework/day11.pdf
[bloch_atomic_basis]: https://lancejnelson.github.io/PH323/course_docs/bloch_atomic_orbital_expansion.pdf
