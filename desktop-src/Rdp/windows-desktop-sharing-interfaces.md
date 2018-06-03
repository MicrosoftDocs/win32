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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Desktop Sharing Interfaces

Windows Desktop Sharing provides the following scriptable interfaces.

## In this section

<dl> <dt>

[**\_IRDPSessionEvents**](/windows/desktop/api/RdpEncomAPI/)
</dt> <dd>

Implement this interface to receive notifications when events occur.

</dd> <dt>

[**IRDPSRAPIApplication**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiapplication)
</dt> <dd>

Groups the sharable windows within a process. Each application object contains a list of window objects. If an application object is shared, all its windows are shared.

</dd> <dt>

[**IRDPSRAPIApplicationFilter**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiapplicationfilter)
</dt> <dd>

Manages the shared desktop area at the window and process level. Applications can use the enumerators to display lists of objects in the session that can be shared.

</dd> <dt>

[**IRDPSRAPIApplicationList**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiapplicationlist)
</dt> <dd>

Manages the application list.

</dd> <dt>

[**IRDPSRAPIAttendee**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendee)
</dt> <dd>

Attendee objects are created as a result of clients connecting to the session and being authenticated. After an attendee object is created, it is automatically added to the attendees list.

</dd> <dt>

[**IRDPSRAPIAttendeeDisconnectInfo**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendeedisconnectinfo)
</dt> <dd>

Contains information about the reason an attendee disconnected.

</dd> <dt>

[**IRDPSRAPIAttendeeManager**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendeemanager)
</dt> <dd>

Manages attendee objects.

</dd> <dt>

[**IRDPSRAPIAudioStream**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiaudiostream)
</dt> <dd>

Enables sending an audio stream from the collaboration sharer Microsoft ActiveX control to collaboration viewer controls.

</dd> <dt>

[**IRDPSRAPIClipboardUseEvents**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiclipboarduseevents)
</dt> <dd>

Implement this interface on the sharer side to track or control use of the clipboard. If you do not enable clipboard sharing, this interface has no effect. You need to set a value for the **SetClipboardRedirectCallback** property described in [**Property**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpsrapisessionproperties-get_property).

This interface is available starting with Windows 10, version 1511.

</dd> <dt>

[**IRDPSRAPIFrameBuffer**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiframebuffer)
</dt> <dd>

Provides data about the frame buffer size and format and allows the contents to be retrieved.

Applications can get a pointer to this interface from the [**FrameBuffer**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiframebuffer) property of the [**IRDPSRAPISharingSession2**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapisharingsession2) interface.

</dd> <dt>

[**IRDPSRAPIInvitation**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiinvitation)
</dt> <dd>

Invitations enable a person or group of persons to connect to a session. When an attendee connects to a session, the client sends a ticket and a password. These two pieces of information are used to authenticate an attendee.

</dd> <dt>

[**IRDPSRAPIInvitationManager**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiinvitationmanager)
</dt> <dd>

Manages invitation objects.

</dd> <dt>

[**IRDPSRAPIPerfCounterLogger**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiperfcounterlogger)
</dt> <dd>

Enables a client application to implement custom performance logging.

</dd> <dt>

[**IRDPSRAPIPerfCounterLoggingManager**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiperfcounterloggingmanager)
</dt> <dd>

Manages [**IRDPSRAPIPerfCounterLogger**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiperfcounterlogger) objects.

</dd> <dt>

[**IRDPSRAPISessionProperties**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapisessionproperties)
</dt> <dd>

Use this interface to get or set session properties.

</dd> <dt>

[**IRDPSRAPISharingSession**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapisharingsession)
</dt> <dd>

The main object that an application must create to start a collaboration session.

</dd> <dt>

[**IRDPSRAPISharingSession2**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapisharingsession2)
</dt> <dd>

The main object that an application must create to start a collaboration session.

</dd> <dt>

[**IRDPSRAPITcpConnectionInfo**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapitcpconnectioninfo)
</dt> <dd>

Supports the methods to retrieve the TCP connection information on the viewer and on the sharer side.

</dd> <dt>

[**IRDPSRAPITransportStream**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstream)
</dt> <dd>

Exposes methods that perform operations with streams.

</dd> <dt>

[**IRDPSRAPITransportStreamBuffer**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstreambuffer)
</dt> <dd>

Created and used by the [**IRDPSRAPITransportStream**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstream) interface for sending and receiving data.

</dd> <dt>

[**IRDPSRAPITransportStreamEvents**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstreamevents)
</dt> <dd>

Exposes methods called by the stream interface ([**IRDPSRAPITransportStream**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapitransportstream)) to notify the Remote Desktop Protocol (RDP) stack about the completion of events.

</dd> <dt>

[**IRDPSRAPIViewer**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiviewer)
</dt> <dd>

The ActiveX interface that is used on the viewer side.

</dd> <dt>

[**IRDPSRAPIVirtualChannel**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapivirtualchannel)
</dt> <dd>

Manages the virtual channel.

</dd> <dt>

[**IRDPSRAPIVirtualChannelManager**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapivirtualchannelmanager)
</dt> <dd>

Manages the list of virtual channels.

</dd> <dt>

[**IRDPSRAPIWindow**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiwindow)
</dt> <dd>

Represents a one-to-one mapping to a sharable window.

</dd> <dt>

[**IRDPSRAPIWindowList**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiwindowlist)
</dt> <dd>

Manages the window list.

</dd> <dt>

[**IRDPViewerInputSink**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpviewerinputsink)
</dt> <dd>

Sends mouse and keyboard events, and supports touch input.

</dd> <dt>

[**IRDPViewerRenderingSurface**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpviewerrenderingsurface)
</dt> <dd>

Manages the rendering surface for the viewer.

</dd> </dl>

 

 




