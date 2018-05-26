---
title: Set method of the MSFT\_DtcLogTask class
description: Modifies DTC log file settings for a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 55aa3998-ea7d-4999-af83-aba72698a8d4
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, MSFT_DtcLogTask class
- MSFT_DtcLogTask class, Set method
topic_type:
- apiref
api_name:
- MSFT_DtcLogTask.Set
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the MSFT\_DtcLogTask class

Modifies DTC log file settings for a DTC instance.

## Syntax


```mof
uint32 Set(
  [in] string DtcName,
  [in] string Path,
  [in] uint32 SizeInMB,
  [in] uint32 MaxSizeInMB
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

The path to the log file.

</dd> <dt>

*SizeInMB* \[in\]
</dt> <dd>

The initial size of the log file, in megabytes.

</dd> <dt>

*MaxSizeInMB* \[in\]
</dt> <dd>

The maximum file size of the new log file, in megabytes.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcLogTask**](msft-dtclogtask.md)
</dt> </dl>

 

 





