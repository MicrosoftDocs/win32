---
title: IDODownload interface
description: Used to start and manage a download.
keywords:
- IDODownload interface
topic_type:
- apiref
api_name:
- IDODownload
api_location:
- do.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownload interface

The **IDODownload** interface is used to start and manage a download.

## Methods

The **IDODownload** interface has these methods.

| Method | Description |
| ---- |:---- |
| [IDODownload::Abort](./nf-do-idomanager-createdownload.md) | Aborts the download. |
| [IDODownload::Finalize](./nf-do-idodownload-finalize.md) | Finalizes the download. |
| [IDODownload::GetProperty](./nf-do-idodownload-getproperty.md) | Retrieves a pointer to a **VARIANT** that contains a specific download property. |
| [IDODownload::GetStatus](./nf-do-idodownload-getstatus.md) | Retrieves a pointer to a **DO_DOWNLOAD_STATUS** structure that reflects the current status of the download. |
| [IDODownload::Pause](./nf-do-idodownload-pause.md) | Pauses the download. |
| [IDODownload::SetProperty](./nf-do-idodownload-setproperty.md) | Sets a download property. |
| [IDODownload::Start](./nf-do-idodownload-start.md) | Starts or resumes a download. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
