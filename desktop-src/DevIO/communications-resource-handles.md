---
description: A process uses the CreateFile function to open a handle to a communications resource.
ms.assetid: eaef6067-97a6-40c4-84ec-c0d86af6bb4a
title: Communications Resource Handles
ms.topic: article
ms.date: 05/31/2018
---

# Communications Resource Handles

A process uses the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function to open a handle to a communications resource. For example, specifying COM1 opens a handle to a serial port, and LPT1 opens a handle to a parallel port. If the specified resource is currently being used by another process, **CreateFile** fails. Any thread of the process can use the handle returned by **CreateFile** to identify the resource in any of the functions that access the resource.

When the process calls [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) to open a communications resource, it specifies the following attributes:

-   What type of read/write access exists for the specified resource.
-   Whether the handle can be inherited by child processes.
-   Whether the handle can be used in overlapped (asynchronous) I/O operations. (For a description of overlapped operations, see [Synchronization](/windows/desktop/Sync/synchronization).)

When the process uses [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) to open a communications resource, it must specify certain values for the following parameters:

-   The *fdwShareMode* parameter must be zero, opening the resource for exclusive access.
-   The *fdwCreate* parameter must specify the OPEN\_EXISTING flag.
-   The *hTemplateFile* parameter must be **NULL**.

When using [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) to open a handle directly to a device, an application must use the special characters " \\\\ .\\" to identify the device. For example, to open a handle to drive A, specify \\\\ .\\a: for the *lpszName* parameter of **CreateFile**. The calling process can use the handle in the [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function to send control codes to the device.

 

 
