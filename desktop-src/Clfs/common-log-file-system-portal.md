---
Description: 'An event logging file subsystem for Windows event log management that any user-mode application or multiple clients that need log management software, event management, event log monitoring, or recovery support can use.'
ms.assetid: 'c8656542-ebfa-4e0a-9199-ed9632ed1ede'
title: Common Log File System
---

# Common Log File System

## Purpose

The Common Log File System (CLFS) API provides a high-performance, general-purpose log file subsystem that dedicated client applications can use and multiple clients can share to optimize log access.

Any user-mode application that needs logging or recovery support can use CLFS.

## Where applicable

You can use CLFS for data and event management and to develop server and enterprise applications.

For data management, you can use CLFS with the following:

-   Database systems
-   Messaging, such as store-and-forward systems
-   Online transactional processing (OLTP) systems
-   Other kinds of transactional systems

For event management, you can use CLFS for the following:

-   Network event logging for firewall, sniffer, and tripwire events
-   Threat analysis, including threat event logging and threat data-stream collection
-   Audit logging, including compliance logs

## Developer audience

The CLFS API is for programmers familiar with C and C++ languages.

## Run-time requirements

Applications that use CLFS are supported starting with Windows Server 2003 R2.

## In this section



| Topic                                                                                         | Description                                                                                             |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [Common Log File System API](common-log-file-system-api.md)<br/>                       | Provides high-performance persistent log services to user-mode and kernel-mode applications.<br/> |
| [Common Log File System Management API](common-log-file-system-management-api.md)<br/> | Handles low-level log management for user-mode and kernel-mode applications.<br/>                 |



 

## Related topics

<dl> <dt>

[CLFS Windows DDK documentation](http://go.microsoft.com/fwlink/p/?linkid=83890)
</dt> <dt>

[Kernel Transaction Manager](fs.kernel_transaction_manager_portal)
</dt> <dt>

[Transactional NTFS](fs.transactional_ntfs_portal)
</dt> </dl>

 

 




