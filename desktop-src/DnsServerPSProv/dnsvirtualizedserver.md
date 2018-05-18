---
title: DnsVirtualizedServer class
description: Describes a virtualized DNS server configuration object.
audience: developer
ms.assetid: 'e9c3ad31-5874-4dba-93ea-a65b12f5b0c4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsVirtualizedServer class", "DnsVirtualizedServer class, described"]
topic_type:
- apiref
api_name:
- DnsVirtualizedServer
- DnsVirtualizedServer.VirtualInstance
- DnsVirtualizedServer.VirtualizedServerZone
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsVirtualizedServer class

Describes a virtualized DNS server configuration object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsVirtualizedServer
{
  DnsServerVirtualizationInstance VirtualInstance;
  DnsServerZone                   VirtualizedServerZone[];
};
```

## Members

The **DnsVirtualizedServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsVirtualizedServer** class has these properties.

<dl> <dt>

**VirtualInstance**
</dt> <dd> <dl> <dt>

Data type: **DnsServerVirtualizationInstance**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("DnsServerVirtualizationInstance")
</dt> </dl>

Describes the DNS virtualization instance.

</dd> <dt>

**VirtualizedServerZone**
</dt> <dd> <dl> <dt>

Data type: **DnsServerZone** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerZone**](dnsserverzone.md)")
</dt> </dl>

Describes the DNS server zones.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





