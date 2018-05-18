---
title: Diagnose method of the MSFT\_SMFileSystem class
description: Runs diagnostics on the file system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a27a1f2e-9e76-402a-8b5f-d08719ff1a8c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Diagnose method", "Diagnose method, MSFT_SMFileSystem class", "MSFT_SMFileSystem class, Diagnose method"]
topic_type:
- apiref
api_name:
- MSFT_SMFileSystem.Diagnose
api_location:
- StorageService.dll
api_type:
- COM
---

# Diagnose method of the MSFT\_SMFileSystem class

Runs diagnostics on the file system.

## Syntax


```mof
UInt32 Diagnose(
  [in, optional] String                       username,
  [in, optional] String                       password,
  [out]          MSFT_SMStorageDiagnoseResult DiagnoseResults[],
  [out]          MSFT_SMExtendedStatus        ExtendedStatus
);
```



## Parameters

<dl> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*DiagnoseResults* \[out\]
</dt> <dd>

An array of [**MSFT\_SMStorageDiagnoseResult**](msft-smstoragediagnoseresult.md) objects that contain the results from calling this method.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that contains an error code or additional information about the result returned in the *DiagnoseResults* parameter.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMFileSystem**](msft-smfilesystem.md)
</dt> </dl>

 

 





