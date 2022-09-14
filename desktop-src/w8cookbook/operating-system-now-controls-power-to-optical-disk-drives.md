---
title: Operating system now controls power to optical disk drives
description: Operating system now controls power to optical disk drives
ms.assetid: FDAE818F-742E-4E8C-9426-2AA86B42B0D9
ms.topic: article
ms.date: 05/31/2018
---

# Operating system now controls power to optical disk drives

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

In previous versions of Windows, power to the optical drive was not managed when the optical drive was not in use. Now, if there is no media present in the optical disk drive (ODD), the operating system turns off the power to the optical drive. This feature is called zero power ODD (ZPODD). The feature is applicable only to optical drives that use a Slimline SATA (Serial Advanced Technology Attachment) connector.

## Manifestation

We have not found any negative impacts from this new behavior; however, you should be aware of it as it may result in unexpected behavior of media-writing software.

## Mitigation

To revert to always-on status, turn off this functionality in the Registry. The absolute path to the registry value is:

`HKLM\SYSTEM\CurrentControlSet\Services\cdrom\Parameters\ZeroPowerODDEnabled`

Its type is DWORD (32 bit), and if its value is 0, then ZPODD is disabled; if it’s any other value, then ZPODD is enabled.

## Tests

Test your media-writing software for any anomalies that occur due to this new feature. Please [inform Microsoft](mailto:OptIssue@microsoft.com) of any issues you find with this new feature.

 

 




