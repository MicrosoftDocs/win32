---
title: StopDiagnosticLog method of the MSFT\_StorageSubSystem class
description: Stops the diagnostic log for the storage subsystem.
ms.assetid: 3D5D7A2B-C052-4834-AF7D-6432F407F647
keywords:
- StopDiagnosticLog method Windows Storage Management API
- StopDiagnosticLog method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , StopDiagnosticLog method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.StopDiagnosticLog
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StopDiagnosticLog method of the MSFT\_StorageSubSystem class

Stops the diagnostic log for the storage subsystem.

## Syntax


```mof
UInt32 StopDiagnosticLog(
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

See [Storage Management API Common Return Codes](storage-management-api-common-return-codes.md).

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





