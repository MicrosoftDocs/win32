---
Description: A securable object is an object that can have a security descriptor.
ms.assetid: '32f2ec06-822f-4d1e-bf51-5ae1d7355e60'
title: Securable Objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Securable Objects

A securable object is an object that can have a [security descriptor](security-descriptors.md). All named Windows objects are securable. Some unnamed objects, such as [*process*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly) and thread objects, can have security descriptors too. For most securable objects, you can specify an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) in the function call that creates the object. For example, you can specify a security descriptor in the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) and [**CreateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms682425) functions.

In addition, the Windows security functions enable you to get and set the security information for securable objects created on operating systems other than Windows. The Windows security functions also provide support for using security descriptors with private, application-defined objects. For more information about private securable objects, see [Client/Server Access Control](client-server-access-control.md).

Each type of securable object defines its own set of specific [access rights](access-rights-and-access-masks.md) and its own [mapping of generic access rights](generic-access-rights.md). For information about the specific and generic access rights for each type of securable object, see the overview for that type of object.

The following table shows the functions to use to manipulate the security information for some common securable objects.



| Object type                                                                                                                                           | Security descriptor functions                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Files or directories](https://msdn.microsoft.com/library/windows/desktop/aa364399) on an NTFS file system                                                                     | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Named pipes](https://msdn.microsoft.com/library/windows/desktop/aa365600)<br/> [Anonymous pipes](https://msdn.microsoft.com/library/windows/desktop/aa365142)<br/>     | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| [Processes](https://msdn.microsoft.com/library/windows/desktop/ms684880)<br/> [Threads](https://msdn.microsoft.com/library/windows/desktop/ms686769)<br/>                          | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| [File-mapping objects](https://msdn.microsoft.com/library/windows/desktop/aa366559)                                                                                  | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Access tokens](access-rights-for-access-token-objects.md)                                                                                           | [**SetKernelObjectSecurity**](https://msdn.microsoft.com/en-us/library/Aa379578(v=VS.85).aspx), [**GetKernelObjectSecurity**](https://msdn.microsoft.com/en-us/library/Aa446641(v=VS.85).aspx)                                                                             |
| Window-management objects ([window stations](https://msdn.microsoft.com/library/windows/desktop/ms687391) and [desktops](https://msdn.microsoft.com/library/windows/desktop/ms682575)) | [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)                                                                                                             |
| [Registry keys](https://msdn.microsoft.com/library/windows/desktop/ms724878)                                                                                         | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Windows services](https://msdn.microsoft.com/library/windows/desktop/ms685981)                                                                                           | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Local or remote printers                                                                                                                              | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Network shares                                                                                                                                        | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Interprocess synchronization objects](https://msdn.microsoft.com/library/windows/desktop/ms686670) (events, mutexes, semaphores, and waitable timers)     | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| [Job objects](https://msdn.microsoft.com/library/windows/desktop/ms684164)                                                                                             | [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo), [**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo) |
| Directory service objects                                                                                                                             | These objects are handled by Active Directory Objects. For more information, see [Active Directory Service Interfaces](https://msdn.microsoft.com/library/aa772170).                             |



 

 

 




