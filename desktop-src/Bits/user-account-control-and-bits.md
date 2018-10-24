---
title: User Account Control and BITS
description: In Windows Vista, when an administrator user logs onto the computer, two access tokens are created a filtered standard user access token, and a full administrator access token.
ms.assetid: 02439ab3-b885-4a2f-b507-0c48d2b30b76
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# User Account Control and BITS

In Windows Vista, when an administrator user logs onto the computer, two access tokens are created: a filtered standard user access token, and a full administrator access token. By default, all users, including administrators, log on a Windows Vista computer as standard users. (The exception are guests which log onto the computer with fewer user rights and privileges than standard users.)

A user in the administrator group can run a process with standard user access or in an elevated state (with administrator privileges). To run in an elevated state, the user can right-click the client and select **Run as administrator...**. BITS will run the job in either state as long as the user is logged onto the computer. However, if the user created the job or took ownership of the job in an elevated state, the user must be in the elevated state to retrieve or modify the job (otherwise, the call fails with Access Denied (0x80070005)). To determine the elevated state of a job, call the [**IBackgroundCopyJob4::GetOwnerElevationState**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-getownerelevationstate) method.

A standard user cannot enumerate jobs owned by other users. If a standard user (a user that is not in the administrators group) asks an administrator to provide credentials, and the user then creates a job, the job is created under the administrator's account and will run only when that administrator is logged on, not when the standard user is logged on. Also, the standard user will not be able to modify the job.

In addition to the elevated state, the integrity level of the token can determine if the user can modify a job. A client cannot modify jobs created by a token with a higher integrity level. In particular, many local-system tokens carry an integrity level higher than the integrity level of an elevated window, and so they cannot be modified by an administrator from an ordinary elevated command window. For example, Windows Update and SMS jobs run as LocalSystem which has a higher integrity level than an elevated token so an administrator cannot modify or delete these jobs. To modify these job, create a Task Scheduler task that runs as local system. The task can execute a console application that uses the BITS API, or the task could execute a script that calls BitsAdmin.exe. To determine the integrity level used, call the [**IBackgroundCopyJob4::GetOwnerIntegrityLevel**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-getownerintegritylevel) method.

 

 




