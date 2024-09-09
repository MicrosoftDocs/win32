---
title: Finding a Specific Driver
description: Finding a Specific Driver
ms.assetid: d48dc313-4606-4f70-b2fe-ed99160e53fc
keywords:
- audio compression manager (ACM),finding drivers
- ACM (audio compression manager),finding drivers
- ACM examples,finding drivers
- finding drivers
- acmDriverEnum function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Finding a Specific Driver

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

You might want your application to send a message directly to a specific driver or to identify certain drivers from the list. For example, you might want your application to identify those drivers that support filters and then query each driver to determine which filter tags it supports. You can use the [**acmDriverEnum**](/windows/desktop/api/Msacm/nf-msacm-acmdriverenum) function to obtain a handle to the desired driver or drivers; this handle can then be used to communicate with that driver.

Note that when an application installs a local driver for its own use, the [**acmDriverAdd**](/windows/desktop/api/Msacm/nf-msacm-acmdriveradd) function returns a driver handle, which can be used to communicate with the driver. It is not necessary to use **acmDriverEnum** in this case.

 

 




