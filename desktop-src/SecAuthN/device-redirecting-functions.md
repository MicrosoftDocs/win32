---
Description: 'The device-redirecting functions redirect standard MS-DOS devices, drive letters and LPT ports. This enables applications running on the system to use the devices and access the network in a totally transparent manner.'
ms.assetid: 'a61ab1e6-dad9-4dc0-a908-f8440619f610'
title: 'Device-Redirecting Functions'
---

# Device-Redirecting Functions

The device-redirecting functions redirect standard MS-DOS devices, drive letters and LPT ports. This enables applications running on the system to use the devices and access the network in a totally transparent manner.



| Function                                                         | Description                                                                                                                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NPAddConnection**](npaddconnection.md)                       | Redirects or connects a local device to a network resource.<br/>                                                                                                                              |
| [**NPAddConnection3**](npaddconnection3.md)                     | Performs the same action as [**NPAddConnection**](npaddconnection.md), but lets the user specify which window should own any dialog boxes and how the connection should be established.<br/> |
| [**NPCancelConnection**](npcancelconnection.md)                 | Breaks a network connection. The changes are remembered if a device is disconnected unless the connection is a deviceless connection.<br/>                                                    |
| [**NPGetConnection**](npgetconnection.md)                       | Returns information about a connection.<br/>                                                                                                                                                  |
| [**NPGetConnection3**](npgetconnection3.md)                     | Returns information about a connection, even if the connection is currently disconnected.<br/>                                                                                                |
| [**NPGetConnectionPerformance**](npgetconnectionperformance.md) | Returns performance information about a connection.<br/>                                                                                                                                      |
| [**NPGetUniversalName**](npgetuniversalname.md)                 | Returns the remote or local universal name, in the format specified during the function call.<br/>                                                                                            |



 

 

 




