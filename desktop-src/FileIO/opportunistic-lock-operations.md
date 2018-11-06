---
Description: If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the CreateFile function with the FILE\_FLAG\_OVERLAPPED flag.
ms.assetid: 1595c03e-9f6d-456c-8164-fafba06bbd79
title: Opportunistic Lock Operations
ms.topic: article
ms.date: 05/31/2018
---

# Opportunistic Lock Operations

If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function with the **FILE\_FLAG\_OVERLAPPED** flag. After the files are opened for overlapped operation, you can use the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with one of the following control codes to work with those files' opportunistic locks:

<dl>

[**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](https://msdn.microsoft.com/en-us/library/Aa364578(v=VS.85).aspx)  
[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](https://msdn.microsoft.com/en-us/library/Aa364580(v=VS.85).aspx)  
[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](https://msdn.microsoft.com/en-us/library/Aa364579(v=VS.85).aspx)  
[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](https://msdn.microsoft.com/en-us/library/Aa364581(v=VS.85).aspx)  
[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](https://msdn.microsoft.com/en-us/library/Aa364588(v=VS.85).aspx)  
[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](https://msdn.microsoft.com/en-us/library/Aa364589(v=VS.85).aspx)  
[**FSCTL\_REQUEST\_OPLOCK**](https://msdn.microsoft.com/en-us/library/Ee681828(v=VS.85).aspx)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](https://msdn.microsoft.com/en-us/library/Aa364590(v=VS.85).aspx)  
[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](https://msdn.microsoft.com/en-us/library/Aa364591(v=VS.85).aspx)  
</dl>

 

 



