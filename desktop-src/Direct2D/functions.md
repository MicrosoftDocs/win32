---
title: Functions
description: Direct2D provides the following functions.
ms.assetid: '8a7c1e7e-9783-4b95-ac4c-4e7cc961f928'
keywords: ["Direct2D,functions"]
---

# Functions

Direct2D provides the following functions. Additional functions are defined in the [D2D1 Namespace](d2d1-namespace.md).

## In this section



| Topic                                                                                                                                                                                         | Description                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**D2D1ComputeMaximumScaleFactor**](d2d1computemaximumscalefactor.md)<br/>                                                                                                             | Computes the maximum factor by which a given transform can stretch any vector.<br/>                                        |
| [**D2D1CreateDevice**](d2d1createdevice.md)<br/>                                                                                                                                       | Creates a new Direct2D device associated with the provided DXGI device. <br/>                                              |
| [**D2D1CreateDeviceContext**](d2d1createdevicecontext.md)<br/>                                                                                                                         | Creates a new Direct2D device context associated with a DXGI surface. <br/>                                                |
| [**D2D1CreateFactory(Factory)(D2D1\_FACTORY\_TYPE,Factory\*\*)**](createfactory-lt-factory-gt--d2d1-factory-type---factory-.md)<br/>                                                   | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(Factory)(D2D1\_FACTORY\_TYPE,D2D1\_FACTORY\_OPTIONS&,Factory\*\*)**](createfactory-lt-factory-gt--d2d1-factory-type--amp-d2d1-factory-options---factory-.md)<br/> | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(D2D1\_FACTORY\_TYPE,REFIID,void\*\*)**](d2d1createfactory-d2d1-factory-type-refiid---void-.md)<br/>                                                               | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1CreateFactory(D2D1\_FACTORY\_TYPE,REFIID,D2D1\_FACTORY\_OPTIONS\*,void\*\*)**](d2d1createfactory.md)<br/>                                                                       | Creates a factory object that can be used to create Direct2D resources.<br/>                                               |
| [**D2D1GetGradientMeshInteriorPointsFromCoonsPatch**](d2d1getgradientmeshinteriorpointsfromcoonspatch.md)<br/>                                                                         | Returns the interior points for a gradient mesh patch based on the points defining a Coons patch.<br/>                     |
| [**D2D1InvertMatrix**](d2d1invertmatrix.md)<br/>                                                                                                                                       | Tries to invert the specified matrix.<br/>                                                                                 |
| [**D2D1IsMatrixInvertible**](d2d1ismatrixinvertible.md)<br/>                                                                                                                           | Indicates whether the specified matrix is invertible.<br/>                                                                 |
| [**D2D1MakeRotateMatrix**](d2d1makerotatematrix.md)<br/>                                                                                                                               | Creates a rotation transformation that rotates by the specified angle about the specified point.<br/>                      |
| [**D2D1MakeSkewMatrix**](d2d1makeskewmatrix.md)<br/>                                                                                                                                   | Creates a skew transformation that has the specified x-axis angle, y-axis angle, and center point. <br/>                   |
| [**operator\* (const D2D1\_MATRIX\_3X2\_F&,const D2D1\_MATRIX\_3X2\_F&)**](operator--const--amp-d2d1-matrix-3x2-f-const--amp-d2d1-matrix-3x2-f-.md)<br/>                               | Multiplies two matrices and returns the result.<br/>                                                                       |
| [**BlobGetter**](blobgetter.md)<br/>                                                                                                                                                   | Calls a member-function property getter callback for a blob-type property.<br/>                                            |
| [**BlobSetter**](blobsetter.md)<br/>                                                                                                                                                   | Calls a member-function property setter callback for a blob-type property.<br/>                                            |
| [**DeducingBlobGetter**](deducingblobgetter.md)<br/>                                                                                                                                   | Deduces the class and arguments and then calls a member-function property getter callback for a blob-type property.<br/>   |
| [**DeducingBlobSetter**](deducingblobsetter.md)<br/>                                                                                                                                   | Deduces the class and arguments and then calls a member-function property setter callback for a blob-type property.<br/>   |
| [**DeducingStringGetter**](deducingstringgetter.md)<br/>                                                                                                                               | Deduces the class and arguments and then calls a member-function property getter callback for a string-type property.<br/> |
| [**DeducingStringSetter**](deducingstringsetter.md)<br/>                                                                                                                               | Deduces the class and arguments and then calls a member-function property setter callback for a string-type property.<br/> |
| [**DeducingValueGetter**](deducingvaluegetter.md)<br/>                                                                                                                                 | Deduces the class and arguments and then calls a member-function property getter callback for a value-type property.<br/>  |
| [**DeducingValueSetter**](deducingvaluesetter.md)<br/>                                                                                                                                 | Deduces the class and arguments and then calls a member-function property setter callback for a value-type property.<br/>  |
| [**GetType**](gettype.md)<br/>                                                                                                                                                         | Retrieves the type of the given property.<br/>                                                                             |
| [**StringGetter**](stringgetter.md)<br/>                                                                                                                                               | Calls a member-function property getter callback for a string-type property.<br/>                                          |
| [**StringSetter**](stringsetter.md)<br/>                                                                                                                                               | Calls a member-function property setter callback for a string-type property.<br/>                                          |
| [**ValueGetter**](valuegetter.md)<br/>                                                                                                                                                 | Calls a member-function property setter callback for a value-type property.<br/>                                           |
| [**ValueSetter**](valuesetter.md)<br/>                                                                                                                                                 | Calls a member-function property setter callback for a value-type property.<br/>                                           |
| [**D2D1ConvertColorSpace**](d2d1convertcolorspace.md)<br/>                                                                                                                             | Converts the given color from one colorspace to another.<br/>                                                              |
| [**D2D1SinCos**](d2d1sincos.md)<br/>                                                                                                                                                   | Returns the sine and cosine of an angle.<br/>                                                                              |
| [**D2D1Tan**](d2d1tan.md)<br/>                                                                                                                                                         | Returns the tangent of an angle.<br/>                                                                                      |
| [**D2D1Vec3Length**](d2d1vec3length.md)<br/>                                                                                                                                           | Returns the length of a 3 dimensional vector.<br/>                                                                         |
| [**PD2D1\_PROPERTY\_GET\_FUNCTION**](pd2d1-property-get-function.md)<br/>                                                                                                              | Gets a property from an effect.<br/>                                                                                       |
| [**PD2D1\_PROPERTY\_SET\_FUNCTION**](pd2d1-property-set-function.md)<br/>                                                                                                              | Sets a property on an effect.<br/>                                                                                         |



 

 

 





