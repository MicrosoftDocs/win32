---
title: DnsServerTimeStatistics class
description: Represents time statistics for a DNS server.
audience: developer
ms.assetid: '7b8f51d0-e77b-4292-86ec-d2a57fc040a3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerTimeStatistics class", "DnsServerTimeStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerTimeStatistics
- DnsServerTimeStatistics.TimeElapsedSinceServerStartBetweenRestart
- DnsServerTimeStatistics.TimeElapsedSinceLastClearedStatisticsBetweenRestart
- DnsServerTimeStatistics.TimeElapsedSinceServerStart
- DnsServerTimeStatistics.TimeElapsedSinceLastClearedStatistics
- DnsServerTimeStatistics.ServerStartTime
- DnsServerTimeStatistics.LastClearTime
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerTimeStatistics class

Represents time statistics for a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerTimeStatistics
{
  datetime TimeElapsedSinceServerStartBetweenRestart;
  datetime TimeElapsedSinceLastClearedStatisticsBetweenRestart;
  datetime TimeElapsedSinceServerStart;
  datetime TimeElapsedSinceLastClearedStatistics;
  datetime ServerStartTime;
  datetime LastClearTime;
};
```

## Members

The **DnsServerTimeStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerTimeStatistics** class has these properties.

<dl> <dt>

**LastClearTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time the server statistics was last cleared.

</dd> <dt>

**ServerStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time the server started.

</dd> <dt>

**TimeElapsedSinceLastClearedStatistics**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of seconds since the last time that the server statistics were cleared.

</dd> <dt>

**TimeElapsedSinceLastClearedStatisticsBetweenRestart**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of seconds that elapsed between the time the server machine was restarted and the last time the server statistics were cleared.

</dd> <dt>

**TimeElapsedSinceServerStart**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of seconds since the server started.

</dd> <dt>

**TimeElapsedSinceServerStartBetweenRestart**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of seconds that has elapsed since the server machine was last restarted.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





