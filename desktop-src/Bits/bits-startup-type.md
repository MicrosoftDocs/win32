---
title: BITS Startup Type
description: The Startup Type for BITS is delayed auto-start. Prior to Windows Vista   The Startup Type for BITS is Manual. When a BITS job is created, the Startup Type changes to Automatic. The Startup Type returns to Manual when all jobs are complete or canceled.
ms.assetid: 0d9ec60f-3488-4eb2-a6a2-22932fd74caf
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BITS Startup Type

The **Startup Type** for BITS is delayed auto-start.

**Prior to Windows Vista:** The **Startup Type** for BITS is Manual. When a BITS job is created, the **Startup Type** changes to Automatic. The **Startup Type** returns to Manual when all jobs are complete or canceled.

You should not set the **Startup Type** to Disabled. Disabling BITS may break applications, such as Windows Update, that rely on BITS to transfer files.

 

 




