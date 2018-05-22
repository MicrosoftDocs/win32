---
Description: 'The five world-to-page transformations can be combined into a single 3-by-3 matrix.'
ms.assetid: 'd17ba826-8e8d-4121-8afd-0f256121b54c'
title: 'Combined World-to-Page Space Transformations'
---

# Combined World-to-Page Space Transformations

The five world-to-page transformations can be combined into a single 3-by-3 matrix. The [**CombineTransform**](combinetransform.md) function can be used to combine two world-space to page-space transformations. The combined transformations can be used to alter output associated with a particular device context (DC) by calling the [**SetWorldTransform**](setworldtransform.md) function and supplying the elements for this matrix. When an application calls **SetWorldTransform**, it stores the elements of the 3-by-3 matrix in an [**XFORM**](xform.md) structure. The members of this structure correspond to the first two columns of a 3-by-3 matrix; the last column of the matrix is not required because its values are constant.

The elements of the current world transformation matrix can be revived by calling the [**GetWorldTransform**](getworldtransform.md) function and supplying a pointer to an [**XFORM**](xform.md) structure.

 

 



