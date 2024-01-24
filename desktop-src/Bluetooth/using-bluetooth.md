---
title: Using Bluetooth
description: This section describes tasks that are related to writing Windows-based applications for Bluetooth.
ms.assetid: a5eddf48-b548-44a8-ac09-ce16f8aa3943
ms.topic: article
ms.date: 05/31/2018
---

# Using Bluetooth

This section describes tasks that are related to writing Windows-based applications for Bluetooth.

Bluetooth provides programming definitions in the Ws2bth.h and BluetoothAPIs.h files. The Bthsdpdef.h file must be included before BluetoothAPIs.h. The Ws2bth.h file must be included after Winsock2.h to use Bluetooth sockets. Link only to Bthprops.lib, and avoid linking to Irprops.lib. Irprops.lib is provided for backward compatibility only. Bthprops.lib is available in the Windows Vista SDK. You can use the Windows Vista SDK to develop applications for Windows XP with Service Pack 2 (SP2).

All standard synchronous and overlapped mechanisms to read and write data that are currently supported with other address families operate properly with the AF\_BTH address family as well.

There is some example code included with the SDK that shows a simple Bluetooth application using Winsock 2.2 and RFCOMM protocol. The source code for the sample can be found in the SDK installation location under C:\\Program Files\\Microsoft SDKs\\Windows\\\<version number\>\\Samples\\NetDs\\winsock\\Bluetooth.

This section describes the following topics.



| Section                                                                                      | Content                                                                          |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [Bluetooth Programming with Windows Sockets](bluetooth-programming-with-windows-sockets.md) | Explains how to use Windows Sockets interfaces to implement a Bluetooth network. |



 

 

 




