from setuptools import setup
setup(
    name="agent-deploy",
    version="0.1.0",
    py_modules=["agent_deploy"],
    entry_points={"console_scripts": ["agent-deploy=agent_deploy:cli"]},
    install_requires=["click>=8.0", "requests>=2.28", "pyyaml>=6.0"],
    python_requires=">=3.9",
)
