---
title: DODownloadPropertyEx enumeration
description: Specifies the ID of extended properties for the Delivery Optimization download operation.
keywords:
- DODownloadPropertyEx enumeration, DODownloadPropertyEx
topic_type:
- apiref
api_name:
- DODownloadPropertyEx
api_location:
- deliveryoptimizationdownloadtypes.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 07/29/2019
---

# DODownloadPropertyEx enumeration

> [!IMPORTANT]
> The **DODownloadPropertyEx** enumeration is deprecated. Instead, use the [DODownloadProperty](../deliveryoptimizationdownloadtypes/ne-deliveryoptimizationdownloadtypes-dodownloadproperty.md) enumeration with [IDODownload::GetProperty](../do/nf-do-idodownload-getproperty.md) and [IDODownload::SetProperty](../do/nf-do-idodownload-setproperty.md).

The **DODownloadPropertyEx** enumeration specifies the ID of extended properties for the Delivery Optimization download operation. This enumeration is used by the **IDODownloadInternal** interface, and a **VARIANT** value is used to get and set the property value.

## Syntax

```cpp
typedef enum _DODownloadPropertyEx
{
  DODownloadPropertyEx_UpdateId = 0,
  DODownloadPropertyEx_CorrelationVector,
  DODownloadPropertyEx_DecryptionInfo,    
  DODownloadPropertyEx_IntegrityCheckInfo,   
  DODownloadPropertyEx_IntegrityCheckMandatory, 
  DODownloadPropertyEx_TotalSizeBytes, 
  DODownloadPropertyEx_TempLocalFileUsage 
} DODownloadPropertyEx;
```
## Constants

| Requirement | Value |
|-|-|
| DODownloadPropertyEx_UpdateId | Reserved. Do not use. |
| DODownloadPropertyEx_CorrelationVector | Optional. Sets a specific correlation vector for telemetry purposes. VARIANT type is VT_BSTR. |
| DODownloadPropertyEx_DecryptionInfo | Reserved. Do not use. |
| DODownloadPropertyEx_IntegrityCheckInfo | Optional write-only. Sets the piece hash file (PHF) location, which is used by Delivery Optimization to perform runtime integrity checks on the downloaded content. VARIANT type is VT_BSTR. |
| DODownloadPropertyEx_IntegrityCheckMandatory | Optional. Sets a boolean flag indicating whether usage of the piece hash file (PHF) is mandatory. If VARIANT_TRUE, the download will be aborted once the integrity check is failed. VARIANT type is VT_BOOL. |
| DODownloadPropertyEx_TotalSizeBytes | Reserved. Do not use. |
| DODownloadPropertyEx_TempLocalFileUsage | Reserved. Do not use. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | DODownloadInternal.h |
