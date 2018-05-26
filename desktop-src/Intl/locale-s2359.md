---
Description: LOCALE\_S2359 and LOCALE\_SPM
ms.assetid: 8a97073e-84f6-47d9-98fb-65760e8a6cd8
title: LOCALE\_S2359 and LOCALE\_SPM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LOCALE\_S2359 and LOCALE\_SPM

String for the PM designator (second 12 hours of the day). The maximum number of characters allowed for this string is different for different releases of Windows.

**Windows XP:** Thirteen including a terminating null character for [**SetLocaleInfo**](/windows/win32/Winnls/nf-winnls-setlocaleinfoa?branch=master). Fifteen including a terminating null character for [**GetLocaleInfo**](/windows/win32/Winnls/nf-winnls-getlocaleinfoa?branch=master).

**Windows Me/98/95, Windows NT 4.0, Windows 2000:** Nine including a terminating null character.

**Windows Server 2003 and later:** Fifteen including a terminating null character.

Windows 10 added the value **LOCALE\_SPM** as a more readable synonym for **LOCALE\_S2359**.

 

 



