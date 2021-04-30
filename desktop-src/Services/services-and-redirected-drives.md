---
description: A service (or any process running in a different security context) that must access a remote resource should use the Universal Naming Convention (UNC) name to access the resource.
ms.assetid: 2582259d-077c-4089-9a87-1a377994f0bd
title: Services and Redirected Drives
ms.topic: article
ms.date: 05/31/2018
---

# Services and Redirected Drives

A service (or any process running in a different security context) that must access a remote resource should use the Universal Naming Convention (UNC) name to access the resource. The service must have appropriate privileges to access the resource. If a server-side service uses an RPC connection, delegation must be enabled on the remote server.

Drive letters are not global to the system. Each logon session receives its own set of drive letters from A to Z. Therefore, redirected drives cannot be shared between processes running under different user accounts. Moreover, a service (or any process running within its own logon session) cannot access the drive letters that were established within a different logon session.

A service should not directly access local or network resources through mapped drive letters, nor should it call the **net use** command to map drive letters at run time. The **net use** command is not recommended for several reasons:

-   Drive mappings exist across logon contexts, so if an application is running in the context of the [LocalService account](localservice-account.md), then any other service running in that context may have access to the mapped drive.
-   If the service provides explicit credentials to a **net use** command, those credentials might be inadvertently shared outside of the service boundaries. Instead, the service should use [client impersonation](/windows/desktop/SecAuthZ/client-impersonation) to impersonate the user.
-   Multiple services running in the same context may interfere with each other. If both services perform an explicit **net use** and provide the same credentials at the same time, one service will fail with an "already connected" error.

Additionally, a service should not use the [Windows Networking Functions](/windows/desktop/WNet/windows-networking-functions) to manage mapped drive letters. Although the WNet functions may return successfully, the resulting behavior is not as intended. When the system establishes a redirected drive, it is stored on a per-user basis. Only the user is able to manage the redirected drive. The system keeps track of redirected drives based on the user's logon security identifier (SID). The logon SID is a unique identifier for the user's logon session. A single user can have multiple, simultaneous logon sessions on the system.

If a service is configured to run under a user account, the system always creates a new logon session for the user and starts the service in that new logon session. Therefore, a service cannot manage the drive mappings established within the user's other sessions.

**Windows Server 2003:** On a computer that has multiple network interfaces (that is, a multihomed computer), delays up to 60 seconds may occur when using UNC paths to access files that are stored on a remote server message block (SMB) server. For more information, see [article 890553](https://support.microsoft.com/kb/890553) in the Help and Support Knowledge Base.

 

 
