---
description: LOCALE\_SLONGDATE
ms.assetid: 1b72cd57-819e-4b1f-bbb0-b600a9e8631c
title: LOCALE_SLONGDATE
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SLONGDATE

Long date formatting string for the locale. The maximum number of characters allowed for this string is 80, including a terminating null character. The string can consist of a combination of [day, month, year, and era format pictures](day--month--year--and-era-format-pictures.md) and any string of characters enclosed in single quotes. Characters in single quotes remain as specified. For example, the Spanish (Spain) long date is "dddd, dd' de 'MMMM' de 'yyyy". Locales can define multiple long date formats.

To get all of the long date formats for a locale, use [EnumDateFormats](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsa), [EnumDateFormatsEx](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexa), or [EnumDateFormatsExEx](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexex).

 

 



