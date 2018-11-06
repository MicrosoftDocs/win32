---
title: RAS AutoDial
description: A feature called \ 0034;default connection \ 0034; was added to the system in Windows XP.
ms.assetid: 8ef832ed-97e4-4941-adb2-b35ce3a75fd1
keywords:
- AutoDial, RAS
ms.topic: article
ms.date: 05/31/2018
---

# RAS AutoDial

A feature called "default connection" was added to the system in Windows XP. If there is a failed connection attempt, the system checks for an explicit match (for Winsock name or share name) in the database if not, it dials the default connection if there is one.

**Windows 2000:** When an attempt to connect to a network address fails because the host cannot be reached, the AutoDial feature can automatically start a dial-up connection operation. To do this, AutoDial searches its database of network addresses to find a phone-book entry that it can use to establish the connection.

**Windows NT 4.0:  ** RAS keeps a database of the Winsock names and/or share names that you have successfully reached while a RAS/VPN connection was active. Later, when a winsock or share connection attempt fails, the system checks this database and offers to dial the stored connection for you.

 

 




