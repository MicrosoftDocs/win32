---
title: BITS Startup Type
description: The Startup Type for BITS is delayed auto-start. Prior to Windows Vista   The Startup Type for BITS is Manual. When a BITS job is created, the Startup Type changes to Automatic. The Startup Type returns to Manual when all jobs are complete or canceled.
ms.assetid: 0d9ec60f-3488-4eb2-a6a2-22932fd74caf
ms.topic: article
ms.date: 05/31/2018
---

# BITS Startup Type

The **Startup Type** for BITS is delayed auto-start (if there are active BITS jobs) or demand start (if there are no active jobs). Versions of Windows prior to the November Update used only the delayed auto-start startup type; versions prior to Vista used the manual startup type.

You should not set the **Startup Type** to Disabled. Disabling BITS may break applications that rely on BITS to transfer files.

 

 




