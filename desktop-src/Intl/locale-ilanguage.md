---
Description: LOCALE\_ILANGUAGE
ms.assetid: 8f80a941-8ba6-4a0d-92fa-77230fe0a9d1
title: LOCALE\_ILANGUAGE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LOCALE\_ILANGUAGE

[Language identifier](language-identifiers.md) with a hexadecimal value. For example, English (United States) has the value 0409, which indicates 0x0409 hexadecimal, and is equivalent to 1033 decimal. The maximum number of characters allowed for this string is five, including a terminating null character.

**Windows Vista and later:** Use of this constant can cause [**GetLocaleInfo**](/windows/win32/Winnls/nf-winnls-getlocaleinfoa?branch=master) to return an invalid locale identifier. Your application should use the [LOCALE\_SNAME](locale-sname.md) constant when calling this function.

 

 



