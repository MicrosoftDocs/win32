---
Description: An application can programmatically create and delete directories.
ms.assetid: 52d1d8a8-e5a7-44f5-9bf2-2a496ef79d32
title: Creating and Deleting Directories
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating and Deleting Directories

An application can programmatically create and delete directories.

To create a new directory, use the [**CreateDirectory**](/windows/win32/FileAPI/nf-fileapi-createdirectorya?branch=master), [**CreateDirectoryEx**](/windows/win32/WinBase/nf-winbase-createdirectoryexa?branch=master), or [**CreateDirectoryTransacted**](/windows/win32/WinBase/nf-winbase-createdirectorytransacteda?branch=master) function. A directory is given the name specified when it is created. The conventions for naming a directory follow the conventions for naming a file. For a description of these conventions, see [Naming a File](naming-a-file.md).

To delete an existing directory, use the [**RemoveDirectory**](/windows/win32/FileAPI/nf-fileapi-removedirectorya?branch=master) or [**RemoveDirectoryTransacted**](/windows/win32/WinBase/nf-winbase-removedirectorytransacteda?branch=master) function. Before removing a directory, you must ensure that the directory is empty and that you have the delete access privilege for the directory. To do the latter, call the [**GetSecurityInfo**](https://msdn.microsoft.com/library/windows/desktop/aa446654) function.

 

 



