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
ms.author: windowssdkdev
ms.localizationpriority: low
ms.topic: interface
ms.date: 07/03/2019
---

# IDODownload interface

The **IDODownload** interface is used to start and manage a download.

## Methods

The **IDODownload** interface has these methods.

| Method | Description |
| ---- |:---- |
| [IDODownload::Abort](/windows/win32/delivery_optimization/do/nf-do-idomanager-createdownload) | Aborts the download. |
| [IDODownload::Finalize](/windows/win32/delivery_optimization/do/nf-do-idodownload-finalize) | Finalizes the download. |
| [IDODownload::GetProperty](/windows/win32/delivery_optimization/do/nf-do-idodownload-getproperty) | Retrieves a pointer to a **VARIANT** that contains a specific download property. |
| [IDODownload::GetStatus](/windows/win32/delivery_optimization/do/nf-do-idodownload-getstatus) | Retrieves a pointer to a **DO_DOWNLOAD_STATUS** structure that reflects the current status of the download. |
| [IDODownload::Pause](/windows/win32/delivery_optimization/do/nf-do-idodownload-pause) | Pauses the download. |
| [IDODownload::SetProperty](/windows/win32/delivery_optimization/do/nf-do-idodownload-setproperty) | Sets a download property. |
| [IDODownload::Start](/windows/win32/delivery_optimization/do/nf-do-idodownload-start) | Starts or resumes a download. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |