---
title: RB\_DRAGMOVE message
description: Updates the drag position in the rebar control after a previous RB\_BEGINDRAG message.
ms.assetid: 0d2ce7fe-4172-45d9-932b-50f3e4cf2d8e
keywords:
- RB_DRAGMOVE message Windows Controls
topic_type:
- apiref
api_name:
- RB_DRAGMOVE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RB\_DRAGMOVE message

Updates the drag position in the rebar control after a previous [**RB\_BEGINDRAG**](rb-begindrag.md) message.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

**DWORD** value that contains the new mouse coordinates. The horizontal coordinate is contained in the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) and the vertical coordinate is contained in the [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657). If you pass (DWORD)-1, the rebar control will use the position of the mouse the last time the control's thread called [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) or [**PeekMessage**](https://msdn.microsoft.com/library/bb432546).

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**RB\_ENDDRAG**](rb-enddrag.md)
</dt> </dl>

 

 





