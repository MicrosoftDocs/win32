---
title: Ensuring Compatibility Between MMC Versions
description: Provides guidelines to ensure compatibility between MMC versions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7b3b81f8-4bbd-47ba-bde3-b7bb56e79ff0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ensuring compatibility between MMC versions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ensuring Compatibility Between MMC Versions

It is important to understand that MMC's contract to compatibility from release to release is its COM interfaces. As long as a snap-in uses the MMC interfaces as documented in the MMC SDK documentation, it will remain compatible from one version to the next. A snap-in *must not* make assumptions about the internal implementation details of MMC, because these are subject to change. A snap-in that makes such assumptions for a particular version of MMC is likely to break in subsequent versions of MMC.

 

 




