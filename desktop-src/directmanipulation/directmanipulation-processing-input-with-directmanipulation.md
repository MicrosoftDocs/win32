---
Description: 'This section provides an overview of the Direct Manipulation threading model, how window messages are processed by Direct Manipulation, and how the state of a viewport changes as input is mapped to output motions.'
ms.assetid: '0818E34E-990E-4C36-9954-EF87EB226AF6'
title: Processing input with DirectManipulation
---

# Processing input with DirectManipulation

This section provides an overview of the [Direct Manipulation](direct-manipulation-portal.md) threading model, how window messages are processed by Direct Manipulation, and how the state of a viewport changes as input is mapped to output motions.

-   [Input flow](#input-flow)
-   [Remarks](#remarks)

[Direct Manipulation](direct-manipulation-portal.md) uses two threads to coordinate asynchronous operations:

*UI thread* - the thread that owns the **HWND** associated with input. This thread owns initialization of [Direct Manipulation](direct-manipulation-portal.md). Mouse and keyboard input processing also happens on the UI thread.

*Delegate thread* - the thread created and owned by [Direct Manipulation](direct-manipulation-portal.md). Touch input processing happens on the delegate thread.

## Input flow

In a typical configuration where hit testing is done on the UI thread, window messages are processed by [Direct Manipulation](direct-manipulation-portal.md) in the following order:

![diagram showing the order in which messages are processed.](images/inputprocessing.png)

For a viewport at rest:

1.  A series of window messages reach the delegate thread.
2.  [**WM\_POINTERDOWN**](inputmsg.wm_pointerdown) and [**DM\_POINTERHITTEST**](inputmsg.dm_pointerhittest) messages are sent by the delegate thread to the Independent Hit Test (IHT) thread.
3.  If [**SetContact**](idirectmanipulationviewport-setcontact.md) is called from the IHT thread, messages might get sent to the UI thread by the delegate thread, depending on the value of [**DIRECTMANIPULATION\_HITTEST\_TYPE**](directmanipulation-hittest-type.md) when [**RegisterHitTestTarget**](idirectmanipulationmanager-registerhittesttarget.md) was called.
4.  If [**SetContact**](idirectmanipulationviewport-setcontact.md) is not called from the IHT thread, messages are always sent by the delegate thread to the UI thread.
5.  The client can call [**SetContact**](idirectmanipulationviewport-setcontact.md) from the UI thread to let [Direct Manipulation](direct-manipulation-portal.md) detect a manipulation.
6.  If a manipulation is detected, [Direct Manipulation](direct-manipulation-portal.md) sends a [**WM\_POINTERCAPTURECHANGED**](inputmsg.wm_pointercapturechanged) message to notify the client that the input is being handled by Direct Manipulation. The viewport status is set to **RUNNING** and the output transform will be updated.
7.  If an interaction other than a manipulation is detected, [Direct Manipulation](direct-manipulation-portal.md) sends remaining messages to the UI thread.

For a viewport in motion (with a status of RUNNING or INERTIA), the window message reaches the delegate thread first, where [Direct Manipulation](direct-manipulation-portal.md) hit tests against all running viewports. Direct Manipulation automatically assigns the contact to the appropriate viewports identified by hit testing. The viewport status is RUNNING and the output transform will be updated.

In some cases, an application UI thread may be too slow to respond to hit testing. A hit test thread may be used ([**RegisterHitTestTarget**](idirectmanipulationmanager-registerhittesttarget.md)) to allow the client to move [**WM\_POINTERDOWN**](inputmsg.wm_pointerdown) and [**DM\_POINTERHITTEST**](inputmsg.dm_pointerhittest) messages to a specific thread to allow for hit testing.

## Remarks

Typically, [Direct Manipulation](direct-manipulation-portal.md) sends only [**WM\_POINTERDOWN**](inputmsg.wm_pointerdown) and [**DM\_POINTERHITTEST**](inputmsg.dm_pointerhittest) messages to the UI thread, withholding later messages while waiting for a response from the client. If the client calls [**SetContact**](idirectmanipulationviewport-setcontact.md), the only messages the UI thread receives when a manipulation is detected are **WM\_POINTERDOWN**,**DM\_POINTERHITTEST**, and [**WM\_POINTERCAPTURECHANGED**](inputmsg.wm_pointercapturechanged).

The client might not call [**SetContact**](idirectmanipulationviewport-setcontact.md) when processing [**WM\_POINTERDOWN**](inputmsg.wm_pointerdown) and [**DM\_POINTERHITTEST**](inputmsg.dm_pointerhittest) messages. In this case, [Direct Manipulation](direct-manipulation-portal.md) sends all messages to the UI thread without analyzing the messages to see if there is a manipulation. The client can then choose any point to call **SetContact** and have Direct Manipulation start detecting manipulations, and send [**WM\_POINTERCAPTURECHANGED**](inputmsg.wm_pointercapturechanged) messages when one is detected.

**Windows 10 and later:** You can decide which manipulations you want to handle by calling [**DeferContact**](idirectmanipulationdefercontactservice-defercontact.md) before calling [**SetContact**](idirectmanipulationviewport-setcontact.md) on a [**WM\_POINTERDOWN**](inputmsg.wm_pointerdown) or [**DM\_POINTERHITTEST**](inputmsg.dm_pointerhittest) message. **DeferContact** ensures all subsequent messages are sent to the UI thread for the specified period of time.

 

 



