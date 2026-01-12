"""
Manim animation: Gradient Descent for Linear Regression
Visualizes how gradient descent finds optimal parameters for a linear model
"""

from manim import *
import numpy as np


class GradientDescentAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Gradient Descent: Finding Optimal Parameters", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Create axes for cost function (2D view: one parameter vs cost)
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 10, 2],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True, "include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT},
        ).shift(DOWN * 0.5)

        # Labels
        x_label = MathTex(r"\beta", font_size=40).next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"\text{RSS}(\beta)", font_size=40).next_to(axes.y_axis, UP)

        # Cost function (quadratic)
        cost_function = axes.plot(lambda x: 0.5 * x**2 + 1, color=BLUE, x_range=[-3, 3])

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(cost_function))
        self.wait()

        # Starting point
        beta_0 = 2.5
        learning_rate = 0.3

        # Animate gradient descent steps
        current_beta = beta_0
        dot = Dot(
            axes.c2p(current_beta, 0.5 * current_beta**2 + 1), color=RED, radius=0.12
        )
        self.play(FadeIn(dot))

        # Show gradient line
        gradient_text = MathTex(r"\nabla_\beta \text{RSS}", font_size=36, color=YELLOW)
        gradient_text.to_corner(UR)
        self.play(Write(gradient_text))

        # Perform gradient descent steps
        for step in range(8):
            gradient = current_beta  # Derivative of 0.5*x^2
            new_beta = current_beta - learning_rate * gradient

            # Draw tangent line (gradient)
            tangent_start = axes.c2p(
                current_beta - 0.3, 0.5 * current_beta**2 + 1 - 0.3 * gradient
            )
            tangent_end = axes.c2p(
                current_beta + 0.3, 0.5 * current_beta**2 + 1 + 0.3 * gradient
            )
            tangent_line = Line(
                tangent_start, tangent_end, color=YELLOW, stroke_width=3
            )

            # Show step
            arrow = Arrow(
                axes.c2p(current_beta, 0.5 * current_beta**2 + 1),
                axes.c2p(new_beta, 0.5 * new_beta**2 + 1),
                color=GREEN,
                buff=0.1,
                stroke_width=4,
            )

            self.play(Create(tangent_line), run_time=0.5)
            self.play(
                GrowArrow(arrow),
                dot.animate.move_to(axes.c2p(new_beta, 0.5 * new_beta**2 + 1)),
                run_time=0.8,
            )
            self.play(FadeOut(tangent_line), FadeOut(arrow), run_time=0.3)

            current_beta = new_beta

            if abs(current_beta) < 0.1:
                break

        # Highlight convergence
        optimal_text = MathTex(r"\beta^* \approx 0", font_size=40, color=GREEN)
        optimal_text.next_to(dot, DOWN)
        self.play(Write(optimal_text))

        # Final result box
        result = VGroup(
            Text("Converged to minimum!", font_size=32, color=GREEN),
            MathTex(r"\text{RSS}(\beta^*) \approx 1", font_size=32),
        ).arrange(DOWN)
        result.to_corner(DR)

        self.play(FadeIn(result))
        self.wait(2)


class ResidualsVisualization(Scene):
    def construct(self):
        # Title
        title = Text("Residuals: Minimizing Squared Errors", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Create data points
        np.random.seed(42)
        x_data = np.linspace(0, 4, 8)
        y_data = 2 + 1.5 * x_data + np.random.normal(0, 0.8, 8)

        # Create axes
        axes = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 10, 2],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5)

        x_label = MathTex(r"x", font_size=40).next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"y", font_size=40).next_to(axes.y_axis, UP)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Plot data points
        dots = VGroup(
            *[
                Dot(axes.c2p(x_data[i], y_data[i]), color=BLUE, radius=0.08)
                for i in range(len(x_data))
            ]
        )
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.1))
        self.wait()

        # Initial bad line
        bad_line = axes.plot(lambda x: 3 + 0.8 * x, color=RED, x_range=[0, 4.5])
        bad_label = MathTex(r"\text{Poor fit}", font_size=28, color=RED).next_to(
            bad_line, UP
        )

        self.play(Create(bad_line), Write(bad_label))

        # Draw residuals for bad line
        residual_lines = VGroup(
            *[
                DashedLine(
                    axes.c2p(x_data[i], y_data[i]),
                    axes.c2p(x_data[i], 3 + 0.8 * x_data[i]),
                    color=RED,
                    stroke_width=2,
                )
                for i in range(len(x_data))
            ]
        )

        self.play(LaggedStartMap(Create, residual_lines, lag_ratio=0.1))

        # Show RSS
        rss_bad = sum(
            (y_data[i] - (3 + 0.8 * x_data[i])) ** 2 for i in range(len(x_data))
        )
        rss_text_bad = MathTex(
            r"\text{RSS} = ", f"{rss_bad:.2f}", font_size=32, color=RED
        ).to_corner(UR)
        self.play(Write(rss_text_bad))
        self.wait()

        # Transform to optimal line
        optimal_line = axes.plot(lambda x: 2 + 1.5 * x, color=GREEN, x_range=[0, 4.5])
        optimal_label = MathTex(
            r"\text{Optimal fit}", font_size=28, color=GREEN
        ).next_to(optimal_line, UP)

        # New residuals
        residual_lines_new = VGroup(
            *[
                DashedLine(
                    axes.c2p(x_data[i], y_data[i]),
                    axes.c2p(x_data[i], 2 + 1.5 * x_data[i]),
                    color=GREEN,
                    stroke_width=2,
                )
                for i in range(len(x_data))
            ]
        )

        rss_optimal = sum(
            (y_data[i] - (2 + 1.5 * x_data[i])) ** 2 for i in range(len(x_data))
        )
        rss_text_optimal = MathTex(
            r"\text{RSS} = ", f"{rss_optimal:.2f}", font_size=32, color=GREEN
        ).to_corner(UR)

        self.play(
            Transform(bad_line, optimal_line),
            Transform(bad_label, optimal_label),
            Transform(residual_lines, residual_lines_new),
            Transform(rss_text_bad, rss_text_optimal),
        )
        self.wait(2)

        # Highlight minimum
        conclusion = Text("Least Squares = Minimum RSS", font_size=32, color=YELLOW)
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)


class GeometricInterpretation(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Interpretation: Projection", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Create 3D-like axes
        axes = ThreeDAxes(
            x_range=[-1, 3, 1],
            y_range=[-1, 3, 1],
            z_range=[-1, 3, 1],
            x_length=5,
            y_length=5,
            z_length=5,
        )

        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)

        self.play(Create(axes))

        # Column space (plane)
        plane = Surface(
            lambda u, v: axes.c2p(u, v, 0.5 * u + 0.3 * v),
            u_range=[-1, 2],
            v_range=[-1, 2],
            resolution=(10, 10),
            fill_opacity=0.3,
            fill_color=BLUE,
        )

        plane_label = MathTex(r"\text{col}(\mathbf{X})", font_size=36, color=BLUE)
        plane_label.to_corner(UL)

        self.play(Create(plane), Write(plane_label))
        self.wait()

        # Vector y (target)
        y_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(1.5, 1.5, 2),
            color=RED,
            thickness=0.03,
        )
        y_label = MathTex(r"\mathbf{y}", font_size=40, color=RED)
        y_label.to_corner(UR)

        self.play(Create(y_vector), Write(y_label))
        self.wait()

        # Projection (ŷ)
        y_hat_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(1.5, 1.5, 1.05),
            color=GREEN,
            thickness=0.03,
        )
        y_hat_label = MathTex(r"\hat{\mathbf{y}}", font_size=40, color=GREEN)
        y_hat_label.next_to(y_label, DOWN)

        self.play(Create(y_hat_vector), Write(y_hat_label))
        self.wait()

        # Residual (perpendicular)
        residual_vector = Arrow3D(
            start=axes.c2p(1.5, 1.5, 1.05),
            end=axes.c2p(1.5, 1.5, 2),
            color=YELLOW,
            thickness=0.03,
        )
        residual_label = MathTex(
            r"\mathbf{y} - \hat{\mathbf{y}}", font_size=36, color=YELLOW
        )
        residual_label.next_to(y_hat_label, DOWN)

        self.play(Create(residual_vector), Write(residual_label))
        self.wait()

        # Emphasize orthogonality
        ortho_text = MathTex(
            r"\mathbf{X}^T(\mathbf{y} - \hat{\mathbf{y}}) = \mathbf{0}", font_size=32
        ).to_edge(DOWN)
        self.play(Write(ortho_text))

        # Rotate view
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.wait(2)


class QuadraticCostFunction2D(Scene):
    def construct(self):
        # Title
        title = Text("Gradient Descent on Quadratic Cost Function", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Create 2D axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 10, 2],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True, "include_numbers": True},
        ).shift(DOWN * 0.5)

        # Axis labels
        x_label = MathTex(r"\beta", font_size=36).next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"\text{RSS}(\beta)", font_size=36).next_to(axes.y_axis, UP)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait()

        # Quadratic cost function (simple parabola)
        def cost_function(x):
            return 0.5 * x**2 + 2 * x + 1

        def cost_derivative(x):
            return x + 2

        # Plot the cost function
        curve = axes.plot(cost_function, x_range=[-2.8, 2.8], color=BLUE)
        equation = MathTex(
            r"\text{RSS}(\beta) = 0.5\beta^2 + 2\beta + 1", font_size=32, color=BLUE
        ).next_to(y_label, LEFT, buff=0.5)

        self.play(Create(curve), Write(equation))
        self.wait()

        # Mark the minimum point
        min_point = Dot(axes.c2p(-2, cost_function(-2)), color=RED, radius=0.1)
        min_label = MathTex(r"\beta^* = -2", font_size=28, color=RED).next_to(
            min_point, DOWN
        )

        self.play(FadeIn(min_point), Write(min_label))
        self.wait()

        # Gradient descent animation
        # Starting point
        beta_current = 2.5
        learning_rate = 0.3

        # Starting point marker
        current_dot = Dot(
            axes.c2p(beta_current, cost_function(beta_current)),
            color=ORANGE,
            radius=0.12,
        )
        current_label = MathTex(r"\beta_0 = 2.5", font_size=28, color=ORANGE).next_to(
            current_dot, UR
        )

        self.play(FadeIn(current_dot), Write(current_label))
        self.wait()

        # Perform gradient descent steps with tangent lines
        num_steps = 8
        for step in range(num_steps):
            # Calculate gradient at current position
            gradient = cost_derivative(beta_current)

            # Draw tangent line
            tangent_slope = gradient
            tangent_length = 1.5
            tangent_x_start = beta_current - tangent_length / 2
            tangent_x_end = beta_current + tangent_length / 2

            tangent_line = Line(
                axes.c2p(
                    tangent_x_start,
                    cost_function(beta_current)
                    + tangent_slope * (tangent_x_start - beta_current),
                ),
                axes.c2p(
                    tangent_x_end,
                    cost_function(beta_current)
                    + tangent_slope * (tangent_x_end - beta_current),
                ),
                color=YELLOW,
                stroke_width=3,
            )

            # Gradient arrow showing direction
            arrow_start = axes.c2p(beta_current, cost_function(beta_current))
            arrow_direction = -gradient * learning_rate * 2
            arrow_end = axes.c2p(
                beta_current + arrow_direction, cost_function(beta_current)
            )
            gradient_arrow = Arrow(arrow_start, arrow_end, color=GREEN, buff=0)

            # Show tangent and gradient
            if step == 0:
                tangent_label = MathTex(
                    r"\text{Tangent (Gradient)}", font_size=24, color=YELLOW
                ).next_to(tangent_line, UP, buff=0.2)
                self.play(Create(tangent_line), Write(tangent_label))
                self.play(Create(gradient_arrow))
            else:
                self.play(Create(tangent_line), Create(gradient_arrow), run_time=0.5)

            self.wait(0.3)

            # Update beta using gradient descent
            beta_new = beta_current - learning_rate * gradient

            # Animate movement to new position
            new_dot = Dot(
                axes.c2p(beta_new, cost_function(beta_new)),
                color=ORANGE,
                radius=0.12,
            )

            step_label = MathTex(
                f"\\beta_{{{step + 1}}} = {beta_new:.2f}",
                font_size=24,
                color=ORANGE,
            ).next_to(new_dot, UR if step % 2 == 0 else DR)

            # Move dot and add trail
            trail_dot = Dot(
                axes.c2p(beta_current, cost_function(beta_current)),
                color=GREEN,
                radius=0.05,
            )

            self.play(
                FadeOut(tangent_line),
                FadeOut(gradient_arrow),
                Transform(current_dot, new_dot),
                FadeIn(trail_dot),
                run_time=0.6,
            )

            if step < 3 or step == num_steps - 1:
                self.play(Write(step_label), run_time=0.4)

            beta_current = beta_new

            # Stop if close to minimum
            if abs(beta_current) < 0.05:
                break

            self.wait(0.2)

        # Final annotation
        self.wait()
        convergence_text = Text(
            "Converged to minimum!", font_size=32, color=GREEN
        ).to_edge(DOWN)
        self.play(Write(convergence_text))
        self.wait(2)


class QuadraticCostFunction3D(ThreeDScene):
    def construct(self):
        # Title
        title = Text("3D Cost Function Surface: RSS(β₀, β₁)", font_size=40)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait()

        # Set camera orientation
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 10, 2],
            x_length=6,
            y_length=6,
            z_length=4,
            axis_config={"include_tip": True},
        )

        # Axis labels
        x_label = MathTex(r"\beta_0", font_size=36).next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"\beta_1", font_size=36).next_to(axes.y_axis, OUT)
        z_label = MathTex(r"\text{RSS}", font_size=36).next_to(axes.z_axis, UP)

        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label), Write(z_label))
        self.wait()

        # Quadratic cost function surface (paraboloid)
        def cost_function(u, v):
            return 0.3 * u**2 + 0.5 * v**2 + 0.8 * u * v + 1

        surface = Surface(
            lambda u, v: axes.c2p(u, v, cost_function(u, v)),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(30, 30),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        # Add surface with animation
        self.play(Create(surface), run_time=3)
        self.wait()

        # Mark the minimum point
        min_point = Dot3D(
            point=axes.c2p(0, 0, cost_function(0, 0)), color=RED, radius=0.15
        )
        min_label = MathTex(r"\beta^*", font_size=32, color=RED)
        min_label.next_to(min_point, DOWN)
        self.add_fixed_in_frame_mobjects(min_label)

        self.play(FadeIn(min_point))
        self.play(Write(min_label))
        self.wait()

        # Show contour lines at different heights
        contour_heights = [2, 3, 5, 7]
        contours = VGroup()

        for height in contour_heights:
            # Create points along contour
            contour_points = []
            theta_range = np.linspace(0, 2 * np.pi, 100)

            for theta in theta_range:
                # Parametric equation for ellipse at given height
                a = np.sqrt(2 * (height - 1) / 0.3)
                b = np.sqrt(2 * (height - 1) / 0.5)
                u = a * np.cos(theta) * 0.7
                v = b * np.sin(theta) * 0.7

                if abs(u) < 2.5 and abs(v) < 2.5:
                    contour_points.append(axes.c2p(u, v, height))

            if len(contour_points) > 2:
                contour = VMobject()
                contour.set_points_smoothly(contour_points)
                contour.set_color(YELLOW)
                contour.set_stroke(width=2)
                contours.add(contour)

        self.play(Create(contours), run_time=2)
        self.wait()

        # Add gradient descent path
        # Starting point
        beta_0 = np.array([2.0, 2.0])
        learning_rate = 0.4
        path_points = [
            axes.c2p(beta_0[0], beta_0[1], cost_function(beta_0[0], beta_0[1]))
        ]

        # Compute gradient descent steps
        current = beta_0.copy()
        for _ in range(15):
            # Gradient of cost function
            grad = np.array(
                [
                    0.6 * current[0] + 0.8 * current[1],
                    1.0 * current[1] + 0.8 * current[0],
                ]
            )
            current = current - learning_rate * grad
            path_points.append(
                axes.c2p(current[0], current[1], cost_function(current[0], current[1]))
            )

            if np.linalg.norm(current) < 0.1:
                break

        # Draw path
        path = VMobject()
        path.set_points_smoothly(path_points)
        path.set_color(GREEN)
        path.set_stroke(width=4)

        # Starting point marker
        start_dot = Dot3D(point=path_points[0], color=ORANGE, radius=0.12)

        self.play(FadeIn(start_dot))
        self.play(Create(path), run_time=3, rate_func=smooth)
        self.wait()

        # Add annotation
        annotation = Text(
            "Gradient Descent Path to Minimum", font_size=28, color=GREEN
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(annotation)
        self.play(Write(annotation))
        self.wait()

        # Rotate camera to show 3D perspective
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # Final view from above to show contours
        self.move_camera(phi=85 * DEGREES, theta=-45 * DEGREES, run_time=2)
        self.wait(2)

        # Show equation
        equation = MathTex(
            r"\text{RSS}(\beta_0, \beta_1) = ",
            r"0.3\beta_0^2 + 0.5\beta_1^2 + 0.8\beta_0\beta_1 + 1",
            font_size=32,
        ).to_corner(UL)
        self.add_fixed_in_frame_mobjects(equation)
        self.play(Write(equation))
        self.wait(2)
