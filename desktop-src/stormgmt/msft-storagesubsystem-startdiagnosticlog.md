---
title: StartDiagnosticLog method of the MSFT\_StorageSubSystem class
description: Starts a diagnostic log for the storage subsystem.
ms.assetid: C3A6500C-E0E4-48D5-AB81-788AACD0AB9C
keywords:
- StartDiagnosticLog method Windows Storage Management API
- StartDiagnosticLog method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , StartDiagnosticLog method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.StartDiagnosticLog
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StartDiagnosticLog method of the MSFT\_StorageSubSystem class

Starts a diagnostic log for the storage subsystem.

## Syntax


```mof
UInt32 StartDiagnosticLog(
  [in]  UInt16 Level,
  [in]  UInt64 MaxLogSize,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Level* \[in\]
</dt> <dd></dd> <dt>

*MaxLogSize* \[in\]
</dt> <dd>

This value is in units of megabytes.

</dd> <dt>

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

 

 





