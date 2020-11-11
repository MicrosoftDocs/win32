---
title: Peer Caching
description: Starting with Background Intelligent Transfer Service (BITS) 4.0, the BITS service was extended to allow subnet-level peer caching for downloaded URL data by using Windows BranchCache.
ms.assetid: 4197eed3-1812-4440-99e7-9462635ef6ad
ms.topic: article
ms.date: 11/29/2018
---

# Peer Caching

Starting with Background Intelligent Transfer Service (BITS) 4.0, the BITS service was extended to allow subnet-level peer caching for downloaded URL data by using Windows BranchCache. BITS clients can retrieve data from other computers in their own subnet that have already downloaded the data, instead of retrieving the data from remote servers. For more information about Windows BranchCache, see the [BranchCache Overview](/previous-versions/windows/it-pro/windows-7/dd755969(v=ws.10)).

If an administrator enables Windows BranchCache on client and server computers in an organization through a group policy or local configuration settings, BITS will use Windows BranchCache for data transfers.

-   [Configuration for BITS 4.0 Peer Caching](#configuration-for-bits-40-peer-caching)
-   [Disabling Windows BranchCache](#disabling-windows-branchcache)
-   [Verification and Monitoring](#verification-and-monitoring)
-   [Peer Caching in BITS 3.0](#peer-caching-in-bits-30)

## Configuration for BITS 4.0 Peer Caching

The following configuration is required for peer caching in BITS 4.0 to function:

-   Windows BranchCache must be enabled on the client through a group policy or local configuration settings. For more information, see [BranchCache client configuration](/previous-versions/windows/it-pro/windows-7/dd637820(v=ws.10)).
    > [!Note]  
    > The Windows BranchCache feature is disabled by default.

     

-   The Windows BranchCache feature is an optional component that must be installed on the server. For more information, see [BranchCache server configuration](/previous-versions/windows/it-pro/windows-7/dd637785(v=ws.10)).
-   The server must also enable the Windows BranchCache feature though group policy or local configuration settings. For more information, see [BranchCache server configuration](/previous-versions/windows/it-pro/windows-7/dd637785(v=ws.10)).
    > [!Note]  
    > The Windows BranchCache feature is disabled by default.

     

The default BITS group policy allows peer caching. If Windows BranchCache is enabled globally on a computer, this feature is also enabled for BITS transfer jobs. For more information about the BITS-specific group policies, see [Group Policies](group-policies.md).

## Disabling Windows BranchCache

An administrator can use a group policy to disable the use of the Windows BranchCache. (See [Group Policies](group-policies.md).) If the Windows BranchCache is disabled, BITS clients will retrieve data only from remote servers.

An application can also disable the Windows BranchCache on a per job basis by calling the [**IBackgroundCopyJob4::SetPeerCachingFlags**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-setpeercachingflags) method and setting the **BG\_DISABLE\_BRANCH\_CACHE** flag.

> [!Note]  
> These settings do not affect the use of Windows BranchCache by applications other than BITS. These settings do not apply to BITS transfers over SMB. BITS does not control any settings for Windows BranchCache transfers over SMB.

 

## Verification and Monitoring

There are a number of ways to verify and monitor peer caching statistics. Administrators can call the [**IBackgroundCopyFile4::GetPeerDownloadStats**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibackgroundcopyfile4-getpeerdownloadstats) method to query the amount of data that was downloaded from peers and from origin servers. Administrators can also check the event log for [Event ID 60](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc734635(v=ws.10)), which provides job-specific information.

The Windows BranchCache feature also provides a number of mechanisms to verify and monitor peer caching statistics. For more information, see [Verification and Monitoring](/previous-versions/windows/it-pro/windows-7/dd637782(v=ws.10)) and [Performance Counters](/previous-versions/windows/it-pro/windows-7/dd637826(v=ws.10)).

The peer caching model that uses Windows BranchCache replaces the peer caching model used in BITS 3.0. For more information about Windows BranchCache, see the following:

-   [BranchCache](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj127252(v=ws.11))
-   [BranchCache Overview](/previous-versions/windows/it-pro/windows-7/dd755969(v=ws.10))
-   [Windows 7 Services](../win7devguide/services.md)
-   [Peer Distribution API](../p2psdk/peer-distribution.md)

## Peer Caching in BITS 3.0

> [!Note]  
> Starting with Windows 7, the BITS 3.0 peer caching model is deprecated. If BITS 4.0 is installed, the BITS 3.0 peer caching model is unavailable.

 

If the administrator enables peer caching and the job permits downloading content from a peer, BITS will try to download the content from one or more peers. Downloading from a peer is much faster than downloading content from the Internet. Peer caching is disabled by default and jobs must explicitly permit downloading content from peers. An administrator can use a group policy to enable peer caching. After enabling peer caching, the administrator can disable either downloading from a peer or serving content to a peer.

An application can also enable peer caching by calling the [**IBitsPeerCacheAdministration::SetConfigurationFlags**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-setconfigurationflags) method. However, these settings are overridden by the group policy settings, if set.

When peer caching is enabled, BITS creates a list of peers that are in the same subnet and belong to the same domain. The list will not include peers from a trusted domain. Peer caching can be enabled only in a domain environment.

BITS discovers the peers by doing the following:

-   Listening for peer servers that announce themselves. A peer server will announce itself when it starts. BITS will add the peer server to the list if the client needs more peers in its list.
-   Broadcasting a request for peer servers when it needs more peers in its peer list. Peer servers that are available to serve content respond to the request.

BITS removes peer servers from the peer list if the server does the following:

-   Fails authentication
-   Is offline (unavailable) for too long
-   Provides a certificate with errors

When a job requests content from a peer, BITS randomly chooses a subset of peers from the peer list and asks them if they have the content. BITS can download content only from authenticated peer servers. The client and server initially authenticate each other using Kerberos and then exchange self-signed certificates for authentication during content discovery and download.

BITS downloads the content from the first authenticated peer to respond to the request. If one peer does not contain all of the content, BITS will download what it can from one or more of the peers before downloading the rest from the origin server. If none of the peers has the content or an error occurs while downloading from a peer, BITS downloads the content from the origin server.

The downloaded content becomes available to serve to other peers only after the application validates the files contents. If the application does not explicitly validate the file, the file is implicitly validated when the application completes the job.

By default, a peer server can serve content to only three clients simultaneously. If the server is currently busy serving three clients, there will be a delay in responding to other requests. BITS limits the bandwidth used to serve content to 1 Mbps. You can use the [MaxBandwidthServed](group-policies.md) group policy to change the limit.

> [!Note]  
> This feature is supported only in domain networks; peer caching is not supported on workgroups or home networks.

See also [Administering the Peer Cache](/windows/desktop/Bits/administering-the-peer-cache)
 

 

 