---
Description: In the original Berkeley Software Distribution (BSD) socket interface the select function was the standard (and only) means to obtain network event indications.
ms.assetid: f7f42b03-1f89-4801-abf0-396ff8b61cae
title: Selects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Selects

In the original Berkeley Software Distribution (BSD) socket interface the [**select**](/windows/win32/Winsock2/nf-winsock2-select?branch=master) function was the standard (and only) means to obtain network event indications. For each socket, information on read, write, or error status can be polled or waited on. See [**WSPSelect**](/windows/win32/Ws2spi/?branch=master) for more information. Note that network event FD\_QOS cannot be obtained by this approach.

 

 



