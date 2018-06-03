---
title: EN\_DROPFILES notification code
description: Notifies a rich edit control parent window that the user is attempting to drop files into the control. A rich edit control sends this notification code in the form of a WM\_NOTIFY message when it receives the WM\_DROPFILES message.
ms.assetid: fcae0ff8-ce37-4c71-b14c-cbd6429b4ab3
keywords:
- EN_DROPFILES notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_DROPFILES
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

# EN\_DROPFILES notification code

Notifies a rich edit control parent window that the user is attempting to drop files into the control. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message when it receives the [**WM\_DROPFILES**](https://msdn.microsoft.com/library/windows/desktop/bb774303) message.


```C++
EN_DROPFILES

      penDropFiles = (ENDROPFILES *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

An [**ENDROPFILES**](/windows/desktop/api/Richedit/ns-richedit-_endropfiles) structure that receives dropped files information.

</dd> </dl>

## Return value

Return a nonzero value to allow the drop operation.

Return zero to ignore the drop operation.

## Remarks

For a rich edit control to receive [**WM\_DROPFILES**](https://msdn.microsoft.com/library/windows/desktop/bb774303) messages, the parent window must register the control as a drop target by using the [**DragAcceptFiles**](https://msdn.microsoft.com/library/windows/desktop/bb776406) function. The control does not register itself.

To receive EN\_DROPFILES notification codes, specify [**ENM\_DROPFILES**](https://www.bing.com/search?q=**ENM\_DROPFILES**) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

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

[**ENDROPFILES**](/windows/desktop/api/Richedit/ns-richedit-_endropfiles)
</dt> </dl>

 

 





