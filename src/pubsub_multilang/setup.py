from setuptools import find_packages, setup

package_name = 'pubsub_multilang'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name] if False else []),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Estudiante',
    maintainer_email='estudiante@ejemplo.com',
    description='Paquete Pub/Sub C++ y Python',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_py = pubsub_multilang.publisher_py:main',
            'subscriber_py = pubsub_multilang.subscriber_py:main',
        ],
    },
)
