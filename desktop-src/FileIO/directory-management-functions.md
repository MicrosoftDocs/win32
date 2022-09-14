---
description: Functions used in directory management.
ms.assetid: 5517b0e7-2264-4173-8e10-ff7626458bfa
title: Directory Management Functions
ms.topic: article
ms.date: 05/31/2018
---

# Directory Management Functions

The following functions are used in directory management.

## In this section



| Function                                                                      | Description                                                                                                                                                               |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDirectory**](/windows/desktop/api/FileAPI/nf-fileapi-createdirectorya)<br/>                         | Creates a new directory.<br/>                                                                                                                                       |
| [**CreateDirectoryEx**](/windows/desktop/api/WinBase/nf-winbase-createdirectoryexa)<br/>                     | Creates a new directory with the attributes of a specified template directory.<br/>                                                                                 |
| [**CreateDirectoryTransacted**](/windows/desktop/api/WinBase/nf-winbase-createdirectorytransacteda)<br/>     | Creates a new directory as a transacted operation, with the attributes of a specified template directory.<br/>                                                      |
| [**FindCloseChangeNotification**](/windows/desktop/api/FileAPI/nf-fileapi-findclosechangenotification)<br/> | Stops change notification handle monitoring.<br/>                                                                                                                   |
| [**FindFirstChangeNotification**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstchangenotificationa)<br/> | Creates a change notification handle and sets up initial change notification filter conditions.<br/>                                                                |
| [**FindNextChangeNotification**](/windows/desktop/api/FileAPI/nf-fileapi-findnextchangenotification)<br/>   | Requests that the operating system signal a change notification handle the next time it detects an appropriate change.<br/>                                         |
| [**GetCurrentDirectory**](/windows/desktop/api/WinBase/nf-winbase-getcurrentdirectory)<br/>                 | Retrieves the current directory for the current process.<br/>                                                                                                       |
| [**ReadDirectoryChangesExW**](/windows/desktop/api/WinBase/nf-winbase-readdirectorychangesexw)<br/>         | Retrieves information that describes the changes within the specified directory, which can include extended information if that information type is specified.<br/> |
| [**ReadDirectoryChangesW**](/windows/desktop/api/WinBase/nf-winbase-readdirectorychangesw)<br/>             | Retrieves information that describes the changes within the specified directory.<br/>                                                                               |
| [**RemoveDirectory**](/windows/desktop/api/FileAPI/nf-fileapi-removedirectorya)<br/>                         | Deletes an existing empty directory.<br/>                                                                                                                           |
| [**RemoveDirectoryTransacted**](/windows/desktop/api/WinBase/nf-winbase-removedirectorytransacteda)<br/>     | Deletes an existing empty directory as a transacted operation.<br/>                                                                                                 |
| [**SetCurrentDirectory**](/windows/desktop/api/WinBase/nf-winbase-setcurrentdirectory)<br/>                 | Changes the current directory for the current process.<br/>                                                                                                         |



 

 

 




