---
Description: LOCALE\_SSHORTDATE
ms.assetid: 55333a53-1205-42eb-aa1a-c248c52a8a3f
title: LOCALE\_SSHORTDATE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LOCALE\_SSHORTDATE

Short date formatting string for the locale. The maximum number of characters allowed for this string is 80, including a terminating null character. The string can consist of a combination of [day, month, year, and era format pictures](day--month--year--and-era-format-pictures.md). For example, "M/d/yyyy" indicates that September 3, 2004 is written 9/3/2004.

Locales can define multiple short date formats. To get all of the short date formats for this locale, use [EnumDateFormats](/windows/win32/Winnls/nf-winnls-enumdateformatsa?branch=master), [EnumDateFormatsEx](/windows/win32/Winnls/nf-winnls-enumdateformatsexa?branch=master), or [EnumDateFormatsExEx](/windows/win32/Winnls/nf-winnls-enumdateformatsexex?branch=master).

 

 



