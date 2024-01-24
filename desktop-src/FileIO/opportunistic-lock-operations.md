---
description: If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the CreateFile function with the FILE\_FLAG\_OVERLAPPED flag.
ms.assetid: 1595c03e-9f6d-456c-8164-fafba06bbd79
title: Opportunistic Lock Operations
ms.topic: article
ms.date: 05/31/2018
---

# Opportunistic Lock Operations

If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function with the **FILE\_FLAG\_OVERLAPPED** flag. After the files are opened for overlapped operation, you can use the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function with one of the following control codes to work with those files' opportunistic locks:

<dl>

[**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](/windows/win32/api/winioctl/ni-winioctl-fsctl_opbatch_ack_close_pending)  
[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](/windows/win32/api/winioctl/ni-winioctl-fsctl_oplock_break_ack_no_2)  
[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](/windows/win32/api/winioctl/ni-winioctl-fsctl_oplock_break_acknowledge)  
[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](/windows/win32/api/winioctl/ni-winioctl-fsctl_oplock_break_notify)  
[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](/windows/win32/api/winioctl/ni-winioctl-fsctl_request_batch_oplock)  
[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](/windows/win32/api/winioctl/ni-winioctl-fsctl_request_filter_oplock)  
[**FSCTL\_REQUEST\_OPLOCK**](/windows/win32/api/winioctl/ni-winioctl-fsctl_request_oplock)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](/windows/win32/api/winioctl/ni-winioctl-fsctl_request_oplock_level_1)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](/windows/win32/api/winioctl/ni-winioctl-fsctl_request_oplock_level_2)  
</dl>

 

 
