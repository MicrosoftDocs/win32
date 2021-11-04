---
title: What's New (BITS)
description: The following table identifies what is new for each release of Background Intelligent Transfer Service (BITS).
ms.assetid: ef05f2e1-88be-4adb-aca7-a7b1451cfd04
keywords:
- what's new BITS
ms.topic: article
ms.date: 7/12/2019
---

# What's New (BITS)

Since its first release as part of Windows XP, the Background Intelligent Transfer Service (BITS) has been constantly improved, adding more powerful controls for the developer and admin to control and manage downloads. A rich set of PowerShell cmdlets has been added; it can connect to more types of HTTP servers; it's more careful of the user's network bandwidth and costs than ever before. 

The following table identifies what is new for each release of Background Intelligent Transfer Service (BITS).




| Version | Description of features | 
|---------|-------------------------|
| Version 10.3 | New features:<br /><ul><li>Added <a href="/windows/win32/api/bits10_3/nn-bits10_3-ibackgroundcopyjobhttpoptions3"><strong>BackgroundCopyJobHttpOptions3</strong></a> to mark HTTP headers as write-only, and to set a server certificate validation callback.</li><li>BITS will retain its service identity when created by another system service.</li><li>BITS will continue to transfer files on connected standby as long as the device is plugged in.</li></ul>BITS version 10.3 is included in the Windows 10 May 2019 Update (10.0; Build 18362), and later. | 
| Version 10.2 | New features:<br /><ul><li>Added <a href="/windows/win32/api/bits10_2/nn-bits10_2-ibackgroundcopyjobhttpoptions2"><strong>BackgroundCopyJobHttpOptions2</strong></a> to change the HTTP method for HTTP downloads.</li><li>BITS now uses the default proxy ordering to be more consistent with the rest of the system.</li><li>It's easier for programmers to set BITS proxy configuration for enterprise scenarios.</li><li>BITS is now more careful of power and supports [Modern Standby](/windows-hardware/design/device-experiences/modern-standby).</li><li>BITS now support Mobile device manager (MDM) [policies](/windows/client-management/mdm/policy-configuration-service-provider) in addition to [group policies](./group-policies).</li></ul>BITS version 10.2 is included in Windows 10 October 2018 Update(10.0; Build 17763), and later. | 
| Version 10.1 | New features:<br /><ul><li>Added <a href="/windows/win32/api/bits10_1/nn-bits10_1-ibackgroundcopyfile6"><strong>BackgroundCopyFile6</strong></a> and <a href="/windows/win32/api/Bits10_1/nn-bits10_1-ibackgroundcopycallback3"><strong>IBackgroundCopyCallback3</strong></a> to enable  random-access scenarios for HTTP downloads.</li><li>Added <strong>BITS_JOB_PROPERTY_ON_DEMAND_MODE</strong> and <strong>BITS_JOB_PROPERTY_MINIMUM_NOTIFICATION_INTERVAL_MS</strong> to the <a href="/windows/win32/api/bits5_0/ne-bits5_0-bits_job_property_id"><strong>BITS_JOB_PROPERTY_ID</strong></a> enumeration to tweak download and notification behaviors, respectively.</li></ul>BITS version 10.1 is included in Windows 10 Creator's Update and later. | 
| Version 5.0 | New features:<br /><ul><li>Added the <a href="/windows/win32/api/Bits5_0/nn-bits5_0-ibackgroundcopyjob5"><strong>IBackgroundCopyJob5</strong></a> interface which adds generic methods for getting and setting BITS job properties to the methods inherited from the <a href="/windows/win32/api/Bits3_0/nn-bits3_0-ibackgroundcopyjob4"><strong>IBackgroundCopyJob4</strong></a> interface.<br /> For information on using the new <a href="/windows/win32/api/Bits5_0/nn-bits5_0-ibackgroundcopyjob5"><strong>IBackgroundCopyJob5</strong></a> interface, see <a href="how-to-block-a-bits-job-from-downloading-over-an-expensive-connection.md">How to control whether a BITS job is allowed to download over an expensive connection</a> and <a href="how-to-get-the-last-set-of-http-headers-received-for-each-file-in-a-bits-download-job.md">How to get the last set of HTTP headers received for each file in a BITS download job</a>.<br /></li><li>Added the <a href="/windows/win32/api/bits5_0/ns-bits5_0-bits_job_property_value"><strong>BITS_JOB_PROPERTY_VALUE</strong></a> union and the <a href="/windows/win32/api/bits5_0/ne-bits5_0-bits_job_property_id"><strong>BITS_JOB_PROPERTY_ID</strong></a>, and <a href="/windows/win32/api/bits5_0/ne-bits5_0-bits_job_transfer_policy"><strong>BITS_JOB_TRANSFER_POLICY</strong></a> enumerations. For usage examples, see the above How to topics.</li><li>Added the <a href="/windows/win32/api/Bits5_0/nn-bits5_0-ibackgroundcopyfile5"><strong>IBackgroundCopyFile5</strong></a> interface, which adds methods for getting and setting generic properties on BackgroundCopyFile objects to the methods inherited from the <a href="/windows/win32/api/Bits4_0/nn-bits4_0-ibackgroundcopyfile4"><strong>IBackgroundCopyFile4</strong></a> interface. The addition of generic properties will make it possible to enhance BackgroundCopyFile capabilities in the future without requiring that a new interface be created.</li><li>The first generic property exposed by <a href="/windows/win32/api/Bits5_0/nn-bits5_0-ibackgroundcopyfile5"><strong>IBackgroundCopyFile5</strong></a> is the <strong>HttpResponseHeaders</strong> property.</li><li>Added the <a href="/windows/win32/api/bits5_0/ns-bits5_0-bits_file_property_value"><strong>BITS_FILE_PROPERTY_VALUE</strong></a> union and the <a href="/windows/win32/api/bits5_0/ne-bits5_0-bits_file_property_id"><strong>BITS_FILE_PROPERTY_ID</strong></a> enumeration.</li></ul>BITS version 5.0 is included in the Windows Server 2012 and Windows 8 operating systems, where the version of %windir%\System32\QMgr.dll is "7.7.xxxx.xxxx".<br /> The following features were added to BITS in Windows 10<br /><ul><li>In Windows 10, version 1607, it is possible to use the BITS COM APIs and BITS PowerShell cmdlets (where available) in a PowerShell Remote Session. This is especially useful when administrating versions of Windows Server 2016 that have no local login capability. BITS jobs started via PowerShell Remote Sessions run in the session's user account context, and will only make progress when there is at least on active local logon session or PowerShell Remote session associated with that user account. Consider using persistent PowerShell Remote sessions (see <a href="/powershell/module/microsoft.powershell.core/new-pssession">New-PSSession</a>) for long-running transfers.</li><li>In Windows 10, version 1607, it is now possible for a BITS job owner to set helper tokens without being an administrator, as long as the helper token does not have administrator capabilities. This reduces the vulnerability footprint of background download or update tools by enabling them to run under the lower-privileged NetworkService account rather than under an account with administrative privileges.</li></ul>BITS version 5.0 is also included in Windows 10, where the version of %windir%\System32\QMgr.dll is "7.8.xxxx.xxxx".<br /> | 
| Version 4.0 | New features:<br /><ul><li>Peer caching now uses Windows BranchCache. This new peer caching model replaces the model used for BITS version 3.0. For more information, see <a href="peer-caching.md">Peer Caching</a>.</li><li>Added a more flexible resource access model that allows applications to associate a pair of security tokens to a BITS transfer job. For more information, see <a href="helper-tokens-for-bits-transfer-jobs.md">Helper tokens for BITS transfer jobs</a>.</li><li>Added the <a href="bits-compact-server.md">BITS Compact Server</a>, which is a stand-alone HTTP/HTTPS file server that provides the ability to transfer a limited number of large files asynchronously between computers.</li><li>Added more granular bandwidth throttling. For more information, see <a href="group-policies.md">Group Policies</a>.</li></ul>BITS version 4.0 is included in the Windows Server 2008 R2 and Windows 7 operating systems.<br /> You can also download BITS 4.0 for Windows Server 2008 with Service Pack 2 (SP2), Windows Vista with Service Pack 1 (SP1), and Windows Vista with Service Pack 2 (SP2). For information about downloading BITS 4.0, see <a href="https://support.microsoft.com/kb/968929">KB968929</a>.<br /> The version of %windir%\System32\QMgr.dll is "7.5.xxxx.xxxx".<br /> | 
| Version 3.0 | New features:<br /><ul><li>Added <a href="peer-caching.md">Peer Caching</a> which lets you download content from peers and also serve content to peers in a domain network.</li><li>Added <a href="/windows/win32/api/Bits3_0/nf-bits3_0-ibackgroundcopycallback2-filetransferred">notification</a> for when a file is downloaded.</li><li>Added access to the <a href="/windows/win32/api/Bits3_0/nf-bits3_0-ibackgroundcopyfile3-gettemporaryname">temporary file</a> while the download is in progress.</li><li>Added the ability to control HTTP <a href="/windows/win32/api/Bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setsecurityflags">redirects</a>.</li><li>Added more <a href="group-policies.md">group policies</a> to control peer caching and limit download times.</li><li>Added diagnostic and troubleshooting events to the system event log.</li><li>Added support for <a href="user-account-control-and-bits.md">User Account Control</a> (UAC).</li><li>On Windows Vista and higher, the default BITS startup type is delayed auto-start.</li></ul><blockquote>[!Note]<br />BITS now uses group policies to limit the number of jobs and files you can create. This might affect applications that currently create a large number of jobs or add a large number of files to a job.</blockquote><br /><br /> BITS version 3.0 is included in the Windows Server 2008 and Windows Vista operating systems. <br /> The version of %windir%\System32\QMgr.dll is "7.0.xxxx.xxxx".<br /> | 
| Version 2.5 | Added support for custom HTTP headers, certificate-based client authentication for secure HTTP transports, and IPv6. Also added the use of Internet gateway device (IGD) counters to more accurately calculate available <a href="network-bandwidth.md">bandwidth</a>.<br /> The BITS 2.5 features are available in the Windows Server 2008, Windows Vista, and Windows XP with Service Pack 3 (SP3) operating systems. <br /> You can also download BITS 2.5 for Windows Server 2003 with Service Pack 2 (SP2), Windows Server 2003 with Service Pack 1 (SP1), and Windows XP with Service Pack 2 (SP2). To download BITS 2.5, go to the <a href="https://www.microsoft.com/download/details.aspx?id=4933">Microsoft Download Center</a> and install KB923845.<br /> The version of %windir%\System32\QMgr.dll is "6.7.xxxx.xxxx".<br /> | 
| Version 2.0 | Added support for performing concurrent foreground downloads, using Server Message Block (SMB) paths for remote names, downloading ranges of a file, changing the prefix or complete name of a remote name, and limiting client bandwidth usage. The JobInactivityTimeout policy is now located under Computer Configuration, Administrative Templates, Network, Background Intelligent Transfer Service (BITS).<br /> BITS version 2.0 is included in Windows XP with SP2 and Windows Server 2003 with SP1. You can also download BITS 2.0 for Windows Server 2003, and Windows XP. To download BITS 2.0, go to the <a href="https://www.microsoft.com/download/details.aspx?id=19031">Microsoft Download Center</a> and install KB842773.<br /> The version of %windir%\System32\QMgr.dll is "6.6.xxxx.xxxx".<br /> | 
| Version 1.5 | Added upload and upload-reply capability, command-line execution for events, and explicit credentials and proxy credentials.<br /> Starting with BITS 1.5, users with a <a href="/windows/win32/secauthz/restricted-tokens">restricted token</a> cannot create or modify jobs.<br /> BITS version 1.5 is included in Windows Server 2003. A redistributable is available for Windows XP from the <a href="https://www.microsoft.com/download/details.aspx?id=22250">Microsoft Download Center</a>.<br /> The version of %windir%\System32\QMgr.dll is "6.5.xxxx.xxxx".<br /> | 
| Version 1.2 | Same functionality as version 1.0. Contains internal upgrades and improvements.<br /> BITS version 1.2 is included in Windows XP with Service Pack 1 (SP1).<br /> The version of %windir%\System32\QMgr.dll is "6.2.xxxx.xxxx".<br /> | 
| Version 1.0 | Initial release. Provides prioritized, throttled, and asynchronous downloads in the background or foreground. The downloads automatically resume after computer restarts and network disconnects.<br /> BITS version 1.0 is included in Windows XP.<br /> The version of %windir%\System32\QMgr.dll is "6.0.xxxx.xxxx".<br /> | 


To light up features in your program based on BITS capabilities, use QueryInterface on (for example) your Job object to see if the Job object allows you to create the version you need. Alternatively, 
see [Determining the Version of BITS on a Computer](./determining-the-version-of-bits-on-a-computer.md) to convert the QMgr.dll version number into the BITS version.

## Version 10.3

The following interfaces were added for this version
-   [**IBackgroundCopyJobHttpOptions3**](/windows/win32/api/Bits10_3/nn-bits10_3-ibackgroundcopyjobhttpoptions3)
    [**IBackgroundCopyServerCertificateValidationCallback**](/windows/win32/api/Bits10_3/nn-bits10_3-ibackgroundcopyservercertificatevalidationcallback)


## Version 10.2

The following interfaces were added for this version
-   [**IBackgroundCopyJobHttpOptions2**](/windows/win32/api/Bits10_2/nn-bits10_2-ibackgroundcopyjobhttpoptions2)


## Version 10.1

The following interfaces were added for this version
-   [**BackgroundCopyFile6**](/windows/win32/api/bits10_1/nn-bits10_1-ibackgroundcopyfile6)
-   [**IBackgroundCopyCallback3**](/windows/win32/api/Bits10_1/nn-bits10_1-ibackgroundcopycallback3)

The following constants were added to use with the [BITS_JOB_PROPERTY_ID enumeration](/windows/win32/api/bits5_0/ne-bits5_0-bits_job_property_id).

-   **BITS\_JOB\_PROPERTY\_ON\_DEMAND\_MODE**
-   **BITS\_JOB\_PROPERTY\_MINIMUM\_NOTIFICATION\_INTERVAL\_MS**


## Version 5.0

The following interfaces were added for this version:

-   [**IBackgroundCopyJob5**](/windows/win32/api/Bits5_0/nn-bits5_0-ibackgroundcopyjob5)

## Version 4.0

The following interfaces were added for this version:

-   [**IBitsToken**](/windows/win32/api/Bits4_0/nn-bits4_0-ibitstokenoptions)
-   [**IBackgroundCopyFile4**](/windows/win32/api/Bits4_0/nn-bits4_0-ibackgroundcopyfile4)

## Version 3.0

The following interfaces were added for this version:

-   [**IBackgroundCopyCallback2**](/windows/win32/api/Bits3_0/nn-bits3_0-ibackgroundcopycallback2)
-   [**IBackgroundCopyFile3**](/windows/win32/api/Bits3_0/nn-bits3_0-ibackgroundcopyfile3)
-   [**IBackgroundCopyJob4**](/windows/win32/api/Bits3_0/nn-bits3_0-ibackgroundcopyjob4)
-   [**IBitsPeer**](/windows/win32/api/Bits3_0/nn-bits3_0-ibitspeer)
-   [**IBitsPeerCacheAdministration**](/windows/win32/api/Bits3_0/nn-bits3_0-ibitspeercacheadministration)
-   [**IBitsPeerCacheRecord**](/windows/win32/api/Bits3_0/nn-bits3_0-ibitspeercacherecord)
-   [**IEnumBitsPeerCacheRecords**](/windows/win32/api/Bits3_0/nn-bits3_0-ienumbitspeercacherecords)
-   [**IEnumBitsPeers**](/windows/win32/api/Bits3_0/nn-bits3_0-ienumbitspeers)

The following constants were added to use with the [**IBackgroundCopyJobHttpOptions::SetSecurityFlags**](/windows/win32/api/Bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setsecurityflags) method:

-   **BG\_HTTP\_REDIRECT\_POLICY\_ALLOW\_SILENT**
-   **BG\_HTTP\_REDIRECT\_POLICY\_ALLOW\_REPORT**
-   **BG\_HTTP\_REDIRECT\_POLICY\_DISALLOW**
-   **BG\_HTTP\_REDIRECT\_POLICY\_MASK**
-   **BG\_HTTP\_REDIRECT\_POLICY\_ALLOW\_HTTPS\_TO\_HTTP**

## Version 2.5

The following interface and enumeration were added for version 2.5:

-   [**IBackgroundCopyJobHttpOptions**](/windows/win32/api/Bits2_5/nn-bits2_5-ibackgroundcopyjobhttpoptions)
-   [**BG\_CERT\_STORE\_LOCATION**](/windows/win32/api/Bits2_5/ne-bits2_5-bg_cert_store_location)

## Version 2.0

The following interfaces, structure, and topics were added for version 2.0:

-   [**IBackgroundCopyJob3**](/windows/win32/api/Bits2_0/nn-bits2_0-ibackgroundcopyjob3)
-   [**IBackgroundCopyFile2**](/windows/win32/api/Bits2_0/nn-bits2_0-ibackgroundcopyfile2)
-   [**BG\_FILE\_RANGE**](/windows/win32/api/Bits2_0/ns-bits2_0-bg_file_range)
-   [Group Policies](group-policies.md)

For information about concurrent foreground downloads, see the Remarks section for [**BG\_JOB\_PRIORITY**](/windows/win32/api/Bits/ne-bits-bg_job_priority).

For information about using the SMB protocol, see [**BG\_FILE\_INFO**](/windows/win32/api/Bits/ns-bits-bg_file_info).

## Version 1.5

The following interfaces and topics were added for version 1.5:

-   [**IBackgroundCopyJob2**](/windows/win32/api/Bits1_5/nn-bits1_5-ibackgroundcopyjob2)
-   [Retrieving the Reply from an Upload-Reply Job](retrieving-the-reply-from-an-upload-reply-job.md)
-   [Registering to Execute a Program](registering-to-execute-a-program.md)
-   [BITS Server Settings for Upload Jobs](bits-server-settings-for-upload-jobs.md)
-   [Setting Up the Server for Uploads](setting-up-the-server-for-uploads.md)
-   [Using BITS Notification Request/Response Headers](using-bits-notification-request-response-headers.md)

 
## Updating BITS versions
 
You can download BITS 4.0 for Windows Server 2008 with Service Pack 2 (SP2), Windows Vista with Service Pack 1 (SP1), and Windows Vista with Service Pack 2 (SP2). For information about downloading BITS 4.0, see [KB968929](https://support.microsoft.com/kb/968929).
