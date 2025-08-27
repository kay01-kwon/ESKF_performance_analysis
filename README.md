# ESKF_performance_analysis

## How to execute the file

1. Simulation data

Since the linear velocity is expressed by the body frame,
it is necessary to transform to the world frame.

In the state demuxer, the bool Is_transform_required
should be "True".

2. Real world data