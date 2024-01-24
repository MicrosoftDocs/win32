---
description: LOCALE\_ITIMEMARKPOSN
ms.assetid: 4aef2631-c05b-41e8-8f4d-f40da4143ab4
title: LOCALE_ITIMEMARKPOSN
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_ITIMEMARKPOSN

Specifier indicating whether the time marker string (AM or PM) precedes or follows the time string. The registry value is iTimePrefix for compatibility with previous Asian versions of Windows. The specifier must have one of the following values. No user-specified values are allowed. It is preferred for your application to use the [LOCALE\_STIMEFORMAT](locale-stime-constants.md) constant instead of LOCALE\_ITIMEMARKPOSN.



| Value | Meaning        |
|-------|----------------|
| 0     | Use as suffix. |
| 1     | Use as prefix. |



 

 

 



