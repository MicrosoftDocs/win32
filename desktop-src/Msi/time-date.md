---
description: The Time/Date data type has the time and the date stored individually, using unsigned integers as bit fields, packed as follows.
ms.assetid: 02c6076e-7f81-489c-9997-1435dec81852
title: Time/Date
ms.topic: article
ms.date: 05/31/2018
---

# Time/Date

The Time/Date data type has the time and the date stored individually, using unsigned integers as bit fields, packed as follows.

## Time

Time is encoded in an unsigned 2-byte integer with the following bit fields.



| Contents           | Bits        | Value range |
|--------------------|-------------|-------------|
| hours              | 0 1 2 3 4   | 0–23        |
| minutes            | 5 6 7 8 9 A | 0–59        |
| 2-second intervals | B C D E F   | 0–29        |



 

## Date

Date is encoded in an unsigned 2-byte integer with the following bit fields.



| Contents | Bits          | Value range              |
|----------|---------------|--------------------------|
| year     | 0 1 2 3 4 5 6 | 0–119 (relative to 1980) |
| month    | 7 8 9 A       | 1–12                     |
| day      | B C D E F     | 1–31                     |



 

 

 



