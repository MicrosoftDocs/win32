---
Description: Sent when a user performs a pen flick. A window receives this message through its WindowProc function.
ms.assetid: 9433aadf-3440-4249-8f2c-3e22ebc949fb
title: WM\_TABLET\_FLICK message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_TABLET\_FLICK message

Sent when a user performs a pen flick. A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\windowing\windowprocedures\windowprocedurereference\windowprocedurefunctions\windowproc.htm) function.


```C++
#define WM_TABLET_DEFBASE  0x02C0
#define WM_TABLET_FLICK    (WM_TABLET_DEFBASE + 11)     
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A [**FLICK\_DATA Structure**](/windows/desktop/api/tabflicks/ns-tabflicks-flick_data) that contains information about the pen flick that occurred.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**FLICK\_POINT Structure**](/windows/desktop/api/tabflicks/ns-tabflicks-flick_point) that specifies where the pen flick occurred.

</dd> </dl>

## Remarks

A pen flick is a unidirectional pen gesture that requires the user to contact the digitizer in a quick, straight flicking motion. A flick is characterized by high speed and a high degree of straightness. A flick is identified by its direction. Flicks can be made in eight directions corresponding to the cardinal and secondary compass directions.

When a pen flick occurs, Windows first notifies an application by sending a **WM\_TABLET\_FLICK** message, which a window receives through its [*WindowProc*](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\windowing\windowprocedures\windowprocedurereference\windowprocedurefunctions\windowproc.htm) function. Return the **FLICK\_WM\_HANDLED\_MASK** constant, described in [Flicks Constants](flicks-constants.md), to indicate that the application responded to the **WM\_TABLET\_FLICK** message. If the application does not return **FLICK\_WM\_HANDLED\_MASK**, Windows performs the default action specified in the flicks control panel by sending a follow-up notification, such as [**WM\_APPCOMMAND**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\userinput\keyboardinput\keyboardinputreference\keyboardinputmessages\wm_appcommand.htm), [**WM\_VSCROLL**](https://msdn.microsoft.com/VS|Controls|~\controls\scrollbars\scrollbarreference\scrollbarmessages\wm_vscroll.htm), or [**WM\_KEYDOWN**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\userinput\keyboardinput\keyboardinputreference\keyboardinputmessages\wm_keydown.htm), depending on which action is associated with the pen flick.

Use caution when handling the **WM\_TABLET\_FLICK** message. **WM\_TABLET\_FLICK** is passed via the [**SendMessageTimeout**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\windowing\messagesandmessagequeues\messagesandmessagequeuesreference\messagesandmessagequeuesfunctions\sendmessagetimeout.htm) function. If you call methods on a COM interface, that object must be within the same process. If not, COM throws an exception.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Tpcshrd.h</dt> </dl> |



## See also

<dl> <dt>

[**flick\_data structure**](/windows/desktop/api/tabflicks/ns-tabflicks-flick_data)
</dt> <dt>

[**wm\_tablet\_flick message**](wm-tablet-flick-message.md)
</dt> <dt>

[flicks gestures](flicks-gestures.md)
</dt> <dt>

[responding to pen flicks](https://msdn.microsoft.com/d5c6fa9a-b7a3-4097-bf4f-6d540130f715)
</dt> </dl>

 

 




