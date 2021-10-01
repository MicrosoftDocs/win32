---
title: IDODownloadStatusCallback interface
description: Used to receive notifications about a download.
keywords:
- IDODownloadStatusCallback interface
topic_type:
- apiref
api_name:
- IDODownloadStatusCallback
api_location:
- do.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownloadStatusCallback interface

The **IDODownloadStatusCallback** interface is used to receive notifications about a download.

## Methods

The **IDODownloadStatusCallback** interface has these methods.

| Method | Description |
| ---- |:---- |
| [IDODownloadStatusCallback::OnStatusChanged](./nf-do-idodownloadstatuscallback-onstatuschanged.md) | Delivery Optimization calls your implementation of this method any time a download status has changed. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |