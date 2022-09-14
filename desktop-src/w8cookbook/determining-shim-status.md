---
title: Determining shim status
description: Determining shim status
ms.assetid: 8D0B633F-9117-4F90-BF8C-AC5F57FCD30B
ms.topic: article
ms.date: 05/31/2018
---

# Determining shim status

## Platforms

<dl> Clients - Windows 8  
Servers - Windows Server 2012  
</dl>

## Description

Windows 8 logs events when apps are being shimmed for various reasons. The easiest way to determine if your app is being shimmed is to check the event viewer. Go to Applications and Services Logs\\Microsoft Windows Application-Experience Program\\Telemetry.

## Mitigation

The best way to get yourself out of shimming is to rename the executable or to increase the major version by 1 (recompile the executable).

 

 




