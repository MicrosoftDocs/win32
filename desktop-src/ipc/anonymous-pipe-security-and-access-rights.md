---
description: You can specify a security descriptor for an anonymous pipe when you call the CreatePipe function. The security descriptor controls access to both the read and write ends of the pipe.
ms.assetid: 17813ce1-b3f6-408f-9c55-5caa7eda6738
title: Anonymous Pipe Security and Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Anonymous Pipe Security and Access Rights

Windows security enables you to control access to anonymous pipes. For more information about security, see [Access-Control Model](/windows/desktop/SecAuthZ/access-control-model).

You can specify a [security descriptor](/windows/desktop/SecAuthZ/security-descriptors) for a pipe when you call the [**CreatePipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-createpipe) function. The security descriptor controls access to both the read and write ends of the pipe. If you specify **NULL**, the pipe gets a default security descriptor. The ACLs in the default security descriptor for a pipe come from the primary or impersonation token of the creator.

To retrieve a pipe's security descriptor, call the [**GetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-getsecurityinfo) function. To change a pipe's security descriptor, call the [**SetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-setsecurityinfo) function.

The [**CreatePipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-createpipe) function returns two handles to the anonymous pipe: a read handle with GENERIC\_READ and SYNCHRONIZE access; and a write handle with GENERIC\_WRITE and SYNCHRONIZE access. GENERIC\_READ and GENERIC\_WRITE access use the same access rights mapping as for named pipes.

GENERIC\_READ access for an anonymous pipe combines the rights to read data from the pipe, read pipe attributes, read extended attributes, and read the pipe's DACL.

GENERIC\_WRITE access for an anonymous pipe combines the rights to write data to the pipe, append data to it, write pipe attributes, write extended attributes, and read the pipe's DACL.

 

 
