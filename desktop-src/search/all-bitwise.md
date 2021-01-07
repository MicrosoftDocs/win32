---
description: The ALL BITWISE and SOME BITWISE keywords are used for testing the bits in an integral type.
ms.assetid: 649f763f-45aa-4086-9e7f-b8934b5bd22c
title: ALL BITWISE and SOME BITWISE
ms.topic: article
ms.date: 05/31/2018
---

# ALL BITWISE and SOME BITWISE

The **ALL BITWISE** and **SOME BITWISE** keywords are used for testing the bits in an integral type. If all of the set bits in a property match the mask, **ALL BITWISE** is true. If at least one of the set bits in a property matches the mask, **SOME BITWISE** is true.

Operators can be applied to both scalar (single-value) properties and vector (multiple-value) properties. The following code example shows how to test property values with **ALL BITWISE** and **SOME BITWISE**.


```sql
ALL array ALL BITWISE [values?]
ALL array SOME BITWISE [values?]
            
```



## Comparison Operators

The supported comparison operators for BITWISE tests are listed in the following table.



| Comparison operator | Description  |
|---------------------|--------------|
| =                   | Equal to     |
| != or <>      | Not equal to |



 

The logic of BITWISE tests is listed in the following table.



| BITWISE test and comparison operator | Logic                   |
|--------------------------------------|-------------------------|
| = ALL BITWISE                        | Property & Mask = Mask  |
| = SOME BITWISE                       | Property & Mask != 0    |
| <> ALL BITWISE                 | Property & Mask != Mask |
| <> SOME BITWISE                | Property & Mask = 0     |



 

The following truth table uses example binary and hex values to demonstate the logic of BITWISE tests.



| Property in binary (hex) | Mask in binary (hex) | Property & Mask = binary (hex) | = SOME BITWISE | = ALL BITWISE |
|--------------------------|----------------------|--------------------------------|----------------|---------------|
| 0001 (0x1)               | 0001 (0x1)           | 0001 (0x1)                     | True           | True          |
| 0001 (0x1)               | 0011 (0x3)           | 0001 (0x1)                     | True           | False         |
| 0011 (0x3)               | 0001 (0x1)           | 0001 (0x1)                     | True           | True          |
| 0010 (0x2)               | 0001 (0x1)           | 0000 (0x0)                     | False          | False         |
| 11110000 (0xF0)          | 00000011 (0x03)      | 00000000 (0x00)                | False          | False         |
| 11110010 (0xF2)          | 11110010 (0xF2)      | 11110010 (0xF2)                | True           | True          |
| 11110010 (0xF2)          | 00000011 (0x03)      | 00000010 (0x02)                | True           | False         |



 

## Example

The following is an example of the **ALL BITWISE** predicate.


```sql
Select system.itemnamedisplay, system.FileAttributes from SystemIndex Where System.FileAttributes <> ALL BITWISE 0x4 AND Scope = 'file:c:\bitwise'
                
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



