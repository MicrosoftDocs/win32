---
Description: A securable object is an object that can have a security descriptor.
ms.assetid: '32f2ec06-822f-4d1e-bf51-5ae1d7355e60'
title: Securable Objects
ms.topic: article
ms.date: 05/31/2018
---

# Securable Objects

A securable object is an object that can have a [security descriptor](security-descriptors.md). All named Windows objects are securable. Some unnamed objects, such as [*process*](https://docs.microsoft.com/windows/desktop/SecGloss/p-gly) and thread objects, can have security descriptors too. For most securable objects, you can specify an object's [*security descriptor*](https://docs.microsoft.com/windows/desktop/SecGloss/s-gly) in the function call that creates the object. For example, you can specify a security descriptor in the [**CreateFile**](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-createfilea) and [**CreateProcess**](https://docs.microsoft.com/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) functions.

In addition, the Windows security functions enable you to get and set the security information for securable objects created on operating systems other than Windows. The Windows security functions also provide support for using security descriptors with private, application-defined objects. For more information about private securable objects, see [Client/Server Access Control](client-server-access-control.md).

Each type of securable object defines its own set of specific [access rights](access-rights-and-access-masks.md) and its own [mapping of generic access rights](generic-access-rights.md). For information about the specific and generic access rights for each type of securable object, see the overview for that type of object.

The following table shows the functions to use to manipulate the security information for some common securable objects.



| Object type                                                                                                                                           | Security descriptor functions                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Files or directories](https://docs.microsoft.com/windows/desktop/FileIO/file-security-and-access-rights) on an NTFS file system                                                                     | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Named pipes](https://docs.microsoft.com/windows/desktop/ipc/named-pipe-security-and-access-rights)<br/> [Anonymous pipes](https://docs.microsoft.com/windows/desktop/ipc/anonymous-pipe-security-and-access-rights)<br/>     | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| [Processes](https://docs.microsoft.com/windows/desktop/ProcThread/process-security-and-access-rights)<br/> [Threads](https://docs.microsoft.com/windows/desktop/ProcThread/thread-security-and-access-rights)<br/>                          | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| [File-mapping objects](https://docs.microsoft.com/windows/desktop/Memory/file-mapping-security-and-access-rights)                                                                                  | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Access tokens](access-rights-for-access-token-objects.md)                                                                                           | [**SetKernelObjectSecurity**](https://msdn.microsoft.com/library/Aa379578(v=VS.85).aspx), [**GetKernelObjectSecurity**](https://msdn.microsoft.com/library/Aa446641(v=VS.85).aspx)                                                                             |
| Window-management objects ([window stations](https://docs.microsoft.com/windows/desktop/winstation/window-station-security-and-access-rights) and [desktops](https://docs.microsoft.com/windows/desktop/winstation/desktop-security-and-access-rights)) | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| [Registry keys](https://docs.microsoft.com/windows/desktop/SysInfo/registry-key-security-and-access-rights)                                                                                         | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Windows services](https://docs.microsoft.com/windows/desktop/Services/service-security-and-access-rights)                                                                                           | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Local or remote printers                                                                                                                              | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Network shares                                                                                                                                        | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Interprocess synchronization objects](https://docs.microsoft.com/windows/desktop/Sync/synchronization-object-security-and-access-rights) (events, mutexes, semaphores, and waitable timers)     | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Job objects](https://docs.microsoft.com/windows/desktop/ProcThread/job-object-security-and-access-rights)                                                                                             | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Directory service objects                                                                                                                             | These objects are handled by Active Directory Objects. For more information, see [Active Directory Service Interfaces](https://docs.microsoft.com/windows/desktop/ADSI/active-directory-service-interfaces-adsi).                             |



 

 

 




