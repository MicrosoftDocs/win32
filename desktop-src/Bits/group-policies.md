---
title: Group Policies
description: Background Intelligent Transfer Service (BITS) uses the following Group Policies to configure BITS transfers and settings. For more information on which version of BITS is used by different versions of Windows, see the What's New topic.
ms.assetid: 32c7e2b1-bac2-4708-a30c-f6b2a816c1a4
ms.topic: article
ms.date: 10/04/2018
---

# Group Policies

> [!NOTE]
> For details about how to use Mobile device management (MDM) to set policies for Background Intelligent Transfer Service (BITS), see [Policy CSP](/windows/client-management/mdm/policy-configuration-service-provider).

Background Intelligent Transfer Service (BITS) uses the following Group Policies to configure BITS transfers and settings. For more information on which version of BITS is used by different versions of Windows, see the [What's New](what-s-new.md) topic.

> [!NOTE]  
> If the policy value is not set, BITS uses the default policy value.

**To enable a BITS policy**

1.  Open Group Policy by entering **gpedit.msc /gpcomputer:"***ComputerName***"** in the **Run** window or at the command prompt in a CMD window.
2.  BITS policies are located under **Computer Configuration**, **Administrative Templates**, **Network**, **Background Intelligent Transfer Service**.
3.  Right-click the policy and select **Edit**.
4.  Follow the directions for enabling and setting the policy.

The group policies for BITS are located in the registry at **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**BITS**. Note that only those policies that are configured are listed in the registry.

|Policy|Description|
|-|-|
|JobInactivityTimeout<br/>BITS 1.0|By default, BITS maintains information about a job for 90 days. If there is no activity against the job for this period of time, BITS cancels the job. Transfer progress or property changes reset the timer.<br/> You might need to adjust this policy if the user does not log on or maintain a network connection for long periods of time.|
|MaxInternetBandwidth<br/>BITS 2.0|Limits the network bandwidth that BITS uses for background transfers (this policy does not affect foreground transfers).<br/>Specify a limit to use during a specific time interval and a limit to use at all other times. For example, limit the use of network bandwidth to 10 kilobits per second (Kbps) from 8:00 A.M. to 5:00 P.M. and use all available unused bandwidth the rest of the time.<br/>**Note**: changing the system clock does not affect the bandwidth limitation time interval. For example, if the current time is 2:00 P.M. and the bandwidth limitation interval begins at 3:00 P.M., moving the system clock forward one hour does not mean BITS will enforce the bandwidth limitation an hour early the bandwidth limitation will still occur in one hour. To reflect the system clock change in BITS, you must restart the computer or the BITS service.<br/>Specify the limit in kilobits per second. Base the limit on the size of the network link, not the size of the computer's network interface card (NIC). BITS uses approximately two kilobits if you specify a value less than two kilobits. To prevent BITS transfers from occurring, specify a limit of zero. If you specify a limit of zero, BITS places all background jobs in a transient error state. (The error code is set to BG_E_BLOCKED_BY_POLICY.) BITS places the jobs in the queued state after the time interval expires.<br/> If you disable or do not configure this policy, BITS uses all available unused bandwidth.<br/> Typically, you use this policy to prevent BITS transfers from competing for network bandwidth when the client has a fast network adapter (10 Mbps) but is connected to the network via a slow link (56 Kbps).<br/> For information on how BITS uses network bandwidth, see [Network Bandwidth](network-bandwidth.md).|
|MaxDownloadTime<br/>BITS 3.0|Determines the length of time that BITS can spend actively transferring the files in the job. The default is 90 days.<br/> To override this policy for a specific job, call the [**IBackgroundCopyJob4::SetMaximumDownloadTime**](/windows/desktop/api/bits3_0/nf-bits3_0-ibackgroundcopyjob4-setmaximumdownloadtime) method.|
|MaxJobsPerMachine<br/>BITS 3.0|Limits the number of jobs that users can create on the computer. The default is 300 jobs. This policy does not apply to a user with administrator privileges or service accounts.|
|MaxJobsPerUser<br/>BITS 3.0|Limits the number of jobs that a user can create on the computer. The default is 60 jobs per user. This policy does not apply to a user with administrator privileges or service accounts.|
|MaxFilesPerJob<br/>BITS 3.0|Limits the number of files that a user can add to a job. The default is 200 files per job. This policy does not apply to a user with administrator privileges or service accounts.|
|MaxRangesPerFile<br/>BITS 3.0|Limits the number of ranges that a user can specify for a file. The default value is 500 ranges. This policy does not apply to a user with administrator privileges or service accounts.|

BITS uses the following Group Policies to enable and configure how BITS interacts with BranchCache.

|Policy|Description|
|-|-|
|DisableBranchCache<br/>BITS 4.0|By default, the Windows BranchCache feature is enabled. Set this policy to prevent BITS clients from transferring content using the Windows BranchCache.<br/>**Note**: this setting does not affect the use of Windows BranchCache by applications other than BITS. This policy does not apply to BITS transfers over Server Message Block (SMB). This setting has no effect if the computer's administrative settings for Windows Branch Cache disable its use entirely.|

BITS uses the following Group Policies to configure bandwidth throttling.

|Policy|Description|
|-|-|
|EnableMaintenanceLimits<br/>BITS 4.0|Limits the network bandwidth that BITS uses for background transfers during the maintenance days and hours. Maintenance schedules further limit the network bandwidth that is used for background transfers.<br/> Specify a limit to use for background jobs during a maintenance schedule. For example, if normal priority jobs are currently limited to 256 Kbps on a work schedule, you can further limit the network bandwidth of normal priority jobs to 0 Kbps from 8:00 A.M. to 10:00 A.M. on a maintenance schedule.<br/>**Note**: the bandwidth limits that are set for the maintenance period supersede any limits defined for work and other schedules.|
|EnableBandwidthLimits<br/>BITS 4.0|Limits the network bandwidth that BITS uses for background transfers during the work and non-work days and hours. The work schedule is defined using a weekly calendar, which consists of days of the week and hours of the day. All hours and days that are not defined in a work schedule are considered non-work hours.<br/> Specify a limit to use for background jobs during a work schedule. For example, you can limit the network bandwidth of low priority jobs to 128 Kbps from 8:00 A.M. to 5:00 P.M. on Monday through Friday, and then set the limit to 512 Kbps for non-work hours.|


## Related topics
* [Policy CSP](/windows/client-management/mdm/policy-configuration-service-provider)
