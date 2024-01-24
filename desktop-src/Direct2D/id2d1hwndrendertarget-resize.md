---
title: ID2D1HwndRenderTarget Resize methods (D2d1.h)
description: Changes the size of the render target to the specified pixel size.
ms.assetid: b8ea2e96-c69b-4018-9572-c9099bf6202d
keywords:
- Resize methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1HwndRenderTarget::Resize methods

Changes the size of the render target to the specified pixel size.

### Overload list



| Method                                                                         | Description                                                                    |
|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**Resize(D2D1\_SIZE\_U&)**](/windows/win32/api/d2d1/nf-d2d1-id2d1hwndrendertarget-resize(constd2d1_size_u_))  | Changes the size of the render target to the specified pixel size. <br/> |
| [**Resize(D2D1\_SIZE\_U\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1hwndrendertarget-resize(constd2d1_size_u)) | Changes the size of the render target to the specified pixel size.<br/>  |



## Remarks

After this method is called, the contents of the render target's back-buffer are not defined, even if the [**D2D1\_PRESENT\_OPTIONS\_RETAIN\_CONTENTS**](/windows/win32/api/d2d1/ne-d2d1-d2d1_present_options) option was specified when the render target was created.

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1HwndRenderTarget**](/previous-versions/windows/desktop/legacy/dd371275(v=vs.85))
</dt> </dl>

�

�
