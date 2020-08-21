---
title: About BITS
description: Use Background Intelligent Transfer Service (BITS) to transfer files asynchronously between a client and a server.
ms.assetid: 056007f4-6a71-4f8e-bf7d-17ed87088edf
keywords:
- Background Intelligent Transfer Service, described
- transfer queue BITS
- transfer queue BITS , throttle
ms.topic: article
ms.date: 7/12/2019
---

# About BITS

Use Background Intelligent Transfer Service (BITS) to download files from or upload files to HTTP web servers or SMB file servers. 

BITS continues to transfer files after an application exits as long as the user who initiated the transfer remains logged on and a network connection is maintained. BITS will not force a network connection. BITS resumes transfers after a network connection that had been lost is reestablished or after a user who had logged off logs back in. For more information, see [Users and Network Connections](users-and-network-connections.md).

BITS is mindful of the current network cost and congestion so that a background job interferes as little as possible with the user's foreground experience. BITS uses idle [network bandwidth](network-bandwidth.md) to transfer the files and will increase or decrease the rate at which files are transferred based on the amount of idle network bandwidth available. If a network application begins to consume more bandwidth, BITS decreases its transfer rate to preserve the user's interactive experience. BITS uses app-specified [transfer policies](how-to-block-a-bits-job-from-downloading-over-an-expensive-connection.md) to prevent files from transferring on costed network connections.

BITS is also mindful of power usage. Starting with the Windows 10 May 2019 Update, BITS will transfer files when the machine is in [Modern Standby](/windows-hardware/design/device-experiences/modern-standby) mode and the machine is plugged in.

The BITS application can use the different BITS [priority levels](/windows/desktop/api/Bits/ne-bits-bg_job_priority) to let BITS intelligently pick which transfer jobs to run. Higher priority jobs preempt lower priority jobs. Jobs at the same priority level share transfer time, which prevents a large job from blocking small jobs in the transfer queue. Lower priority jobs do not receive transfer time until all higher priority jobs are complete or in an error state.

BITS uses Windows BranchCache for peer caching. For more information, see the [BranchCache Overview](/previous-versions/windows/it-pro/windows-7/dd755969(v=ws.10)).

Universal Windows Platform (UWP) developers should use the [Windows.Networking.BackgroundTransfer](/uwp/api/Windows.Networking.BackgroundTransfer) API and not the BITS API.

There are three types of [**transfer jobs**](/windows/desktop/api/Bits/ne-bits-bg_job_type). A download job downloads files to the client, an upload job uploads a file to the server, and an upload-reply job uploads a file to the server and receives a reply file from the server application.

The following topics provide more detailed information about BITS:

-   [Authentication](authentication.md)
-   [Life Cycle of a BITS Job](life-cycle-of-a-bits-job.md)
-   [Users and Network Connections](users-and-network-connections.md)
-   [Network Bandwidth](network-bandwidth.md)
-   [Group Policies](group-policies.md)
-   [Service Accounts and BITS](service-accounts-and-bits.md)
-   [Helper Tokens for BITS Transfer Jobs](helper-tokens-for-bits-transfer-jobs.md)
-   [File Transfer Consistency](file-transfer-consistency.md)
-   [HTTP Requirements for BITS Downloads](http-requirements-for-bits-downloads.md)
-   [IIS Requirements for BITS Uploads](iis-requirements-for-bits-uploads.md)
-   [Virtual Directory Cleanup](virtual-directory-cleanup.md)
-   [BITS and System Restore](bits-and-system-restore.md)
-   [BITS Startup Type](bits-startup-type.md)
-   [Internet Connection Sharing](internet-connection-sharing.md)
-   [Peer Caching](peer-caching.md)
-   [BITS Security, Tokens, and Administrator Accounts](user-account-control-and-bits.md)
-   [BITS Compact Server](bits-compact-server.md)

Use the BITS [interfaces](bits-interfaces.md) to write applications that create and monitor transfer jobs. For details on using the BITS interfaces, see [Using BITS](using-bits.md).