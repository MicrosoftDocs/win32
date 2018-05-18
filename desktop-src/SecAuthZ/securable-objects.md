---
Description: 'A securable object is an object that can have a security descriptor.'
ms.assetid: '40871179-d383-43d0-810d-0805c88dbbd6'
title: Securable Objects
---

# Securable Objects

A securable object is an object that can have a [security descriptor](security-descriptors.md). All named Windows objects are securable. Some unnamed objects, such as [*process*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-process-gly) and thread objects, can have security descriptors too. For most securable objects, you can specify an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) in the function call that creates the object. For example, you can specify a security descriptor in the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) and [**CreateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms682425) functions.

In addition, the Windows security functions enable you to get and set the security information for securable objects created on operating systems other than Windows. The Windows security functions also provide support for using security descriptors with private, application-defined objects. For more information about private securable objects, see [Client/Server Access Control](client-server-access-control.md).

Each type of securable object defines its own set of specific [access rights](access-rights-and-access-masks.md) and its own [mapping of generic access rights](generic-access-rights.md). For information about the specific and generic access rights for each type of securable object, see the overview for that type of object.

The following table shows the functions to use to manipulate the security information for some common securable objects.



| Object type                                                                                                                                           | Security descriptor functions                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Files or directories](https://msdn.microsoft.com/library/windows/desktop/aa364399) on an NTFS file system                                                                     | [**GetNamedSecurityInfo**](getnamedsecurityinfo.md), [**SetNamedSecurityInfo**](setnamedsecurityinfo.md), [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md) |
| [Named pipes](https://msdn.microsoft.com/library/windows/desktop/aa365600)<br/> [Anonymous pipes](https://msdn.microsoft.com/library/windows/desktop/aa365142)<br/>     | [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md)                                                                                                             |
| [Processes](https://msdn.microsoft.com/library/windows/desktop/ms684880)<br/> [Threads](https://msdn.microsoft.com/library/windows/desktop/ms686769)<br/>                          | [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md)                                                                                                             |
| [File-mapping objects](https://msdn.microsoft.com/library/windows/desktop/aa366559)                                                                                  | [**GetNamedSecurityInfo**](getnamedsecurityinfo.md), [**SetNamedSecurityInfo**](setnamedsecurityinfo.md), [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md) |
| [Access tokens](access-rights-for-access-token-objects.md)                                                                                           | [**SetKernelObjectSecurity**](setkernelobjectsecurity.md), [**GetKernelObjectSecurity**](getkernelobjectsecurity.md)                                                                             |
| Window-management objects ([window stations](https://msdn.microsoft.com/library/windows/desktop/ms687391) and [desktops](https://msdn.microsoft.com/library/windows/desktop/ms682575)) | [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md)                                                                                                             |
| [Registry keys](https://msdn.microsoft.com/library/windows/desktop/ms724878)                                                                                         | [**GetNamedSecurityInfo**](getnamedsecurityinfo.md), [**SetNamedSecurityInfo**](setnamedsecurityinfo.md), [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md) |
| [Windows services](https://msdn.microsoft.com/library/windows/desktop/ms685981)                                                                                           | [**GetNamedSecurityInfo**](getnamedsecurityinfo.md), [**SetNamedSecurityInfo**](setnamedsecurityinfo.md), [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md) |
| Local or remote printers                                                                                                                              | [**GetNamedSecurityInfo**](getnamedsecurityinfo.md), [**SetNamedSecurityInfo**](setnamedsecurityinfo.md), [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md) |
| Network shares                                                                                                                                        | [**GetNamedSecurityInfo**](getnamedsecurityinfo.md), [**SetNamedSecurityInfo**](setnamedsecurityinfo.md), [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md) |
| [Interprocess synchronization objects](https://msdn.microsoft.com/library/windows/desktop/ms686670) (events, mutexes, semaphores, and waitable timers)     | [**GetNamedSecurityInfo**](getnamedsecurityinfo.md), [**SetNamedSecurityInfo**](setnamedsecurityinfo.md), [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md) |
| [Job objects](https://msdn.microsoft.com/library/windows/desktop/ms684164)                                                                                             | [**GetNamedSecurityInfo**](getnamedsecurityinfo.md), [**SetNamedSecurityInfo**](setnamedsecurityinfo.md), [**GetSecurityInfo**](getsecurityinfo.md), [**SetSecurityInfo**](setsecurityinfo.md) |
| Directory service objects                                                                                                                             | These objects are handled by Active Directory Objects. For more information, see [Active Directory Service Interfaces](https://msdn.microsoft.com/library/aa772170).                             |



 

 

 




