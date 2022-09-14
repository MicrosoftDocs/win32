---
title: DeliveryOptimizationFileProperty enumeration  (Deliveryoptimization.h)
description: The DeliveryOptimizationFileProperty enumeration specifies the ID of an optional property for the Delivery Optimization file.
keywords:
- DeliveryOptimizationFileProperty enumeration
topic_type:
- apiref
api_name:
- DeliveryOptimizationFileProperty
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 01/18/2019
ROBOTS: INDEX,FOLLOW
---

# DeliveryOptimizationFileProperty enumeration

The DeliveryOptimizationFileProperty enumeration specifies the ID of an optional property for the Delivery Optimization file. This enumeration is used in the IDeliveryOptimizationFile2 interface where the property value of type VARIANT is passed

## Syntax

```C++
typedef enum _DeliveryOptimizationFileProperty {  
  DOFilePropertyId_DecryptionInfo,
  DOFilePropertyId_IntegrityCheckInfo,
  DOFilePropertyId_IntegrityCheckMandatory,
  DOFilePropertyId_DownloadSinkInterface,
  DOFilePropertyId_DownloadSinkFilePath,
  DOFilePropertyId_DownloadSinkMemoryStream,
  DOFilePropertyId_TotalSizeBytes
} DOFilePropertyId;
```

## Constants

<dl> <dt>

DOFilePropertyId_DecryptionInfo
</dt> <dd>

The DOFilePropertyId_DecryptionInfo property ID sets decryption information in the form of a JSON string. DOFilePropertyId_DecryptionInfo is a Write only property of type VT_BSTR.

</dd> <dt>

DOFilePropertyId_IntegrityCheckInfo
</dt> <dd>

The DOFilePropertyId_IntegrityCheckInfo property ID sets the piece hash file (PHF) location, which is used by Delivery Optimization to perform runtime integrity checks on the downloaded content. DOFilePropertyId_IntegrityCheckInfo is a Write only property of type VT_BSTR.

</dd> <dt>

DOFilePropertyId_IntegrityCheckMandatory
</dt> <dd>

The DOFilePropertyId_IntegrityCheckMandatory property ID sets a boolean flag indicating whether usage of the PHF is mandatory. If TRUE, the download will be aborted once the integrity check is failed. DOFilePropertyId_IntegrityCheckMandatory is a Read/Write property of type VT_BOOL.

</dd> <dt>

DOFilePropertyId_DownloadSinkFilePath
</dt> <dd>

The DOFilePropertyId_DownloadSinkFilePath property ID sets a fully qualified file system location where Delivery Optimization should store the downloaded pieces. DOFilePropertyId_DownloadSinkFilePath is of type VT_BSTR.

</dd> <dt>

DOFilePropertyId_DownloadSinkMemoryStream
</dt> <dd>

The DOFilePropertyId_DownloadSinkMemoryStream property ID is deprecated. Do not use.

</dd> <dt>

DOFilePropertyId_TotalSizeBytes
</dt> <dd>

The DOFilePropertyId_TotalSizeBytes property ID specifies the total download size. DOFilePropertyId_TotalSizeBytes is of type VT_UI8.
</dd> </dl>

## Requirements

| Requirement | Value |
|-------------------------------|----------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>      |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>  |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>               |
