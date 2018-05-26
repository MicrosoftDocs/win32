---
title: Remote Desktop Services API Functions
description: The following functions are used with Remote Desktop Services.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e99a86ee-af0e-46db-8dad-69703ca84fa0
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Desktop Services API Functions

The following functions are used with Remote Desktop Services.

## In this section

<dl> <dt>

[**ProcessIdToSessionId**](/windows/win32/Winbase/?branch=master)
</dt> <dd>

Retrieves the Remote Desktop Services session associated with a specified process.

</dd> <dt>

[**TLSConnectToLsServer**](tlsconnecttolsserver.md)
</dt> <dd>

Opens a handle to the specified Remote Desktop license server.

</dd> <dt>

[**TLSDisconnectFromServer**](tlsdisconnectfromserver.md)
</dt> <dd>

Closes an open handle to a Remote Desktop license server.

</dd> <dt>

[**TLSGetServerCertificate**](tlsgetservercertificate.md)
</dt> <dd>

Returns the certificate of the Remote Desktop license server.

</dd> <dt>

[**TLSKeyPackEnumBegin**](tlskeypackenumbegin.md)
</dt> <dd>

Begins enumeration through all key packs that are installed on a Remote Desktop license server based on search criteria.

</dd> <dt>

[**TLSKeyPackEnumEnd**](tlskeypackenumend.md)
</dt> <dd>

Continues from a previous call to the [**TLSKeyPackEnumBegin**](tlskeypackenumbegin.md) function and terminates the enumeration.

</dd> <dt>

[**TLSKeyPackEnumNext**](tlskeypackenumnext.md)
</dt> <dd>

Continues from a previous call to the [**TLSKeyPackEnumBegin**](tlskeypackenumbegin.md) function and returns the next key pack that is installed on a Remote Desktop license server that matches the search criteria.

</dd> <dt>

[**TLSLicenseEnumBegin**](tlslicenseenumbegin.md)
</dt> <dd>

Begins enumeration of licenses that are issued by the Remote Desktop license server based on search criteria.

</dd> <dt>

[**TLSLicenseEnumEnd**](tlslicenseenumend.md)
</dt> <dd>

Continues from a previous call to the [**TLSLicenseEnumBegin**](tlslicenseenumbegin.md) function and terminates the enumeration.

</dd> <dt>

[**TLSLicenseEnumNext**](tlslicenseenumnext.md)
</dt> <dd>

Continues from a previous call to the [**TLSLicenseEnumBegin**](tlslicenseenumbegin.md) function and returns the next license that is installed on a Remote Desktop license server that matches the search criteria.

</dd> <dt>

[**VirtualChannelClose**](/windows/win32/Cchannel/nc-cchannel-virtualchannelclose?branch=master)
</dt> <dd>

Closes the client end of a virtual channel.

</dd> <dt>

[**VirtualChannelEntry**](/windows/win32/Cchannel/nc-cchannel-virtualchannelentry?branch=master)
</dt> <dd>

An application-defined entry point for the client-side DLL of an application that uses Remote Desktop Services virtual channels.

</dd> <dt>

[**VirtualChannelInit**](/windows/win32/Cchannel/nc-cchannel-virtualchannelinit?branch=master)
</dt> <dd>

Initializes a client DLL's access to Remote Desktop Services virtual channels.

</dd> <dt>

[*VirtualChannelInitEvent*](/windows/win32/Cchannel/nc-cchannel-channel_init_event_fn?branch=master)
</dt> <dd>

An application-defined callback function that Remote Desktop Services calls to notify the client DLL of virtual channel events.

</dd> <dt>

[**VirtualChannelOpen**](/windows/win32/Cchannel/nc-cchannel-virtualchannelopen?branch=master)
</dt> <dd>

Opens the client end of a virtual channel.

</dd> <dt>

[*VirtualChannelOpenEvent*](/windows/win32/Cchannel/nc-cchannel-channel_open_event_fn?branch=master)
</dt> <dd>

An application-defined callback function that Remote Desktop Services calls to notify the client DLL of events for a specific virtual channel.

</dd> <dt>

[**VirtualChannelWrite**](/windows/win32/Cchannel/nc-cchannel-virtualchannelwrite?branch=master)
</dt> <dd>

Sends data from the client end of a virtual channel to a partner application on the server end.

</dd> <dt>

[**WTSCloseServer**](/windows/win32/Wtsapi32/nf-wtsapi32-wtscloseserver?branch=master)
</dt> <dd>

Closes an open handle to a Remote Desktop Session Host (RD Session Host) server.

</dd> <dt>

[**WTSConnectSession**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsconnectsessiona?branch=master)
</dt> <dd>

Connects a Remote Desktop Services session to an existing session on the local computer.

</dd> <dt>

[**WTSCreateListener**](/windows/win32/Wtsapi32/nf-wtsapi32-wtscreatelistenera?branch=master)
</dt> <dd>

Creates a new Remote Desktop Services listener or configures an existing listener.

</dd> <dt>

[**WTSDisconnectSession**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsdisconnectsession?branch=master)
</dt> <dd>

Disconnects the logged-on user from the specified Remote Desktop Services session without closing the session.

</dd> <dt>

[**WTSEnableChildSessions**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenablechildsessions?branch=master)
</dt> <dd>

Enables or disables [Child Sessions](child-sessions.md).

</dd> <dt>

[**WTSEnumerateListeners**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenumeratelistenersa?branch=master)
</dt> <dd>

Enumerates all the Remote Desktop Services listeners on a RD Session Host server.

</dd> <dt>

[**WTSEnumerateProcesses**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenumerateprocessesa?branch=master)
</dt> <dd>

Retrieves information about the active processes on a specified RD Session Host server.

</dd> <dt>

[**WTSEnumerateProcessesEx**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenumerateprocessesexa?branch=master)
</dt> <dd>

Retrieves information about the active processes on the specified RD Session Host server or Remote Desktop Virtualization Host (RD Virtualization Host) server.

</dd> <dt>

[**WTSEnumerateServers**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenumerateserversa?branch=master)
</dt> <dd>

Returns a list of all RD Session Host servers within the specified domain.

</dd> <dt>

[**WTSEnumerateSessions**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenumeratesessionsa?branch=master)
</dt> <dd>

Retrieves a list of sessions on a RD Session Host server.

</dd> <dt>

[**WTSEnumerateSessionsEx**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsenumeratesessionsexa?branch=master)
</dt> <dd>

Retrieves a list of sessions on a specified RD Session Host server or RD Virtualization Host server.

</dd> <dt>

[**WTSFreeMemory**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsfreememory?branch=master)
</dt> <dd>

Frees memory allocated by a Remote Desktop Services function.

</dd> <dt>

[**WTSFreeMemoryEx**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsfreememoryexa?branch=master)
</dt> <dd>

Frees memory that contains [**WTS\_PROCESS\_INFO\_EX**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_process_info_exa?branch=master) or [**WTS\_SESSION\_INFO\_1**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_session_info_1a?branch=master) structures allocated by a Remote Desktop Services function.

</dd> <dt>

[**WTSGetActiveConsoleSessionId**](/windows/win32/Winbase/nf-winbase-wtsgetactiveconsolesessionid?branch=master)
</dt> <dd>

Retrieves the session identifier of the console session.

</dd> <dt>

[**WTSGetChildSessionId**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsgetchildsessionid?branch=master)
</dt> <dd>

Retrieves the child session identifier, if present.

</dd> <dt>

[**WTSGetListenerSecurity**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsgetlistenersecuritya?branch=master)
</dt> <dd>

Retrieves the security descriptor of a Remote Desktop Services listener.

</dd> <dt>

[**WTSIsChildSessionsEnabled**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsischildsessionsenabled?branch=master)
</dt> <dd>

Determines whether child sessions are enabled.

</dd> <dt>

[**WTSLogoffSession**](/windows/win32/Wtsapi32/nf-wtsapi32-wtslogoffsession?branch=master)
</dt> <dd>

Logs off a specified Remote Desktop Services session.

</dd> <dt>

[**WTSOpenServer**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsopenservera?branch=master)
</dt> <dd>

Opens a handle to the specified RD Session Host server.

</dd> <dt>

[**WTSOpenServerEx**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsopenserverexa?branch=master)
</dt> <dd>

Opens a handle to the specified RD Session Host server or RD Virtualization Host server.

</dd> <dt>

[**WTSQueryListenerConfig**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsquerylistenerconfiga?branch=master)
</dt> <dd>

Retrieves configuration information for a Remote Desktop Services listener.

</dd> <dt>

[**WTSQuerySessionInformation**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsquerysessioninformationa?branch=master)
</dt> <dd>

Retrieves session information for the specified session on the specified RD Session Host server.

</dd> <dt>

[**WTSQueryUserConfig**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsqueryuserconfiga?branch=master)
</dt> <dd>

Retrieves configuration information for the specified user on the specified domain controller or RD Session Host server.

</dd> <dt>

[**WTSQueryUserToken**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsqueryusertoken?branch=master)
</dt> <dd>

Obtains the primary access token of the logged-on user specified by the session ID.

</dd> <dt>

[**WTSRegisterSessionNotification**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsregistersessionnotification?branch=master)
</dt> <dd>

Registers the specified window to receive session change notifications.

</dd> <dt>

[**WTSRegisterSessionNotificationEx**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsregistersessionnotificationex?branch=master)
</dt> <dd>

Registers the specified window to receive session change notifications.

</dd> <dt>

[**WTSSendMessage**](/windows/win32/Wtsapi32/nf-wtsapi32-wtssendmessagea?branch=master)
</dt> <dd>

Displays a message box on the client desktop of a specified Remote Desktop Services session.

</dd> <dt>

[**WTSSetListenerSecurity**](/windows/win32/Wtsapi32/nf-wtsapi32-wtssetlistenersecuritya?branch=master)
</dt> <dd>

Configures the security descriptor of a Remote Desktop Services listener.

</dd> <dt>

[**WTSSetUserConfig**](/windows/win32/Wtsapi32/nf-wtsapi32-wtssetuserconfiga?branch=master)
</dt> <dd>

Modifies configuration information for the specified user on the specified domain controller or RD Session Host server.

</dd> <dt>

[**WTSShutdownSystem**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsshutdownsystem?branch=master)
</dt> <dd>

Shuts down (and optionally restarts) the specified RD Session Host server.

</dd> <dt>

[**WTSStartRemoteControlSession**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsstartremotecontrolsessiona?branch=master)
</dt> <dd>

Starts the remote control of another Remote Desktop Services session. You must call this function from a remote session.

</dd> <dt>

[**WTSStopRemoteControlSession**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsstopremotecontrolsession?branch=master)
</dt> <dd>

Stops a remote control session.

</dd> <dt>

[**WTSTerminateProcess**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsterminateprocess?branch=master)
</dt> <dd>

Terminates the specified process on the specified RD Session Host server.

</dd> <dt>

[**WTSUnRegisterSessionNotification**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsunregistersessionnotification?branch=master)
</dt> <dd>

Unregisters the specified window so that it receives no further session change notifications.

</dd> <dt>

[**WTSUnRegisterSessionNotificationEx**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsunregistersessionnotificationex?branch=master)
</dt> <dd>

Unregisters the specified window so that it receives no further session change notifications.

</dd> <dt>

[**WTSVirtualChannelClose**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelclose?branch=master)
</dt> <dd>

Closes an open virtual channel handle.

</dd> <dt>

[**WTSVirtualChannelOpen**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopen?branch=master)
</dt> <dd>

Opens a handle to the server end of a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelOpenEx**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopenex?branch=master)
</dt> <dd>

Creates a virtual channel in a manner similar to [**WTSVirtualChannelOpen**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopen?branch=master).

</dd> <dt>

[**WTSVirtualChannelPurgeInput**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelpurgeinput?branch=master)
</dt> <dd>

Deletes all queued input data sent from the client to the server on a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelPurgeOutput**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelpurgeoutput?branch=master)
</dt> <dd>

Deletes all queued output data sent from the server to the client on a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelQuery**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelquery?branch=master)
</dt> <dd>

Returns information about a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelRead**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelread?branch=master)
</dt> <dd>

Reads data from the server end of a virtual channel.

</dd> <dt>

[**WTSVirtualChannelWrite**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelwrite?branch=master)
</dt> <dd>

Writes data to the server end of a virtual channel.

</dd> <dt>

[**WTSWaitSystemEvent**](/windows/win32/Wtsapi32/nf-wtsapi32-wtswaitsystemevent?branch=master)
</dt> <dd>

Waits for a Remote Desktop Services event before returning to the caller.

</dd> </dl>

 

 




