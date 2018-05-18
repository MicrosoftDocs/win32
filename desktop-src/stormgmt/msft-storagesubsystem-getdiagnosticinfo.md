---
title: GetDiagnosticInfo method of the MSFT\_StorageSubSystem class
description: Gets the diagnostic information of the storage subsystem.
ms.assetid: 'F0ED1A8C-3F20-460C-8D60-1461332C75AA'
keywords: ["GetDiagnosticInfo method Windows Storage Management API", "GetDiagnosticInfo method Windows Storage Management API , MSFT_StorageSubSystem class", "MSFT_StorageSubSystem class Windows Storage Management API , GetDiagnosticInfo method"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.GetDiagnosticInfo
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# GetDiagnosticInfo method of the MSFT\_StorageSubSystem class

Gets the diagnostic information of the storage subsystem.

## Syntax


```mof
UInt32 GetDiagnosticInfo(
  [in]  String  DestinationPath,
  [in]  UInt32  TimeSpan,
  [in]  String  ActivityId,
  [in]  Boolean IncludeOperationalLog,
  [in]  Boolean IncludeDiagnosticLog,
  [in]  Boolean IncludeLiveDump,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*DestinationPath* \[in\]
</dt> <dd></dd> <dt>

*TimeSpan* \[in\]
</dt> <dd></dd> <dt>

*ActivityId* \[in\]
</dt> <dd></dd> <dt>

*IncludeOperationalLog* \[in\]
</dt> <dd></dd> <dt>

*IncludeDiagnosticLog* \[in\]
</dt> <dd></dd> <dt>

*IncludeLiveDump* \[in\]
</dt> <dd></dd> <dt>

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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





