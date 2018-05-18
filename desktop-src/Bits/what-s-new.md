---
title: What's New
description: The following table identifies what is new for each release of Background Intelligent Transfer Service (BITS).
ms.assetid: 'ef05f2e1-88be-4adb-aca7-a7b1451cfd04'
keywords: ["what's new BITS"]
---

# What's New

The following table identifies what is new for each release of Background Intelligent Transfer Service (BITS).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Version</th>
<th>Description of features</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Version 10.1</td>
<td>New features:<br/>
<ul>
<li>BITS version 10.1 is included in Windows 10 Creator’s Update and later.</li>
<li>Added [<strong>BackgroundCopyFile6</strong>](ibackgroundcopyfile6.md) and [<strong>IBackgroundCopyCallback3</strong>](ibackgroundcopycallback3.md) to enable “random access” scenarios for HTTP downloads.</li>
<li>Added <strong>BITS_JOB_PROPERTY_ON_DEMAND_MODE</strong> and <strong>BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS</strong> to the [<strong>BITS_JOB_PROPERTY_ID</strong>](bits-job-property-id.md) enumeration to tweak download and notification behaviors, respectively.</li>
</ul></td>
</tr>
<tr class="even">
<td>Version 5.0</td>
<td>New features:<br/>
<ul>
<li>Added the [<strong>IBackgroundCopyJob5</strong>](bits5-functions.md) interface which adds generic methods for getting and setting BITS job properties to the methods inherited from the [<strong>IBackgroundCopyJob4</strong>](ibackgroundcopyjob4.md) interface.<br/> For information on using the new [<strong>IBackgroundCopyJob5</strong>](bits5-functions.md) interface, see [How to control whether a BITS job is allowed to download over an expensive connection](how-to-block-a-bits-job-from-downloading-over-an-expensive-connection.md) and [How to get the last set of HTTP headers received for each file in a BITS download job](how-to-get-the-last-set-of-http-headers-received-for-each-file-in-a-bits-download-job.md).<br/></li>
<li>Added the [<strong>BITS_JOB_PROPERTY_VALUE</strong>](bits-job-property-value.md) union and the [<strong>BITS_JOB_PROPERTY_ID</strong>](bits-job-property-id.md), and [<strong>BITS_JOB_TRANSFER_POLICY</strong>](bits-job-transfer-policy.md) enumerations. For usage examples, see the above How to topics.</li>
<li>Added the [<strong>IBackgroundCopyFile5</strong>](ibackgroundcopyfile5.md) interface, which adds methods for getting and setting generic properties on BackgroundCopyFile objects to the methods inherited from the [<strong>IBackgroundCopyFile4</strong>](ibackgroundcopyfile4.md) interface. The addition of generic properties will make it possible to enhance BackgroundCopyFile capabilities in the future without requiring that a new interface be created.</li>
<li>The first generic property exposed by [<strong>IBackgroundCopyFile5</strong>](ibackgroundcopyfile5.md) is the <strong>HttpResponseHeaders</strong> property.</li>
<li>Added the [<strong>BITS_FILE_PROPERTY_VALUE</strong>](bits-file-property-value.md) union and the [<strong>BITS_FILE_PROPERTY_ID</strong>](bits-file-property-id.md) enumeration.</li>
</ul>
BITS version 5.0 is included in the Windows Server 2012 and Windows 8 operating systems, where the version of %windir%\System32\QMgr.dll is &quot;7.7.xxxx.xxxx&quot;.<br/> The following features were added to BITS in Windows 10<br/>
<ul>
<li>In Windows 10, version 1607, it is possible to use the BITS COM APIs and BITS PowerShell cmdlets (where available) in a PowerShell Remote Session. This is especially useful when administrating versions of Windows Server 2016 that have no local login capability. BITS jobs started via PowerShell Remote Sessions run in the session's user account context, and will only make progress when there is at least on active local logon session or PowerShell Remote session associated with that user account. Consider using persistent PowerShell Remote sessions (see [New-PSSession](https://technet.microsoft.com/library/hh849717.aspx)) for long-running transfers.</li>
<li>In Windows 10, version 1607, it is now possible for a BITS job owner to set helper tokens without being an administrator, as long as the helper token does not have administrator capabilities. This reduces the vulnerability footprint of background download or update tools by enabling them to run under the lower-privileged NetworkService account rather than under an account with administrative privileges.</li>
</ul>
BITS version 5.0 is also included in Windows 10, where the version of %windir%\System32\QMgr.dll is &quot;7.8.xxxx.xxxx&quot;.<br/></td>
</tr>
<tr class="odd">
<td>Version 4.0</td>
<td>New features:<br/>
<ul>
<li>Peer caching now uses Windows BranchCache. This new peer caching model replaces the model used for BITS version 3.0. For more information, see [Peer Caching](peer-caching.md).</li>
<li>Added a more flexible resource access model that allows applications to associate a pair of security tokens to a BITS transfer job. For more information, see [Helper tokens for BITS transfer jobs](helper-tokens-for-bits-transfer-jobs.md).</li>
<li>Added the [BITS Compact Server](bits-compact-server.md), which is a stand-alone HTTP/HTTPS file server that provides the ability to transfer a limited number of large files asynchronously between computers.</li>
<li>Added more granular bandwidth throttling. For more information, see [Group Policies](group-policies.md).</li>
</ul>
BITS version 4.0 is included in the Windows Server 2008 R2 and Windows 7 operating systems.<br/> You can also download BITS 4.0 for Windows Server 2008 with Service Pack 2 (SP2), Windows Vista with Service Pack 1 (SP1), and Windows Vista with Service Pack 2 (SP2). For information about downloading BITS 4.0, see [KB968929](http://go.microsoft.com/fwlink/p/?linkid=151321).<br/> The version of %windir%\System32\QMgr.dll is &quot;7.5.xxxx.xxxx&quot;.<br/></td>
</tr>
<tr class="even">
<td>Version 3.0</td>
<td>New features:<br/>
<ul>
<li>Added [Peer Caching](peer-caching.md) which lets you download content from peers and also serve content to peers in a domain network.</li>
<li>Added [notification](ibackgroundcopycallback2-filetransferred.md) for when a file is downloaded.</li>
<li>Added access to the [temporary file](ibackgroundcopyfile3-gettemporaryname.md) while the download is in progress.</li>
<li>Added the ability to control HTTP [redirects](ibackgroundcopyjobhttpoptions-setsecurityflags.md).</li>
<li>Added more [group policies](group-policies.md) to control peer caching and limit download times.</li>
<li>Added diagnostic and troubleshooting events to the system event log.</li>
<li>Added support for [User Account Control](user-account-control-and-bits.md) (UAC).</li>
</ul>
<blockquote>
[!Note]<br />
BITS now uses group policies to limit the number of jobs and files you can create. This might affect applications that currently create a large number of jobs or add a large number of files to a job.
</blockquote>
<br/> <br/> BITS version 3.0 is included in the Windows Server 2008 and Windows Vista operating systems. <br/> The version of %windir%\System32\QMgr.dll is &quot;7.0.xxxx.xxxx&quot;.<br/></td>
</tr>
<tr class="odd">
<td>Version 2.5</td>
<td>Added support for custom HTTP headers, certificate-based client authentication for secure HTTP transports, and IPv6. Also added the use of Internet gateway device (IGD) counters to more accurately calculate available [bandwidth](network-bandwidth.md).<br/> The BITS 2.5 features are available in the Windows Server 2008, Windows Vista, and Windows XP with Service Pack 3 (SP3) operating systems. <br/> You can also download BITS 2.5 for Windows Server 2003 with Service Pack 2 (SP2), Windows Server 2003 with Service Pack 1 (SP1), and Windows XP with Service Pack 2 (SP2). To download BITS 2.5, go to the [Microsoft Download Center](http://go.microsoft.com/fwlink/p/?linkid=93607) and install KB923845.<br/> The version of %windir%\System32\QMgr.dll is &quot;6.7.xxxx.xxxx&quot;.<br/></td>
</tr>
<tr class="even">
<td>Version 2.0</td>
<td>Added support for performing concurrent foreground downloads, using Server Message Block (SMB) paths for remote names, downloading ranges of a file, changing the prefix or complete name of a remote name, and limiting client bandwidth usage.<br/> BITS version 2.0 is included in Windows XP with SP2 and Windows Server 2003 with SP1. You can also download BITS 2.0 for Windows Server 2003, and Windows XP. To download BITS 2.0, go to the [Microsoft Download Center](http://go.microsoft.com/fwlink/p/?linkid=84094) and install KB842773.<br/> The version of %windir%\System32\QMgr.dll is &quot;6.6.xxxx.xxxx&quot;.<br/></td>
</tr>
<tr class="odd">
<td>Version 1.5</td>
<td>Added upload and upload-reply capability, command-line execution for events, and explicit credentials.<br/> BITS version 1.5 is included in Windows Server 2003. A redistributable is available for Windows XP from the [Microsoft Download Center](http://go.microsoft.com/fwlink/p/?linkid=83468).<br/> The version of %windir%\System32\QMgr.dll is &quot;6.5.xxxx.xxxx&quot;.<br/></td>
</tr>
<tr class="even">
<td>Version 1.2</td>
<td>Same functionality as version 1.0. Contains internal upgrades and improvements.<br/> BITS version 1.2 is included in Windows XP with Service Pack 1 (SP1).<br/> The version of %windir%\System32\QMgr.dll is &quot;6.2.xxxx.xxxx&quot;.<br/></td>
</tr>
<tr class="odd">
<td>Version 1.0</td>
<td>Initial release. Provides prioritized, throttled, and asynchronous downloads in the background or foreground. The downloads automatically resume after computer restarts and network disconnects.<br/> BITS version 1.0 is included in Windows XP.<br/> The version of %windir%\System32\QMgr.dll is &quot;6.0.xxxx.xxxx&quot;.<br/></td>
</tr>
</tbody>
</table>



 

## Version 5.0

The following interfaces were added for this version:

-   [**IBackgroundCopyJob5**](bits5-functions.md)

## Version 4.0

The following interfaces were added for this version:

-   [**IBitsToken**](ibitstokenoptions.md)
-   [**IBackgroundCopyFile4**](ibackgroundcopyfile4.md)

## Version 3.0

The following interfaces were added for this version:

-   [**IBackgroundCopyCallback2**](ibackgroundcopycallback2.md)
-   [**IBackgroundCopyFile3**](ibackgroundcopyfile3.md)
-   [**IBackgroundCopyJob4**](ibackgroundcopyjob4.md)
-   [**IBitsPeer**](ibitspeer.md)
-   [**IBitsPeerCacheAdministration**](ibitspeercacheadministration.md)
-   [**IBitsPeerCacheRecord**](ibitspeercacherecord.md)
-   [**IEnumBitsPeerCacheRecords**](ienumbitspeercacherecords.md)
-   [**IEnumBitsPeers**](ienumbitspeers.md)

The following constants were added to use with the [**IBackgroundCopyJobHttpOptions::SetSecurityFlags**](ibackgroundcopyjobhttpoptions-setsecurityflags.md) method:

-   **BG\_HTTP\_REDIRECT\_POLICY\_ALLOW\_SILENT**
-   **BG\_HTTP\_REDIRECT\_POLICY\_ALLOW\_REPORT**
-   **BG\_HTTP\_REDIRECT\_POLICY\_DISALLOW**
-   **BG\_HTTP\_REDIRECT\_POLICY\_MASK**
-   **BG\_HTTP\_REDIRECT\_POLICY\_ALLOW\_HTTPS\_TO\_HTTP**

## Version 2.5

The following interface and enumeration were added for version 2.5:

-   [**IBackgroundCopyJobHttpOptions**](ibackgroundcopyjobhttpoptions.md)
-   [**BG\_CERT\_STORE\_LOCATION**](bg-cert-store-location.md)

## Version 2.0

The following interfaces, structure, and topics were added for version 2.0:

-   [**IBackgroundCopyJob3**](ibackgroundcopyjob3.md)
-   [**IBackgroundCopyFile2**](ibackgroundcopyfile2.md)
-   [**BG\_FILE\_RANGE**](bg-file-range.md)
-   [Group Policies](group-policies.md)

For information about concurrent foreground downloads, see the Remarks section for [**BG\_JOB\_PRIORITY**](bg-job-priority.md).

For information about using the SMB protocol, see [**BG\_FILE\_INFO**](bg-file-info.md).

## Version 1.5

The following interfaces and topics were added for version 1.5:

-   [**IBackgroundCopyJob2**](ibackgroundcopyjob2.md)
-   [Retrieving the Reply from an Upload-Reply Job](retrieving-the-reply-from-an-upload-reply-job.md)
-   [Registering to Execute a Program](registering-to-execute-a-program.md)
-   [BITS Server Settings for Upload Jobs](bits-server-settings-for-upload-jobs.md)
-   [Setting Up the Server for Uploads](setting-up-the-server-for-uploads.md)
-   [Using BITS Notification Request/Response Headers](using-bits-notification-request-response-headers.md)

 

 





