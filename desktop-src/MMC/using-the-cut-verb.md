---
title: Using the Cut Verb
description: In MMC 2.0, the Cut verb is treated like any other verb.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bee1f41d-38ad-47f6-8f30-1f2a49bb17ca
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using the Cut Verb

In MMC 2.0, the Cut verb is treated like any other verb. In MMC 1.2, the Cut verb's status was dependent on the state of the Copy and Delete verbs (for example, you cannot enable the Cut verb if the Copy and Delete verbs are disabled). In MMC 2.0, there is no dependence of the Cut, Copy, and Delete verbs on each other's enabled state.

In MMC 1.2, if a snap-in enables Cut and disables Copy, then both Cut and Copy are disabled. The same snap-in in MMC 2.0 will have Cut enabled and Copy disabled. In MMC 1.2, note that a snap-in should not directly enable Cut; instead, the snap-in should rely on the state of Copy and Delete to determine the Cut state.

 

 




