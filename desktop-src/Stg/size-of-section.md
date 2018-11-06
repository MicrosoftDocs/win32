---
title: Size of Section
description: The section size data type indicates the size, in bytes, of the section.
ms.assetid: 6438fbce-42b9-4b16-a6b0-80c80246e546
ms.topic: article
ms.date: 05/31/2018
---

# Size of Section

The section size data type indicates the size, in bytes, of the section. Because the section size is the first 4 bytes, sections can be copied as an array of bytes. The section size should always be a multiple of four.

For example, an empty section, that is, one with zero properties in it, would have a byte count of eight (the **DWORD** byte count and the **DWORD** count of properties). The section itself would contain the 8 bytes: **08 00 00 00 00 00 00 00**.

 

 




