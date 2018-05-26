---
title: Windows Desktop Sharing Interfaces
description: Windows Desktop Sharing provides the following scriptable interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bb1df622-bfcd-4d84-b5f6-780b693cc760
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- Windows Desktop Sharing RDP , interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Windows Desktop Sharing Interfaces

Windows Desktop Sharing provides the following scriptable interfaces.

## In this section

<dl> <dt>

[**\_IRDPSessionEvents**](/windows/win32/RdpEncomAPI/?branch=master)
</dt> <dd>

Implement this interface to receive notifications when events occur.

</dd> <dt>

[**IRDPSRAPIApplication**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiapplication?branch=master)
</dt> <dd>

Groups the sharable windows within a process. Each application object contains a list of window objects. If an application object is shared, all its windows are shared.

</dd> <dt>

[**IRDPSRAPIApplicationFilter**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiapplicationfilter?branch=master)
</dt> <dd>

Manages the shared desktop area at the window and process level. Applications can use the enumerators to display lists of objects in the session that can be shared.

</dd> <dt>

[**IRDPSRAPIApplicationList**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiapplicationlist?branch=master)
</dt> <dd>

Manages the application list.

</dd> <dt>

[**IRDPSRAPIAttendee**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendee?branch=master)
</dt> <dd>

Attendee objects are created as a result of clients connecting to the session and being authenticated. After an attendee object is created, it is automatically added to the attendees list.

</dd> <dt>

[**IRDPSRAPIAttendeeDisconnectInfo**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendeedisconnectinfo?branch=master)
</dt> <dd>

Contains information about the reason an attendee disconnected.

</dd> <dt>

[**IRDPSRAPIAttendeeManager**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendeemanager?branch=master)
</dt> <dd>

Manages attendee objects.

</dd> <dt>

[**IRDPSRAPIAudioStream**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiaudiostream?branch=master)
</dt> <dd>

Enables sending an audio stream from the collaboration sharer Microsoft ActiveX control to collaboration viewer controls.

</dd> <dt>

[**IRDPSRAPIClipboardUseEvents**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiclipboarduseevents?branch=master)
</dt> <dd>

Implement this interface on the sharer side to track or control use of the clipboard. If you do not enable clipboard sharing, this interface has no effect. You need to set a value for the **SetClipboardRedirectCallback** property described in [**Property**](/windows/win32/RdpEncomAPI/nf-rdpencomapi-irdpsrapisessionproperties-get_property?branch=master).

This interface is available starting with Windows 10, version 1511.

</dd> <dt>

[**IRDPSRAPIFrameBuffer**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiframebuffer?branch=master)
</dt> <dd>

Provides data about the frame buffer size and format and allows the contents to be retrieved.

Applications can get a pointer to this interface from the [**FrameBuffer**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiframebuffer?branch=master) property of the [**IRDPSRAPISharingSession2**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapisharingsession2?branch=master) interface.

</dd> <dt>

[**IRDPSRAPIInvitation**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiinvitation?branch=master)
</dt> <dd>

Invitations enable a person or group of persons to connect to a session. When an attendee connects to a session, the client sends a ticket and a password. These two pieces of information are used to authenticate an attendee.

</dd> <dt>

[**IRDPSRAPIInvitationManager**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiinvitationmanager?branch=master)
</dt> <dd>

Manages invitation objects.

</dd> <dt>

[**IRDPSRAPIPerfCounterLogger**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiperfcounterlogger?branch=master)
</dt> <dd>

Enables a client application to implement custom performance logging.

</dd> <dt>

[**IRDPSRAPIPerfCounterLoggingManager**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiperfcounterloggingmanager?branch=master)
</dt> <dd>

Manages [**IRDPSRAPIPerfCounterLogger**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiperfcounterlogger?branch=master) objects.

</dd> <dt>

[**IRDPSRAPISessionProperties**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapisessionproperties?branch=master)
</dt> <dd>

Use this interface to get or set session properties.

</dd> <dt>

[**IRDPSRAPISharingSession**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapisharingsession?branch=master)
</dt> <dd>

The main object that an application must create to start a collaboration session.

</dd> <dt>

[**IRDPSRAPISharingSession2**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapisharingsession2?branch=master)
</dt> <dd>

The main object that an application must create to start a collaboration session.

</dd> <dt>

[**IRDPSRAPITcpConnectionInfo**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapitcpconnectioninfo?branch=master)
</dt> <dd>

Supports the methods to retrieve the TCP connection information on the viewer and on the sharer side.

</dd> <dt>

[**IRDPSRAPITransportStream**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstream?branch=master)
</dt> <dd>

Exposes methods that perform operations with streams.

</dd> <dt>

[**IRDPSRAPITransportStreamBuffer**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstreambuffer?branch=master)
</dt> <dd>

Created and used by the [**IRDPSRAPITransportStream**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstream?branch=master) interface for sending and receiving data.

</dd> <dt>

[**IRDPSRAPITransportStreamEvents**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstreamevents?branch=master)
</dt> <dd>

Exposes methods called by the stream interface ([**IRDPSRAPITransportStream**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstream?branch=master)) to notify the Remote Desktop Protocol (RDP) stack about the completion of events.

</dd> <dt>

[**IRDPSRAPIViewer**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiviewer?branch=master)
</dt> <dd>

The ActiveX interface that is used on the viewer side.

</dd> <dt>

[**IRDPSRAPIVirtualChannel**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapivirtualchannel?branch=master)
</dt> <dd>

Manages the virtual channel.

</dd> <dt>

[**IRDPSRAPIVirtualChannelManager**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapivirtualchannelmanager?branch=master)
</dt> <dd>

Manages the list of virtual channels.

</dd> <dt>

[**IRDPSRAPIWindow**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiwindow?branch=master)
</dt> <dd>

Represents a one-to-one mapping to a sharable window.

</dd> <dt>

[**IRDPSRAPIWindowList**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiwindowlist?branch=master)
</dt> <dd>

Manages the window list.

</dd> <dt>

[**IRDPViewerInputSink**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpviewerinputsink?branch=master)
</dt> <dd>

Sends mouse and keyboard events, and supports touch input.

</dd> <dt>

[**IRDPViewerRenderingSurface**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpviewerrenderingsurface?branch=master)
</dt> <dd>

Manages the rendering surface for the viewer.

</dd> </dl>

 

 




