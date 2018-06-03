---
Description: The Windows security model enables you to control access to event, mutex, semaphore, and waitable timer objects. Timer queues, interlocked variables, and critical section objects are not securable. For more information, see Access-Control Model.
ms.assetid: 92478298-617c-4672-a1cc-9a8e9af40327
title: Synchronization Object Security and Access Rights
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Synchronization Object Security and Access Rights

The Windows security model enables you to control access to event, mutex, semaphore, and waitable timer objects. Timer queues, interlocked variables, and critical section objects are not securable. For more information, see [Access-Control Model](https://msdn.microsoft.com/windows/desktop/fd3b718a-5eff-4894-9fc6-d157ddb67330).

You can specify a [security descriptor](https://msdn.microsoft.com/windows/desktop/4ab0e7b1-1b44-4368-b2bd-106c9d2c652c) for an interprocess synchronization object when you call the [**CreateEvent**](/windows/desktop/api/WinBase/nf-synchapi-createeventa), [**CreateMutex**](/windows/desktop/api/WinBase/nf-synchapi-createmutexa), [**CreateSemaphore**](/windows/desktop/api/WinBase/nf-winbase-createsemaphorea), or [**CreateWaitableTimer**](/windows/desktop/api/WinBase/nf-winbase-createwaitabletimera) function. If you specify **NULL**, the object gets a default security descriptor. The [Access-Control Lists (ACLs)](https://www.bing.com/search?q=Access-Control Lists (ACLs)) in the default security descriptor for a synchronization object come from the primary or impersonation token of the creator.

To get or set the security descriptor of an event, mutex, semaphore, or waitable timer object, call the [**GetNamedSecurityInfo**](https://msdn.microsoft.com/windows/desktop/11f2119b-5314-4fa1-8016-9c01f79d037d), [**SetNamedSecurityInfo**](https://msdn.microsoft.com/windows/desktop/70fbba50-2576-4857-a955-119fb12bf7b6), [**GetSecurityInfo**](https://msdn.microsoft.com/windows/desktop/64767a6b-cd79-4e02-881a-706a078ff446), or [**SetSecurityInfo**](https://msdn.microsoft.com/windows/desktop/f1781ba9-81eb-46f9-b530-c390b67d65de) functions.

The handles returned by [**CreateEvent**](/windows/desktop/api/WinBase/nf-synchapi-createeventa), [**CreateMutex**](/windows/desktop/api/WinBase/nf-synchapi-createmutexa), [**CreateSemaphore**](/windows/desktop/api/WinBase/nf-winbase-createsemaphorea), and [**CreateWaitableTimer**](/windows/desktop/api/WinBase/nf-winbase-createwaitabletimera) have full access to the new object. When you call the [**OpenEvent**](/windows/desktop/api/WinBase/nf-synchapi-openeventa), [**OpenMutex**](/windows/desktop/api/WinBase/nf-winbase-openmutexa), [**OpenSemaphore**](/windows/desktop/api/WinBase/nf-winbase-opensemaphorea), and [**OpenWaitableTimer**](/windows/desktop/api/WinBase/nf-winbase-openwaitabletimera) functions, the system checks the requested access rights against the object's security descriptor.

The valid access rights for the interprocess synchronization objects include the [standard access rights](https://msdn.microsoft.com/windows/desktop/f43bccce-0f8c-4732-b678-5fd3218a9f84) and some object-specific access rights. The following table lists the standard access rights used by all objects.

| Value                           | Meaning                                                                                                                                                                                                                                                                                  |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DELETE** (0x00010000L)        | Required to delete the object.                                                                                                                                                                                                                                                           |
| **READ\_CONTROL** (0x00020000L) | Required to read information in the security descriptor for the object, not including the information in the SACL. To read or write the SACL, you must request the **ACCESS\_SYSTEM\_SECURITY** access right. For more information, see [SACL Access Right](https://msdn.microsoft.com/windows/desktop/88198243-dae5-49ac-9d54-bfae7a3a0b1a). |
| **SYNCHRONIZE** (0x00100000L)   | The right to use the object for synchronization. This enables a thread to wait until the object is in the signaled state.                                                                                                                                                                |
| **WRITE\_DAC** (0x00040000L)    | Required to modify the DACL in the security descriptor for the object.                                                                                                                                                                                                                   |
| **WRITE\_OWNER** (0x00080000L)  | Required to change the owner in the security descriptor for the object.                                                                                                                                                                                                                  |



 

The following table lists the object-specific access rights for event objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                                                          |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_ALL\_ACCESS** (0x1F0003) | All possible access rights for an event object. Use this right only if your application requires access beyond that granted by the standard access rights and **EVENT\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **EVENT\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**SetEvent**](/windows/desktop/api/WinBase/nf-synchapi-setevent), [**ResetEvent**](/windows/desktop/api/WinBase/nf-synchapi-resetevent) and [**PulseEvent**](/windows/desktop/api/WinBase/nf-winbase-pulseevent) functions.                                                                                                                                    |



 

The following table lists the object-specific access rights for mutex objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                            |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MUTEX\_ALL\_ACCESS** (0x1F0001) | All possible access rights for a mutex object. Use this right only if your application requires access beyond that granted by the standard access rights. Using this access right increases the possibility that your application must be run by an Administrator. |
| **MUTEX\_MODIFY\_STATE** (0x0001) | Reserved for future use.                                                                                                                                                                                                                                           |



 

The following table lists the object-specific access rights for semaphore objects. These rights are supported in addition to the standard access rights.



| Value                                 | Meaning                                                                                                                                                                                                                                                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SEMAPHORE\_ALL\_ACCESS** (0x1F0003) | All possible access rights for a semaphore object. Use this right only if your application requires access beyond that granted by the standard access rights and **SEMAPHORE\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **SEMAPHORE\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**ReleaseSemaphore**](/windows/desktop/api/WinBase/nf-synchapi-releasesemaphore) function.                                                                                                                                                                                                   |



 

The following table lists the object-specific access rights for waitable timer objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                                                                  |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TIMER\_ALL\_ACCESS** (0x1F0003) | All possible access rights for a waitable timer object. Use this right only if your application requires access beyond that granted by the standard access rights and **TIMER\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **TIMER\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**SetWaitableTimer**](/windows/desktop/api/WinBase/nf-synchapi-setwaitabletimer) and [**CancelWaitableTimer**](/windows/desktop/api/WinBase/nf-synchapi-cancelwaitabletimer) functions.                                                                                                                                            |
| **TIMER\_QUERY\_STATE** (0x0001)  | Reserved for future use.                                                                                                                                                                                                                                                                                 |



 

To read or write the SACL of an interprocess synchronization object, you must request the **ACCESS\_SYSTEM\_SECURITY** access right. For more information, see [Access-Control Lists (ACLs)](https://www.bing.com/search?q=Access-Control Lists (ACLs)) and [SACL Access Right](https://msdn.microsoft.com/windows/desktop/88198243-dae5-49ac-9d54-bfae7a3a0b1a).

 

 



