---
Description: The Windows security model enables you to control access to event, mutex, semaphore, and waitable timer objects. Timer queues, interlocked variables, and critical section objects are not securable. For more information, see Access-Control Model.
ms.assetid: 92478298-617c-4672-a1cc-9a8e9af40327
title: Synchronization Object Security and Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Synchronization Object Security and Access Rights

The Windows security model enables you to control access to event, mutex, semaphore, and waitable timer objects. Timer queues, interlocked variables, and critical section objects are not securable. For more information, see [Access-Control Model](https://msdn.microsoft.com/library/Aa374876(v=VS.85).aspx).

You can specify a [security descriptor](https://msdn.microsoft.com/library/Aa379563(v=VS.85).aspx) for an interprocess synchronization object when you call the [**CreateEvent**](https://msdn.microsoft.com/library/ms682396(v=VS.85).aspx), [**CreateMutex**](https://msdn.microsoft.com/library/ms682411(v=VS.85).aspx), [**CreateSemaphore**](/windows/desktop/api/WinBase/nf-winbase-createsemaphorea), or [**CreateWaitableTimer**](/windows/desktop/api/WinBase/nf-winbase-createwaitabletimera) function. If you specify **NULL**, the object gets a default security descriptor. The [Access-Control Lists (ACLs)](https://msdn.microsoft.com/library/Aa374872(v=VS.85).aspx) in the default security descriptor for a synchronization object come from the primary or impersonation token of the creator.

To get or set the security descriptor of an event, mutex, semaphore, or waitable timer object, call the [**GetNamedSecurityInfo**](https://msdn.microsoft.com/library/Aa446645(v=VS.85).aspx), [**SetNamedSecurityInfo**](https://msdn.microsoft.com/library/Aa379579(v=VS.85).aspx), [**GetSecurityInfo**](https://msdn.microsoft.com/library/Aa446654(v=VS.85).aspx), or [**SetSecurityInfo**](https://msdn.microsoft.com/library/Aa379588(v=VS.85).aspx) functions.

The handles returned by [**CreateEvent**](https://msdn.microsoft.com/library/ms682396(v=VS.85).aspx), [**CreateMutex**](https://msdn.microsoft.com/library/ms682411(v=VS.85).aspx), [**CreateSemaphore**](/windows/desktop/api/WinBase/nf-winbase-createsemaphorea), and [**CreateWaitableTimer**](/windows/desktop/api/WinBase/nf-winbase-createwaitabletimera) have full access to the new object. When you call the [**OpenEvent**](https://msdn.microsoft.com/library/ms684305(v=VS.85).aspx), [**OpenMutex**](/windows/desktop/api/WinBase/nf-winbase-openmutexa), [**OpenSemaphore**](/windows/desktop/api/WinBase/nf-winbase-opensemaphorea), and [**OpenWaitableTimer**](/windows/desktop/api/WinBase/nf-winbase-openwaitabletimera) functions, the system checks the requested access rights against the object's security descriptor.

The valid access rights for the interprocess synchronization objects include the [standard access rights](https://msdn.microsoft.com/library/Aa379607(v=VS.85).aspx) and some object-specific access rights. The following table lists the standard access rights used by all objects.

| Value                           | Meaning                                                                                                                                                                                                                                                                                  |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DELETE** (0x00010000L)        | Required to delete the object.                                                                                                                                                                                                                                                           |
| **READ\_CONTROL** (0x00020000L) | Required to read information in the security descriptor for the object, not including the information in the SACL. To read or write the SACL, you must request the **ACCESS\_SYSTEM\_SECURITY** access right. For more information, see [SACL Access Right](https://msdn.microsoft.com/library/Aa379321(v=VS.85).aspx). |
| **SYNCHRONIZE** (0x00100000L)   | The right to use the object for synchronization. This enables a thread to wait until the object is in the signaled state.                                                                                                                                                                |
| **WRITE\_DAC** (0x00040000L)    | Required to modify the DACL in the security descriptor for the object.                                                                                                                                                                                                                   |
| **WRITE\_OWNER** (0x00080000L)  | Required to change the owner in the security descriptor for the object.                                                                                                                                                                                                                  |



 

The following table lists the object-specific access rights for event objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                                                          |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_ALL\_ACCESS** (0x1F0003) | All possible access rights for an event object. Use this right only if your application requires access beyond that granted by the standard access rights and **EVENT\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **EVENT\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**SetEvent**](https://msdn.microsoft.com/library/ms685081(v=VS.85).aspx), [**ResetEvent**](https://msdn.microsoft.com/library/ms685081(v=VS.85).aspx) and [**PulseEvent**](/windows/desktop/api/WinBase/nf-winbase-pulseevent) functions.                                                                                                                                    |



 

The following table lists the object-specific access rights for mutex objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                            |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MUTEX\_ALL\_ACCESS** (0x1F0001) | All possible access rights for a mutex object. Use this right only if your application requires access beyond that granted by the standard access rights. Using this access right increases the possibility that your application must be run by an Administrator. |
| **MUTEX\_MODIFY\_STATE** (0x0001) | Reserved for future use.                                                                                                                                                                                                                                           |



 

The following table lists the object-specific access rights for semaphore objects. These rights are supported in addition to the standard access rights.



| Value                                 | Meaning                                                                                                                                                                                                                                                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SEMAPHORE\_ALL\_ACCESS** (0x1F0003) | All possible access rights for a semaphore object. Use this right only if your application requires access beyond that granted by the standard access rights and **SEMAPHORE\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **SEMAPHORE\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**ReleaseSemaphore**](https://msdn.microsoft.com/library/ms685071(v=VS.85).aspx) function.                                                                                                                                                                                                   |



 

The following table lists the object-specific access rights for waitable timer objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                                                                  |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TIMER\_ALL\_ACCESS** (0x1F0003) | All possible access rights for a waitable timer object. Use this right only if your application requires access beyond that granted by the standard access rights and **TIMER\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **TIMER\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**SetWaitableTimer**](https://msdn.microsoft.com/library/ms686289(v=VS.85).aspx) and [**CancelWaitableTimer**](https://msdn.microsoft.com/library/ms681985(v=VS.85).aspx) functions.                                                                                                                                            |
| **TIMER\_QUERY\_STATE** (0x0001)  | Reserved for future use.                                                                                                                                                                                                                                                                                 |



 

To read or write the SACL of an interprocess synchronization object, you must request the **ACCESS\_SYSTEM\_SECURITY** access right. For more information, see [Access-Control Lists (ACLs)](https://msdn.microsoft.com/library/Aa374872(v=VS.85).aspx) and [SACL Access Right](https://msdn.microsoft.com/library/Aa379321(v=VS.85).aspx).

 

 



