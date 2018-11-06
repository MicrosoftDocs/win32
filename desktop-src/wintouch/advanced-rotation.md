---
title: Advanced Rotation
description: This section explains how to rotate an object based on where the user is performing the rotation manipulation.
ms.assetid: 56b339b1-a062-4c0e-91c8-aec08a17bc65
keywords:
- Windows Touch,rotation
- Windows Touch,advanced rotation
- Windows Touch,manipulations
- manipulations,rotation
- manipulations,advanced rotation
- rotation,advanced
ms.topic: article
ms.date: 05/31/2018
---

# Advanced Rotation

This section explains how to rotate an object based on where the user is performing the rotation manipulation.

The following image illustrates two different ways that an object can be rotated.

![illustration showing two types of single-finger rotation: around the center or around the edge, with the edge involving both rotation and translation](images/rotation.png)

In example A, the object is manipulated around the center point of the object. In example B, the object is rotated around the center point of the manipulation. To support manipulation around a point other than the center point of the object, you must perform a compound manipulation that performs both rotation and translation. The following code shows how this manipulation is performed and calculated.


```C++
RotateVector(FLOAT *vector, FLOAT *tVector, FLOAT fAngle) {
    FLOAT fAngleRads = fAngle / 180.0f * 3.14159f;
    FLOAT fSin = sin(fAngleRads);
    FLOAT fCos = cos(fAngleRads);

    FLOAT fNewX = (vector[0]*fCos) - (vector[1]*fSin);
    FLOAT fNewY = (vector[0]*fSin) + (vector[1]*fCos);

    tVector[0] = fNewX;
    tVector[1] = fNewY;
}
     
```



## Related topics

<dl> <dt>

[Advanced Manipulations](advanced-manipulations.md)
</dt> <dt>

[Manipulations](getting-started-with-manipulations.md)
</dt> </dl>

 

 




