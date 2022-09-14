---
title: Enhanced storage is now optional for WINPE and server SKU
description: Enhanced storage is now optional for WINPE and server SKU
ms.assetid: 8A6B6194-5867-4B76-BD7B-152FD8A7DD77
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced storage is now optional for WINPE and server SKU

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

Enhanced storage was always available in Windows 7 USB devices. With the release of Windows 8, it is available for all storage devices. In client-based devices, it is enabled by default; in server devices it is optional and must be provisioned through Windows Preinstallation Environment (WinPE).

## Manifestation

The server device will fail if enhanced storage is not enabled.

Boot devices must be provisioned through WinPE with this enabled.

## Solution

Because enhanced storage is optional for runtime server, developers must add it to WinPE for provisioning and activation of those drives. See the deployment guide for details.

Server administrators must then explicitly configure their server to use enhanced storage.

 

 




