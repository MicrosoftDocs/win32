---
Description: 'If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the CreateFile function with the FILE\_FLAG\_OVERLAPPED flag.'
ms.assetid: '1595c03e-9f6d-456c-8164-fafba06bbd79'
title: Opportunistic Lock Operations
---

# Opportunistic Lock Operations

If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the [**CreateFile**](createfile.md) function with the **FILE\_FLAG\_OVERLAPPED** flag. After the files are opened for overlapped operation, you can use the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with one of the following control codes to work with those files' opportunistic locks:

<dl>

[**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](fsctl-opbatch-ack-close-pending.md)  
[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](fsctl-oplock-break-ack-no-2.md)  
[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](fsctl-oplock-break-acknowledge.md)  
[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](fsctl-oplock-break-notify.md)  
[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](fsctl-request-batch-oplock.md)  
[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](fsctl-request-filter-oplock.md)  
[**FSCTL\_REQUEST\_OPLOCK**](fsctl-request-oplock.md)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](fsctl-request-oplock-level-1.md)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](fsctl-request-oplock-level-2.md)  
</dl>

 

 



