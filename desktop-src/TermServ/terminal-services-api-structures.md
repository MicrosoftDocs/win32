---
title: Remote Desktop Services API Structures
description: Lists structures that are used with the Remote Desktop Services API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d467241-499c-4038-8d9c-4244457e484f
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Desktop Services API Structures

The following structures are used with the Remote Desktop Services API.

## In this section

<dl> <dt>

[**CHANNEL\_DEF**](/windows/win32/Pchannel/ns-pchannel-tagchannel_def?branch=master)
</dt> <dd>

Contains the name and options of a Remote Desktop Services virtual channel.

</dd> <dt>

[**CHANNEL\_ENTRY\_POINTS**](/windows/win32/Cchannel/ns-cchannel-tagchannel_entry_points?branch=master)
</dt> <dd>

Contains pointers to the functions called by a client-side DLL to access virtual channels.

</dd> <dt>

[**CHANNEL\_PDU\_HEADER**](/windows/win32/Pchannel/ns-pchannel-tagchannel_pdu_header?branch=master)
</dt> <dd>

Contains information about a data block being received by the server end of a virtual channel.

</dd> <dt>

[**LSKeyPack**](lskeypack.md)
</dt> <dd>

Contains information about a specific Remote Desktop Services licensing key pack.

</dd> <dt>

[**LSLicense**](lslicense.md)
</dt> <dd>

Contains information about a specific Remote Desktop Services license.

</dd> <dt>

[**WTSCLIENT**](/windows/win32/Wtsapi32/ns-wtsapi32-_wtsclienta?branch=master)
</dt> <dd>

Contains information about a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**WTSCONFIGINFO**](/windows/win32/Wtsapi32/ns-wtsapi32-_wtsconfiginfoa?branch=master)
</dt> <dd>

Contains information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFO**](/windows/win32/Wtsapi32/ns-wtsapi32-_wtsinfoa?branch=master)
</dt> <dd>

Contains information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFOEX**](/windows/win32/Wtsapi32/ns-wtsapi32-_wtsinfoexa?branch=master)
</dt> <dd>

Contains a [**WTSINFOEX\_LEVEL**](/windows/win32/Wtsapi32/ns-wtsapi32-_wtsinfoex_level_a?branch=master) union that contains extended information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFOEX\_LEVEL1**](/windows/win32/Wtsapi32/ns-wtsapi32-_wtsinfoex_level1_a?branch=master)
</dt> <dd>

Contains extended information about a Remote Desktop Services session.

</dd> <dt>

[**WTSLISTENERCONFIG**](/windows/win32/Wtsapi32/ns-wtsapi32-_wtslistenerconfiga?branch=master)
</dt> <dd>

Contains information about a Remote Desktop Services listener.

</dd> <dt>

[**WTSSBX\_IP\_ADDRESS**](/windows/win32/Tssbx/ns-tssbx-__midl_iwtssbplugin_0004?branch=master)
</dt> <dd>

Contains information about the IP address of a network resource.

</dd> <dt>

[**WTSSBX\_MACHINE\_CONNECT\_INFO**](/windows/win32/Tssbx/ns-tssbx-__midl_iwtssbplugin_0006?branch=master)
</dt> <dd>

Contains information about a computer that is accepting remote connections.

</dd> <dt>

[**WTSSBX\_MACHINE\_INFO**](/windows/win32/Tssbx/ns-tssbx-__midl_iwtssbplugin_0007?branch=master)
</dt> <dd>

Contains information about a computer and its current state.

</dd> <dt>

[**WTSSBX\_SESSION\_INFO**](/windows/win32/Tssbx/ns-tssbx-__midl_iwtssbplugin_0009?branch=master)
</dt> <dd>

Contains information about sessions that are available to Remote Desktop Connection Broker (RD Connection Broker).

</dd> <dt>

[**WTSSESSION\_NOTIFICATION**](/windows/win32/Winuser/ns-winuser-tagwtssession_notification?branch=master)
</dt> <dd>

Provides information about the session change notification. A service receives this structure in its [*HandlerEx*](https://msdn.microsoft.com/library/windows/desktop/ms683241) function in response to a session change event.

</dd> <dt>

[**WTSUSERCONFIG**](/windows/win32/Wtsapi32/ns-wtsapi32-_wtsuserconfiga?branch=master)
</dt> <dd>

Contains configuration information for a user on a domain controller or Remote Desktop Session Host (RD Session Host) server.

</dd> <dt>

[**WTS\_CLIENT\_ADDRESS**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_client_address?branch=master)
</dt> <dd>

Contains the client network address of a Remote Desktop Services session.

</dd> <dt>

[**WTS\_CLIENT\_DISPLAY**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_client_display?branch=master)
</dt> <dd>

Contains information about the display of a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**WTS\_PROCESS\_INFO**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_process_infoa?branch=master)
</dt> <dd>

Contains information about a process running on a RD Session Host server.

</dd> <dt>

[**WTS\_PROCESS\_INFO\_EX**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_process_info_exa?branch=master)
</dt> <dd>

Contains extended information about a process running on a RD Session Host server.

</dd> <dt>

[**WTS\_PRODUCT\_INFO**](/windows/win32/Wtsapi32/?branch=master)
</dt> <dd>

The details of the product license that is required to connect to a terminal server.

</dd> <dt>

[**WTS\_SERVER\_INFO**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_server_infoa?branch=master)
</dt> <dd>

Contains information about a specific Remote Desktop Services server.

</dd> <dt>

[**WTS\_SESSION\_ADDRESS**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_session_address?branch=master)
</dt> <dd>

Contains the virtual IP address assigned to a session.

</dd> <dt>

[**WTS\_SESSION\_INFO**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_session_infoa?branch=master)
</dt> <dd>

Contains information about a client session on a RD Session Host server.

</dd> <dt>

[**WTS\_SESSION\_INFO\_1**](/windows/win32/Wtsapi32/ns-wtsapi32-_wts_session_info_1a?branch=master)
</dt> <dd>

Contains extended information about a client session on a RD Session Host server or Remote Desktop Virtualization Host (RD Virtualization Host) server.

</dd> </dl>

 

 




