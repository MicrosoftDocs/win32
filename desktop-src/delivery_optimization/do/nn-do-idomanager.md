---
title: IDOManager interface
description: Used to create a new download, and to enumerate existing downloads.
keywords:
- IDOManager interface
topic_type:
- apiref
api_name:
- IDOManager
api_location:
- do.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.localizationpriority: low
ms.topic: interface
ms.date: 07/03/2019
---

# IDOManager interface

The **IDOManager** interface is used to create a new download, and to enumerate existing downloads.

## Methods

The **IDOManager** interface has these methods.

| Method | Description |
| ---- |:---- |
| [ID3D12Device5::CheckDriverMatchingIdentifier](/windows/win32/delivery_optimization/do/nf-do-idomanager-createdownload) | Creates a new download. |
| [ID3D12Device5::EnumDownloads](/windows/win32/delivery_optimization/do/nf-do-idomanager-enumdownloads) | Retrieves an interface pointer to an enumerator object that is used to enumerate existing downloads. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |