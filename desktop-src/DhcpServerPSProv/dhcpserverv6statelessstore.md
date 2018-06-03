---
title: DhcpServerv6StatelessStore class
description: Dhcp Server v6StatelessStore.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd37b78f-fa79-4789-8849-477457822fe2
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv6StatelessStore class
- DhcpServerv6StatelessStore class, described
topic_type:
- apiref
api_name:
- DhcpServerv6StatelessStore
- DhcpServerv6StatelessStore.Prefix
- DhcpServerv6StatelessStore.Enabled
- DhcpServerv6StatelessStore.PurgeInterval
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv6StatelessStore class

Dhcp Server v6StatelessStore.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6StatelessStore
{
  string   Prefix;
  boolean  Enabled;
  DateTime PurgeInterval;
};
```

## Members

The **DhcpServerv6StatelessStore** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6StatelessStore** class has these properties.

<dl> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if stateless clients inventory is enabled.

</dd> <dt>

**Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Scope identifier for the given scope on Dhcp server.

</dd> <dt>

**PurgeInterval**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Purge interval for stateless clients.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





