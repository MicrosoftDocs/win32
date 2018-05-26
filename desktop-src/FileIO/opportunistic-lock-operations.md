---
Description: If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the CreateFile function with the FILE\_FLAG\_OVERLAPPED flag.
ms.assetid: 1595c03e-9f6d-456c-8164-fafba06bbd79
title: Opportunistic Lock Operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Opportunistic Lock Operations

If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master) function with the **FILE\_FLAG\_OVERLAPPED** flag. After the files are opened for overlapped operation, you can use the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with one of the following control codes to work with those files' opportunistic locks:

<dl>

[**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](/windows/win32/WinIoCtl/?branch=master)  
[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](/windows/win32/WinIoCtl/?branch=master)  
[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](/windows/win32/WinIoCtl/?branch=master)  
[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](/windows/win32/WinIoCtl/?branch=master)  
[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](/windows/win32/WinIoCtl/?branch=master)  
[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](/windows/win32/WinIoCtl/?branch=master)  
[**FSCTL\_REQUEST\_OPLOCK**](/windows/win32/WinIoCtl/?branch=master)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](/windows/win32/WinIoCtl/?branch=master)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](/windows/win32/WinIoCtl/?branch=master)  
</dl>

 

 



