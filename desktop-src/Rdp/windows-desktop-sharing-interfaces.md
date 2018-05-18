---
title: Windows Desktop Sharing Interfaces
description: Windows Desktop Sharing provides the following scriptable interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bb1df622-bfcd-4d84-b5f6-780b693cc760'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["Windows Desktop Sharing RDP , interfaces"]
---

# Windows Desktop Sharing Interfaces

Windows Desktop Sharing provides the following scriptable interfaces.

## In this section

<dl> <dt>

[**\_IRDPSessionEvents**](-irdpsessionevents.md)
</dt> <dd>

Implement this interface to receive notifications when events occur.

</dd> <dt>

[**IRDPSRAPIApplication**](irdpsrapiapplication.md)
</dt> <dd>

Groups the sharable windows within a process. Each application object contains a list of window objects. If an application object is shared, all its windows are shared.

</dd> <dt>

[**IRDPSRAPIApplicationFilter**](irdpsrapiapplicationfilter.md)
</dt> <dd>

Manages the shared desktop area at the window and process level. Applications can use the enumerators to display lists of objects in the session that can be shared.

</dd> <dt>

[**IRDPSRAPIApplicationList**](irdpsrapiapplicationlist.md)
</dt> <dd>

Manages the application list.

</dd> <dt>

[**IRDPSRAPIAttendee**](irdpsrapiattendee.md)
</dt> <dd>

Attendee objects are created as a result of clients connecting to the session and being authenticated. After an attendee object is created, it is automatically added to the attendees list.

</dd> <dt>

[**IRDPSRAPIAttendeeDisconnectInfo**](irdpsrapiattendeedisconnectinfo.md)
</dt> <dd>

Contains information about the reason an attendee disconnected.

</dd> <dt>

[**IRDPSRAPIAttendeeManager**](irdpsrapiattendeemanager.md)
</dt> <dd>

Manages attendee objects.

</dd> <dt>

[**IRDPSRAPIAudioStream**](irdpsrapiaudiostream.md)
</dt> <dd>

Enables sending an audio stream from the collaboration sharer Microsoft ActiveX control to collaboration viewer controls.

</dd> <dt>

[**IRDPSRAPIClipboardUseEvents**](irdpsrapiclipboarduseevents.md)
</dt> <dd>

Implement this interface on the sharer side to track or control use of the clipboard. If you do not enable clipboard sharing, this interface has no effect. You need to set a value for the **SetClipboardRedirectCallback** property described in [**Property**](irdpsrapisessionproperties-property.md).

This interface is available starting with Windows 10, version 1511.

</dd> <dt>

[**IRDPSRAPIFrameBuffer**](irdpsrapiframebuffer.md)
</dt> <dd>

Provides data about the frame buffer size and format and allows the contents to be retrieved.

Applications can get a pointer to this interface from the [**FrameBuffer**](irdpsrapiframebuffer.md) property of the [**IRDPSRAPISharingSession2**](irdpsrapisharingsession2.md) interface.

</dd> <dt>

[**IRDPSRAPIInvitation**](irdpsrapiinvitation.md)
</dt> <dd>

Invitations enable a person or group of persons to connect to a session. When an attendee connects to a session, the client sends a ticket and a password. These two pieces of information are used to authenticate an attendee.

</dd> <dt>

[**IRDPSRAPIInvitationManager**](irdpsrapiinvitationmanager.md)
</dt> <dd>

Manages invitation objects.

</dd> <dt>

[**IRDPSRAPIPerfCounterLogger**](irdpsrapiperfcounterlogger.md)
</dt> <dd>

Enables a client application to implement custom performance logging.

</dd> <dt>

[**IRDPSRAPIPerfCounterLoggingManager**](irdpsrapiperfcounterloggingmanager.md)
</dt> <dd>

Manages [**IRDPSRAPIPerfCounterLogger**](irdpsrapiperfcounterlogger.md) objects.

</dd> <dt>

[**IRDPSRAPISessionProperties**](irdpsrapisessionproperties.md)
</dt> <dd>

Use this interface to get or set session properties.

</dd> <dt>

[**IRDPSRAPISharingSession**](irdpsrapisharingsession.md)
</dt> <dd>

The main object that an application must create to start a collaboration session.

</dd> <dt>

[**IRDPSRAPISharingSession2**](irdpsrapisharingsession2.md)
</dt> <dd>

The main object that an application must create to start a collaboration session.

</dd> <dt>

[**IRDPSRAPITcpConnectionInfo**](irdpsrapitcpconnectioninfo.md)
</dt> <dd>

Supports the methods to retrieve the TCP connection information on the viewer and on the sharer side.

</dd> <dt>

[**IRDPSRAPITransportStream**](irdpsrapitransportstream.md)
</dt> <dd>

Exposes methods that perform operations with streams.

</dd> <dt>

[**IRDPSRAPITransportStreamBuffer**](irdpsrapitransportstreambuffer.md)
</dt> <dd>

Created and used by the [**IRDPSRAPITransportStream**](irdpsrapitransportstream.md) interface for sending and receiving data.

</dd> <dt>

[**IRDPSRAPITransportStreamEvents**](irdpsrapitransportstreamevents.md)
</dt> <dd>

Exposes methods called by the stream interface ([**IRDPSRAPITransportStream**](irdpsrapitransportstream.md)) to notify the Remote Desktop Protocol (RDP) stack about the completion of events.

</dd> <dt>

[**IRDPSRAPIViewer**](irdpsrapiviewer.md)
</dt> <dd>

The ActiveX interface that is used on the viewer side.

</dd> <dt>

[**IRDPSRAPIVirtualChannel**](irdpsrapivirtualchannel.md)
</dt> <dd>

Manages the virtual channel.

</dd> <dt>

[**IRDPSRAPIVirtualChannelManager**](irdpsrapivirtualchannelmanager.md)
</dt> <dd>

Manages the list of virtual channels.

</dd> <dt>

[**IRDPSRAPIWindow**](irdpsrapiwindow.md)
</dt> <dd>

Represents a one-to-one mapping to a sharable window.

</dd> <dt>

[**IRDPSRAPIWindowList**](irdpsrapiwindowlist.md)
</dt> <dd>

Manages the window list.

</dd> <dt>

[**IRDPViewerInputSink**](irdpviewerinputsink.md)
</dt> <dd>

Sends mouse and keyboard events, and supports touch input.

</dd> <dt>

[**IRDPViewerRenderingSurface**](irdpviewerrenderingsurface.md)
</dt> <dd>

Manages the rendering surface for the viewer.

</dd> </dl>

 

 




