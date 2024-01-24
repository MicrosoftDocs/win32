---
description: LOCALE\_SGROUPING
ms.assetid: 3f07ecae-38f4-477b-8b23-a9cd87613c24
title: LOCALE_SGROUPING
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SGROUPING

Sizes for each group of digits to the left of the decimal. The maximum number of characters allowed for this string is ten, including a terminating null character. An explicit size is needed for each group, and sizes are separated by semicolons. If the last value is 0, the preceding value is repeated. For example, to group thousands, specify 3;0. Indic locales group the first thousand and then group by hundreds. For example, 12,34,56,789 is represented by 3;2;0.

Further examples:



| Specification | Resulting string   |
|---------------|--------------------|
| 3;0           | 3,000,000,000,000  |
| 3;2;0         | 30,00,00,00,00,000 |
| 3             | 3000000000,000     |
| 3;2           | 30000000,00,000    |



 

 

 



