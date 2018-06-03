---
title: EN\_CLIPFORMAT notification code
description: Notifies a rich edit control's parent window that a paste occurred with a particular clipboard format. A windowless rich edit control sends this notification by using the ITextHost TxNotify method.
ms.assetid: 79FE1350-4D45-447B-B705-63E966AC7F0E
keywords:
- EN_CLIPFORMAT notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_CLIPFORMAT
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

# EN\_CLIPFORMAT notification code

Notifies a rich edit control's parent window that a paste occurred with a particular clipboard format. A windowless rich edit control sends this notification by using the [**ITextHost::TxNotify**](/windows/desktop/api/Textserv/nf-textserv-itexthost-txnotify) method.


```C++
EN_CLIPFORMAT

      pClipboardFmt = (CLIPBOARDFORMAT *) lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The window ID retrieved by calling the [**GetWindowLong**](https://msdn.microsoft.com/library/windows/desktop/ms633584) function with the GWL\_ID value.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**CLIPBOARDFORMAT**](/windows/desktop/api/Richedit/ns-richedit-_clipboardformat) structure that contains information about the clipboard format.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

To receive EN\_CLIPFORMAT notification codes, specify [**ENM\_CLIPFORMAT**](https://www.bing.com/search?q=**ENM\_CLIPFORMAT**) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**CLIPBOARDFORMAT**](/windows/desktop/api/Richedit/ns-richedit-_clipboardformat)
</dt> </dl>

 

 





