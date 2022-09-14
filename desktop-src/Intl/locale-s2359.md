---
description: LOCALE\_S2359 and LOCALE\_SPM
ms.assetid: 8a97073e-84f6-47d9-98fb-65760e8a6cd8
title: LOCALE_S2359 and LOCALE_SPM
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_S2359 and LOCALE\_SPM

String for the PM designator (second 12 hours of the day). The maximum number of characters allowed for this string is different for different releases of Windows.

**Windows XP:** Thirteen including a terminating null character for [**SetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-setlocaleinfoa). Fifteen including a terminating null character for [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa).

**Windows Me/98/95, Windows NT 4.0, Windows 2000:** Nine including a terminating null character.

**Windows Server 2003 and later:** Fifteen including a terminating null character.

Windows 10 added the value **LOCALE\_SPM** as a more readable synonym for **LOCALE\_S2359**.

 

 



