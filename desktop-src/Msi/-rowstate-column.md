---
description: The reserved column name \_RowState represents the non-persistent state associated with each table row in an installer database table.
ms.assetid: ff570b47-7c16-47ae-b1c2-2ecad9266372
title: '_RowState Column'
ms.topic: article
ms.date: 05/31/2018
---

# \_RowState Column

The reserved column name \_RowState represents the non-persistent state associated with each table row in an installer database table. The pseudo-column is of type [Integer](integer.md), and the value consists of a set of bit flags. All the bits are readable, but only the UserInfo and Temporary bits can be set. This data is available only as long as the tables are locked or in use (that is, while a view containing the tables exists). The following table shows the attributes a row can have.



| Name           | Value | Meaning                                                        |
|----------------|-------|----------------------------------------------------------------|
| iraUserInfo    | 0x01  | The attribute is for external use. This value can be updated.  |
| iraTemporary   | 0x02  | The row is not persistent. This value can be updated.          |
| iraModified    | 0x04  | A row has been updated.                                        |
| iraInserted    | 0x08  | A row has been inserted.                                       |
| iraMergeFailed | 0x0F  | An attempt was made to merge with non-identical, non-key data. |



 

Bits 6 through 8 are reserved.

 

 



