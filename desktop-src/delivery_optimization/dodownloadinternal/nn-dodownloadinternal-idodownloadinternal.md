---
title: IDODownloadInternal interface
description: Used to get or set extended download properties.
keywords:
- IDODownloadInternal interface
topic_type:
- apiref
api_name:
- IDODownloadInternal
api_location:
- do.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 07/29/2019
---

# IDODownloadInternal interface

> [!IMPORTANT]
> The **IDODownloadInternal** interface is deprecated. Instead, use the [IDODownload](../do/nn-do-idodownload.md) interface.

The **IDODownloadInternal** interface is used to get or set extended download properties.

## Methods

The **IDODownloadInternal** interface has these methods.

| Method | Description |
| ---- |:---- |
| [IDODownloadInternal::GetPropertyEx](./nf-dodownloadinternal-idodownloadinternal-getpropertyex.md) | Retrieves a pointer to a **VARIANT** that contains a specific extended download property value. |
| [IDODownloadInternal::SetPropertyEx](./nf-dodownloadinternal-idodownloadinternal-setpropertyex.md) | Sets an extended download property. The method accepts a pointer to a **VARIANT** that contains a specific property value to apply to the download. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | DODownloadInternal.h |
