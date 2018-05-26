---
title: DnsServerGlobalNameZone class
description: Represents the configuration of a GlobalName zone on a DNS server.
audience: developer
ms.assetid: 20ab3ff2-c707-446f-9245-9d932ef487bc
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerGlobalNameZone class
- DnsServerGlobalNameZone class, described
topic_type:
- apiref
api_name:
- DnsServerGlobalNameZone
- DnsServerGlobalNameZone.Enable
- DnsServerGlobalNameZone.GlobalOverLocal
- DnsServerGlobalNameZone.PreferAaaa
- DnsServerGlobalNameZone.EnableEDnsProbes
- DnsServerGlobalNameZone.BlockUpdates
- DnsServerGlobalNameZone.AlwaysQueryServer
- DnsServerGlobalNameZone.ServerQueryInterval
- DnsServerGlobalNameZone.SendTimeout
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerGlobalNameZone class

Represents the configuration of a GlobalName zone on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerGlobalNameZone
{
  boolean  Enable;
  boolean  GlobalOverLocal;
  boolean  PreferAaaa;
  boolean  EnableEDnsProbes;
  boolean  BlockUpdates;
  boolean  AlwaysQueryServer;
  datetime ServerQueryInterval;
  uint32   SendTimeout;
};
```

## Members

The **DnsServerGlobalNameZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerGlobalNameZone** class has these properties.

<dl> <dt>

**AlwaysQueryServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to update GlobalName zone service records from a cache or remote DNS server; otherwise, **false**.

</dd> <dt>

**BlockUpdates**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to block updates in zones that contain fully qualified domain names that conflict with labels in the GlobalName zone; otherwise, **false**.

</dd> <dt>

**Enable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the GlobalName zone; otherwise, **false**.

</dd> <dt>

**EnableEDnsProbes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable Extension Mechanisms for DNS (EDNS0); otherwise, **false**.

</dd> <dt>

**GlobalOverLocal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to use GlobalName zone data to answer queries. **false** to use local data to answer queries.

</dd> <dt>

**PreferAaaa**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to prioritize AAAA records over A records; otherwise, **false**.

</dd> <dt>

**SendTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum duration, in minutes, for which a DNS server can wait for a response from the GlobalName zone.

</dd> <dt>

**ServerQueryInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum interval between queries to refresh the remote DNS servers that host the GlobalName zone.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





