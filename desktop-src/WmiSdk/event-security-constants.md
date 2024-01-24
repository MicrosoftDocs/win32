---
description: The following shows the WMI security constants used for events. They are used to set access control entries (ACEs) in security descriptors used for events or sinks.
ms.assetid: 18318262-d948-4329-8d48-23664798fc58
ms.tgt_platform: multiple
title: Event Security Constants (Wbemcli.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Event Security Constants

The following shows the WMI security constants used for events. They are used to set access control entries (ACEs) in security descriptors used for events or sinks.

<dl> <dt>

<span id="WBEM_RIGHT_PUBLISH"></span><span id="wbem_right_publish"></span>**WBEM\_RIGHT\_PUBLISH**
</dt> <dd> <dl> <dt>

128 (0x80)
</dt> <dt>



Specifies that the account can publish events to the instance of [**\_\_EventFilter**](--eventfilter.md) that defines the event filter for a permanent consumer. Available in wbemcli.h.


</dt> </dl> </dd> <dt>

<span id="WBEM_RIGHT_SUBSCRIBE"></span><span id="wbem_right_subscribe"></span>**WBEM\_RIGHT\_SUBSCRIBE**
</dt> <dd> <dl> <dt>

64 (0x40)
</dt> <dt>



Specifies that a consumer can subscribe to the events delivered to a sink. Used in [**IWbemEventSink::SetSinkSecurity**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventsink-setsinksecurity). Available in wbemcli.h.


</dt> </dl> </dd> <dt>

<span id="WBEM_S_SUBJECT_TO_SDS"></span><span id="wbem_s_subject_to_sds"></span>**WBEM\_S\_SUBJECT\_TO\_SDS**
</dt> <dd> <dl> <dt>

274435 (0x43003)
</dt> <dt>



Event provider indicates that WMI checks the **SECURITY\_DESCRIPTOR** property in each event (inherited from [**\_\_Event**](--event.md)), and only sends events to consumers with the appropriate access permissions. Available in wbemprov.h.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                         |
| Header<br/>                   | <dl> <dt>Wbemcli.h; </dt> <dt>Wbemprov.h</dt> </dl> |



## See also

<dl> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> <dt>

[Securing WMI Events](securing-wmi-events.md)
</dt> </dl>

 

 




