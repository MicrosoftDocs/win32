---
title: Direct2D functions
description: Direct2D provides the following functions.
ms.assetid: '1a7ae962-9b70-442c-a676-f172a2d9bfd3'
keywords:
- Direct2D,functions
ms.topic: article
ms.date: 09/19/2019
---

# Direct2D functions

Direct2D provides the following functions. Additional functions are defined in the [D2D1 Namespace](d2d1-namespace.md).

## In this section

| Topic | Description |
|-|-|
| [**D2D1ComputeMaximumScaleFactor**](/windows/desktop/api/d2d1_2/nf-d2d1_2-d2d1computemaximumscalefactor) | Computes the maximum factor by which a given transform can stretch any vector. |
| [**D2D1CreateDevice**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1createdevice) | Creates a new Direct2D device associated with the provided DXGI device.  |
| [**D2D1CreateDeviceContext**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1createdevicecontext) | Creates a new Direct2D device context associated with a DXGI surface.  |
| [**D2D1CreateFactory(D2D1_FACTORY_TYPE,REFIID,void\*\*)**](/windows/win32/api/d2d1/nf-d2d1-d2d1createfactory-r1) | Creates a factory object that can be used to create Direct2D resources. |
| [**D2D1CreateFactory(D2D1_FACTORY_TYPE,REFIID,D2D1_FACTORY_OPTIONS\*,void\*\*)**](/windows/desktop/api/d2d1/nf-d2d1-d2d1createfactory) | Creates a factory object that can be used to create Direct2D resources. |
| [**D2D1GetGradientMeshInteriorPointsFromCoonsPatch**](/windows/desktop/api/d2d1_3/nf-d2d1_3-d2d1getgradientmeshinteriorpointsfromcoonspatch) | Returns the interior points for a gradient mesh patch based on the points defining a Coons patch. |
| [**D2D1InvertMatrix**](/windows/desktop/api/d2d1/nf-d2d1-d2d1invertmatrix) | Tries to invert the specified matrix. |
| [**D2D1IsMatrixInvertible**](/windows/desktop/api/d2d1/nf-d2d1-d2d1ismatrixinvertible) | Indicates whether the specified matrix is invertible. |
| [**D2D1MakeRotateMatrix**](/windows/desktop/api/d2d1/nf-d2d1-d2d1makerotatematrix) | Creates a rotation transformation that rotates by the specified angle about the specified point. |
| [**D2D1MakeSkewMatrix**](/windows/desktop/api/d2d1/nf-d2d1-d2d1makeskewmatrix) | Creates a skew transformation that has the specified x-axis angle, y-axis angle, and center point.  |
| [**operator\* (const D2D1\MATRIX\3X2\F&,const D2D1\MATRIX\3X2\F&)**](/windows/win32/api/d2d1helper/nf-d2d1helper-matrix3x2f-setproduct) | Multiplies two matrices and returns the result. |
| [**BlobGetter**](blobgetter.md) | Calls a member-function property getter callback for a blob-type property. |
| [**BlobSetter**](blobsetter.md) | Calls a member-function property setter callback for a blob-type property. |
| [**DeducingBlobGetter**](deducingblobgetter.md) | Deduces the class and arguments and then calls a member-function property getter callback for a blob-type property. |
| [**DeducingBlobSetter**](deducingblobsetter.md) | Deduces the class and arguments and then calls a member-function property setter callback for a blob-type property. |
| [**DeducingStringGetter**](deducingstringgetter.md) | Deduces the class and arguments and then calls a member-function property getter callback for a string-type property. |
| [**DeducingStringSetter**](deducingstringsetter.md) | Deduces the class and arguments and then calls a member-function property setter callback for a string-type property. |
| [**DeducingValueGetter**](deducingvaluegetter.md) | Deduces the class and arguments and then calls a member-function property getter callback for a value-type property. |
| [**DeducingValueSetter**](deducingvaluesetter.md) | Deduces the class and arguments and then calls a member-function property setter callback for a value-type property. |
| [**GetType**](/previous-versions/windows/desktop/legacy/hh847962(v=vs.85)) | Retrieves the type of the given property. |
| [**StringGetter**](/windows/desktop/api/d2d1effecthelpers/nf-d2d1effecthelpers-stringgetter) | Calls a member-function property getter callback for a string-type property. |
| [**StringSetter**](/windows/desktop/api/d2d1effecthelpers/nf-d2d1effecthelpers-stringsetter) | Calls a member-function property setter callback for a string-type property. |
| [**ValueGetter**](/windows/desktop/api/d2d1effecthelpers/nf-d2d1effecthelpers-valuegetter) | Calls a member-function property setter callback for a value-type property. |
| [**ValueSetter**](/windows/desktop/api/d2d1effecthelpers/nf-d2d1effecthelpers-valuesetter) | Calls a member-function property setter callback for a value-type property. |
| [**D2D1ConvertColorSpace**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1convertcolorspace) | Converts the given color from one colorspace to another. |
| [**D2D1SinCos**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1sincos) | Returns the sine and cosine of an angle. |
| [**D2D1Tan**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1tan) | Returns the tangent of an angle. |
| [**D2D1Vec3Length**](/windows/desktop/api/d2d1_1/nf-d2d1_1-d2d1vec3length) | Returns the length of a 3 dimensional vector. |
| [**PD2D1\PROPERTY\GET\FUNCTION**](/windows/desktop/api/D2d1effectauthor/nc-d2d1effectauthor-pd2d1_property_get_function) | Gets a property from an effect. |
| [**PD2D1\PROPERTY\SET\FUNCTION**](/windows/desktop/api/D2d1effectauthor/nc-d2d1effectauthor-pd2d1_property_set_function) | Sets a property on an effect. |