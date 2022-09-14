---
description: Your Unicode applications should always cast zero to TCHAR when using null-terminated strings.
ms.assetid: 43bbf0ab-9b69-4f7d-acda-d0f8b6caf4b5
title: Using Null-terminated Strings
ms.topic: article
ms.date: 05/31/2018
---

# Using Null-terminated Strings

Your Unicode applications should always cast zero to TCHAR when using null-terminated strings. The code 0x0000 is the Unicode string terminator for a null-terminated string. A single null byte is not sufficient for this code, because many Unicode characters contain null bytes as either the high or the low byte. An example is the letter A, for which the character code is 0x0041.

## Related topics

<dl> <dt>

[Using Special Characters in Unicode](using-special-characters-in-unicode.md)
</dt> </dl>

 

 



