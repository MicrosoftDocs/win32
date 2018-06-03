---
title: QOS-enabling Your Application
description: Quality of Service is enabled through the use of specific Windows Sockets APIs, as well as APIs and structures created specifically for use with Quality of Service.
ms.assetid: 7eed40ff-c789-41c8-89e8-ccc5c823dd36
keywords:
- Quality of Service QOS ,tasks, enabling an application
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QOS-enabling Your Application

Quality of Service is enabled through the use of specific Windows Sockets APIs, as well as APIs and structures created specifically for use with Quality of Service. Applications taking advantage of Quality of Service use Windows Sockets 2 APIs, in conjunction with QOS APIs and structures, to create a connection and provide QOS parameters that articulate the application's QOS requirements. QOS APIs and structures are also used to maintain (or change) settings associated with a particular QOS session.

The call sequence involved in establishing and maintaining a QOS-enabled connection generally includes preparation calls, such as enumerating protocols, and then querying available protocols for QOS capability. The process of enumerating and querying protocols for QOS capability is outlined in [Opening a QOS-Enabled Socket](opening-a-qos-enabled-socket.md).

 

 




