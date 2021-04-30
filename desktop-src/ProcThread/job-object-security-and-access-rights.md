---
description: The Microsoft Windows security model enables you to control access to job objects. For more information about security, see Access-Control Model.
ms.assetid: 8d212292-f087-41e4-884e-cec4423dac49
title: Job Object Security and Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Job Object Security and Access Rights

The Microsoft Windows security model enables you to control access to job objects. For more information about security, see [Access-Control Model](../secauthz/access-control-model.md).

You can specify a [security descriptor](../secauthz/security-descriptors.md) for a job object when you call the [**CreateJobObject**](/windows/desktop/api/WinBase/nf-winbase-createjobobjecta) function. If you specify NULL, the job object gets a default security descriptor. The ACLs in the default security descriptor for a job object come from the primary or impersonation token of the creator.

To get or set the security descriptor for a job object, call the [**GetNamedSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-getnamedsecurityinfoa), [**SetNamedSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-setnamedsecurityinfoa), [**GetSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-getsecurityinfo), or [**SetSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-setsecurityinfo) function.

The valid access rights for job objects include the [standard access rights](../secauthz/standard-access-rights.md) and some job-specific access rights. The following table lists the standard access rights used by all objects.

| Value                           | Meaning                                                                                                                                                                                                                                                                                  |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DELETE** (0x00010000L)        | Required to delete the object.                                                                                                                                                                                                                                                           |
| **READ\_CONTROL** (0x00020000L) | Required to read information in the security descriptor for the object, not including the information in the SACL. To read or write the SACL, you must request the **ACCESS\_SYSTEM\_SECURITY** access right. For more information, see [SACL Access Right](../secauthz/sacl-access-right.md). |
| **SYNCHRONIZE** (0x00100000L)   | The right to use the object for synchronization. This enables a thread to wait until the object is in the signaled state.                                                                                                                                                                |
| **WRITE\_DAC** (0x00040000L)    | Required to modify the DACL in the security descriptor for the object.                                                                                                                                                                                                                   |
| **WRITE\_OWNER** (0x00080000L)  | Required to change the owner in the security descriptor for the object.                                                                                                                                                                                                                  |



 

The following table lists the job-specific access rights.



| Value                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **JOB\_OBJECT\_ALL\_ACCESS** (0x1F001F)             | Combines all valid job object access rights.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **JOB\_OBJECT\_ASSIGN\_PROCESS** (0x0001)           | Required to call the [**AssignProcessToJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-assignprocesstojobobject) function to assign processes to the job object.                                                                                                                                                                                                                                                                                                                                                                |
| **JOB\_OBJECT\_QUERY** (0x0004)                     | Required to retrieve certain information about a job object, such as attributes and accounting information (see [**QueryInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-queryinformationjobobject) and [**IsProcessInJob**](/windows/win32/api/jobapi/nf-jobapi-isprocessinjob)).                                                                                                                                                                                                                                                                    |
| **JOB\_OBJECT\_SET\_ATTRIBUTES** (0x0002)           | Required to call the [**SetInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-setinformationjobobject) function to set the attributes of the job object.                                                                                                                                                                                                                                                                                                                                                                |
| **JOB\_OBJECT\_SET\_SECURITY\_ATTRIBUTES** (0x0010) | This flag is not supported. You must set security limitations individually for each process associated with a job object.**Windows Server 2003 and Windows XP:** Required to call the [**SetInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-setinformationjobobject) function with the **JobObjectSecurityLimitInformation** information class to set security limitations for the processes associated with the job object. Support for this flag was removed in Windows Vista and Windows Server 2008. <br/> |
| **JOB\_OBJECT\_TERMINATE** (0x0008)                 | Required to call the [**TerminateJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-terminatejobobject) function to terminate all processes in the job object.                                                                                                                                                                                                                                                                                                                                                                     |



 

The handle returned by [**CreateJobObject**](/windows/desktop/api/WinBase/nf-winbase-createjobobjecta) has **JOB\_OBJECT\_ALL\_ACCESS** access to the job object. When you call the [**OpenJobObject**](/windows/desktop/api/WinBase/nf-winbase-openjobobjecta) function, the system checks the requested access rights against the object's security descriptor. If a job object is in a hierarchy of [nested jobs](nested-jobs.md), a caller with access to the job object implicitly has access to all of its child jobs in the hierarchy.

You can request the **ACCESS\_SYSTEM\_SECURITY** access right to a job object if you want to read or write the object's SACL. For more information, see [Access-Control Lists (ACLs)](../secauthz/access-control-lists.md) and [SACL Access Right](../secauthz/sacl-access-right.md).

You must set security limitations individually for each process associated with a job object, rather than setting them for the job object itself. For information, see [Process Security and Access Rights](process-security-and-access-rights.md).

**Windows Server 2003 and Windows XP:** You can use the [**SetInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-setinformationjobobject) function to set security limitations for the job object. This capability was removed in Windows Vista and Windows Server 2008.

 

 
