---
description: The device-redirecting functions redirect standard MS-DOS devices, drive letters and LPT ports. This enables applications running on the system to use the devices and access the network in a totally transparent manner.
ms.assetid: a61ab1e6-dad9-4dc0-a908-f8440619f610
title: Device-Redirecting Functions
ms.topic: article
ms.date: 05/31/2018
---

# Device-Redirecting Functions

The device-redirecting functions redirect standard MS-DOS devices, drive letters and LPT ports. This enables applications running on the system to use the devices and access the network in a totally transparent manner.



| Function                                                         | Description                                                                                                                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NPAddConnection**](/windows/desktop/api/Npapi/nf-npapi-npaddconnection)                       | Redirects or connects a local device to a network resource.<br/>                                                                                                                              |
| [**NPAddConnection3**](/windows/desktop/api/Npapi/nf-npapi-npaddconnection3)                     | Performs the same action as [**NPAddConnection**](/windows/desktop/api/Npapi/nf-npapi-npaddconnection), but lets the user specify which window should own any dialog boxes and how the connection should be established.<br/> |
| [**NPCancelConnection**](/windows/desktop/api/Npapi/nf-npapi-npcancelconnection)                 | Breaks a network connection. The changes are remembered if a device is disconnected unless the connection is a deviceless connection.<br/>                                                    |
| [**NPGetConnection**](/windows/desktop/api/Npapi/nf-npapi-npgetconnection)                       | Returns information about a connection.<br/>                                                                                                                                                  |
| [**NPGetConnection3**](/windows/desktop/api/Npapi/nf-npapi-npgetconnection3)                     | Returns information about a connection, even if the connection is currently disconnected.<br/>                                                                                                |
| [**NPGetConnectionPerformance**](/windows/desktop/api/Npapi/nf-npapi-npgetconnectionperformance) | Returns performance information about a connection.<br/>                                                                                                                                      |
| [**NPGetUniversalName**](/windows/desktop/api/Npapi/nf-npapi-npgetuniversalname)                 | Returns the remote or local universal name, in the format specified during the function call.<br/>                                                                                            |



 

 

 




