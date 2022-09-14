---
title: ISAN
description: The ISAN attribute contains the International Standard Audiovisual Number (ISAN) that identifies the content.
ms.assetid: 2937d422-f062-4373-845e-dd200512ed0b
keywords:
- ISAN windows Media Format
topic_type:
- apiref
api_name:
- ISAN
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ISAN

The **ISAN** attribute contains the International Standard Audiovisual Number (ISAN) that identifies the content.

## Global Constant

g\_wszISAN

## Data Type

**WMT\_TYPE\_STRING**

## Remarks

ISAN is an international standard for identifying audiovisual works. For information about ISAN, visit the standard's [Web site](https://www.isan.org/).

The metadata editor object verifies the ISAN string when you set this attribute. The acceptable string formatting, as described in section 4.1 of the ISAN specification, consists of 16 hexadecimal digits, optionally separated by whitespace or hyphens into 4-digit segments. The formatted number must be followed, also optionally separated by a space or hyphen, by a valid check character. The check character can be a decimal digit or a capital letter. Refer to annex A of the ISAN user guide for information about how to derive the check number.

The standard ISAN string may be followed by version information. If present, version information consists of eight hexadecimal digits followed by a check number. The formatting of these characters follows the same rules as the basic string.

## Examples

The following are three acceptably formatted strings for an example ISAN.


```
00003BAB93520000G
0000 3BAB 9352 0000 G
0000-3BAB-9352-0000-G
```



The following string shows the format of an ISAN with version information.


```C++
0000-3BAB-9352-0000-G-0000-0000-Q
```



## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




