---
title: CreateDump method of the MSFT\_MTProcess class
description: Creates a process mini-dump of the process instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '55a7c652-51a0-41ea-9399-b9203a258bb2'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateDump method", "CreateDump method, MSFT_MTProcess class", "MSFT_MTProcess class, CreateDump method"]
topic_type:
- apiref
api_name:
- MSFT_MTProcess.CreateDump
api_location:
- MtTmProv.dll
api_type:
- COM
---

# CreateDump method of the MSFT\_MTProcess class

Creates a process mini-dump of the process instance.

## Syntax


```mof
uint32 CreateDump(
  [out] string DumpFilePath
);
```



## Parameters

<dl> <dt>

*DumpFilePath* \[out\]
</dt> <dd>

On success, returns a string containing the dump path file.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTProcess**](msft-mtprocess.md)
</dt> </dl>

 

 





