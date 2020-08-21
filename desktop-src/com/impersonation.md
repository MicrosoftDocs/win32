---
title: Impersonation
description: Impersonation is the ability of a thread to execute in a security context that is different from the context of the process that owns the thread.
ms.assetid: 'b33ca3b0-0423-4338-b3d6-4bb3db3d3e1b'
ms.topic: article
ms.date: 05/31/2018
---

# Impersonation

Impersonation is the ability of a thread to execute in a security context that is different from the context of the process that owns the thread. When running in the client's security context, the server "is" the client, to some degree. The server thread uses an access token representing the client's credentials to obtain access to the objects to which the client has access.

The primary reason for impersonation is to cause access checks to be performed against the client's identity. Using the client's identity for access checks can cause access to be either restricted or expanded, depending on what the client has permission to do. For example, suppose a file server has files containing confidential information and that each of these files is protected by an ACL. To help prevent a client from obtaining unauthorized access to information in these files, the server can impersonate the client before accessing the files.

## Access Tokens for Impersonation

Access tokens are objects that describe the security context of a process or thread. They provide information that includes the identity of a user account and a subset of the privileges available to the user account. Every process has a *primary access token* that describes the security context of the user account associated with the process. By default, the system uses the primary token when a thread of the process interacts with a securable object. However, when a thread impersonates a client, the impersonating thread has both a primary access token and an *impersonation token*. The impersonation token represents the client's security context, and this access token is the one that is used for access checks during impersonation. When impersonation is over, the thread reverts to using only the primary access token.

You can use the [**OpenProcessToken**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-openprocesstoken) function to get a handle to the primary token of a process. Use the [**OpenThreadToken**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-openthreadtoken) function to get a handle to the impersonation token of a thread.

## Related topics

<dl> <dt>

[Access Tokens](/windows/desktop/SecAuthZ/access-tokens)
</dt> <dt>

[Delegation and Impersonation](delegation-and-impersonation.md)
</dt> </dl>

 

 