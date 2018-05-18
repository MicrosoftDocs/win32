---
title: GetSupportedClusterSizes method of the MSFT\_Volume class
description: Retrieves the supported cluster sizes for the volume.
ms.assetid: '5D1AE94F-37BB-4B0C-B98E-F19D95D69143'
keywords: ["GetSupportedClusterSizes method Windows Storage Management API", "GetSupportedClusterSizes method Windows Storage Management API , MSFT_Volume class", "MSFT_Volume class Windows Storage Management API , GetSupportedClusterSizes method"]
topic_type:
- apiref
api_name:
- MSFT_Volume.GetSupportedClusterSizes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# GetSupportedClusterSizes method of the MSFT\_Volume class

Retrieves the supported cluster sizes for the volume.

## Syntax


```mof
UInt32 GetSupportedClusterSizes(
  [in]  String FileSystem,
  [out] UInt32 SupportedClusterSizes[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FileSystem* \[in\]
</dt> <dd>

The volume's file system. One of the following:

-   "ExFAT"
-   "FAT"
-   "FAT32"
-   "NTFS"
-   "ReFS"

</dd> <dt>

*SupportedClusterSizes* \[out\]
</dt> <dd>

An array of values specifying the supported cluster sizes for the volume.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





