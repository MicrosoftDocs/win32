---
title: DnsServerDiagnostics class
description: Represents event logging details for a DNS server.
audience: developer
ms.assetid: '577bfa3d-19ab-42cb-b697-b1ea0e51e6b2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerDiagnostics class", "DnsServerDiagnostics class, described"]
topic_type:
- apiref
api_name:
- DnsServerDiagnostics
- DnsServerDiagnostics.EventLogLevel
- DnsServerDiagnostics.LogFilePath
- DnsServerDiagnostics.MaxMBFileSize
- DnsServerDiagnostics.FilterIPAddressList
- DnsServerDiagnostics.UseSystemEventLog
- DnsServerDiagnostics.Answers
- DnsServerDiagnostics.Notifications
- DnsServerDiagnostics.Queries
- DnsServerDiagnostics.QuestionTransactions
- DnsServerDiagnostics.ReceivePackets
- DnsServerDiagnostics.SendPackets
- DnsServerDiagnostics.TcpPackets
- DnsServerDiagnostics.UdpPackets
- DnsServerDiagnostics.Update
- DnsServerDiagnostics.FullPackets
- DnsServerDiagnostics.UnmatchedResponse
- DnsServerDiagnostics.WriteThrough
- DnsServerDiagnostics.SaveLogsToPersistentStorage
- DnsServerDiagnostics.EnableLoggingToFile
- DnsServerDiagnostics.EnableLogFileRollover
- DnsServerDiagnostics.EnableLoggingForServerStartStopEvent
- DnsServerDiagnostics.EnableLoggingForZoneLoadingEvent
- DnsServerDiagnostics.EnableLoggingForZoneDataWriteEvent
- DnsServerDiagnostics.EnableLoggingForLocalLookupEvent
- DnsServerDiagnostics.EnableLoggingForTombstoneEvent
- DnsServerDiagnostics.EnableLoggingForRecursiveLookupEvent
- DnsServerDiagnostics.EnableLoggingForRemoteServerEvent
- DnsServerDiagnostics.EnableLoggingForPluginDllEvent
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerDiagnostics class

Represents event logging details for a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerDiagnostics
{
  uint32  EventLogLevel;
  string  LogFilePath;
  uint32  MaxMBFileSize;
  string  FilterIPAddressList[];
  boolean UseSystemEventLog;
  boolean Answers;
  boolean Notifications;
  boolean Queries;
  boolean QuestionTransactions;
  boolean ReceivePackets;
  boolean SendPackets;
  boolean TcpPackets;
  boolean UdpPackets;
  boolean Update;
  boolean FullPackets;
  boolean UnmatchedResponse;
  boolean WriteThrough;
  boolean SaveLogsToPersistentStorage;
  boolean EnableLoggingToFile;
  boolean EnableLogFileRollover;
  boolean EnableLoggingForServerStartStopEvent;
  boolean EnableLoggingForZoneLoadingEvent;
  boolean EnableLoggingForZoneDataWriteEvent;
  boolean EnableLoggingForLocalLookupEvent;
  boolean EnableLoggingForTombstoneEvent;
  boolean EnableLoggingForRecursiveLookupEvent;
  boolean EnableLoggingForRemoteServerEvent;
  boolean EnableLoggingForPluginDllEvent;
};
```

## Members

The **DnsServerDiagnostics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerDiagnostics** class has these properties.

<dl> <dt>

**Answers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of authoritative answers; otherwise, **false**.

</dd> <dt>

**EnableLogFileRollover**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of a file rollover operation; otherwise, **false**.

</dd> <dt>

**EnableLoggingForLocalLookupEvent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of a local lookup event; otherwise, **false**.

</dd> <dt>

**EnableLoggingForPluginDllEvent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of a plugin DLL event; otherwise, **false**.

</dd> <dt>

**EnableLoggingForRecursiveLookupEvent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of a recursive lookup event; otherwise, **false**.

</dd> <dt>

**EnableLoggingForRemoteServerEvent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of a remote server event; otherwise, **false**.

</dd> <dt>

**EnableLoggingForServerStartStopEvent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of an event triggered when the DNS server starts or stops; otherwise, **false**.

</dd> <dt>

**EnableLoggingForTombstoneEvent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of a tombstone event; otherwise, **false**.

</dd> <dt>

**EnableLoggingForZoneDataWriteEvent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of a write operation for zone data; otherwise, **false**.

</dd> <dt>

**EnableLoggingForZoneLoadingEvent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable logging of a loading event in the zone; otherwise, **false**.

</dd> <dt>

**EnableLoggingToFile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to save logs to a log file; otherwise, **false**.

</dd> <dt>

**EventLogLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An integer that indicates the event type.

<dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (2)


</dt> <dd></dd> <dt>

<span id="Warning_and_Error"></span><span id="warning_and_error"></span><span id="WARNING_AND_ERROR"></span>

**Warning and Error** (3)


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**FilterIPAddressList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the IP addresses to filter.

</dd> <dt>

**FullPackets**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the full packet diagnostic; otherwise, **false**.

</dd> <dt>

**LogFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The full path to the log file.

</dd> <dt>

**MaxMBFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum size of the log file, in megabytes.

</dd> <dt>

**Notifications**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the notifications diagnostic; otherwise, **false**.

</dd> <dt>

**Queries**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the queries diagnostic; otherwise, **false**.

</dd> <dt>

**QuestionTransactions**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the question transactions diagnostic; otherwise, **false**.

</dd> <dt>

**ReceivePackets**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the incoming packet diagnostic; otherwise, **false**.

</dd> <dt>

**SaveLogsToPersistentStorage**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to save logs in persistent storage; otherwise, **false**.

</dd> <dt>

**SendPackets**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the outgoing packet diagnostic; otherwise, **false**.

</dd> <dt>

**TcpPackets**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the TCP packet diagnostic; otherwise, **false**.

</dd> <dt>

**UdpPackets**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the UDP packet diagnostic; otherwise, **false**.

</dd> <dt>

**UnmatchedResponse**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the unmatched response diagnostic; otherwise, **false**.

</dd> <dt>

**Update**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the update diagnostic; otherwise, **false**.

</dd> <dt>

**UseSystemEventLog**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to write event logs to the local repository; otherwise, **false**.

</dd> <dt>

**WriteThrough**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable the write through diagnostic; otherwise, **false**.

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

 

 





