---
title: Previous versions UI removed for local volumes
description: Previous versions UI removed for local volumes
ms.assetid: 0BD3D046-EB06-4C9A-952C-306AC99396C6
ms.topic: article
ms.date: 05/31/2018
---

# Previous versions UI removed for local volumes

## Platform

**Clients** – Windows 8 


## Description

Earlier versions of Windows allowed users to restore previous versions of individual files from “shadow copies” of local volumes. These shadow copies are created by the “Previous Versions” feature through Volume Shadow Copy service (VSS). In Windows 7, users could configure and schedule shadow copies in System Protection UI available through System Properties.

However, Previous Versions were rarely used and negatively impacted the overall Windows performance; as a result the feature was removed. In Windows 8, these features are no longer available:

-   The ability to browse, search or restore previous versions of files through Previous Versions UI
-   The ability to configure or schedule previous versions of files through System Protection UI

However, users can still use the Previous Versions tab when accessing file shares on a Windows server.

## Manifestation

The Previous Versions option is no longer available for local volumes in the Windows Explorer Properties menu.

## Solution

Developers who need to create shadow copies of local volumes can still do so by calling VSS APIs in custom code.

 

 




