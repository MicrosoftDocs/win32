---
title: Send method of the MSFT\_EtwTraceSession class
description: Sends the log file of the specified ETW trace session to a remote share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 65c64190-a259-46c0-bdc4-88742a2d34d9
ms.prod: windows-server-dev
ms.technology:
- event-tracing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Send method
- Send method, MSFT_EtwTraceSession class
- MSFT_EtwTraceSession class, Send method
topic_type:
- apiref
api_name:
- MSFT_EtwTraceSession.Send
api_location:
- EventTracingManagement.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Send method of the MSFT\_EtwTraceSession class

Sends the log file of the specified ETW trace session to a remote share.

## Syntax


```mof
uint32 Send(
  [in]  string  destinationFolder,
  [in]  boolean deleteFile,
  [out] string  sourceFilePath,
  [out] uint32  ErrorCode
);
```



## Parameters

<dl> <dt>

*destinationFolder* \[in\]
</dt> <dd>

The name of the remote folder that receives the log file.

</dd> <dt>

*deleteFile* \[in\]
</dt> <dd>

**True** to delete the log file from the local folder after it is copied to the remote share; otherwise, **False**.

</dd> <dt>

*sourceFilePath* \[out\]
</dt> <dd>

When this method returns, this parameter contains the source path from which the log file was copied.

</dd> <dt>

*ErrorCode* \[out\]
</dt> <dd>

If this operation encounters an error, when this method returns, this parameter will contain the error code.

</dd> </dl>

## Return value

Returns 0 on success.

<dl> <dt>

**Success** (0)
</dt> <dt>

**CreateNewFileFailed** (1)
</dt> <dt>

**CopyFileFailed** (2)
</dt> <dt>

**DeleteOldFileFailed** (3)
</dt> </dl>

## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\EventTracingManagement<br/>                                           |
| MOF<br/>                      | <dl> <dt>EventTracingManagement.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>EventTracingManagement.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_EtwTraceSession**](msft-etwtracesession.md)
</dt> </dl>

 

 





