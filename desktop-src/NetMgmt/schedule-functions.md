---
title: Schedule Functions
description: The network management schedule service functions submit and manage jobs that execute on a specified computer at a particular time (or times) in the future.
ms.assetid: 1ddc9b95-fdbc-4e39-9b55-2a5bc570b95d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Schedule Functions

The network management schedule service functions submit and manage jobs that execute on a specified computer at a particular time (or times) in the future. Jobs can include commands and programs. The functions manage jobs at remote and local computers, provided the schedule service is running on the computer.

The schedule service functions are listed following.



| Function                                                                     | Description                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**NetScheduleJobAdd**](/windows/win32/Lmat/nf-lmat-netschedulejobadd?branch=master)                               | Submits a job to run at a specified future date and time.        |
| [**NetScheduleJobDel**](/windows/win32/Lmat/nf-lmat-netschedulejobdel?branch=master)                               | Cancels a range of jobs queued to run on a computer.             |
| [**NetScheduleJobEnum**](/windows/win32/Lmat/nf-lmat-netschedulejobenum?branch=master)                             | Lists the jobs queued on a specified computer.                   |
| [**NetScheduleJobGetInfo**](/windows/win32/Lmat/nf-lmat-netschedulejobgetinfo?branch=master)                       | Returns information about a particular job queued on a computer. |
| [**GetNetScheduleAccountInformation**](/windows/win32/AtAcct/nf-atacct-getnetscheduleaccountinformation?branch=master) | Retrieves the AT Service account name.                           |
| [**SetNetScheduleAccountInformation**](/windows/win32/AtAcct/nf-atacct-setnetscheduleaccountinformation?branch=master) | Sets the AT Service account name and password.                   |



 

For the network management schedule functions to succeed, a caller must have administrator's privilege at the computer where the schedule service is running. The schedule service functions are also known as "Job" and "AT command" functions. For more information about calling functions that require administrator privileges, see [Running with Special Privileges](https://msdn.microsoft.com/library/windows/desktop/ms717802).

The [**AT\_INFO**](/windows/win32/Lmat/ns-lmat-_at_info?branch=master) structure is used by the [**NetScheduleJobAdd**](/windows/win32/Lmat/nf-lmat-netschedulejobadd?branch=master) function to specify information when submitting a job, and by the [**NetScheduleJobGetInfo**](/windows/win32/Lmat/nf-lmat-netschedulejobgetinfo?branch=master) function to retrieve information about a job that has been submitted. The [**AT\_ENUM**](/windows/win32/Lmat/ns-lmat-_at_enum?branch=master) structure is used by [**NetScheduleJobEnum**](/windows/win32/Lmat/nf-lmat-netschedulejobenum?branch=master) to enumerate and return information about an entire queue of submitted jobs.

 

 




