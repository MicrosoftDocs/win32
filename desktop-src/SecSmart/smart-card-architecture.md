---
title: Smart Card Architecture
description: Architecture of Microsoft smart card support.
ms.assetid: bde43785-d0a9-4fb7-9eaa-a952abfa8662
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card Architecture

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The following illustration shows the architecture of Microsoft smart card support.

Cryptographic applications communicate through the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) to individual smart card modules. Smart card modules communicate through the [Smart Card Resource Manager](https://msdn.microsoft.com/library/windows/desktop/aa380148) to smart cards. For information about smart card modules, see [Smart Card Modules](smart-card-modules.md).

![architecture of microsoft smart card support](images/smartcardarchitecture.png)

 

 




