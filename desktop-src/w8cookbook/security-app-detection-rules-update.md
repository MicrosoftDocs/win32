---
title: Security app detection rules update
description: Security app detection rules update
ms.assetid: A272C09B-A777-4119-BAB9-F91ABC03717A
ms.topic: article
ms.date: 05/31/2018
---

# Security app detection rules update

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


### Description

The Windows Store apps being added in Windows 8 are all being installed to a common location under “Program Files” (%programfiles%) called \\program files\\WindowsApps.

### Manifestation

This can cause collisions with existing configurations, and some antivirus/anti-malware detectors see this location as a potential location that is a cause for concern.

### Mitigation

The current recommendations are:

-   Move away from \\program files\\WindowsApps for storing any custom apps
-   Antivirus/antimalware vendors should update their heuristics so they do not identify that location as a malware location

 

 




