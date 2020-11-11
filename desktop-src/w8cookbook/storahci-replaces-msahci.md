---
title: StorAHCI replaces MSAHCI
description: StorAHCI replaces MSAHCI
ms.assetid: 9C6FAFA7-A6B3-4D3A-94EE-B53626DBF183
ms.topic: article
ms.date: 05/31/2018
---

# StorAHCI replaces MSAHCI

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

StorAHCI, a Storport miniport, supports serial advanced technology attachment (SATA) advanced host controller interface (AHCI) controllers in Windows, and replaces MSAHCI, an ATAport miniport.

## Manifestation

There should be no change in functionality or performance; this driver supports all the same devices that MSAHCI supports.

This change is transparent to the user.

## Mitigation

Update any utilities and scripts that rely on ATAport bindings. Do not rely on the drive name. Instead use standard disk detection.

 

 




