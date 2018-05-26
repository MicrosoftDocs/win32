---
Description: Functions used in directory management.
ms.assetid: 5517b0e7-2264-4173-8e10-ff7626458bfa
title: Directory Management Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Directory Management Functions

The following functions are used in directory management.

## In this section



| Function                                                                      | Description                                                                                                                                                               |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDirectory**](/windows/win32/FileAPI/nf-fileapi-createdirectorya?branch=master)<br/>                         | Creates a new directory.<br/>                                                                                                                                       |
| [**CreateDirectoryEx**](/windows/win32/WinBase/nf-winbase-createdirectoryexa?branch=master)<br/>                     | Creates a new directory with the attributes of a specified template directory.<br/>                                                                                 |
| [**CreateDirectoryTransacted**](/windows/win32/WinBase/nf-winbase-createdirectorytransacteda?branch=master)<br/>     | Creates a new directory as a transacted operation, with the attributes of a specified template directory.<br/>                                                      |
| [**FindCloseChangeNotification**](/windows/win32/FileAPI/nf-fileapi-findclosechangenotification?branch=master)<br/> | Stops change notification handle monitoring.<br/>                                                                                                                   |
| [**FindFirstChangeNotification**](/windows/win32/FileAPI/nf-fileapi-findfirstchangenotificationa?branch=master)<br/> | Creates a change notification handle and sets up initial change notification filter conditions.<br/>                                                                |
| [**FindNextChangeNotification**](/windows/win32/FileAPI/nf-fileapi-findnextchangenotification?branch=master)<br/>   | Requests that the operating system signal a change notification handle the next time it detects an appropriate change.<br/>                                         |
| [**GetCurrentDirectory**](/windows/win32/WinBase/nf-winbase-getcurrentdirectory?branch=master)<br/>                 | Retrieves the current directory for the current process.<br/>                                                                                                       |
| [**ReadDirectoryChangesExW**](/windows/win32/WinBase/nf-winbase-readdirectorychangesexw?branch=master)<br/>         | Retrieves information that describes the changes within the specified directory, which can include extended information if that information type is specified.<br/> |
| [**ReadDirectoryChangesW**](/windows/win32/WinBase/nf-winbase-readdirectorychangesw?branch=master)<br/>             | Retrieves information that describes the changes within the specified directory.<br/>                                                                               |
| [**RemoveDirectory**](/windows/win32/FileAPI/nf-fileapi-removedirectorya?branch=master)<br/>                         | Deletes an existing empty directory.<br/>                                                                                                                           |
| [**RemoveDirectoryTransacted**](/windows/win32/WinBase/nf-winbase-removedirectorytransacteda?branch=master)<br/>     | Deletes an existing empty directory as a transacted operation.<br/>                                                                                                 |
| [**SetCurrentDirectory**](/windows/win32/WinBase/nf-winbase-setcurrentdirectory?branch=master)<br/>                 | Changes the current directory for the current process.<br/>                                                                                                         |



 

 

 




