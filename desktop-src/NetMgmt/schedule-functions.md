---
title: Schedule Functions
description: The network management schedule service functions submit and manage jobs that execute on a specified computer at a particular time (or times) in the future.
ms.assetid: 1ddc9b95-fdbc-4e39-9b55-2a5bc570b95d
ms.topic: article
ms.date: 05/31/2018
---

# Schedule Functions

The network management schedule service functions submit and manage jobs that execute on a specified computer at a particular time (or times) in the future. Jobs can include commands and programs. The functions manage jobs at remote and local computers, provided the schedule service is running on the computer.

The schedule service functions are listed following.



| Function                                                                     | Description                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**NetScheduleJobAdd**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobadd)                               | Submits a job to run at a specified future date and time.        |
| [**NetScheduleJobDel**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobdel)                               | Cancels a range of jobs queued to run on a computer.             |
| [**NetScheduleJobEnum**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobenum)                             | Lists the jobs queued on a specified computer.                   |
| [**NetScheduleJobGetInfo**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobgetinfo)                       | Returns information about a particular job queued on a computer. |
| [**GetNetScheduleAccountInformation**](/windows/desktop/api/AtAcct/nf-atacct-getnetscheduleaccountinformation) | Retrieves the AT Service account name.                           |
| [**SetNetScheduleAccountInformation**](/windows/desktop/api/AtAcct/nf-atacct-setnetscheduleaccountinformation) | Sets the AT Service account name and password.                   |



 

For the network management schedule functions to succeed, a caller must have administrator's privilege at the computer where the schedule service is running. The schedule service functions are also known as "Job" and "AT command" functions. For more information about calling functions that require administrator privileges, see [Running with Special Privileges](/windows/desktop/SecBP/running-with-special-privileges).

The [**AT\_INFO**](/windows/desktop/api/Lmat/ns-lmat-at_info) structure is used by the [**NetScheduleJobAdd**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobadd) function to specify information when submitting a job, and by the [**NetScheduleJobGetInfo**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobgetinfo) function to retrieve information about a job that has been submitted. The [**AT\_ENUM**](/windows/desktop/api/Lmat/ns-lmat-at_enum) structure is used by [**NetScheduleJobEnum**](/windows/desktop/api/Lmat/nf-lmat-netschedulejobenum) to enumerate and return information about an entire queue of submitted jobs.

 

 