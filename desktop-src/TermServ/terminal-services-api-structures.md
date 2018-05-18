---
title: Remote Desktop Services API Structures
description: Lists structures that are used with the Remote Desktop Services API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5d467241-499c-4038-8d9c-4244457e484f'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Remote Desktop Services API Structures

The following structures are used with the Remote Desktop Services API.

## In this section

<dl> <dt>

[**CHANNEL\_DEF**](channel-def-str.md)
</dt> <dd>

Contains the name and options of a Remote Desktop Services virtual channel.

</dd> <dt>

[**CHANNEL\_ENTRY\_POINTS**](channel-entry-points-str.md)
</dt> <dd>

Contains pointers to the functions called by a client-side DLL to access virtual channels.

</dd> <dt>

[**CHANNEL\_PDU\_HEADER**](channel-pdu-header-str.md)
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

[**WTSCLIENT**](wtsclient.md)
</dt> <dd>

Contains information about a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**WTSCONFIGINFO**](wtsconfiginfo.md)
</dt> <dd>

Contains information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFO**](wtsinfo.md)
</dt> <dd>

Contains information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFOEX**](wtsinfoex.md)
</dt> <dd>

Contains a [**WTSINFOEX\_LEVEL**](wtsinfoex-level.md) union that contains extended information about a Remote Desktop Services session.

</dd> <dt>

[**WTSINFOEX\_LEVEL1**](wtsinfoex-level1.md)
</dt> <dd>

Contains extended information about a Remote Desktop Services session.

</dd> <dt>

[**WTSLISTENERCONFIG**](wtslistenerconfig.md)
</dt> <dd>

Contains information about a Remote Desktop Services listener.

</dd> <dt>

[**WTSSBX\_IP\_ADDRESS**](wtssbx-ip-address.md)
</dt> <dd>

Contains information about the IP address of a network resource.

</dd> <dt>

[**WTSSBX\_MACHINE\_CONNECT\_INFO**](wtssbx-machine-connect-info.md)
</dt> <dd>

Contains information about a computer that is accepting remote connections.

</dd> <dt>

[**WTSSBX\_MACHINE\_INFO**](wtssbx-machine-info.md)
</dt> <dd>

Contains information about a computer and its current state.

</dd> <dt>

[**WTSSBX\_SESSION\_INFO**](wtssbx-session-info.md)
</dt> <dd>

Contains information about sessions that are available to Remote Desktop Connection Broker (RD Connection Broker).

</dd> <dt>

[**WTSSESSION\_NOTIFICATION**](wtssession-notification-str.md)
</dt> <dd>

Provides information about the session change notification. A service receives this structure in its [*HandlerEx*](https://msdn.microsoft.com/library/windows/desktop/ms683241) function in response to a session change event.

</dd> <dt>

[**WTSUSERCONFIG**](wtsuserconfig.md)
</dt> <dd>

Contains configuration information for a user on a domain controller or Remote Desktop Session Host (RD Session Host) server.

</dd> <dt>

[**WTS\_CLIENT\_ADDRESS**](wts-client-address-str.md)
</dt> <dd>

Contains the client network address of a Remote Desktop Services session.

</dd> <dt>

[**WTS\_CLIENT\_DISPLAY**](wts-client-display-str.md)
</dt> <dd>

Contains information about the display of a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**WTS\_PROCESS\_INFO**](wts-process-info-str.md)
</dt> <dd>

Contains information about a process running on a RD Session Host server.

</dd> <dt>

[**WTS\_PROCESS\_INFO\_EX**](wts-process-info-ex.md)
</dt> <dd>

Contains extended information about a process running on a RD Session Host server.

</dd> <dt>

[**WTS\_PRODUCT\_INFO**](wts-product-info.md)
</dt> <dd>

The details of the product license that is required to connect to a terminal server.

</dd> <dt>

[**WTS\_SERVER\_INFO**](wts-server-info.md)
</dt> <dd>

Contains information about a specific Remote Desktop Services server.

</dd> <dt>

[**WTS\_SESSION\_ADDRESS**](wts-session-address.md)
</dt> <dd>

Contains the virtual IP address assigned to a session.

</dd> <dt>

[**WTS\_SESSION\_INFO**](wts-session-info-str.md)
</dt> <dd>

Contains information about a client session on a RD Session Host server.

</dd> <dt>

[**WTS\_SESSION\_INFO\_1**](wts-session-info-1.md)
</dt> <dd>

Contains extended information about a client session on a RD Session Host server or Remote Desktop Virtualization Host (RD Virtualization Host) server.

</dd> </dl>

 

 




