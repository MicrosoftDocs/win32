---
Description: An access right is a bit flag that corresponds to a particular set of operations that a thread can perform on a securable object.
ms.assetid: da67c486-d2e7-4632-ac7a-c18aabc3f21d
title: Access Rights and Access Masks
ms.topic: article
ms.date: 05/31/2018
---

# Access Rights and Access Masks

An *access right* is a bit flag that corresponds to a particular set of operations that a thread can perform on a securable object. For example, a registry key has the KEY\_SET\_VALUE access right, which corresponds to the ability of a thread to set a value under the key. If a thread tries to perform an operation on an object, but does not have the necessary access right to the object, the system does not carry out the operation.

An [*access mask*](https://docs.microsoft.com/windows/desktop/SecGloss/a-gly) is a 32-bit value whose bits correspond to the access rights supported by an object. All Windows securable objects use an [access mask format](access-mask-format.md) that includes bits for the following types of access rights:

-   [Generic access rights](generic-access-rights.md)
-   [Standard access rights](standard-access-rights.md)
-   [SACL access right](sacl-access-right.md)
-   [Directory services access rights](directory-services-access-rights.md)

When a thread tries to open a handle to an object, the thread typically specifies an access mask to [request a set of access rights](requesting-access-rights-to-an-object.md). For example, an application that needs to set and query the values of a registry key can open the key by using an access mask to request the KEY\_SET\_VALUE and KEY\_QUERY\_VALUE access rights.

The following table shows the functions that manipulate the security information for each type of securable object.



| Object type                                                                                                                                           | Security descriptor functions                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Files or directories](https://docs.microsoft.com/windows/desktop/FileIO/file-security-and-access-rights) on an NTFS file system                                                                     | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Named pipes](https://docs.microsoft.com/windows/desktop/ipc/named-pipe-security-and-access-rights)[Anonymous pipes](https://docs.microsoft.com/windows/desktop/ipc/anonymous-pipe-security-and-access-rights)<br/>                 | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| Console screen buffers                                                                                                                                | Not supported.                                                                                                                                                                                     |
| [Processes](https://docs.microsoft.com/windows/desktop/ProcThread/process-security-and-access-rights)[Threads](https://docs.microsoft.com/windows/desktop/ProcThread/thread-security-and-access-rights)<br/>                                      | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| [File-mapping objects](https://docs.microsoft.com/windows/desktop/Memory/file-mapping-security-and-access-rights)                                                                                  | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Access tokens](access-rights-for-access-token-objects.md)                                                                                           | [**SetKernelObjectSecurity**](https://msdn.microsoft.com/en-us/library/Aa379578(v=VS.85).aspx), [**GetKernelObjectSecurity**](https://msdn.microsoft.com/en-us/library/Aa446641(v=VS.85).aspx)                                                                             |
| Window-management objects ([window stations](https://docs.microsoft.com/windows/desktop/winstation/window-station-security-and-access-rights) and [desktops](https://docs.microsoft.com/windows/desktop/winstation/desktop-security-and-access-rights)) | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| [Registry keys](https://docs.microsoft.com/windows/desktop/SysInfo/registry-key-security-and-access-rights)                                                                                         | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Windows services](https://docs.microsoft.com/windows/desktop/Services/service-security-and-access-rights)                                                                                           | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Local or remote printers                                                                                                                              | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Network shares                                                                                                                                        | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Interprocess synchronization objects](https://docs.microsoft.com/windows/desktop/Sync/synchronization-object-security-and-access-rights) (events, mutexes, semaphores, and waitable timers)     | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Job objects](https://docs.microsoft.com/windows/desktop/ProcThread/job-object-security-and-access-rights)                                                                                             | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |



 

 

 




