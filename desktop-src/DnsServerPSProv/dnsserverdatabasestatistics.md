---
title: DnsServerDatabaseStatistics class
description: DNS server statistics related to the database tree.
audience: developer
ms.assetid: 7190ebb4-d119-4d32-bf9f-574c7da1ce97
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerDatabaseStatistics class
- DnsServerDatabaseStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerDatabaseStatistics
- DnsServerDatabaseStatistics.NodeMemory
- DnsServerDatabaseStatistics.NodeInUse
- DnsServerDatabaseStatistics.NodeUsed
- DnsServerDatabaseStatistics.NodeReturn
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerDatabaseStatistics class

DNS server statistics related to the database tree.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerDatabaseStatistics
{
  uint32 NodeMemory;
  uint32 NodeInUse;
  uint32 NodeUsed;
  uint32 NodeReturn;
};
```

## Members

The **DnsServerDatabaseStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerDatabaseStatistics** class has these properties.

<dl> <dt>

**NodeInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of nodes currently allocated for use in the record database.

</dd> <dt>

**NodeMemory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total size, in bytes, of server memory currently used for nodes.

</dd> <dt>

**NodeReturn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of nodes freed from the record database.

</dd> <dt>

**NodeUsed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cumulative number of nodes allocated for use in the record database.

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

 

 





