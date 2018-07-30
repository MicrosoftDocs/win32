---
Description: The Microsoft Windows security model enables you to control access to job objects. For more information about security, see Access-Control Model.
ms.assetid: 8d212292-f087-41e4-884e-cec4423dac49
title: Job Object Security and Access Rights
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Job Object Security and Access Rights

The Microsoft Windows security model enables you to control access to job objects. For more information about security, see [Access-Control Model](https://msdn.microsoft.com/en-us/library/Aa374876(v=VS.85).aspx).

You can specify a [security descriptor](https://msdn.microsoft.com/en-us/library/Aa379563(v=VS.85).aspx) for a job object when you call the [**CreateJobObject**](/windows/desktop/api/WinBase/nf-winbase-createjobobjecta) function. If you specify NULL, the job object gets a default security descriptor. The ACLs in the default security descriptor for a job object come from the primary or impersonation token of the creator.

To get or set the security descriptor for a job object, call the [**GetNamedSecurityInfo**](https://msdn.microsoft.com/en-us/library/Aa446645(v=VS.85).aspx), [**SetNamedSecurityInfo**](https://msdn.microsoft.com/en-us/library/Aa379579(v=VS.85).aspx), [**GetSecurityInfo**](https://msdn.microsoft.com/en-us/library/Aa446654(v=VS.85).aspx), or [**SetSecurityInfo**](https://msdn.microsoft.com/en-us/library/Aa379588(v=VS.85).aspx) function.

The valid access rights for job objects include the [standard access rights](https://msdn.microsoft.com/en-us/library/Aa379607(v=VS.85).aspx) and some job-specific access rights. The following table lists the standard access rights used by all objects.

| Value                           | Meaning                                                                                                                                                                                                                                                                                  |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DELETE** (0x00010000L)        | Required to delete the object.                                                                                                                                                                                                                                                           |
| **READ\_CONTROL** (0x00020000L) | Required to read information in the security descriptor for the object, not including the information in the SACL. To read or write the SACL, you must request the **ACCESS\_SYSTEM\_SECURITY** access right. For more information, see [SACL Access Right](https://msdn.microsoft.com/en-us/library/Aa379321(v=VS.85).aspx). |
| **SYNCHRONIZE** (0x00100000L)   | The right to use the object for synchronization. This enables a thread to wait until the object is in the signaled state.                                                                                                                                                                |
| **WRITE\_DAC** (0x00040000L)    | Required to modify the DACL in the security descriptor for the object.                                                                                                                                                                                                                   |
| **WRITE\_OWNER** (0x00080000L)  | Required to change the owner in the security descriptor for the object.                                                                                                                                                                                                                  |



 

The following table lists the job-specific access rights.



| Value                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **JOB\_OBJECT\_ALL\_ACCESS** (0x1F001F)             | Combines all valid job object access rights.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **JOB\_OBJECT\_ASSIGN\_PROCESS** (0x0001)           | Required to call the [**AssignProcessToJobObject**](https://msdn.microsoft.com/en-us/library/ms681949(v=VS.85).aspx) function to assign processes to the job object.                                                                                                                                                                                                                                                                                                                                                                |
| **JOB\_OBJECT\_QUERY** (0x0004)                     | Required to retrieve certain information about a job object, such as attributes and accounting information (see [**QueryInformationJobObject**](https://msdn.microsoft.com/en-us/library/ms684925(v=VS.85).aspx) and [**IsProcessInJob**](https://msdn.microsoft.com/en-us/library/ms684127(v=VS.85).aspx)).                                                                                                                                                                                                                                                                    |
| **JOB\_OBJECT\_SET\_ATTRIBUTES** (0x0002)           | Required to call the [**SetInformationJobObject**](https://msdn.microsoft.com/en-us/library/ms686216(v=VS.85).aspx) function to set the attributes of the job object.                                                                                                                                                                                                                                                                                                                                                                |
| **JOB\_OBJECT\_SET\_SECURITY\_ATTRIBUTES** (0x0010) | This flag is not supported. You must set security limitations individually for each process associated with a job object.**Windows Server 2003 and Windows XP:** Required to call the [**SetInformationJobObject**](https://msdn.microsoft.com/en-us/library/ms686216(v=VS.85).aspx) function with the **JobObjectSecurityLimitInformation** information class to set security limitations for the processes associated with the job object. Support for this flag was removed in Windows Vista and Windows Server 2008. <br/> |
| **JOB\_OBJECT\_TERMINATE** (0x0008)                 | Required to call the [**TerminateJobObject**](https://msdn.microsoft.com/en-us/library/ms686709(v=VS.85).aspx) function to terminate all processes in the job object.                                                                                                                                                                                                                                                                                                                                                                     |



 

The handle returned by [**CreateJobObject**](/windows/desktop/api/WinBase/nf-winbase-createjobobjecta) has **JOB\_OBJECT\_ALL\_ACCESS** access to the job object. When you call the [**OpenJobObject**](/windows/desktop/api/WinBase/nf-winbase-openjobobjecta) function, the system checks the requested access rights against the object's security descriptor. If a job object is in a hierarchy of [nested jobs](nested-jobs.md), a caller with access to the job object implicitly has access to all of its child jobs in the hierarchy.

You can request the **ACCESS\_SYSTEM\_SECURITY** access right to a job object if you want to read or write the object's SACL. For more information, see [Access-Control Lists (ACLs)](https://msdn.microsoft.com/library/Aa374872(v=VS.85).aspx) and [SACL Access Right](https://msdn.microsoft.com/en-us/library/Aa379321(v=VS.85).aspx).

You must set security limitations individually for each process associated with a job object, rather than setting them for the job object itself. For information, see [Process Security and Access Rights](process-security-and-access-rights.md).

**Windows Server 2003 and Windows XP:  ** You can use the [**SetInformationJobObject**](https://msdn.microsoft.com/en-us/library/ms686216(v=VS.85).aspx) function to set security limitations for the job object. This capability was removed in Windows Vista and Windows Server 2008.

 

 




