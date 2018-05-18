---
title: Remote Desktop Services API Functions
description: The following functions are used with Remote Desktop Services.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e99a86ee-af0e-46db-8dad-69703ca84fa0'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Remote Desktop Services API Functions

The following functions are used with Remote Desktop Services.

## In this section

<dl> <dt>

[**ProcessIdToSessionId**](processidtosessionid.md)
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

[**VirtualChannelClose**](virtualchannelclose.md)
</dt> <dd>

Closes the client end of a virtual channel.

</dd> <dt>

[**VirtualChannelEntry**](virtualchannelentry.md)
</dt> <dd>

An application-defined entry point for the client-side DLL of an application that uses Remote Desktop Services virtual channels.

</dd> <dt>

[**VirtualChannelInit**](virtualchannelinit.md)
</dt> <dd>

Initializes a client DLL's access to Remote Desktop Services virtual channels.

</dd> <dt>

[*VirtualChannelInitEvent*](virtualchannelinitevent.md)
</dt> <dd>

An application-defined callback function that Remote Desktop Services calls to notify the client DLL of virtual channel events.

</dd> <dt>

[**VirtualChannelOpen**](virtualchannelopen.md)
</dt> <dd>

Opens the client end of a virtual channel.

</dd> <dt>

[*VirtualChannelOpenEvent*](virtualchannelopenevent.md)
</dt> <dd>

An application-defined callback function that Remote Desktop Services calls to notify the client DLL of events for a specific virtual channel.

</dd> <dt>

[**VirtualChannelWrite**](virtualchannelwrite.md)
</dt> <dd>

Sends data from the client end of a virtual channel to a partner application on the server end.

</dd> <dt>

[**WTSCloseServer**](wtscloseserver.md)
</dt> <dd>

Closes an open handle to a Remote Desktop Session Host (RD Session Host) server.

</dd> <dt>

[**WTSConnectSession**](wtsconnectsession.md)
</dt> <dd>

Connects a Remote Desktop Services session to an existing session on the local computer.

</dd> <dt>

[**WTSCreateListener**](wtscreatelistener.md)
</dt> <dd>

Creates a new Remote Desktop Services listener or configures an existing listener.

</dd> <dt>

[**WTSDisconnectSession**](wtsdisconnectsession.md)
</dt> <dd>

Disconnects the logged-on user from the specified Remote Desktop Services session without closing the session.

</dd> <dt>

[**WTSEnableChildSessions**](wtsenablechildsessions.md)
</dt> <dd>

Enables or disables [Child Sessions](child-sessions.md).

</dd> <dt>

[**WTSEnumerateListeners**](wtsenumeratelisteners.md)
</dt> <dd>

Enumerates all the Remote Desktop Services listeners on a RD Session Host server.

</dd> <dt>

[**WTSEnumerateProcesses**](wtsenumerateprocesses.md)
</dt> <dd>

Retrieves information about the active processes on a specified RD Session Host server.

</dd> <dt>

[**WTSEnumerateProcessesEx**](wtsenumerateprocessesex.md)
</dt> <dd>

Retrieves information about the active processes on the specified RD Session Host server or Remote Desktop Virtualization Host (RD Virtualization Host) server.

</dd> <dt>

[**WTSEnumerateServers**](wtsenumerateservers.md)
</dt> <dd>

Returns a list of all RD Session Host servers within the specified domain.

</dd> <dt>

[**WTSEnumerateSessions**](wtsenumeratesessions.md)
</dt> <dd>

Retrieves a list of sessions on a RD Session Host server.

</dd> <dt>

[**WTSEnumerateSessionsEx**](wtsenumeratesessionsex.md)
</dt> <dd>

Retrieves a list of sessions on a specified RD Session Host server or RD Virtualization Host server.

</dd> <dt>

[**WTSFreeMemory**](wtsfreememory.md)
</dt> <dd>

Frees memory allocated by a Remote Desktop Services function.

</dd> <dt>

[**WTSFreeMemoryEx**](wtsfreememoryex.md)
</dt> <dd>

Frees memory that contains [**WTS\_PROCESS\_INFO\_EX**](wts-process-info-ex.md) or [**WTS\_SESSION\_INFO\_1**](wts-session-info-1.md) structures allocated by a Remote Desktop Services function.

</dd> <dt>

[**WTSGetActiveConsoleSessionId**](wtsgetactiveconsolesessionid.md)
</dt> <dd>

Retrieves the session identifier of the console session.

</dd> <dt>

[**WTSGetChildSessionId**](wtsgetchildsessionid.md)
</dt> <dd>

Retrieves the child session identifier, if present.

</dd> <dt>

[**WTSGetListenerSecurity**](wtsgetlistenersecurity.md)
</dt> <dd>

Retrieves the security descriptor of a Remote Desktop Services listener.

</dd> <dt>

[**WTSIsChildSessionsEnabled**](wtsischildsessionsenabled.md)
</dt> <dd>

Determines whether child sessions are enabled.

</dd> <dt>

[**WTSLogoffSession**](wtslogoffsession.md)
</dt> <dd>

Logs off a specified Remote Desktop Services session.

</dd> <dt>

[**WTSOpenServer**](wtsopenserver.md)
</dt> <dd>

Opens a handle to the specified RD Session Host server.

</dd> <dt>

[**WTSOpenServerEx**](wtsopenserverex.md)
</dt> <dd>

Opens a handle to the specified RD Session Host server or RD Virtualization Host server.

</dd> <dt>

[**WTSQueryListenerConfig**](wtsquerylistenerconfig.md)
</dt> <dd>

Retrieves configuration information for a Remote Desktop Services listener.

</dd> <dt>

[**WTSQuerySessionInformation**](wtsquerysessioninformation.md)
</dt> <dd>

Retrieves session information for the specified session on the specified RD Session Host server.

</dd> <dt>

[**WTSQueryUserConfig**](wtsqueryuserconfig.md)
</dt> <dd>

Retrieves configuration information for the specified user on the specified domain controller or RD Session Host server.

</dd> <dt>

[**WTSQueryUserToken**](wtsqueryusertoken.md)
</dt> <dd>

Obtains the primary access token of the logged-on user specified by the session ID.

</dd> <dt>

[**WTSRegisterSessionNotification**](wtsregistersessionnotification.md)
</dt> <dd>

Registers the specified window to receive session change notifications.

</dd> <dt>

[**WTSRegisterSessionNotificationEx**](wtsregistersessionnotificationex.md)
</dt> <dd>

Registers the specified window to receive session change notifications.

</dd> <dt>

[**WTSSendMessage**](wtssendmessage.md)
</dt> <dd>

Displays a message box on the client desktop of a specified Remote Desktop Services session.

</dd> <dt>

[**WTSSetListenerSecurity**](wtssetlistenersecurity.md)
</dt> <dd>

Configures the security descriptor of a Remote Desktop Services listener.

</dd> <dt>

[**WTSSetUserConfig**](wtssetuserconfig.md)
</dt> <dd>

Modifies configuration information for the specified user on the specified domain controller or RD Session Host server.

</dd> <dt>

[**WTSShutdownSystem**](wtsshutdownsystem.md)
</dt> <dd>

Shuts down (and optionally restarts) the specified RD Session Host server.

</dd> <dt>

[**WTSStartRemoteControlSession**](wtsstartremotecontrolsession.md)
</dt> <dd>

Starts the remote control of another Remote Desktop Services session. You must call this function from a remote session.

</dd> <dt>

[**WTSStopRemoteControlSession**](wtsstopremotecontrolsession.md)
</dt> <dd>

Stops a remote control session.

</dd> <dt>

[**WTSTerminateProcess**](wtsterminateprocess.md)
</dt> <dd>

Terminates the specified process on the specified RD Session Host server.

</dd> <dt>

[**WTSUnRegisterSessionNotification**](wtsunregistersessionnotification.md)
</dt> <dd>

Unregisters the specified window so that it receives no further session change notifications.

</dd> <dt>

[**WTSUnRegisterSessionNotificationEx**](wtsunregistersessionnotificationex.md)
</dt> <dd>

Unregisters the specified window so that it receives no further session change notifications.

</dd> <dt>

[**WTSVirtualChannelClose**](wtsvirtualchannelclose.md)
</dt> <dd>

Closes an open virtual channel handle.

</dd> <dt>

[**WTSVirtualChannelOpen**](wtsvirtualchannelopen.md)
</dt> <dd>

Opens a handle to the server end of a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelOpenEx**](wtsvirtualchannelopenex.md)
</dt> <dd>

Creates a virtual channel in a manner similar to [**WTSVirtualChannelOpen**](wtsvirtualchannelopen.md).

</dd> <dt>

[**WTSVirtualChannelPurgeInput**](wtsvirtualchannelpurgeinput.md)
</dt> <dd>

Deletes all queued input data sent from the client to the server on a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelPurgeOutput**](wtsvirtualchannelpurgeoutput.md)
</dt> <dd>

Deletes all queued output data sent from the server to the client on a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelQuery**](wtsvirtualchannelquery.md)
</dt> <dd>

Returns information about a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelRead**](wtsvirtualchannelread.md)
</dt> <dd>

Reads data from the server end of a virtual channel.

</dd> <dt>

[**WTSVirtualChannelWrite**](wtsvirtualchannelwrite.md)
</dt> <dd>

Writes data to the server end of a virtual channel.

</dd> <dt>

[**WTSWaitSystemEvent**](wtswaitsystemevent.md)
</dt> <dd>

Waits for a Remote Desktop Services event before returning to the caller.

</dd> </dl>

 

 




