"""Test InteractiveRenderWrapper functionality."""

import pytest
import os
import tempfile


class TestInteractiveRenderWrapper:
    """Test InteractiveRenderWrapper functionality."""

    def test_interactive_render_wrapper_with_gym(self):
        """Test InteractiveRenderWrapper with Gymnasium if available."""
        pytest.importorskip("gymnasium")
        pytest.importorskip("mujoco")

        import gymnasium as gym
        from simrender.gym import InteractiveRenderWrapper

        # Try to create a MuJoCo env if available
        try:
            env = gym.make("Ant-v5")
            wrapped_env = InteractiveRenderWrapper(env)

            # Record a short episode
            with wrapped_env.animation(fps=30):
                obs, _ = wrapped_env.reset(seed=42)
                for _ in range(5):  # Short test
                    action = wrapped_env.action_space.sample()
                    obs, reward, terminated, truncated, info = wrapped_env.step(action)
                    wrapped_env.render()
                    if terminated or truncated:
                        break

            # Save to temporary file
            with tempfile.NamedTemporaryFile(suffix=".glb", delete=False) as tmp:
                wrapped_env.save(tmp.name)
                assert os.path.exists(tmp.name)
                os.unlink(tmp.name)

        except Exception as e:
            pytest.skip(f"MuJoCo environment not available: {e}")
