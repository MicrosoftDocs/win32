---
title: Remote Desktop Protocol Provider Structures
description: The custom remote protocol API supports the following structures.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 45d17758-4554-42aa-aeb9-c8d4e7fc6bb7
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Desktop Protocol Provider Structures

The custom remote protocol API supports the following structures.

## In this section

<dl> <dt>

[**TSMF\_SUPPORT\_DATA\_IN**](tsmf-support-data-in.md)
</dt> <dd>

Contains information about media formats.

</dd> <dt>

[**TSMF\_SUPPORT\_DATA\_OUT**](tsmf-support-data-out.md)
</dt> <dd>

Contains information about media formats.

</dd> <dt>

[**TSMF\_SUPPORT\_NODEDATA\_IN**](tsmf-support-nodedata-in.md)
</dt> <dd>

Used inside the [**TSMF\_SUPPORT\_DATA\_IN**](tsmf-support-data-in.md) structure to contain information about supported media formats.

</dd> <dt>

[**TSMF\_SUPPORT\_NODEDATA\_OUT**](tsmf-support-nodedata-out.md)
</dt> <dd>

Used inside the [**TSMF\_SUPPORT\_DATA\_OUT**](tsmf-support-data-out.md) structure to contain information about supported media formats.

</dd> <dt>

[**WRDS\_CONNECTION\_SETTINGS**](/windows/win32/Wtsdefs/ns-wtsdefs-_wrds_connection_settings?branch=master)
</dt> <dd>

Contains connection setting information for a remote session.

</dd> <dt>

[**WRDS\_CONNECTION\_SETTINGS\_1**](/windows/win32/Wtsdefs/ns-wtsdefs-_wrds_connection_settings_1?branch=master)
</dt> <dd>

Contains connection setting information for a remote session.

</dd> <dt>

[**WRDS\_DYNAMIC\_TIME\_ZONE\_INFORMATION**](/windows/win32/Wtsdefs/ns-wtsdefs-_wrds_dynamic_time_zone_information?branch=master)
</dt> <dd>

Contains dynamic time zone information.

</dd> <dt>

[**WRDS\_LISTENER\_SETTINGS**](/windows/win32/Wtsdefs/ns-wtsdefs-_wrds_listener_settings?branch=master)
</dt> <dd>

Contains listener setting information for a remote session.

</dd> <dt>

[**WRDS\_LISTENER\_SETTINGS\_1**](/windows/win32/Wtsdefs/ns-wtsdefs-_wrds_listener_settings_1?branch=master)
</dt> <dd>

Contains listener settings for a remote session.

</dd> <dt>

[**WRDS\_SETTINGS**](/windows/win32/Wtsdefs/ns-wtsdefs-_wrds_settings?branch=master)
</dt> <dd>

Contains policy-related setting information for a remote session.

</dd> <dt>

[**WRDS\_SETTINGS\_1**](/windows/win32/Wtsdefs/ns-wtsdefs-_wrds_settings_1?branch=master)
</dt> <dd>

Contains policy-related settings for a remote session.

</dd> <dt>

[**WTS\_CACHE\_STATS**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_cache_stats?branch=master)
</dt> <dd>

Contains protocol cache statistics.

</dd> <dt>

[**WTS\_DISPLAY\_IOCTL**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_display_ioctl?branch=master)
</dt> <dd>

Contains information about the client display.

</dd> <dt>

[**WTS\_CLIENT\_DATA**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_client_data?branch=master)
</dt> <dd>

Contains information about the client connection.

</dd> <dt>

[**WTS\_LICENSE\_CAPABILITIES**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_license_capabilities?branch=master)
</dt> <dd>

Contains information about the licensing capabilities of the client.

</dd> <dt>

[**WTS\_POLICY\_DATA**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_policy_data?branch=master)
</dt> <dd>

Contains policy information that is passed by the Remote Desktop Services service to the protocol.

</dd> <dt>

[**WTS\_PROPERTY\_VALUE**](/windows/win32/Wtsdefs/ns-wtsdefs-__wts_property_value?branch=master)
</dt> <dd>

Contains information about a property value to retrieve from the protocol.

</dd> <dt>

[**WTS\_PROTOCOL\_CACHE**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_protocol_cache?branch=master)
</dt> <dd>

Contains the number of cache reads and cache hits.

</dd> <dt>

[**WTS\_PROTOCOL\_COUNTERS**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_protocol_counters?branch=master)
</dt> <dd>

Contains protocol performance counters.

</dd> <dt>

[**WTS\_PROTOCOL\_STATUS**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_protocol_status?branch=master)
</dt> <dd>

Contains information about the status of the protocol.

</dd> <dt>

[**WTS\_SERVICE\_STATE**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_service_state?branch=master)
</dt> <dd>

Contains information about changes in the state of the Remote Desktop Services service.

</dd> <dt>

[**WTS\_SESSION\_ID**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_session_id?branch=master)
</dt> <dd>

Contains a **GUID** that uniquely identifies a session.

</dd> <dt>

[**WTS\_SMALL\_RECT**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_small_rect?branch=master)
</dt> <dd>

Contains client window coordinates.

</dd> <dt>

[**WTS\_SOCKADDR**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_sockaddr?branch=master)
</dt> <dd>

Contains a socket address.

</dd> <dt>

[**WTS\_SYSTEMTIME**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_systemtime?branch=master)
</dt> <dd>

Specifies date and time information for transitions between standard time and daylight saving time.

</dd> <dt>

[**WTS\_TIME\_ZONE\_INFORMATION**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_time_zone_information?branch=master)
</dt> <dd>

Contains client time zone information.

</dd> <dt>

[**WTS\_USER\_CREDENTIAL**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_user_credential?branch=master)
</dt> <dd>

Contains credential information for a user.

</dd> <dt>

[**WTS\_USER\_DATA**](/windows/win32/Wtsdefs/ns-wtsdefs-_wts_user_data?branch=master)
</dt> <dd>

Contains select client property values.

</dd> </dl>

## Related topics

<dl> <dt>

[Remote Desktop Protocol Provider Reference](custom-remote-protocol-reference.md)
</dt> <dt>

[Remote Desktop Protocol Provider Enumerations](custom-remote-protocol-enumerations.md)
</dt> <dt>

[Remote Desktop Protocol Provider Interfaces](custom-remote-protocol-interfaces.md)
</dt> <dt>

[Remote Desktop Protocol Provider Unions](custom-remote-protocol-unions.md)
</dt> </dl>

 

 




