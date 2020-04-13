---
Description: The following topic describes how the Windows as a Service (WaaS) Assessment Platform API works.
ms.assetid: B107AAF3-4248-40EF-ABD2-C5B31602AEF7
title: About the WaaS Assessment Platform
ms.topic: article
ms.date: 05/31/2018
---

# About the WaaS Assessment Platform

The following topic describes how the Windows as a Service (WaaS) Assessment Platform API works.

The WaaS Assessment API offers the caller the following information:

-   If a device is on the latest Microsoft updates.
-   Whether the device has reached end of support.
-   The release times for the latest applicable updates for the device.
-   An assessment of why a device is not up-to-date and the potential impact it may have on the device.

The WaaS Assessment Platform uses the COM API model and runs automatically at least once a day. This cycle catches applicable release information. During the cached period, assessments are made against the cached release information. If a call is made outside of the cache expiration window, a fresh call and assessment is made, cached, and returned. When a call is made, the WaaS Assessment Client contacts the WaaS Assessment Service with the device's attributes, and receives back a dossier of information applicable to the device. The client then uses this information against the information it gathers about the device to perform the assessment.

For the use case of this API, one needs to have the admin right to run or use the elevated visual studio for development. 

 



