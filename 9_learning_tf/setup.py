from setuptools import find_packages, setup

package_name = '9_learning_tf'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='desheng',
    maintainer_email='chenxu.l@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'static_tf = 9_learning_tf.static_broadcaster_tf:main',
            'listener = 9_learning_tf.tf_listener:main',
        ],
    },
)
