---
title: DnsServerGlobalQueryBlockList class
description: Represents a global query block list on a DNS server.
audience: developer
ms.assetid: 881316ba-f6db-4e7e-a113-5af9d09e4e96
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerGlobalQueryBlockList class
- DnsServerGlobalQueryBlockList class, described
topic_type:
- apiref
api_name:
- DnsServerGlobalQueryBlockList
- DnsServerGlobalQueryBlockList.List
- DnsServerGlobalQueryBlockList.Enable
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerGlobalQueryBlockList class

Represents a global query block list on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerGlobalQueryBlockList
{
  string  List[];
  boolean Enable;
};
```

## Members

The **DnsServerGlobalQueryBlockList** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerGlobalQueryBlockList** class has these properties.

<dl> <dt>

**Enable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the block list; otherwise, **false**.

</dd> <dt>

**List**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the items on block list.

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

 

 





