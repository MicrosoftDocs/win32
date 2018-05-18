---
title: Background Intelligent Transfer Service
description: Background Intelligent Transfer Service (BITS) transfers files (downloads or uploads) between a client and server and provides progress information related to the transfers.
ms.assetid: 'ce91f87c-8273-4a1c-99e0-ef55e2a50334'
keywords: ["Background Intelligent Transfer Service", "Background Intelligent Transfer Service, start page", "BITS (See Background Intelligent Transfer Service)", "downloading files BITS", "background file transfer BITS", "uploading files BITS"]
---

# Background Intelligent Transfer Service

## Purpose

Background Intelligent Transfer Service (BITS) transfers files (downloads or uploads) between a client and server and provides progress information related to the transfers. You can also download files from a peer.

> [!Note]  
> BITS is most commonly used by Windows to download updates to your local system. If you are an end-user searching for ways to troubleshoot your BITS installation, see the knowledge base (KB) article link at the bottom of this page. If you are seeking to download or re-install BITS 4.0, see [KB968929](http://go.microsoft.com/fwlink/p/?linkid=151321).

 

## Where applicable

Use BITS for applications that need to:

-   Asynchronously transfer files in the foreground or background.
-   Preserve the responsiveness of other network applications.
-   Automatically resume file transfers after network disconnects and computer restarts.

## Developer audience

BITS is designed for C and C++ developers.

## Run-time requirements

BITS version 4.0 is included in the Windows 7 and Windows Server 2008 R2 operating systems.

You can also download BITS 4.0 for Windows Server 2008 with Service Pack 2 (SP2), Windows Vista with Service Pack 1 (SP1), and Windows Vista with Service Pack 2 (SP2). For information about downloading BITS 4.0, see [KB968929](http://go.microsoft.com/fwlink/p/?linkid=151321).

For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

For complete version history, see [What's New](what-s-new.md).

## In this section



| Topic                                                           | Description                                                                                                                                                                     |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About BITS](about-bits.md)<br/>                         | General information about BITS.<br/>                                                                                                                                      |
| [Using BITS](using-bits.md)<br/>                         | Procedural guide for developing BITS clients that transfer files between a client and server.<br/>                                                                        |
| [BITS Reference](bits-reference.md)<br/>                 | Reference information for the BITS programming interfaces. Also contains information about samples, tools, server settings for upload jobs, and the upload protocol.<br/> |
| [Best Practices](best-practices-when-using-bits.md)<br/> | Information to consider when designing an application that uses BITS.<br/>                                                                                                |



 

## Additional resources

The following are additional resources.



|             |                                                                                                                                                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| KB articles | For a list of Knowledge Base (KB) articles for BITS, see [KB331716](http://go.microsoft.com/fwlink/p/?linkid=83988).                            |
| BITS Blog   | For feature updates, samples, and BITS news, see the [Windows Management Infrastructure Blog](http://go.microsoft.com/fwlink/p/?linkid=155250). |
| .NET Bits   | For a set of .NET wrappers for the BITS API, see [SharpBITS.NET](http://sharpbits.codeplex.com/), at CodePlex.                                  |



 

 

 





