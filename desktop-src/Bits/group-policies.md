---
title: Group Policies
description: Background Intelligent Transfer Service (BITS) uses the following Group Policies to configure BITS transfers and settings. For more information on which version of BITS is used by different versions of Windows, see the What's New topic.
ms.assetid: 32c7e2b1-bac2-4708-a30c-f6b2a816c1a4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 08/16/2018
---

# Group Policies

> [!NOTE]
> For details about how to use Mobile device management (MDM) to set policies for Background Intelligent Transfer Service (BITS), see [Policy CSP](/windows/client-management/mdm/policy-configuration-service-provider).

Background Intelligent Transfer Service (BITS) uses the following Group Policies to configure BITS transfers and settings. For more information on which version of BITS is used by different versions of Windows, see the [What's New](what-s-new.md) topic.

> [!NOTE]  
> If the policy value is not set, BITS uses the default policy value.

**To enable a BITS policy**

1.  Open Group Policy by entering **gpedit.msc /gpcomputer:"***ComputerName***"** in the **Run** window or at the command prompt in an MS-DOS window.
2.  BITS policies are located under **Computer Configuration**, **Administrative Templates**, **Network**, **Background Intelligent Transfer Service**.
3.  Right-click the policy and select **Properties**.
4.  Follow the directions for enabling and setting the policy.

**BITS 1.5 and earlier:** The **JobInactivityTimeout** policy is located under **Computer Configuration**, **Administrative Templates**, **Network**.

The group policies for BITS are located in the registry at **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**BITS**. Note that only those policies that are configured are listed in the registry.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Policy</th>
<th>Introduced</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>JobInactivityTimeout</td>
<td>BITS 1.0</td>
<td>By default, BITS maintains information about a job for 90 days. If there is no activity against the job for this period of time, BITS cancels the job. Transfer progress or property changes reset the timer.<br/> You might need to adjust this policy if the user does not log on or maintain a network connection for long periods of time.<br/></td>
</tr>
<tr class="even">
<td>MaxInternetBandwidth</td>
<td>BITS 2.0</td>
<td>Limits the network bandwidth that BITS uses for background transfers (this policy does not affect foreground transfers).<br/> Specify a limit to use during a specific time interval and a limit to use at all other times. For example, limit the use of network bandwidth to 10 kilobits per second (Kbps) from 8:00 A.M. to 5:00 P.M. and use all available unused bandwidth the rest of the time.
<blockquote>
[!Note]<br />
Changing the system clock does not affect the bandwidth limitation time interval. For example, if the current time is 2:00 P.M. and the bandwidth limitation interval begins at 3:00 P.M., moving the system clock forward one hour does not mean BITS will enforce the bandwidth limitation an hour early the bandwidth limitation will still occur in one hour. To reflect the system clock change in BITS, you must restart the computer or the BITS service.
</blockquote>
<br/> <br/> Specify the limit in kilobits per second. Base the limit on the size of the network link, not the size of the computer's network interface card (NIC). BITS uses approximately two kilobits if you specify a value less than two kilobits. To prevent BITS transfers from occurring, specify a limit of zero. If you specify a limit of zero, BITS places all background jobs in a transient error state. (The error code is set to BG_E_BLOCKED_BY_POLICY.) BITS places the jobs in the queued state after the time interval expires.<br/> If you disable or do not configure this policy, BITS uses all available unused bandwidth.<br/> Typically, you use this policy to prevent BITS transfers from competing for network bandwidth when the client has a fast network adapter (10 Mbps) but is connected to the network via a slow link (56 Kbps).<br/> For information on how BITS uses network bandwidth, see <a href="network-bandwidth">Network Bandwidth</a>.<br/></td>
</tr>
<tr class="odd">
<td>MaxDownloadTime</td>
<td>BITS 3.0</td>
<td>Determines the length of time that BITS can spend actively transferring the files in the job. The default is 90 days.<br/> To override this policy for a specific job, call the <a href="/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-setmaximumdownloadtime"><strong>IBackgroundCopyJob4::SetMaximumDownloadTime</strong></a> method.<br/></td>
</tr>
<tr class="even">
<td>MaxJobsPerMachine</td>
<td>BITS 3.0</td>
<td>Limits the number of jobs that users can create on the computer. The default is 300 jobs. This policy does not apply to a user with administrator privileges or service accounts.<br/></td>
</tr>
<tr class="odd">
<td>MaxJobsPerUser</td>
<td>BITS 3.0</td>
<td>Limits the number of jobs that a user can create on the computer. The default is 60 jobs per user. This policy does not apply to a user with administrator privileges or service accounts.<br/></td>
</tr>
<tr class="even">
<td>MaxFilesPerJob</td>
<td>BITS 3.0</td>
<td>Limits the number of files that a user can add to a job. The default is 200 files per job. This policy does not apply to a user with administrator privileges or service accounts.<br/></td>
</tr>
<tr class="odd">
<td>MaxRangesPerFile</td>
<td>BITS 3.0</td>
<td>Limits the number of ranges that a user can specify for a file. The default value is 500 ranges. This policy does not apply to a user with administrator privileges or service accounts.<br/></td>
</tr>
</tbody>
</table>

BITS uses the following Group Policies to enable and configure the peer caching.

**BITS 4.0:** The BITS 3.0 Group Policies are deprecated. Setting any of these policies will have no effect.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Policy</th>
<th>Introduced</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EnablePeerCaching</td>
<td>BITS 3.0</td>
<td>By default, peer caching is disabled. To enable peer caching, set this policy. Enabling peer caching allows BITS to download content from peers and to serve the content to peers. <br/> To prevent BITS from downloading content from peers, set the DisablePeerCachingClient policy. To prevent BITS from serving content to peers, set the DisablePeerCachingServer.<br/> A job controls if it can download content from a peer or serve content to peers. For details, see the <a href="/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-setpeercachingflags"><strong>IBackgroundCopyJob4::SetPeerCachingFlags</strong></a> method.<br/> If this policy is not set, you can use the <a href="/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-setconfigurationflags"><strong>IBitsPeerCacheAdministration::SetConfigurationFlags</strong></a> method to enable peer caching; however, if the policy is set later, the policy will override the preference set by the <strong>SetConfigurationFlags</strong> method.<br/></td>
</tr>
<tr class="even">
<td>DisablePeerCachingClient</td>
<td>BITS 3.0</td>
<td>Set this policy to prevent BITS from downloading content from peers.<br/></td>
</tr>
<tr class="odd">
<td>DisablePeerCachingServer</td>
<td>BITS 3.0</td>
<td>Set this policy to prevent BITS from serving content to peers.<br/></td>
</tr>
<tr class="even">
<td>MaxContentAge</td>
<td>BITS 3.0</td>
<td>Specifies the maximum length of time that a file can remain in the peer cache without being accessed. The default is 90 days.<br/> If this policy is not set, you can use the <a href="/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-setmaximumcontentage"><strong>IBitsPeerCacheAdministration::SetMaximumContentAge</strong></a> method to limit the time that a file can remain in the peer cache without being accessed; however, if the policy is set later, the policy will override the preference set by the method.<br/></td>
</tr>
<tr class="odd">
<td>MaxCacheSize</td>
<td>BITS 3.0</td>
<td>Specifies the maximum amount of disk space to use for the peer cache. The default is 1% of the disk.<br/> If this policy is not set, you can use the <a href="/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-setmaximumcachesize"><strong>IBitsPeerCacheAdministration::SetMaximumCacheSize</strong></a> method to set the size of the peer cache; however, if the policy is set later, the policy will override the preference set by the method.<br/></td>
</tr>
<tr class="even">
<td>MaxBandwidthServed</td>
<td>BITS 3.0</td>
<td>Limits the amount of network bandwidth to use when serving content to peers. The default is 1 Mbps.<br/></td>
</tr>
<tr class="odd">
<td>DisableBranchCache</td>
<td>BITS 4.0</td>
<td>By default, the Windows BranchCache feature is enabled. Set this policy to prevent BITS clients from transferring content using the Windows BranchCache.<br/>
<blockquote>
[!Note]<br />
This setting does not affect the use of Windows BranchCache by applications other than BITS. This policy does not apply to BITS transfers over Server Message Block (SMB). This setting has no effect if the computer's administrative settings for Windows Branch Cache disable its use entirely.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>

BITS uses the following Group Policies to configure bandwidth throttling.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Policy</th>
<th>Introduced</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EnableMaintenanceLimits</td>
<td>BITS 4.0</td>
<td>Limits the network bandwidth that BITS uses for background transfers during the maintenance days and hours. Maintenance schedules further limit the network bandwidth that is used for background transfers.<br/> Specify a limit to use for background jobs during a maintenance schedule. For example, if normal priority jobs are currently limited to 256 Kbps on a work schedule, you can further limit the network bandwidth of normal priority jobs to 0 Kbps from 8:00 A.M. to 10:00 A.M. on a maintenance schedule.<br/>
<blockquote>
[!Note]<br />
The bandwidth limits that are set for the maintenance period supersede any limits defined for work and other schedules.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>EnableBandwidthLimits</td>
<td>BITS 4.0</td>
<td>Limits the network bandwidth that BITS uses for background transfers during the work and non-work days and hours. The work schedule is defined using a weekly calendar, which consists of days of the week and hours of the day. All hours and days that are not defined in a work schedule are considered non-work hours.<br/> Specify a limit to use for background jobs during a work schedule. For example, you can limit the network bandwidth of low priority jobs to 128 Kbps from 8:00 A.M. to 5:00 P.M. on Monday through Friday, and then set the limit to 512 Kbps for non-work hours.<br/></td>
</tr>
</tbody>
</table>


## Related topics
* [Policy CSP](/windows/client-management/mdm/policy-configuration-service-provider)