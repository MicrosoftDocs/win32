---
title: Remote Desktop Services API Structures
description: Lists structures that are used with the Remote Desktop Services API.
ms.assetid: 5d467241-499c-4038-8d9c-4244457e484f
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services API Structures

The following structures are used with the Remote Desktop Services API.

## In this section

<dl> <dt>

[**CHANNEL\_DEF**](/previous-versions/windows/embedded/aa513856(v=msdn.10))
</dt> <dd>

Contains the name and options of a Remote Desktop Services virtual channel.

</dd> <dt>

[**CHANNEL\_ENTRY\_POINTS**](/windows/win32/api/cchannel/ns-cchannel-channel_entry_points)
</dt> <dd>

Contains pointers to the functions called by a client-side DLL to access virtual channels.

</dd> <dt>

[**CHANNEL\_PDU\_HEADER**](/windows/win32/api/pchannel/ns-pchannel-channel_pdu_header)
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

[**WTSCLIENT**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wtsclienta)
</dt> <dd>

Contains information about a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**WTSCONFIGINFO**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wtsconfiginfoa)
</dt> <dd>

Contains information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFO**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wtsinfoa)
</dt> <dd>

Contains information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFOEX**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wtsinfoexa)
</dt> <dd>

Contains a [**WTSINFOEX\_LEVEL**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wtsinfoex_level_a) union that contains extended information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFOEX\_LEVEL1**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wtsinfoex_level1_a)
</dt> <dd>

Contains extended information about a Remote Desktop Services session.

</dd> <dt>

[**WTSLISTENERCONFIG**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wtslistenerconfiga)
</dt> <dd>

Contains information about a Remote Desktop Services listener.

</dd> <dt>

[**WTSSBX\_IP\_ADDRESS**](/windows/win32/api/tssbx/ns-tssbx-wtssbx_ip_address)
</dt> <dd>

Contains information about the IP address of a network resource.

</dd> <dt>

[**WTSSBX\_MACHINE\_CONNECT\_INFO**](/windows/win32/api/tssbx/ns-tssbx-wtssbx_machine_connect_info)
</dt> <dd>

Contains information about a computer that is accepting remote connections.

</dd> <dt>

[**WTSSBX\_MACHINE\_INFO**](/windows/win32/api/tssbx/ns-tssbx-wtssbx_machine_info)
</dt> <dd>

Contains information about a computer and its current state.

</dd> <dt>

[**WTSSBX\_SESSION\_INFO**](/windows/win32/api/tssbx/ns-tssbx-wtssbx_session_info)
</dt> <dd>

Contains information about sessions that are available to Remote Desktop Connection Broker (RD Connection Broker).

</dd> <dt>

[**WTSSESSION\_NOTIFICATION**](/windows/win32/api/winuser/ns-winuser-wtssession_notification)
</dt> <dd>

Provides information about the session change notification. A service receives this structure in its [*HandlerEx*](/windows/desktop/api/winsvc/nc-winsvc-lphandler_function_ex) function in response to a session change event.

</dd> <dt>

[**WTSUSERCONFIG**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wtsuserconfiga)
</dt> <dd>

Contains configuration information for a user on a domain controller or Remote Desktop Session Host (RD Session Host) server.

</dd> <dt>

[**WTS\_CLIENT\_ADDRESS**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wts_client_address)
</dt> <dd>

Contains the client network address of a Remote Desktop Services session.

</dd> <dt>

[**WTS\_CLIENT\_DISPLAY**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wts_client_display)
</dt> <dd>

Contains information about the display of a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**WTS\_PROCESS\_INFO**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wts_process_infoa)
</dt> <dd>

Contains information about a process running on a RD Session Host server.

</dd> <dt>

[**WTS\_PROCESS\_INFO\_EX**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wts_process_info_exa)
</dt> <dd>

Contains extended information about a process running on a RD Session Host server.

</dd> <dt>

**WTS\_PRODUCT\_INFO**
</dt> <dd>

The details of the product license that is required to connect to a terminal server.

</dd> <dt>

[**WTS\_SERVER\_INFO**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wts_server_infoa)
</dt> <dd>

Contains information about a specific Remote Desktop Services server.

</dd> <dt>

[**WTS\_SESSION\_ADDRESS**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wts_session_address)
</dt> <dd>

Contains the virtual IP address assigned to a session.

</dd> <dt>

[**WTS\_SESSION\_INFO**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wts_session_infoa)
</dt> <dd>

Contains information about a client session on a RD Session Host server.

</dd> <dt>

[**WTS\_SESSION\_INFO\_1**](/windows/desktop/api/Wtsapi32/ns-wtsapi32-wts_session_info_1a)
</dt> <dd>

Contains extended information about a client session on a RD Session Host server or Remote Desktop Virtualization Host (RD Virtualization Host) server.

</dd> </dl>

 

 
