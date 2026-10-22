from setuptools import find_packages, setup

package_name = 'learning_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
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
            'publisher = learning_topic.HelloWorldTopicPulisher:main',
            'subscriber = learning_topic.HelloWorldTopicSubscriber:main',
            'publisherCam = learning_topic.TopicWebCamPub:main',
            'subscribeCam = learning_topic.TopicWebCamSub:main'
        ],
    },
)
