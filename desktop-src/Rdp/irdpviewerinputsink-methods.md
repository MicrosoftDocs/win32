---
title: IRDPViewerInputSink Methods
description: The IRDPViewerInputSink interface exposes the following methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3D7917B2-6076-47BC-B0AF-20EDF46846B1
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IRDPViewerInputSink Methods

\[The [**IRDPViewerInputSink**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpviewerinputsink) interface is no longer available for use for UWP applications as of Windows 10, version 1709. It is still supported for Desktop apps.\]

The [**IRDPViewerInputSink**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpviewerinputsink) interface exposes the following methods.

## In this section

<dl> <dt>

[**AddTouchInput method**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpviewerinputsink-addtouchinput)
</dt> <dd>

Accepts a description of a touch input.

</dd> <dt>

[**BeginTouchFrame method**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpviewerinputsink-begintouchframe)
</dt> <dd>

Begins to accept a series of touch inputs.

</dd> <dt>

[**EndTouchFrame method**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpviewerinputsink-endtouchframe)
</dt> <dd>

Stops to accept a series of touch inputs.

</dd> <dt>

[**SendKeyboardEvent method**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpviewerinputsink-sendkeyboardevent)
</dt> <dd>

Sends a keyboard event message.

</dd> <dt>

[**SendMouseButtonEvent method**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpviewerinputsink-sendmousebuttonevent)
</dt> <dd>

Sends a mouse button event message.

</dd> <dt>

[**SendMouseMoveEvent method**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpviewerinputsink-sendmousemoveevent)
</dt> <dd>

Sends a mouse move event message.

</dd> <dt>

[**SendMouseWheelEvent method**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpviewerinputsink-sendmousewheelevent)
</dt> <dd>

Sends a mouse wheel event message.

</dd> <dt>

[**SendSyncEvent method**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpviewerinputsink-sendsyncevent)
</dt> <dd>

Sends an event message to indicate a change in the state of the keyboard, such as when the Caps Lock key is pressed.

</dd> </dl>

 

 




