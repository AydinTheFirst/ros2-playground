from setuptools import find_packages, setup

package_name = "my_robot_controller"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="aydin",
    maintainer_email="84444757+AydinTheFirst@users.noreply.github.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "listener = my_robot_controller.listener:main",
            "talker = my_robot_controller.talker:main",
            "turtle_controller = my_robot_controller.turtle_controller:main",
            "msg_talker = my_robot_controller.msg_talker:main",
        ],
    },
)
