---
title: About BITS
description: Use Background Intelligent Transfer Service (BITS) to transfer files asynchronously between a client and a server.
ms.assetid: 056007f4-6a71-4f8e-bf7d-17ed87088edf
keywords:
- Background Intelligent Transfer Service, described
- transfer queue BITS
- transfer queue BITS , throttle
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About BITS

Use Background Intelligent Transfer Service (BITS) to transfer files asynchronously between a client and a server. There are three types of [**transfer jobs**](/windows/desktop/api/Bits/ne-bits-__midl_ibackgroundcopyjob_0003). A download job downloads files to the client, an upload job uploads a file to the server, and an upload-reply job uploads a file to the server and receives a reply file from the server application.

BITS continues to transfer files after an application exits if the user who initiated the transfer remains logged on and a network connection is maintained. BITS will not force a connection.

BITS suspends the transfer if a connection is lost or if the user logs off. BITS persists transfer information while the user is logged off, across network disconnects, and during computer restarts.

When the user logs on again, BITS resumes the user's transfer job. For more information, see [Users and Network Connections](users-and-network-connections.md).

BITS provides one foreground and three background [priority levels](/windows/desktop/api/Bits/ne-bits-__midl_ibackgroundcopyjob_0001) that you use to prioritize transfer jobs. Higher priority jobs preempt lower priority jobs. Jobs at the same priority level share transfer time, which prevents a large job from blocking small jobs in the transfer queue. Lower priority jobs do not receive transfer time until all higher priority jobs are complete or in an error state.

Background transfers are optimal in that BITS uses idle [network bandwidth](network-bandwidth.md) to transfer the files and will increase or decrease the rate at which files are transferred based on the amount of idle network bandwidth available. If a network application begins to consume more bandwidth, BITS decreases its transfer rate to preserve the user's interactive experience.

BITS uses the Windows BranchCache for peer caching. For more information, see the [BranchCache Overview](http://go.microsoft.com/fwlink/p/?linkid=150953).

The following topics provide more detailed information about BITS:

-   [Users and Network Connections](users-and-network-connections.md)
-   [Service Accounts and BITS](service-accounts-and-bits.md)
-   [Life Cycle of a BITS Job](life-cycle-of-a-bits-job.md)
-   [Network Bandwidth](network-bandwidth.md)
-   [Peer Caching](peer-caching.md)
-   [HTTP Requirements for BITS Downloads](http-requirements-for-bits-downloads.md)
-   [IIS Requirements for BITS Uploads](iis-requirements-for-bits-uploads.md)
-   [Authentication](authentication.md)
-   [Group Policies](group-policies.md)
-   [File Transfer Consistency](file-transfer-consistency.md)
-   [Virtual Directory Cleanup](virtual-directory-cleanup.md)
-   [Internet Connection Sharing](internet-connection-sharing.md)
-   [BITS and System Restore](bits-and-system-restore.md)
-   [BITS Startup Type](bits-startup-type.md)

Use the BITS [interfaces](bits-interfaces.md) to write applications that create and monitor transfer jobs. For details on using the BITS interfaces, see [Using BITS](using-bits.md).

 

 




