---
title: GetExtendedStatus method of the MSFT\_StorageJob class
description: Retrieves extended status information for an unsuccessful storage job.
ms.assetid: '75B8C19E-F25D-4201-B895-24B8B0587E4A'
keywords: ["GetExtendedStatus method Windows Storage Management API", "GetExtendedStatus method Windows Storage Management API , MSFT_StorageJob class", "MSFT_StorageJob class Windows Storage Management API , GetExtendedStatus method"]
topic_type:
- apiref
api_name:
- MSFT_StorageJob.GetExtendedStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# GetExtendedStatus method of the MSFT\_StorageJob class

Retrieves extended status information for an unsuccessful storage job.

## Syntax


```mof
UInt32 GetExtendedStatus(
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageJob**](msft-storagejob.md)
</dt> </dl>

 

 





