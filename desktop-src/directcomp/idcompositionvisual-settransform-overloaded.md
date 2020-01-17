---
title: IDCompositionVisual SetTransform methods (Dcomp.h)
description: Sets the Transform property of this visual. The Transform property specifies a 2D transform used to modify the coordinate system of this visual. The property can specify either a 3-by-2 transform matrix or a transform object.
ms.assetid: DA3CBBB6-DB0A-4FCE-9DAC-7A767783A18D
keywords:
- SetTransform methods DirectComposition
topic_type:
- apiref
api_location:
- Dcomp.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# IDCompositionVisual::SetTransform methods

Sets the Transform property of this visual. The Transform property specifies a 2D transform used to modify the coordinate system of this visual. The property can specify either a 3-by-2 transform matrix or a transform object.

### Overload list



| Method                                                                                                    | Description                                                                    |
|:----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**SetTransform(D2D\_MATRIX\_3X2\_F&)**](https://msdn.microsoft.com/library/Hh449174(v=VS.85).aspx)          | Sets the Transform property to the specified transform matrix.<br/>      |
| [**SetTransform(IDCompositionTransform\*)**](https://msdn.microsoft.com/library/Hh449176(v=VS.85).aspx) | Sets the Transform property to the specified transformation object.<br/> |



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

[**IDCompositionMatrixTransform**](https://msdn.microsoft.com/library/Hh437424(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionRotateTransform**](https://msdn.microsoft.com/library/Hh448924(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionScaleTransform**](https://msdn.microsoft.com/library/Hh448990(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionSkewTransform**](https://msdn.microsoft.com/library/Hh449057(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionTransform**](https://msdn.microsoft.com/library/Hh449110(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionTranslateTransform**](https://msdn.microsoft.com/library/Hh449113(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionVisual**](https://msdn.microsoft.com/library/Hh449139(v=VS.85).aspx)
</dt> <dt>

[**IDCompositionVisual::SetOffsetX**](idcompositionvisual-setoffsetx-overloaded.md)
</dt> <dt>

[**IDCompositionVisual::SetOffsetY**](idcompositionvisual-setoffsety-overloaded.md)
</dt> </dl>

�

�





