---
title: WM/MCDI
description: The WM/MCDI attribute contains the music CD identifier. This is a binary dump of the table of contents from the CD that is used to uniquely identify the CD.
ms.assetid: cb16c62b-b9e0-4676-b1bb-ff26a2e09cb7
keywords:
- WM/MCDI windows Media Format
topic_type:
- apiref
api_name:
- WM/MCDI
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/MCDI

The **WM/MCDI** attribute contains the music CD identifier. This is a binary dump of the table of contents from the CD that is used to uniquely identify the CD.

## Global Constant

g\_wszWMMCDI

## Data Type

**WMT\_TYPE\_BINARY**

## Remarks

This attribute is compatible with the ID3 frame, MCDI. The ID3 specification for the MCDI frame requires that only one such frame exist per file and that a valid TRCK frame exist. The metadata editor does not perform any validation for these rules. Also, the size of WM/MCDI is not limited to 804 bytes, as is the MCDI ID3 frame.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




