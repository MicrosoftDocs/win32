---
Description: If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the CreateFile function with the FILE\_FLAG\_OVERLAPPED flag.
ms.assetid: 1595c03e-9f6d-456c-8164-fafba06bbd79
title: Opportunistic Lock Operations
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Opportunistic Lock Operations

If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function with the **FILE\_FLAG\_OVERLAPPED** flag. After the files are opened for overlapped operation, you can use the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with one of the following control codes to work with those files' opportunistic locks:

<dl>

[**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_OPLOCK**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](/windows/desktop/api/WinIoCtl/)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](/windows/desktop/api/WinIoCtl/)  
</dl>

 

 



