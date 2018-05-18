---
title: SetByLogLevel method of the PS\_DnsServerDiagnostics class
description: Sets debug and logging parameters.
audience: developer
ms.assetid: '40f45a59-abe4-43f1-aa29-f3fe3c4b809f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByLogLevel method", "SetByLogLevel method, PS_DnsServerDiagnostics class", "PS_DnsServerDiagnostics class, SetByLogLevel method"]
topic_type:
- apiref
api_name:
- PS_DnsServerDiagnostics.SetByLogLevel
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# SetByLogLevel method of the PS\_DnsServerDiagnostics class

Sets debug and logging parameters.

## Syntax


```mof
uint32 SetByLogLevel(
  [in]  uint32               DebugLogging,
  [in]  uint32               OperationLogLevel2,
  [in]  uint32               OperationLogLevel1,
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [out] DnsServerDiagnostics cmdletOutput
);
```



## Parameters

<dl> <dt>

*DebugLogging* \[in\]
</dt> <dd>

Specifies the bitmask for Debug Logging.

<dt>

0x0
</dt> <dd>

The DNS server does not create a log. This is the default entry.

</dd> <dt>

0x10
</dt> <dd>

Logs notifications.

</dd> <dt>

0x20
</dt> <dd>

Logs updates.

</dd> <dt>

0xFE
</dt> <dd>

Logs non-query.

</dd> <dt>

0x100
</dt> <dd>

Logs question transactions.

</dd> <dt>

0x200
</dt> <dd>

Logs answers.

</dd> <dt>

0x1000
</dt> <dd>

Logs send packets.

</dd> <dt>

0x2000
</dt> <dd>

Logs receive packets.

</dd> <dt>

0x4000
</dt> <dd>

Logs UDP packets.

</dd> <dt>

0x8000
</dt> <dd>

Logs TCP packets.

</dd> <dt>

0xFFFF
</dt> <dd>

Logs all packets.

</dd> <dt>

0x10000
</dt> <dd>

Logs Active Directory write transactions.

</dd> <dt>

0x20000
</dt> <dd>

Logs Active Directory update transactions.

</dd> <dt>

0x1000000
</dt> <dd>

Logs full packets.

</dd> <dt>

0x80000000
</dt> <dd>

Logs write-through transactions.

</dd> </dl> </dd> <dt>

*OperationLogLevel2* \[in\]
</dt> <dd>

Bit flag for log level:

<dt>

0x01000000
</dt> <dd>

The server logs operational logging information to the log file for activities related to interaction with plug-in DLLs.

</dd> </dl> </dd> <dt>

*OperationLogLevel1* \[in\]
</dt> <dd>

Bit flag for log level:

<dt>

0x00000001
</dt> <dd>

The server saves operational logging information to persistent storage.

</dd> <dt>

0x00000010
</dt> <dd>

The server logs event logging information to the log file.

</dd> <dt>

0x00000020
</dt> <dd>

The server logs operational logging information to the log file for server start and stop activities.

</dd> <dt>

0x00002000
</dt> <dd>

The server logs operational logging information to the log file for activities related to loading a zone from the directory server.

</dd> <dt>

0x00004000
</dt> <dd>

The server logs operational logging information to the log file for activities related to writing zone data to the directory server.

</dd> <dt>

0x00020000
</dt> <dd>

The server logs operational logging information to the log file for activities related to updating tombstoned nodes.

</dd> <dt>

0x00100000
</dt> <dd>

The server logs operational logging information to the log file for local resource lookup activities.

</dd> <dt>

0x00200000
</dt> <dd>

The server logs operational logging information to the log file for activities performed during recursive query lookup.

</dd> <dt>

0x00400000
</dt> <dd>

The server logs operational logging information to the log file for activities related to interaction with remote name servers.

</dd> </dl> </dd> <dt>

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

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

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

[**PS\_DnsServerDiagnostics**](ps-dnsserverdiagnostics.md)
</dt> </dl>

 

 





