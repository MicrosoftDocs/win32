---
description: This section introduces the basic concepts of the view transform and provides details on how to set up a view transform matrix in a Direct3D application.
ms.assetid: a9885a77-f04e-4ca5-9202-67c4779d03de
title: View Transform (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# View Transform (Direct3D 9)

This section introduces the basic concepts of the view transform and provides details on how to set up a view transform matrix in a Direct3D application.

The view transform locates the viewer in world space, transforming vertices into camera space. In camera space, the camera, or viewer, is at the origin, looking in the positive z-direction. Recall that Direct3D uses a left-handed coordinate system, so z is positive into a scene. The view matrix relocates the objects in the world around a camera's position - the origin of camera space - and orientation.

There are many ways to create a view matrix. In all cases, the camera has some logical position and orientation in world space that is used as a starting point to create a view matrix that will be applied to the models in a scene. The view matrix translates and rotates objects to place them in camera space, where the camera is at the origin. One way to create a view matrix is to combine a translation matrix with rotation matrices for each axis. In this approach, the following general matrix equation applies.

![equation of the view transform](images/viewtran.png)

In this formula, V is the view matrix being created, T is a translation matrix that repositions objects in the world, and Rₓ through R<sub>z</sub> are rotation matrices that rotate objects along the x-, y-, and z-axis. The translation and rotation matrices are based on the camera's logical position and orientation in world space. So, if the camera's logical position in the world is <10,20,100>, the aim of the translation matrix is to move objects -10 units along the x-axis, -20 units along the y-axis, and -100 units along the z-axis. The rotation matrices in the formula are based on the camera's orientation, in terms of how much the axes of camera space are rotated out of alignment with world space. For example, if the camera mentioned earlier is pointing straight down, its z-axis is 90 degrees (pi/2 radians) out of alignment with the z-axis of world space, as shown in the following illustration.

![illustration of the view space of the camera in comparison to world space](images/camtop.png)

The rotation matrices apply rotations of equal, but opposite, magnitude to the models in the scene. The view matrix for this camera includes a rotation of -90 degrees around the x-axis. The rotation matrix is combined with the translation matrix to create a view matrix that adjusts the position and orientation of the objects in the scene so that their top is facing the camera, giving the appearance that the camera is above the model.

## Setting Up a View Matrix

The [**D3DXMatrixLookAtLH**](d3dxmatrixlookatlh.md) and [**D3DXMatrixLookAtRH**](d3dxmatrixlookatrh.md) helper functions create a view matrix based on the camera location and a look-at point.

The following example creates a view matrix for left-handed coordinates.


```
D3DXMATRIX out;
D3DXVECTOR3 eye(2,3,3);
D3DXVECTOR3 at(0,0,0);
D3DXVECTOR3 up(0,1,0);
D3DXMatrixLookAtLH(&out, &eye, &at, &up);
```



Direct3D uses the world and view matrices to configure several internal data structures. Each time you set a new world or view matrix, the system recalculates the associated internal structures. Setting these matrices frequently is computationally time-consuming. You can minimize the number of required calculations by concatenating your world and view matrices into a world-view matrix that you set as the world matrix, and then setting the view matrix to the identity. Keep cached copies of individual world and view matrices that you can modify, concatenate, and reset the world matrix as needed. For clarity, the samples rarely employ this optimization.

## Related topics

<dl> <dt>

[Transforms](transforms.md)
</dt> </dl>

 

 



