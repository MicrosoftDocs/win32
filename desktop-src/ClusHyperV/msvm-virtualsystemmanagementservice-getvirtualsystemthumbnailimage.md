---
title: GetVirtualSystemThumbnailImage method of the Msvm\_VirtualSystemManagementService class
description: Retrieves the thumbnail image, in raw RGB 565 format, of a virtual system or virtual system snapshot.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bd2408cc-4605-4c4d-8fb0-e39cdb0a77a9
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetVirtualSystemThumbnailImage method
- GetVirtualSystemThumbnailImage method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, GetVirtualSystemThumbnailImage method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.GetVirtualSystemThumbnailImage
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetVirtualSystemThumbnailImage method of the Msvm\_VirtualSystemManagementService class

Retrieves the thumbnail image, in raw RGB 565 format, of a virtual system or virtual system snapshot.

## Syntax


```mof
uint32 GetVirtualSystemThumbnailImage(
  [in]  CIM_VirtualSystemSettingData REF TargetSystem,
  [in]  uint16                           WidthPixels,
  [in]  uint16                           HeightPixels,
  [out] uint8                            ImageData[]
);
```



## Parameters

<dl> <dt>

*TargetSystem* \[in\]
</dt> <dd>

A reference to the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) that contains setting data for the virtual system.

</dd> <dt>

*WidthPixels* \[in\]
</dt> <dd>

The width of the image.

</dd> <dt>

*HeightPixels* \[in\]
</dt> <dd>

The height of the image.

</dd> <dt>

*ImageData* \[out\]
</dt> <dd>

An array that contains the image data, in raw RGB 565 format.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





