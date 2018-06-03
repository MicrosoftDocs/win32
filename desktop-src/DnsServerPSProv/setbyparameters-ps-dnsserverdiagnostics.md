---
title: SetByParameters method of the PS\_DnsServerDiagnostics class
description: Sets debug and logging parameters.
audience: developer
ms.assetid: da93fd19-22ff-4526-aa4a-3907697f31c1
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByParameters method
- SetByParameters method, PS_DnsServerDiagnostics class
- PS_DnsServerDiagnostics class, SetByParameters method
topic_type:
- apiref
api_name:
- PS_DnsServerDiagnostics.SetByParameters
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByParameters method of the PS\_DnsServerDiagnostics class

Sets debug and logging parameters.

## Syntax


```mof
uint32 SetByParameters(
  [in]  boolean              Answers,
  [in]  uint32               EventLogLevel,
  [in]  boolean              FullPackets,
  [in]  string               IPFilterList[],
  [in]  string               LogFilePath,
  [in]  uint32               MaxMBFileSize,
  [in]  boolean              Notifications,
  [in]  boolean              Queries,
  [in]  boolean              QuestionTransactions,
  [in]  boolean              ReceivePackets,
  [in]  boolean              SendPackets,
  [in]  boolean              TcpPackets,
  [in]  boolean              UdpPackets,
  [in]  boolean              UnmatchedResponse,
  [in]  boolean              Updates,
  [in]  boolean              WriteThrough,
  [in]  boolean              SaveLogsToPersistentStorage,
  [in]  boolean              EnableLoggingForServerStartStopEvent,
  [in]  boolean              EnableLoggingForZoneLoadingEvent,
  [in]  boolean              EnableLoggingForLocalLookupEvent,
  [in]  boolean              EnableLoggingToFile,
  [in]  boolean              EnableLogFileRollover,
  [in]  boolean              EnableLoggingForZoneDataWriteEvent,
  [in]  boolean              EnableLoggingForTombstoneEvent,
  [in]  boolean              EnableLoggingForRecursiveLookupEvent,
  [in]  boolean              EnableLoggingForRemoteServerEvent,
  [in]  boolean              EnableLoggingForPluginDllEvent,
  [in]  boolean              UseSystemEventLog,
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [out] DnsServerDiagnostics cmdletOutput
);
```



## Parameters

<dl> <dt>

*Answers* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EventLogLevel* \[in\]
</dt> <dd>

Event Log Level - Warning, Error, both Warning and Error, None

</dd> <dt>

*FullPackets* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*IPFilterList* \[in\]
</dt> <dd>

IP Address list to filter.

</dd> <dt>

*LogFilePath* \[in\]
</dt> <dd>

Log file path.

</dd> <dt>

*MaxMBFileSize* \[in\]
</dt> <dd>

Maximum size of Log file

</dd> <dt>

*Notifications* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*Queries* \[in\]
</dt> <dd>

When True, the server allows query packet exchanges through the content filter.

</dd> <dt>

*QuestionTransactions* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*ReceivePackets* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*SendPackets* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*TcpPackets* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*UdpPackets* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*UnmatchedResponse* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*Updates* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*WriteThrough* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*SaveLogsToPersistentStorage* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLoggingForServerStartStopEvent* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLoggingForZoneLoadingEvent* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLoggingForLocalLookupEvent* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLoggingToFile* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLogFileRollover* \[in\]
</dt> <dd>

Bit flag for log File Rollover

</dd> <dt>

*EnableLoggingForZoneDataWriteEvent* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLoggingForTombstoneEvent* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLoggingForRecursiveLookupEvent* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLoggingForRemoteServerEvent* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*EnableLoggingForPluginDllEvent* \[in\]
</dt> <dd>

Bit flag for log level

</dd> <dt>

*UseSystemEventLog* \[in\]
</dt> <dd>

DNS server will write event logs to global/local repository

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of a [**DnsServerDiagnostics**](dnsserverdiagnostics.md) class. This parameter returns a value only if *PassThru* is set to **true.**

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

[**PS\_DnsServerDiagnostics**](ps-dnsserverdiagnostics.md)
</dt> </dl>

 

 





