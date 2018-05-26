---
title: Functions
description: Direct2D provides the following functions.
ms.assetid: 8a7c1e7e-9783-4b95-ac4c-4e7cc961f928
keywords:
- Direct2D,functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions

Direct2D provides the following functions. Additional functions are defined in the [D2D1 Namespace](d2d1-namespace.md).

## In this section



| Topic                                                                                                                                                                                         | Description                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**D2D1ComputeMaximumScaleFactor**](/windows/win32/d2d1_2/nf-d2d1_2-d2d1computemaximumscalefactor?branch=master)<br/>                                                                                                             | Computes the maximum factor by which a given transform can stretch any vector.<br/>                                        |
| [**D2D1CreateDevice**](/windows/win32/d2d1_1/nf-d2d1_1-d2d1createdevice?branch=master)<br/>                                                                                                                                       | Creates a new Direct2D device associated with the provided DXGI device. <br/>                                              |
| [**D2D1CreateDeviceContext**](/windows/win32/d2d1_1/nf-d2d1_1-d2d1createdevicecontext?branch=master)<br/>                                                                                                                         | Creates a new Direct2D device context associated with a DXGI surface. <br/>                                                |
| [**D2D1CreateFactory(Factory)(D2D1\_FACTORY\_TYPE,Factory\*\*)**](createfactory-lt-factory-gt--d2d1-factory-type---factory-.md)<br/>                                                   | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(Factory)(D2D1\_FACTORY\_TYPE,D2D1\_FACTORY\_OPTIONS&,Factory\*\*)**](createfactory-lt-factory-gt--d2d1-factory-type--amp-d2d1-factory-options---factory-.md)<br/> | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(D2D1\_FACTORY\_TYPE,REFIID,void\*\*)**](/windows/win32/d2d1/?branch=master)<br/>                                                               | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(D2D1\_FACTORY\_TYPE,REFIID,D2D1\_FACTORY\_OPTIONS\*,void\*\*)**](/windows/win32/d2d1/nf-d2d1-d2d1createfactory?branch=master)<br/>                                                                       | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1GetGradientMeshInteriorPointsFromCoonsPatch**](/windows/win32/d2d1_3/nf-d2d1_3-d2d1getgradientmeshinteriorpointsfromcoonspatch?branch=master)<br/>                                                                         | Returns the interior points for a gradient mesh patch based on the points defining a Coons patch.<br/>                     |
| [**D2D1InvertMatrix**](/windows/win32/d2d1/nf-d2d1-d2d1invertmatrix?branch=master)<br/>                                                                                                                                       | Tries to invert the specified matrix.<br/>                                                                                 |
| [**D2D1IsMatrixInvertible**](/windows/win32/d2d1/nf-d2d1-d2d1ismatrixinvertible?branch=master)<br/>                                                                                                                           | Indicates whether the specified matrix is invertible.<br/>                                                                 |
| [**D2D1MakeRotateMatrix**](/windows/win32/d2d1/nf-d2d1-d2d1makerotatematrix?branch=master)<br/>                                                                                                                               | Creates a rotation transformation that rotates by the specified angle about the specified point.<br/>                      |
| [**D2D1MakeSkewMatrix**](/windows/win32/d2d1/nf-d2d1-d2d1makeskewmatrix?branch=master)<br/>                                                                                                                                   | Creates a skew transformation that has the specified x-axis angle, y-axis angle, and center point. <br/>                   |
| [**operator\* (const D2D1\_MATRIX\_3X2\_F&,const D2D1\_MATRIX\_3X2\_F&)**](/windows/win32/windowsnumerics.inl/nf-d2d1helper-operator?branch=master)<br/>                               | Multiplies two matrices and returns the result.<br/>                                                                       |
| [**BlobGetter**](blobgetter.md)<br/>                                                                                                                                                   | Calls a member-function property getter callback for a blob-type property.<br/>                                            |
| [**BlobSetter**](blobsetter.md)<br/>                                                                                                                                                   | Calls a member-function property setter callback for a blob-type property.<br/>                                            |
| [**DeducingBlobGetter**](deducingblobgetter.md)<br/>                                                                                                                                   | Deduces the class and arguments and then calls a member-function property getter callback for a blob-type property.<br/>   |
| [**DeducingBlobSetter**](deducingblobsetter.md)<br/>                                                                                                                                   | Deduces the class and arguments and then calls a member-function property setter callback for a blob-type property.<br/>   |
| [**DeducingStringGetter**](deducingstringgetter.md)<br/>                                                                                                                               | Deduces the class and arguments and then calls a member-function property getter callback for a string-type property.<br/> |
| [**DeducingStringSetter**](deducingstringsetter.md)<br/>                                                                                                                               | Deduces the class and arguments and then calls a member-function property setter callback for a string-type property.<br/> |
| [**DeducingValueGetter**](deducingvaluegetter.md)<br/>                                                                                                                                 | Deduces the class and arguments and then calls a member-function property getter callback for a value-type property.<br/>  |
| [**DeducingValueSetter**](deducingvaluesetter.md)<br/>                                                                                                                                 | Deduces the class and arguments and then calls a member-function property setter callback for a value-type property.<br/>  |
| [**GetType**](/windows/win32/d2d1_1/nf-d2d1effecthelpers-gettype?branch=master)<br/>                                                                                                                                                         | Retrieves the type of the given property.<br/>                                                                             |
| [**StringGetter**](/windows/win32/d2d1effecthelpers/nf-d2d1effecthelpers-stringgetter?branch=master)<br/>                                                                                                                                               | Calls a member-function property getter callback for a string-type property.<br/>                                          |
| [**StringSetter**](/windows/win32/d2d1effecthelpers/nf-d2d1effecthelpers-stringsetter?branch=master)<br/>                                                                                                                                               | Calls a member-function property setter callback for a string-type property.<br/>                                          |
| [**ValueGetter**](/windows/win32/d2d1effecthelpers/nf-d2d1effecthelpers-valuegetter?branch=master)<br/>                                                                                                                                                 | Calls a member-function property setter callback for a value-type property.<br/>                                           |
| [**ValueSetter**](/windows/win32/d2d1effecthelpers/nf-d2d1effecthelpers-valuesetter?branch=master)<br/>                                                                                                                                                 | Calls a member-function property setter callback for a value-type property.<br/>                                           |
| [**D2D1ConvertColorSpace**](/windows/win32/d2d1_1/nf-d2d1_1-d2d1convertcolorspace?branch=master)<br/>                                                                                                                             | Converts the given color from one colorspace to another.<br/>                                                              |
| [**D2D1SinCos**](/windows/win32/d2d1_1/nf-d2d1_1-d2d1sincos?branch=master)<br/>                                                                                                                                                   | Returns the sine and cosine of an angle.<br/>                                                                              |
| [**D2D1Tan**](/windows/win32/d2d1_1/nf-d2d1_1-d2d1tan?branch=master)<br/>                                                                                                                                                         | Returns the tangent of an angle.<br/>                                                                                      |
| [**D2D1Vec3Length**](/windows/win32/d2d1_1/nf-d2d1_1-d2d1vec3length?branch=master)<br/>                                                                                                                                           | Returns the length of a 3 dimensional vector.<br/>                                                                         |
| [**PD2D1\_PROPERTY\_GET\_FUNCTION**](/windows/win32/D2d1effectauthor/nc-d2d1effectauthor-pd2d1_property_get_function?branch=master)<br/>                                                                                                              | Gets a property from an effect.<br/>                                                                                       |
| [**PD2D1\_PROPERTY\_SET\_FUNCTION**](/windows/win32/D2d1effectauthor/nc-d2d1effectauthor-pd2d1_property_set_function?branch=master)<br/>                                                                                                              | Sets a property on an effect.<br/>                                                                                         |



 

 

 





