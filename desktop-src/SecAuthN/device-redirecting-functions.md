---
Description: The device-redirecting functions redirect standard MS-DOS devices, drive letters and LPT ports. This enables applications running on the system to use the devices and access the network in a totally transparent manner.
ms.assetid: a61ab1e6-dad9-4dc0-a908-f8440619f610
title: Device-Redirecting Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device-Redirecting Functions

The device-redirecting functions redirect standard MS-DOS devices, drive letters and LPT ports. This enables applications running on the system to use the devices and access the network in a totally transparent manner.



| Function                                                         | Description                                                                                                                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NPAddConnection**](/windows/win32/Npapi/nf-npapi-npaddconnection?branch=master)                       | Redirects or connects a local device to a network resource.<br/>                                                                                                                              |
| [**NPAddConnection3**](/windows/win32/Npapi/nf-npapi-npaddconnection3?branch=master)                     | Performs the same action as [**NPAddConnection**](/windows/win32/Npapi/nf-npapi-npaddconnection?branch=master), but lets the user specify which window should own any dialog boxes and how the connection should be established.<br/> |
| [**NPCancelConnection**](/windows/win32/Npapi/nf-npapi-npcancelconnection?branch=master)                 | Breaks a network connection. The changes are remembered if a device is disconnected unless the connection is a deviceless connection.<br/>                                                    |
| [**NPGetConnection**](/windows/win32/Npapi/nf-npapi-npgetconnection?branch=master)                       | Returns information about a connection.<br/>                                                                                                                                                  |
| [**NPGetConnection3**](/windows/win32/Npapi/nf-npapi-npgetconnection3?branch=master)                     | Returns information about a connection, even if the connection is currently disconnected.<br/>                                                                                                |
| [**NPGetConnectionPerformance**](/windows/win32/Npapi/nf-npapi-npgetconnectionperformance?branch=master) | Returns performance information about a connection.<br/>                                                                                                                                      |
| [**NPGetUniversalName**](/windows/win32/Npapi/nf-npapi-npgetuniversalname?branch=master)                 | Returns the remote or local universal name, in the format specified during the function call.<br/>                                                                                            |



 

 

 




