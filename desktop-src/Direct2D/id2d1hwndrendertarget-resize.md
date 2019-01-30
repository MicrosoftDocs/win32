---
title: ID2D1HwndRenderTarget Resize methods
description: Changes the size of the render target to the specified pixel size.
ms.assetid: 'b8ea2e96-c69b-4018-9572-c9099bf6202d'
keywords: ["Resize methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1HwndRenderTarget::Resize methods

Changes the size of the render target to the specified pixel size.

### Overload list



| Method                                                                         | Description                                                                    |
|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**Resize(D2D1\_SIZE\_U&)**](https://msdn.microsoft.com/en-us/library/Dd371479(v=VS.85).aspx)  | Changes the size of the render target to the specified pixel size. <br/> |
| [**Resize(D2D1\_SIZE\_U\*)**](https://msdn.microsoft.com/en-us/library/Dd371474(v=VS.85).aspx) | Changes the size of the render target to the specified pixel size.<br/>  |



## Remarks

After this method is called, the contents of the render target's back-buffer are not defined, even if the [**D2D1\_PRESENT\_OPTIONS\_RETAIN\_CONTENTS**](https://msdn.microsoft.com/en-us/library/Dd368144(v=VS.85).aspx) option was specified when the render target was created.

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1HwndRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371275(v=VS.85).aspx)
</dt> </dl>

�

�





