---
title: EM_REQUESTRESIZE message
description: Forces a rich edit control to send an EN\_REQUESTRESIZE notification code to its parent window.
ms.assetid: efc22771-9b9f-4a30-a906-f02095607c21
keywords:
- EM_REQUESTRESIZE message Windows Controls
topic_type:
- apiref
api_name:
- EM_REQUESTRESIZE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EM\_REQUESTRESIZE message

Forces a rich edit control to send an [**EN\_REQUESTRESIZE**](en-requestresize.md) notification code to its parent window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

This message is useful during [**WM\_SIZE**](https://msdn.microsoft.com/library/windows/desktop/ms632646) processing for the parent of a bottomless rich edit control.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EN\_REQUESTRESIZE**](en-requestresize.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_SIZE**](https://msdn.microsoft.com/library/windows/desktop/ms632646)
</dt> </dl>

 

 





