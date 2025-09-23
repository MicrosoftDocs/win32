---
description: An access right is a bit flag that corresponds to a particular set of operations that a thread can perform on a securable object.
ms.assetid: da67c486-d2e7-4632-ac7a-c18aabc3f21d
title: Access Rights and Access Masks
ms.topic: concept-article
ms.date: 07/08/2025
# customer intent: As a Windows app developer, I want to understand how access rights and access masks work in the Windows security model, so that I can manage permissions for securable objects effectively in my applications.
---

# Access rights and access masks

An *access right* is a bit flag that corresponds to a particular set of operations that a thread can perform on a securable object. For example, a registry key has the **KEY\_SET\_VALUE** access right, which corresponds to the ability of a thread to set a value under the key. If a thread tries to perform an operation on an object, but does not have the necessary access right to the object, the system does not carry out the operation.

An [access mask](/windows/win32/SecGloss/a-gly) is a 32-bit value whose bits correspond to the access rights supported by an object. All Windows securable objects use an [access mask format](access-mask-format.md) that includes bits for the following types of access rights:

-   [Generic access rights](generic-access-rights.md)
-   [Standard access rights](standard-access-rights.md)
-   [SACL access right](sacl-access-right.md)
-   [Directory services access rights](directory-services-access-rights.md)

When a thread tries to open a handle to an object, the thread typically specifies an access mask to [request a set of access rights](requesting-access-rights-to-an-object.md). For example, an application that needs to set and query the values of a registry key can open the key by using an access mask to request the **KEY\_SET\_VALUE** and **KEY\_QUERY\_VALUE** access rights.

## Access rights and securable objects

The following table shows the functions that manipulate the security information for each type of securable object.

| Object type | Security descriptor functions |
|-------------|-------------------------------|
| [Files or directories](/windows/win32/FileIO/file-security-and-access-rights) on an NTFS file system | [GetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [SetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Named pipes](/windows/win32/ipc/named-pipe-security-and-access-rights) [Anonymous pipes](/windows/win32/ipc/anonymous-pipe-security-and-access-rights) | [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Console screen buffers | Not supported. |
| [Processes](/windows/win32/ProcThread/process-security-and-access-rights) [Threads](/windows/win32/ProcThread/thread-security-and-access-rights) | [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [File-mapping objects](/windows/win32/Memory/file-mapping-security-and-access-rights) | [GetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [SetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Access tokens](access-rights-for-access-token-objects.md) | [SetKernelObjectSecurity](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setkernelobjectsecurity), [GetKernelObjectSecurity](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getkernelobjectsecurity) |
| Window-management objects ([window stations](/windows/win32/winstation/window-station-security-and-access-rights) and [desktops](/windows/win32/winstation/desktop-security-and-access-rights)) | [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Registry keys](/windows/win32/SysInfo/registry-key-security-and-access-rights) | [GetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [SetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Windows services](/windows/win32/Services/service-security-and-access-rights) | [GetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [SetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Local or remote printers | [GetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [SetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Network shares | [GetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [SetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Interprocess synchronization objects](/windows/win32/Sync/synchronization-object-security-and-access-rights) (events, mutexes, semaphores, and waitable timers) | [GetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [SetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Job objects](/windows/win32/ProcThread/job-object-security-and-access-rights) | [GetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [SetNamedSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [GetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-getsecurityinfo), [SetSecurityInfo](/windows/win32/api/Aclapi/nf-aclapi-setsecurityinfo) |

## Related content

[Access mask format](access-mask-format.md)

[Directory services access rights](directory-services-access-rights.md)

[Request a set of access rights](requesting-access-rights-to-an-object.md)
