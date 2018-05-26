---
Description: LOCALE\_S1159 and LOCALE\_SAM
ms.assetid: dc7058af-1d5f-40a0-8d0b-17d2ff5662ce
title: LOCALE\_S1159 and LOCALE\_SAM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LOCALE\_S1159 and LOCALE\_SAM

String for the AM designator (first 12 hours of the day). The maximum number of characters allowed for this string, including a terminating null character, is different for different releases of Windows.

**Windows XP:** Thirteen including a terminating null character for [**SetLocaleInfo**](/windows/win32/Winnls/nf-winnls-setlocaleinfoa?branch=master). Fifteen including a terminating null character for [**GetLocaleInfo**](/windows/win32/Winnls/nf-winnls-getlocaleinfoa?branch=master).

**Windows Me/98/95, Windows NT 4.0, Windows 2000:** Nine including a terminating null character.

**Windows Server 2003 and later:** Fifteen including a terminating null character.

Windows 10 added the value **LOCALE\_SAM** as a more readable synonym for **LOCALE\_S1159**.

 

 



