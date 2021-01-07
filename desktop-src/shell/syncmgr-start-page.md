---
description: The Synchronization Manager provides a centralized, standard technology for synchronizing files for offline use on a mobile computer or a computer connected to a local area network.
title: Synchronization Manager
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 6cdac7e5-8985-407a-98bb-936bb20ed069
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbOrient

---

# Synchronization Manager

## Purpose

The Synchronization Manager provides a centralized, standard technology for synchronizing files for offline use on a mobile computer or a computer connected to a local area network. Together with the connectivity functions, notifications (System Event Notification Service), and client side caching, the Synchronization Manager provides an infrastructure to support mobile computing. Instead of each application implementing its own technology to cache and synchronize network resources for local use, the operating system provides an integrated model that all applications can use. Files are synchronized independent of the protocol. For example, an email program can transfer its messages using SMTP, NMTP, or POP3, while a browser can use HTTP, and a database can use remote procedure call (RPC) (RPC). Developers can use the common interface to the Synchronization Manager in their applications to synchronize files between the user's local computer and network storage.

## Where applicable

The Synchronization Manager is intended for applications that run primarily on mobile computers. Applications that run on computers connected to high latency local area networks may also benefit from using the Synchronization Manager.

## Developer audience

This document is intended for software developers who develop applications for mobile computing and high latency local area networks. This document provides a complete reference of all parts of the Synchronization Manager including the methods and interfaces to the Synchronization Manager.

## Run-time requirements

Requires Windows Server 2003, Windows XP, Windows 2000, or Windows Millennium Edition (Windows Me). Also available as a redistributable for Microsoft Windows NT 4.0, Windows 98, and Windows 95.

## In this section



| Topic                                                                                       | Description                                                                                                                                         |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Synchronization Manager](syncmgr-about.md)<br/>                               | The Synchronization Manager provides a centralized, standard technology for synchronizing files for offline use on a local computer.<br/>     |
| [Mobile Computing Configurations](syncmgr-mobile-computing-configs.md)<br/>          | Applications can use Sychronization Manager to keep files and resources cached locally and synchronized on mobile and desktop computers.<br/> |
| [Application Scenarios](syncmgr-app-scenarios.md)<br/>                               | Applications and services that can use Synchronization Manager.<br/>                                                                          |
| [Synchronization Manager Architecture](syncmgr-architecture.md)<br/>                 |                                                                                                                                                     |
| [Using Synchronization Manager from a Program](syncmgr-using-from-a-program.md)<br/> |                                                                                                                                                     |
| [Synchronization Manager Reference](syncmgr-reference.md)<br/>                       | The following programming elements make up the API for Synchronization Manager.<br/>                                                          |



 

## Related topics

<dl> <dt>

[About System Event Notification Service](../sens/about-system-event-notification-service.md)
</dt> </dl>

 

 
