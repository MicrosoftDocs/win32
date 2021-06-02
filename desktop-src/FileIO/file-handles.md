---
description: When a file is opened by a process using the CreateFile function, a file handle is associated with it until either the process terminates or the handle is closed using the CloseHandle function.
ms.assetid: c8188e28-ec1b-4746-86f6-5996ff271677
title: File Handles
ms.topic: article
ms.date: 05/31/2018
---

# File Handles

When a file is opened by a process using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function, a *file handle* is associated with it until either the process terminates or the handle is closed using the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function. The file handle is used to identify the file in many function calls.

Each file handle and file object is generally unique to each process that opens a file—the only exceptions to this are when a file handle held by a process is duplicated, or when a child process inherits the file handles of the parent process. In these situations, these file handles are unique, but see a single, shared file object. See [**DuplicateHandle**](/windows/desktop/api/handleapi/nf-handleapi-duplicatehandle) for more information on duplicating file handles held by processes.

Note that while the file handles are typically private to a process, the file data that the file handles point to is not. Therefore, processes and threads that share the same file must synchronize their access. For most operations on a file, a process identifies the file through its private pool of handles.

 

 
