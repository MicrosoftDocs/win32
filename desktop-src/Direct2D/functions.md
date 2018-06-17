---
title: Functions
description: Direct2D provides the following functions.
ms.assetid: 8a7c1e7e-9783-4b95-ac4c-4e7cc961f928
keywords:
- Direct2D,functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Functions

Direct2D provides the following functions. Additional functions are defined in the [D2D1 Namespace](d2d1-namespace.md).

## In this section



| Topic                                                                                                                                                                                         | Description                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**D2D1ComputeMaximumScaleFactor**](/windows/desktop/api/d2d1_2/nf-d2d1_2-d2d1computemaximumscalefactor)<br/>                                                                                                             | Computes the maximum factor by which a given transform can stretch any vector.<br/>                                        |
| [**D2D1CreateDevice**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1createdevice)<br/>                                                                                                                                       | Creates a new Direct2D device associated with the provided DXGI device. <br/>                                              |
| [**D2D1CreateDeviceContext**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1createdevicecontext)<br/>                                                                                                                         | Creates a new Direct2D device context associated with a DXGI surface. <br/>                                                |
| [**D2D1CreateFactory(Factory)(D2D1\_FACTORY\_TYPE,Factory\*\*)**](createfactory-lt-factory-gt--d2d1-factory-type---factory-.md)<br/>                                                   | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(Factory)(D2D1\_FACTORY\_TYPE,D2D1\_FACTORY\_OPTIONS&,Factory\*\*)**](createfactory-lt-factory-gt--d2d1-factory-type--amp-d2d1-factory-options---factory-.md)<br/> | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(D2D1\_FACTORY\_TYPE,REFIID,void\*\*)**](https://msdn.microsoft.com/en-us/library/Dd368036(v=VS.85).aspx)<br/>                                                               | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(D2D1\_FACTORY\_TYPE,REFIID,D2D1\_FACTORY\_OPTIONS\*,void\*\*)**](/windows/desktop/api/d2d1/nf-d2d1-d2d1createfactory)<br/>                                                                       | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1GetGradientMeshInteriorPointsFromCoonsPatch**](/windows/desktop/api/d2d1_3/nf-d2d1_3-d2d1getgradientmeshinteriorpointsfromcoonspatch)<br/>                                                                         | Returns the interior points for a gradient mesh patch based on the points defining a Coons patch.<br/>                     |
| [**D2D1InvertMatrix**](/windows/desktop/api/d2d1/nf-d2d1-d2d1invertmatrix)<br/>                                                                                                                                       | Tries to invert the specified matrix.<br/>                                                                                 |
| [**D2D1IsMatrixInvertible**](/windows/desktop/api/d2d1/nf-d2d1-d2d1ismatrixinvertible)<br/>                                                                                                                           | Indicates whether the specified matrix is invertible.<br/>                                                                 |
| [**D2D1MakeRotateMatrix**](/windows/desktop/api/d2d1/nf-d2d1-d2d1makerotatematrix)<br/>                                                                                                                               | Creates a rotation transformation that rotates by the specified angle about the specified point.<br/>                      |
| [**D2D1MakeSkewMatrix**](/windows/desktop/api/d2d1/nf-d2d1-d2d1makeskewmatrix)<br/>                                                                                                                                   | Creates a skew transformation that has the specified x-axis angle, y-axis angle, and center point. <br/>                   |
| [**operator\* (const D2D1\_MATRIX\_3X2\_F&,const D2D1\_MATRIX\_3X2\_F&)**](/windows/desktop/api)<br/>                               | Multiplies two matrices and returns the result.<br/>                                                                       |
| [**BlobGetter**](blobgetter.md)<br/>                                                                                                                                                   | Calls a member-function property getter callback for a blob-type property.<br/>                                            |
| [**BlobSetter**](blobsetter.md)<br/>                                                                                                                                                   | Calls a member-function property setter callback for a blob-type property.<br/>                                            |
| [**DeducingBlobGetter**](deducingblobgetter.md)<br/>                                                                                                                                   | Deduces the class and arguments and then calls a member-function property getter callback for a blob-type property.<br/>   |
| [**DeducingBlobSetter**](deducingblobsetter.md)<br/>                                                                                                                                   | Deduces the class and arguments and then calls a member-function property setter callback for a blob-type property.<br/>   |
| [**DeducingStringGetter**](deducingstringgetter.md)<br/>                                                                                                                               | Deduces the class and arguments and then calls a member-function property getter callback for a string-type property.<br/> |
| [**DeducingStringSetter**](deducingstringsetter.md)<br/>                                                                                                                               | Deduces the class and arguments and then calls a member-function property setter callback for a string-type property.<br/> |
| [**DeducingValueGetter**](deducingvaluegetter.md)<br/>                                                                                                                                 | Deduces the class and arguments and then calls a member-function property getter callback for a value-type property.<br/>  |
| [**DeducingValueSetter**](deducingvaluesetter.md)<br/>                                                                                                                                 | Deduces the class and arguments and then calls a member-function property setter callback for a value-type property.<br/>  |
| [**GetType**](https://msdn.microsoft.com/en-us/library/Hh847962(v=VS.85).aspx)<br/>                                                                                                                                                         | Retrieves the type of the given property.<br/>                                                                             |
| [**StringGetter**](/windows/desktop/api/d2d1effecthelpers/nf-d2d1effecthelpers-stringgetter)<br/>                                                                                                                                               | Calls a member-function property getter callback for a string-type property.<br/>                                          |
| [**StringSetter**](/windows/desktop/api/d2d1effecthelpers/nf-d2d1effecthelpers-stringsetter)<br/>                                                                                                                                               | Calls a member-function property setter callback for a string-type property.<br/>                                          |
| [**ValueGetter**](/windows/desktop/api/d2d1effecthelpers/nf-d2d1effecthelpers-valuegetter)<br/>                                                                                                                                                 | Calls a member-function property setter callback for a value-type property.<br/>                                           |
| [**ValueSetter**](/windows/desktop/api/d2d1effecthelpers/nf-d2d1effecthelpers-valuesetter)<br/>                                                                                                                                                 | Calls a member-function property setter callback for a value-type property.<br/>                                           |
| [**D2D1ConvertColorSpace**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1convertcolorspace)<br/>                                                                                                                             | Converts the given color from one colorspace to another.<br/>                                                              |
| [**D2D1SinCos**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1sincos)<br/>                                                                                                                                                   | Returns the sine and cosine of an angle.<br/>                                                                              |
| [**D2D1Tan**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1tan)<br/>                                                                                                                                                         | Returns the tangent of an angle.<br/>                                                                                      |
| [**D2D1Vec3Length**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1vec3length)<br/>                                                                                                                                           | Returns the length of a 3 dimensional vector.<br/>                                                                         |
| [**PD2D1\_PROPERTY\_GET\_FUNCTION**](/windows/desktop/api/D2d1effectauthor/nc-d2d1effectauthor-pd2d1_property_get_function)<br/>                                                                                                              | Gets a property from an effect.<br/>                                                                                       |
| [**PD2D1\_PROPERTY\_SET\_FUNCTION**](/windows/desktop/api/D2d1effectauthor/nc-d2d1effectauthor-pd2d1_property_set_function)<br/>                                                                                                              | Sets a property on an effect.<br/>                                                                                         |



 

 

 





