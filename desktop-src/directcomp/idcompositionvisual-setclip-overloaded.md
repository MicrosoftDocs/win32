---
title: IDCompositionVisual SetClip methods
description: Sets the Clip property of this visual to the specified rectangular region or clip object.
ms.assetid: ACEBA4F9-E1B0-459B-8DC2-272A822AB214
keywords:
- SetClip methods DirectComposition
topic_type:
- apiref
api_location:
- Dcomp.dll
api_type:
- DllExport
ms.date: 07/02/2019
---

# IDCompositionVisual::SetClip methods

Sets the Clip property of this visual to the specified rectangular region or clip object. The Clip property restricts the rendering of the visual subtree that is rooted at this visual to a rectangular region.

### Overload list



| Method                                                                                | Description                                                            |
|:--------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**SetClip(const D2D\_RECT\_F&)**](https://msdn.microsoft.com/en-us/library/Hh449151(v=VS.85).aspx) | Sets the Clip property to the specified rectangular region.<br/> |
| [**SetClip(IDCompositionClip\*)**](https://msdn.microsoft.com/en-us/library/Hh449153(v=VS.85).aspx) | Sets the Clip property to the specified clip object.<br/>        |



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

[Clipping](clipping.md)
</dt> <dt>

[**IDCompositionVisual**](https://msdn.microsoft.com/en-us/library/Hh449139(v=VS.85).aspx)
</dt> </dl>

�

�





