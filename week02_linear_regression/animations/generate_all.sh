#!/bin/bash
# Script to generate all animations for Week 2

echo "Generating gradient descent animations..."
manim -pqh gradient_descent.py GradientDescentAnimation
manim -pqh gradient_descent.py ResidualsVisualization
manim -pqh gradient_descent.py GeometricInterpretation
manim -pqh gradient_descent.py QuadraticCostFunction3D

echo "All animations generated!"
echo "Videos are located in: animations/media/videos/"
