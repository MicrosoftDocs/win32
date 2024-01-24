---
description: There are some considerations that are unique to remotely administered systems.
ms.assetid: bfdf121e-9b4e-4323-82ec-9bd32531caad
title: WFP Remote Administration Considerations
ms.topic: article
ms.date: 05/31/2018
---

# WFP Remote Administration Considerations

There are some considerations that are unique to remotely administered systems. First, when software installation is remotely deployed (using SMS or MSI), WFP error dialog boxes are displayed on the screen of a locally logged on administrator (if present), not to the installation service. Second, if an administrator logs into a terminal server remotely and installs an application that replaces protected system files, the WFP error dialog boxes are displayed only in the main console, not the administrator's remote window.

For these reasons, WFP suppresses its error dialog boxes until an administrator logs on locally. Remote administrators can find file replacement errors in the system event log.

**Windows Vista and Windows Server 2008:** WFP remote administration is not supported.

 

 



