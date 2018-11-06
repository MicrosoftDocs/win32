---
title: EN_LINK notification code
description: A rich edit control sends EN\_LINK notification codes when it receives various messages, for example, when the user clicks the mouse or when the mouse pointer is over text that has the CFE\_LINK effect.
ms.assetid: 67f02908-957e-4d91-8a70-70399ce9cf2e
keywords:
- EN_LINK notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_LINK
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# EN\_LINK notification code

A rich edit control sends EN\_LINK notification codes when it receives various messages, for example, when the user clicks the mouse or when the mouse pointer is over text that has the **CFE\_LINK** effect. A windowless rich edit control sends this notification by using the [**ITextHost::TxNotify**](/windows/desktop/api/Textserv/nf-textserv-itexthost-txnotify) method. The parent window of the control receives this notification code through a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_LINK

    penLink = (ENLINK *) lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The window ID retrieved by calling the [**GetWindowLong**](https://msdn.microsoft.com/library/windows/desktop/ms633584) function with the GWL\_ID value.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**ENLINK**](/windows/desktop/api/Richedit/ns-richedit-_enlink) structure. The structure contains an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-_nmhdr) structure, information about the notification code, and a [**CHARRANGE**](/windows/desktop/api/Richedit/ns-richedit-_charrange) structure that indicates the range of characters that have the **CFE\_LINK** effect.

</dd> </dl>

## Return value

Return zero to allow the control to proceed with its normal handling of the message.

Return a nonzero value to prevent the control from handling the message.

**Windows 8**: Return **EN\_LINK\_DO\_DEFAULT** to direct the rich edit control to perform the default action.

## Remarks

To receive **EN\_LINK** notification codes when the link has focus, specify the [**ENM\_LINK**](rich-edit-control-event-mask-flags.md) flag in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

If the link has no focus, to receive **EN\_LINK** notification codes specify the **SES\_NOFOCUSLINKNOTIFY** flag in the mask sent with the [**EM\_SETEDITSTYLE**](em-seteditstyle.md) message.

A rich edit control sends **EN\_LINK** notification codes when it receives the following messages while the mouse pointer is over text that has the **CFE\_LINK** effect:

-   [**WM\_LBUTTONDBLCLK**](https://msdn.microsoft.com/library/windows/desktop/ms645606)
-   [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607)
-   [**WM\_LBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms645608)
-   [**WM\_MOUSEMOVE**](https://msdn.microsoft.com/library/windows/desktop/ms645616)
-   [**WM\_RBUTTONDBLCLK**](https://msdn.microsoft.com/library/windows/desktop/ms646241)
-   [**WM\_RBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646242)
-   [**WM\_RBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms646243)
-   [**WM\_SETCURSOR**](https://msdn.microsoft.com/library/windows/desktop/ms648382)

The **CFE\_LINK** effect typically identifies a range of text that contains an URL. Applications can handle the EN\_LINK notification code by changing the mouse pointer when it is over the URL, or by starting a browser to view the location identified by the URL.

If you send the [**EM\_AUTOURLDETECT**](em-autourldetect.md) message to enable automatic URL detection, the rich edit control automatically sets the **CFE\_LINK** effect for modified text that it identifies as a URL.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**CHARRANGE**](/windows/desktop/api/Richedit/ns-richedit-_charrange)
</dt> <dt>

[**EM\_AUTOURLDETECT**](em-autourldetect.md)
</dt> <dt>

[**ENLINK**](/windows/desktop/api/Richedit/ns-richedit-_enlink)
</dt> <dt>

[**ITextRange2::SetURL**](/windows/desktop/api/Tom/nf-tom-itextrange2-seturl)
</dt> <dt>

[**NMHDR**](/windows/desktop/api/richedit/ns-richedit-_nmhdr)
</dt> </dl>

 

 





