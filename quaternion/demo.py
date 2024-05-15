# %%
# quaternion test

# %%
# 基本能力演示

# %%
from pyquaternion import Quaternion
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True) # Suppress insignificant values for clarity


# %%
# basic test
# define a vector [0,0,1]
v = np.array([0,0,1])

# %%

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
# use quiver to draw three unit vectors (0,0,1), (0,1,0), (1,0,0)
ax.quiver(0,0,0,0,0,1,length=0.2,normalize=True,color='r')
ax.quiver(0,0,0,0,1,0,length=0.2,normalize=True,color='g')
ax.quiver(0,0,0,1,0,0,length=0.2,normalize=True,color='b')
# add x,y,z label
ax.text(0.2,0,0,'x')
ax.text(0,0.2,0,'y')
ax.text(0,0,0.2,'z')

# axis range
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# ax.scatter(xs, ys, zs, marker=m)
ax.scatter(v[0], v[1], v[2], marker='^')
# draw a line from [0,0,0] to [0,0,1]
ax.plot([0,0],[0,0],[0,1],color='r',linestyle='--', linewidth=0.5)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

# %%
# define a quaternion
# rotate 90 degree around x axis
q = Quaternion(axis=[1,0,0],angle=np.pi/2)

# %%
# apply rotation
v_rot = q.rotate(v)
v_rot

# %%

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
# use quiver to draw three unit vectors (0,0,1), (0,1,0), (1,0,0)
ax.quiver(0,0,0,0,0,1,length=0.2,normalize=True,color='r')
ax.quiver(0,0,0,0,1,0,length=0.2,normalize=True,color='g')
ax.quiver(0,0,0,1,0,0,length=0.2,normalize=True,color='b')
# add x,y,z label
ax.text(0.2,0,0,'x')
ax.text(0,0.2,0,'y')
ax.text(0,0,0.2,'z')

# axis range
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# ax.scatter(xs, ys, zs, marker=m)
ax.scatter(v[0], v[1], v[2], marker='^')
# draw a line from [0,0,0] to [0,0,1]
ax.plot([0,0],[0,0],[0,1],color='r', linestyle='--', linewidth=0.5)

# plot v_rot
ax.scatter(v_rot[0], v_rot[1], v_rot[2], marker='o')
ax.plot([0,v_rot[0]],[0,v_rot[1]],[0,v_rot[2]],color='b' , linestyle='--',linewidth=0.5)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

# %%
# 定义一个长方体，长宽高分别是：0.5, 0.3, 0.2
# 顶点坐标
v1 = np.array([0.25,0.15,0.1]) * 2
v2 = np.array([0.25,0.15,-0.1]) * 2
v3 = np.array([0.25,-0.15,-0.1]) * 2
v4 = np.array([0.25,-0.15,0.1]) * 2
v5 = np.array([-0.25,0.15,0.1]) * 2
v6 = np.array([-0.25,0.15,-0.1]) * 2
v7 = np.array([-0.25,-0.15,-0.1]) * 2
v8 = np.array([-0.25,-0.15,0.1]) * 2

# 绘制长方体
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
# use quiver to draw three unit vectors (0,0,1), (0,1,0), (1,0,0)
ax.quiver(0,0,0,0,0,1,length=0.2,normalize=True,color='r')
ax.quiver(0,0,0,0,1,0,length=0.2,normalize=True,color='g')
ax.quiver(0,0,0,1,0,0,length=0.2,normalize=True,color='b')
# add x,y,z label
ax.text(0.2,0,0,'x')
ax.text(0,0.2,0,'y')
ax.text(0,0,0.2,'z')

# axis range
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# ax.scatter(xs, ys, zs, marker=m)
ax.scatter(v1[0], v1[1], v1[2], marker='o')
ax.scatter(v2[0], v2[1], v2[2], marker='o')
ax.scatter(v3[0], v3[1], v3[2], marker='o')
ax.scatter(v4[0], v4[1], v4[2], marker='o')
ax.scatter(v5[0], v5[1], v5[2], marker='o')
ax.scatter(v6[0], v6[1], v6[2], marker='o')
ax.scatter(v7[0], v7[1], v7[2], marker='o')
ax.scatter(v8[0], v8[1], v8[2], marker='o')

# draw a line between two points
ax.plot([v1[0],v2[0]],[v1[1],v2[1]],[v1[2],v2[2]],color='r', linewidth=0.5)
ax.plot([v2[0],v3[0]],[v2[1],v3[1]],[v2[2],v3[2]],color='r', linewidth=0.5)
ax.plot([v3[0],v4[0]],[v3[1],v4[1]],[v3[2],v4[2]],color='r', linewidth=0.5)
ax.plot([v4[0],v1[0]],[v4[1],v1[1]],[v4[2],v1[2]],color='r', linewidth=0.5)
ax.plot([v5[0],v6[0]],[v5[1],v6[1]],[v5[2],v6[2]],color='r', linewidth=0.5)
ax.plot([v6[0],v7[0]],[v6[1],v7[1]],[v6[2],v7[2]],color='r', linewidth=0.5)
ax.plot([v7[0],v8[0]],[v7[1],v8[1]],[v7[2],v8[2]],color='r', linewidth=0.5)
ax.plot([v8[0],v5[0]],[v8[1],v5[1]],[v8[2],v5[2]],color='r', linewidth=0.5)
ax.plot([v1[0],v5[0]],[v1[1],v5[1]],[v1[2],v5[2]],color='r', linewidth=0.5)
ax.plot([v2[0],v6[0]],[v2[1],v6[1]],[v2[2],v6[2]],color='r', linewidth=0.5)
ax.plot([v3[0],v7[0]],[v3[1],v7[1]],[v3[2],v7[2]],color='r', linewidth=0.5)
ax.plot([v4[0],v8[0]],[v4[1],v8[1]],[v4[2],v8[2]],color='r', linewidth=0.5)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


# %%
# 沿着y轴旋转90度
q = Quaternion(axis=[0,1,0],angle=np.pi/2)

# %%
# 对所有顶点进行旋转
v1_rot = q.rotate(v1)
v2_rot = q.rotate(v2)
v3_rot = q.rotate(v3)
v4_rot = q.rotate(v4)
v5_rot = q.rotate(v5)
v6_rot = q.rotate(v6)
v7_rot = q.rotate(v7)
v8_rot = q.rotate(v8)


# %%
# 绘制旋转后的长方体

# 绘制长方体
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
# use quiver to draw three unit vectors (0,0,1), (0,1,0), (1,0,0)
ax.quiver(0,0,0,0,0,1,length=0.2,normalize=True,color='r')
ax.quiver(0,0,0,0,1,0,length=0.2,normalize=True,color='g')
ax.quiver(0,0,0,1,0,0,length=0.2,normalize=True,color='b')
# add x,y,z label
ax.text(0.2,0,0,'x')
ax.text(0,0.2,0,'y')
ax.text(0,0,0.2,'z')

# axis range
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# ax.scatter(xs, ys, zs, marker=m)
ax.scatter(v1[0], v1[1], v1[2], marker='o')
ax.scatter(v2[0], v2[1], v2[2], marker='o')
ax.scatter(v3[0], v3[1], v3[2], marker='o')
ax.scatter(v4[0], v4[1], v4[2], marker='o')
ax.scatter(v5[0], v5[1], v5[2], marker='o')
ax.scatter(v6[0], v6[1], v6[2], marker='o')
ax.scatter(v7[0], v7[1], v7[2], marker='o')
ax.scatter(v8[0], v8[1], v8[2], marker='o')

# draw a line between two points
ax.plot([v1[0],v2[0]],[v1[1],v2[1]],[v1[2],v2[2]],color='r', linewidth=0.5)
ax.plot([v2[0],v3[0]],[v2[1],v3[1]],[v2[2],v3[2]],color='r', linewidth=0.5)
ax.plot([v3[0],v4[0]],[v3[1],v4[1]],[v3[2],v4[2]],color='r', linewidth=0.5)
ax.plot([v4[0],v1[0]],[v4[1],v1[1]],[v4[2],v1[2]],color='r', linewidth=0.5)
ax.plot([v5[0],v6[0]],[v5[1],v6[1]],[v5[2],v6[2]],color='r', linewidth=0.5)
ax.plot([v6[0],v7[0]],[v6[1],v7[1]],[v6[2],v7[2]],color='r', linewidth=0.5)
ax.plot([v7[0],v8[0]],[v7[1],v8[1]],[v7[2],v8[2]],color='r', linewidth=0.5)
ax.plot([v8[0],v5[0]],[v8[1],v5[1]],[v8[2],v5[2]],color='r', linewidth=0.5)
ax.plot([v1[0],v5[0]],[v1[1],v5[1]],[v1[2],v5[2]],color='r', linewidth=0.5)
ax.plot([v2[0],v6[0]],[v2[1],v6[1]],[v2[2],v6[2]],color='r', linewidth=0.5)
ax.plot([v3[0],v7[0]],[v3[1],v7[1]],[v3[2],v7[2]],color='r', linewidth=0.5)
ax.plot([v4[0],v8[0]],[v4[1],v8[1]],[v4[2],v8[2]],color='r', linewidth=0.5)


# 绘制旋转后的长方体
ax.scatter(v1_rot[0], v1_rot[1], v1_rot[2], marker='^')
ax.scatter(v2_rot[0], v2_rot[1], v2_rot[2], marker='^')
ax.scatter(v3_rot[0], v3_rot[1], v3_rot[2], marker='^')
ax.scatter(v4_rot[0], v4_rot[1], v4_rot[2], marker='^')
ax.scatter(v5_rot[0], v5_rot[1], v5_rot[2], marker='^')
ax.scatter(v6_rot[0], v6_rot[1], v6_rot[2], marker='^')
ax.scatter(v7_rot[0], v7_rot[1], v7_rot[2], marker='^')
ax.scatter(v8_rot[0], v8_rot[1], v8_rot[2], marker='^')

# draw a line between two points
ax.plot([v1_rot[0],v2_rot[0]],[v1_rot[1],v2_rot[1]],[v1_rot[2],v2_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v2_rot[0],v3_rot[0]],[v2_rot[1],v3_rot[1]],[v2_rot[2],v3_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v3_rot[0],v4_rot[0]],[v3_rot[1],v4_rot[1]],[v3_rot[2],v4_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v4_rot[0],v1_rot[0]],[v4_rot[1],v1_rot[1]],[v4_rot[2],v1_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v5_rot[0],v6_rot[0]],[v5_rot[1],v6_rot[1]],[v5_rot[2],v6_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v6_rot[0],v7_rot[0]],[v6_rot[1],v7_rot[1]],[v6_rot[2],v7_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v7_rot[0],v8_rot[0]],[v7_rot[1],v8_rot[1]],[v7_rot[2],v8_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v8_rot[0],v5_rot[0]],[v8_rot[1],v5_rot[1]],[v8_rot[2],v5_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v1_rot[0],v5_rot[0]],[v1_rot[1],v5_rot[1]],[v1_rot[2],v5_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v2_rot[0],v6_rot[0]],[v2_rot[1],v6_rot[1]],[v2_rot[2],v6_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v3_rot[0],v7_rot[0]],[v3_rot[1],v7_rot[1]],[v3_rot[2],v7_rot[2]],color='r', linestyle='--',linewidth=0.5)
ax.plot([v4_rot[0],v8_rot[0]],[v4_rot[1],v8_rot[1]],[v4_rot[2],v8_rot[2]],color='r', linestyle='--',linewidth=0.5)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


# %%


# %% [markdown]
# ![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/202311101211239.png?x-oss-process=style/wp)

# %%
# 转为yaw_pitch_roll，即欧拉角，手性：右手，即大拇指指向x轴，食指指向y轴，中指指向z轴
# yaw：绕z轴旋转
# pitch：绕y轴旋转
# roll：绕x轴旋转

# %%
# 绕着y轴旋转90度
q = Quaternion(axis=[0,1,0],angle=np.pi/2)

# %%
# 转为yaw_pitch_roll，弧度制
yaw, pitch, roll = q.yaw_pitch_roll
yaw, pitch, roll

# %%
# 转为四元数
w,x,y,z  = q.q
w,x,y,z

# %%
# 根据四元数计算yaw_pitch_roll
q2 = Quaternion(w,x,y,z)
q2.yaw_pitch_roll

# %%
# 使用四元数，绕着x轴旋转90度
q = Quaternion(w=0.7071068,x=0.7071068,y=0,z=0)
yaw, pitch, roll = q.yaw_pitch_roll
yaw, pitch, roll

# %%
# 使用四元数，绕着y轴旋转45度
q = Quaternion(w=0.9238795,x=0,y=0.3826834,z=0)
yaw, pitch, roll = q.yaw_pitch_roll
yaw, pitch, roll


