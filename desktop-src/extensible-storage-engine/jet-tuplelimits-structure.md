---
description: "Learn more about: JET_TUPLELIMITS Structure"
title: JET_TUPLELIMITS Structure
TOCTitle: JET_TUPLELIMITS Structure
ms:assetid: 2610e2e5-5883-4aec-bc66-e6160b76c264
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269207(v=EXCHG.10)
ms:contentKeyID: 32765510
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_TUPLELIMITS Structure


_**Applies to:** Windows | Windows Server_

## JET_TUPLELIMITS Structure

The **JET_TUPLELIMITS** structure allows customization of the tuple index characteristics on a per-index basis, rather than a per-instance basis, using [JetSetSystemParameter](./jetsetsystemparameter-function.md).

**Windows Server 2003:** The **JET_TUPLELIMITS** structure is introduced in Windows Server 2003.

```cpp
    typedef struct tagJET_TUPLELIMITS {
      unsigned long chLengthMin;
      unsigned long chLengthMax;
      unsigned long chToIndexMax;
      unsigned long cchIncrement;
      unsigned long ichStart;
    } JET_TUPLELIMITS;
```

### Members

**chLengthMin**

The minimum length of a tuple. The default value is 3.

**chLengthMax**

The maximum length of a tuple. The default value is 10.

**chToIndexMax**

The maximum length of a string to index. For example, if a column is 100 characters long, and **chToIndexMax** is set to 60, then only the first 60 characters of the column will be indexed. The default value is 32767.

**cchIncrement**

This allows the stride to be configured on a per index basis.

**Windows Vista:** The **cchIncrement** member is introduced in Windows Vista. Prior to Windows Vista, the amount to shift the window (the "stride") was always 1, as is shown in the example in the remarks section.

**ichStart**

The offset into the value to begin taking retrieving tuples from the value.

**Windows Vista:** The **ichStart** member is introduced in Windows Vista.

### Remarks

A tuple index walks a string and indexes all of its possible substrings of **chLengthMax**. At the end of the string (or at position **chToIndexMax**, whichever occurs first), the substrings of at least **chLengthMin** will be indexed.

A tuple index can be used for searching strings with both leading and trailing wildcards.

Assuming a row with a text field of "RAIN IN SPAIN\!", if a tuple index gets created with parameters **chLengthMin**=2, and **chLengthMax**=3, the following entries are created in the index:

"RAI"  
"AIN"  
"IN "  
"N I"  
" IN"  
"IN "  
"N S"  
" SP"  
"SPA"  
"PAI"  
"AIN"  
"IN\!"  
"N\!"

Note that "IN " occurs twice, and that the last entry ("N\!") is shorter than 3 (**chLengthMax**). Also note that the splitting algorithm is not aware of spaces or words, and treats all characters identically.

**Windows XP:** Windows XP supports tuple indexes, but does not have **JET_TUPLELIMITS**. The database engine will used the default values (**chLengthMin**=3, **chLengthMax**=10, **chToIndexMax**=32767). It is still possible to change these values, but they are set on a per-instance basis using [JetSetSystemParameter](./jetsetsystemparameter-function.md) with [JET_paramIndexTuplesLengthMin](./index-parameters.md), [JET_paramIndexTuplesLengthMax](./index-parameters.md), and [JET_paramIndexTuplesToIndexMax](./index-parameters.md).

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_INDEXCREATE](./jet-indexcreate-structure.md)  
[JET_TUPLELIMITS]()  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
