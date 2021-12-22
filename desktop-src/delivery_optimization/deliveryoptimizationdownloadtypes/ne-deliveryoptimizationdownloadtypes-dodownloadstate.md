---
title: DODownloadState enumeration
description: Specifies the ID of the current download state, which is part of the **DO_DOWNLOAD_STATUS** structure.
keywords:
- DODownloadState enumeration, DODownloadState
topic_type:
- apiref
api_name:
- DODownloadState
api_location:
- deliveryoptimizationdownloadtypes.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 07/02/2019
---

# DODownloadState enumeration

The **DODownloadState** enumeration specifies the ID of the current download state, which is part of the **DO_DOWNLOAD_STATUS** structure.

## Syntax

```cpp
typedef enum _DODownloadState
{
  DODownloadState_Created = 0, 
  DODownloadState_Transferring,
  DODownloadState_Transferred, 
  DODownloadState_Finalized,   
  DODownloadState_Aborted,     
  DODownloadState_Paused
} DODownloadState;
```

## Constants

| Requirement | Value |
|-|-|
| DODownloadState_Created | Download object is created but hasn't been started yet. |
| DODownloadState_Transferring | Download is in progress. |
| DODownloadState_Transferred | Download is transferred and can start again by downloading another portion of the file. |
| DODownloadState_Finalized | Download is finalized and cannot be started again. |
| DODownloadState_Aborted | Download was aborted. |
| DODownloadState_Paused | Download has been paused on demand or due to transient error. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | DeliveryOptimizationDownloadTypes.h |
