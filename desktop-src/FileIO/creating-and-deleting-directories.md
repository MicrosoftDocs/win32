---
description: An application can programmatically create and delete directories.
ms.assetid: 52d1d8a8-e5a7-44f5-9bf2-2a496ef79d32
title: Creating and Deleting Directories
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Deleting Directories

An application can programmatically create and delete directories.

To create a new directory, use the [**CreateDirectory**](/windows/desktop/api/FileAPI/nf-fileapi-createdirectorya), [**CreateDirectoryEx**](/windows/desktop/api/WinBase/nf-winbase-createdirectoryexa), or [**CreateDirectoryTransacted**](/windows/desktop/api/WinBase/nf-winbase-createdirectorytransacteda) function. A directory is given the name specified when it is created. The conventions for naming a directory follow the conventions for naming a file. For a description of these conventions, see [Naming a File](naming-a-file.md).

To delete an existing directory, use the [**RemoveDirectory**](/windows/desktop/api/FileAPI/nf-fileapi-removedirectorya) or [**RemoveDirectoryTransacted**](/windows/desktop/api/WinBase/nf-winbase-removedirectorytransacteda) function. Before removing a directory, you must ensure that the directory is empty and that you have the delete access privilege for the directory. To do the latter, call the [**GetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-getsecurityinfo) function.

 

 
