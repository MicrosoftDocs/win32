---
title: IDCompositionVisual3 SetTransform methods
description: Sets the Transform property of this visual. The Transform property specifies a 3D transform used to modify the coordinate system of this visual. The property can specify either a 4-by-4 transform matrix or a transform object.
ms.assetid: a59498c2-8659-dd35-8dc2-87457f493965
keywords:
- SetTransform methods DirectComposition
topic_type:
- apiref
api_location:
- Dcomp.dll
api_type:
- DllExport
ms.date: 07/02/2019
---

# IDCompositionVisual3::SetTransform methods

Sets the Transform property of this visual. The Transform property specifies a 3D transform used to modify the coordinate system of this visual. The property can specify either a 4-by-4 transform matrix or a transform object.

### Overload list



| Method                                                                                  | Description                                                                    |
|:----------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**SetTransform(D2D\_MATRIX\_4X4\_F&)**](https://msdn.microsoft.com/en-us/library/Dn904492(v=VS.85).aspx)       | Sets the Transform property to the specified transform matrix.<br/>      |
| [**SetTransform(IDCompositionTransform3D\*)**](https://msdn.microsoft.com/en-us/library/Dn904493(v=VS.85).aspx) | Sets the Transform property to the specified transformation object.<br/> |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server�2012 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Dcomp.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Dcomp.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dcomp.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDCompositionVisual3**](https://msdn.microsoft.com/en-us/library/Dn904490(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionMatrixTransform**](https://msdn.microsoft.com/en-us/library/Hh437424(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionRotateTransform**](https://msdn.microsoft.com/en-us/library/Hh448924(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionScaleTransform**](https://msdn.microsoft.com/en-us/library/Hh448990(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionSkewTransform**](https://msdn.microsoft.com/en-us/library/Hh449057(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionTransform**](https://msdn.microsoft.com/en-us/library/Hh449110(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionTranslateTransform**](https://msdn.microsoft.com/en-us/library/Hh449113(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionVisual**](https://msdn.microsoft.com/en-us/library/Hh449139(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionVisual::SetOffsetX**](idcompositionvisual-setoffsetx-overloaded.md)
</dt> <dt>

[**IDCompositionVisual::SetOffsetY**](idcompositionvisual-setoffsety-overloaded.md)
</dt> </dl>

�

�





