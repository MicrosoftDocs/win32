---
Description: The Windows security model enables you to control access to event, mutex, semaphore, and waitable timer objects. Timer queues, interlocked variables, and critical section objects are not securable. For more information, see Access-Control Model.
ms.assetid: 92478298-617c-4672-a1cc-9a8e9af40327
title: Synchronization Object Security and Access Rights
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Synchronization Object Security and Access Rights

The Windows security model enables you to control access to event, mutex, semaphore, and waitable timer objects. Timer queues, interlocked variables, and critical section objects are not securable. For more information, see [Access-Control Model](security.access_control_model).

You can specify a [security descriptor](security.security_descriptors) for an interprocess synchronization object when you call the [**CreateEvent**](/windows/win32/WinBase/nf-synchapi-createeventa?branch=master), [**CreateMutex**](/windows/win32/WinBase/nf-synchapi-createmutexa?branch=master), [**CreateSemaphore**](/windows/win32/WinBase/nf-winbase-createsemaphorea?branch=master), or [**CreateWaitableTimer**](/windows/win32/WinBase/nf-winbase-createwaitabletimera?branch=master) function. If you specify **NULL**, the object gets a default security descriptor. The [Access-Control Lists (ACLs)](security.access_control_lists_acls_) in the default security descriptor for a synchronization object come from the primary or impersonation token of the creator.

To get or set the security descriptor of an event, mutex, semaphore, or waitable timer object, call the [**GetNamedSecurityInfo**](security.getnamedsecurityinfo), [**SetNamedSecurityInfo**](security.setnamedsecurityinfo), [**GetSecurityInfo**](security.getsecurityinfo), or [**SetSecurityInfo**](security.setsecurityinfo) functions.

The handles returned by [**CreateEvent**](/windows/win32/WinBase/nf-synchapi-createeventa?branch=master), [**CreateMutex**](/windows/win32/WinBase/nf-synchapi-createmutexa?branch=master), [**CreateSemaphore**](/windows/win32/WinBase/nf-winbase-createsemaphorea?branch=master), and [**CreateWaitableTimer**](/windows/win32/WinBase/nf-winbase-createwaitabletimera?branch=master) have full access to the new object. When you call the [**OpenEvent**](/windows/win32/WinBase/nf-synchapi-openeventa?branch=master), [**OpenMutex**](/windows/win32/WinBase/nf-winbase-openmutexa?branch=master), [**OpenSemaphore**](/windows/win32/WinBase/nf-winbase-opensemaphorea?branch=master), and [**OpenWaitableTimer**](/windows/win32/WinBase/nf-winbase-openwaitabletimera?branch=master) functions, the system checks the requested access rights against the object's security descriptor.

The valid access rights for the interprocess synchronization objects include the [standard access rights](security.standard_access_rights) and some object-specific access rights. The following table lists the standard access rights used by all objects.

| Value                           | Meaning                                                                                                                                                                                                                                                                                  |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DELETE** (0x00010000L)        | Required to delete the object.                                                                                                                                                                                                                                                           |
| **READ\_CONTROL** (0x00020000L) | Required to read information in the security descriptor for the object, not including the information in the SACL. To read or write the SACL, you must request the **ACCESS\_SYSTEM\_SECURITY** access right. For more information, see [SACL Access Right](security.sacl_access_right). |
| **SYNCHRONIZE** (0x00100000L)   | The right to use the object for synchronization. This enables a thread to wait until the object is in the signaled state.                                                                                                                                                                |
| **WRITE\_DAC** (0x00040000L)    | Required to modify the DACL in the security descriptor for the object.                                                                                                                                                                                                                   |
| **WRITE\_OWNER** (0x00080000L)  | Required to change the owner in the security descriptor for the object.                                                                                                                                                                                                                  |



 

The following table lists the object-specific access rights for event objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                                                          |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_ALL\_ACCESS** (0x1F0003) | All possible access rights for an event object. Use this right only if your application requires access beyond that granted by the standard access rights and **EVENT\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **EVENT\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**SetEvent**](/windows/win32/WinBase/nf-synchapi-setevent?branch=master), [**ResetEvent**](/windows/win32/WinBase/nf-synchapi-resetevent?branch=master) and [**PulseEvent**](/windows/win32/WinBase/nf-winbase-pulseevent?branch=master) functions.                                                                                                                                    |



 

The following table lists the object-specific access rights for mutex objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                            |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MUTEX\_ALL\_ACCESS** (0x1F0001) | All possible access rights for a mutex object. Use this right only if your application requires access beyond that granted by the standard access rights. Using this access right increases the possibility that your application must be run by an Administrator. |
| **MUTEX\_MODIFY\_STATE** (0x0001) | Reserved for future use.                                                                                                                                                                                                                                           |



 

The following table lists the object-specific access rights for semaphore objects. These rights are supported in addition to the standard access rights.



| Value                                 | Meaning                                                                                                                                                                                                                                                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SEMAPHORE\_ALL\_ACCESS** (0x1F0003) | All possible access rights for a semaphore object. Use this right only if your application requires access beyond that granted by the standard access rights and **SEMAPHORE\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **SEMAPHORE\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**ReleaseSemaphore**](/windows/win32/WinBase/nf-synchapi-releasesemaphore?branch=master) function.                                                                                                                                                                                                   |



 

The following table lists the object-specific access rights for waitable timer objects. These rights are supported in addition to the standard access rights.



| Value                             | Meaning                                                                                                                                                                                                                                                                                                  |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TIMER\_ALL\_ACCESS** (0x1F0003) | All possible access rights for a waitable timer object. Use this right only if your application requires access beyond that granted by the standard access rights and **TIMER\_MODIFY\_STATE**. Using this access right increases the possibility that your application must be run by an Administrator. |
| **TIMER\_MODIFY\_STATE** (0x0002) | Modify state access, which is required for the [**SetWaitableTimer**](/windows/win32/WinBase/nf-synchapi-setwaitabletimer?branch=master) and [**CancelWaitableTimer**](/windows/win32/WinBase/nf-synchapi-cancelwaitabletimer?branch=master) functions.                                                                                                                                            |
| **TIMER\_QUERY\_STATE** (0x0001)  | Reserved for future use.                                                                                                                                                                                                                                                                                 |



 

To read or write the SACL of an interprocess synchronization object, you must request the **ACCESS\_SYSTEM\_SECURITY** access right. For more information, see [Access-Control Lists (ACLs)](security.access_control_lists_acls_) and [SACL Access Right](security.sacl_access_right).

 

 



