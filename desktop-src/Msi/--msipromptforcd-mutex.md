---
description: The \_\_MsiPromptForCD Mutex exists when the installer prompts the user to insert a CD-ROM.
ms.assetid: f6319cda-48ac-4351-8eb5-f326490e3aff
title: '__MsiPromptForCD Mutex'
ms.topic: article
ms.date: 05/31/2018
---

# \_\_MsiPromptForCD Mutex

The \_\_MsiPromptForCD Mutex exists when the installer prompts the user to insert a CD-ROM. Autoplay programs should check that the \_\_MsiPromptForCD mutex is not currently set before starting. Note that it is possible for a CD-ROM prompt to occur before either the InProgress key or the \_MSIExecute Mutex exist.

 

 



