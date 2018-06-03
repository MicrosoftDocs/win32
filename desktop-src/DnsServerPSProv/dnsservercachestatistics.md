---
title: DnsServerCacheStatistics class
description: DNS server statistics related to the server cache.
audience: developer
ms.assetid: 27cd581d-2829-4149-b16c-78855854ef7b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerCacheStatistics class
- DnsServerCacheStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerCacheStatistics
- DnsServerCacheStatistics.SuccessfulFreePasses
- DnsServerCacheStatistics.FailedFreePasses
- DnsServerCacheStatistics.PassesWithNoFrees
- DnsServerCacheStatistics.PassesRequiringAggressiveFree
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerCacheStatistics class

DNS server statistics related to the server cache.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerCacheStatistics
{
  uint32 SuccessfulFreePasses;
  uint32 FailedFreePasses;
  uint32 PassesWithNoFrees;
  uint32 PassesRequiringAggressiveFree;
};
```

## Members

The **DnsServerCacheStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerCacheStatistics** class has these properties.

<dl> <dt>

**FailedFreePasses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times since the server last started that the server cache was found to exceed the cache size limit, which is 90 percent of the MaxCacheSize, and that an attempt to free nodes was unsuccessful in meeting the cache size limit.

</dd> <dt>

**PassesRequiringAggressiveFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times since the server last started that the server cache was found to exceed the cache size limit, which is 90 percent of the MaxCacheSize, and that the server scanned the cache aggressively attempting to free even nodes that contain unexpired records.

</dd> <dt>

**PassesWithNoFrees**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times since the server last started that the server cache was found to exceed the cache size limit, which is 90 percent of the MaxCacheSize, but when the server scanned the cache looking for nodes containing no records or only expired records to free, it found no nodes that could be freed.

</dd> <dt>

**SuccessfulFreePasses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times since the server last started that the server cache was found to exceed the cache size limit, which is 90 percent of the MaxCacheSize, and that an attempt to free nodes resulted in the cache size limit being met.

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

 

 





