---
title: DnsServerDsSetting class
description: Represents DNS Server Active Directory settings.
audience: developer
ms.assetid: 36cbfec6-54aa-4ec1-9e6e-673e07e233e1
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerDsSetting class
- DnsServerDsSetting class, described
topic_type:
- apiref
api_name:
- DnsServerDsSetting
- DnsServerDsSetting.PollingInterval
- DnsServerDsSetting.TombstoneInterval
- DnsServerDsSetting.LazyUpdateInterval
- DnsServerDsSetting.MinimumBackgroundLoadThreads
- DnsServerDsSetting.RemoteReplicationDelay
- DnsServerDsSetting.DirectoryPartitionAutoEnlistInterval
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerDsSetting class

Represents DNS Server Active Directory settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerDsSetting
{
  uint32   PollingInterval;
  datetime TombstoneInterval;
  uint32   LazyUpdateInterval;
  uint32   MinimumBackgroundLoadThreads;
  uint32   RemoteReplicationDelay;
  datetime DirectoryPartitionAutoEnlistInterval;
};
```

## Members

The **DnsServerDsSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerDsSetting** class has these properties.

<dl> <dt>

**DirectoryPartitionAutoEnlistInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The auto enlistment interval for directory partitions.

</dd> <dt>

**LazyUpdateInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The lazy update interval.

</dd> <dt>

**MinimumBackgroundLoadThreads**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum amount of background load threads to run.

</dd> <dt>

**PollingInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The polling interval for Directory Services, in seconds.

</dd> <dt>

**RemoteReplicationDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The remote replication delay setting.

</dd> <dt>

**TombstoneInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The tombstone interval for Active Directory.

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

 

 





