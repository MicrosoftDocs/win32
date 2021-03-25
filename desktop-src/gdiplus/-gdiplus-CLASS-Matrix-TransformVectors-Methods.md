---
description: This topic lists the TransformVectors methods of the Matrix class. For a complete list of methods for the Matrix class, see Matrix Methods.
ms.assetid: 6a2ed6a7-825a-422b-b035-b88746f3ab5d
title: Matrix.TransformVectors methods (Gdiplusmatrix.h)
ms.date: 07/02/2019
ms.topic: reference
---

# Matrix.TransformVectors methods

This topic lists the TransformVectors methods of the [**Matrix**](/windows/win32/api/gdiplusmatrix/nl-gdiplusmatrix-matrix) class. For a complete list of methods for the **Matrix** class, see [Matrix Methods](-gdiplus-class-matrix-methods.md).

### Overload list



| Method                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                      |
|:-------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TransformVectors(Point\*,INT)**](/windows/win32/api/gdiplusmatrix/nf-gdiplusmatrix-matrix-transformvectors(inoutpoint_inint))   | The [**Matrix::TransformVectors**](/windows/win32/api/gdiplusmatrix/nf-gdiplusmatrix-matrix-transformvectors(inoutpoint_inint)) method multiplies each vector in an array by this matrix. The translation elements of this matrix (third row) are ignored. Each vector is treated as a row matrix. The multiplication is performed with the row matrix on the left and this matrix on the right.<br/>  |
| [**TransformVectors(PointF\*,INT)**](/previous-versions//ms535319(v=vs.85)) | The [**Matrix::TransformVectors**](/previous-versions//ms535319(v=vs.85)) method multiplies each vector in an array by this matrix. The translation elements of this matrix (third row) are ignored. Each vector is treated as a row matrix. The multiplication is performed with the row matrix on the left and this matrix on the right.<br/> |



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Gdiplusmatrix.h</dt> </dl> |



 

 
