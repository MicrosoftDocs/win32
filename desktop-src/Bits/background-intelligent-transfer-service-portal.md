---
title: Background Intelligent Transfer Service
description: Background Intelligent Transfer Service (BITS) transfers files (downloads or uploads) between a client and server and provides progress information related to the transfers.
ms.assetid: ce91f87c-8273-4a1c-99e0-ef55e2a50334
keywords:
- Background Intelligent Transfer Service
- Background Intelligent Transfer Service, start page
- BITS (See Background Intelligent Transfer Service)
- downloading files BITS
- background file transfer BITS
- uploading files BITS
ms.topic: article
ms.date: 11/29/2018
---

# Background Intelligent Transfer Service

## Purpose

Background Intelligent Transfer Service (BITS) is used by programmers and system administrators to download files from or upload files to HTTP web servers and SMB file shares. BITS will take the cost of the transfer into consideration, as well as the network usage so that the user's foreground work has as little impact as possible. BITS also handles network interuptions, pausing and automatically resuming transfers, even after a reboot. BITS includes PowerShell cmdlets for creating and managing transfers as well as the BitsAdmin command-line utility.

> [!Note]  
> BITS can be used by Windows to download updates to your local system. If you are an end-user searching for ways to troubleshoot your BITS installation, see [Fix Windows Update Issues](https://support.microsoft.com/help/10164/fix-windows-update-errors). 
 

## Where applicable

Use BITS for applications that need to:

-   Download from or upload files to an HTTP or REST web server or SMB file server.
-   Automatically resume file transfers after network disconnects and computer restarts.
-   Preserve the responsiveness of other network applications.
-   Be mindful of the network cost on e.g. roaming networks
-   Optionally work with [BranchCache](/windows-server/networking/branchcache/branchcache) to optimize wide area network (WAN) traffic

## Developer audience

BITS is a COM interface designed for C and C++ developers that can also be used by .NET developers. UWP developers should use the [Windows.Networking.BackgroundTransfer](/uwp/api/Windows.Networking.BackgroundTransfer) API and not the BITS API.

## BITS versions

For complete version history and information on earlier operating system, see [What's New](what-s-new.md).


## In this section



| Topic                                                           | Description                                                                                                                                                                     |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About BITS](about-bits.md)<br/>                         | General information about BITS.<br/>                                                                                                                                      |
| [Using BITS](using-bits.md)<br/>                         | Procedural guide for developing BITS clients that transfer files between a client and server.<br/>                                                                        |
| [BITS Reference](bits-reference.md)<br/>                 | Reference information for the BITS programming interfaces. Also contains information about samples, tools, server settings for upload jobs, and the upload protocol.<br/> |
| [Best Practices](best-practices-when-using-bits.md)<br/> | Information to consider when designing an application that uses BITS.<br/>                                                                                                |



 

## Additional resources

The following are additional resources.


|    Resource         |    Description                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| .NET Reference DLL   | For information on using BITS from .NET using reference DLLs, see [Calling into BITS from .NET using Reference DLLs](/windows/desktop/Bits/bits-dot-net)      |
| .NET Wrapper   | For other .NET wrappers for BITS, you can search [nuget](https://www.nuget.org/packages?q=Tags%3A%22BITS%22) for projects tagged with the BITS tag.        |



 

 

