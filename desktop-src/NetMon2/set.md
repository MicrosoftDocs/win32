---
description: The SET structure defines a set of values.
ms.assetid: '88e0ffa1-71a2-4a3f-bdf1-964de0adea62'
title: SET structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SET
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# SET structure

The **SET** structure defines a set of values.

## Syntax


```C++
typedef struct _SET {
  DWORD nEntries;
  union {
    LPBYTE               lpByteTable;
    LPWORD               lpWordTable;
    LPDWORD              lpDwordTable;
    LPLARGEINT           lpLargeIntTable;
    LPSYSTEMTIME         lpSystemTimeTable;
    LPLABELED_BYTE       lpLabeledByteTable;
    LPLABELED_WORD       lpLabeledWordTable;
    LPLABELED_DWORD      lpLabeledDwordTable;
    LPLABELED_LARGEINT   lpLabeledLargeIntTable;
    LPLABELED_SYSTEMTIME lpLabeledSystemTimeTable;
    LPLABELED_BIT        lpLabeledBit;
    LPVOID               lpVoidTable;
  };
} SET, *LPSET;
```



## Members

<dl> <dt>

**nEntries**
</dt> <dd>

Total number of entries in a set.

</dd> <dt>

**lpByteTable**
</dt> <dd>

Pointer to an array of BYTE values.

</dd> <dt>

**lpWordTable**
</dt> <dd>

Pointer to an array of WORD values.

</dd> <dt>

**lpDwordTable**
</dt> <dd>

Pointer to an array of DWORD values.

</dd> <dt>

**lpLargeIntTable**
</dt> <dd>

Pointer to an array of [LARGEINT](largeint.md) structures.

</dd> <dt>

**lpSystemTimeTable**
</dt> <dd>

Pointer to an array of SYSTEMTIME values.

</dd> <dt>

**lpLabeledByteTable**
</dt> <dd>

Pointer to an array of [LABELED\_BYTE](labeled-byte.md) structures. Each **LABELED\_BYTE** structure defines a value and label. Network Monitor displays a label if it finds a corresponding value in the protocol packet.

</dd> <dt>

**lpLabeledWordTable**
</dt> <dd>

Pointer to an array of [LABELED\_WORD](labeled-word.md) structures that define a set of WORD values and labels.

</dd> <dt>

**lpLabeledDwordTable**
</dt> <dd>

Pointer to an array of [LABELED\_DWORD](labeled-dword.md) structures that define a set of DWORD values and labels.

</dd> <dt>

**lpLabeledLargeIntTable**
</dt> <dd>

Pointer to an array of [LABELED\_LARGEINT](labeled-largeint.md) structures that define a set of LARGEINT values and labels.

</dd> <dt>

**lpLabeledSystemTimeTable**
</dt> <dd>

Pointer to an array of [LABELED\_SYSTEMTIME](labeled-systemtime.md) structures that define a set of SYSTEM values and labels.

</dd> <dt>

**lpLabeledBit**
</dt> <dd>

Pointer to an array of [LABELED\_BIT](labeled-bit.md) structures that define a set of labeled BIT pairs. Each BIT can specify two labels   one label for each state (0 or 1) of the BIT.

</dd> <dt>

**lpVoidTable**
</dt> <dd>

Pointer to an array of values.

</dd> </dl>

## Remarks

The **SET** structure is used to define a set of comparison data that Network Monitor can use to interpret the value of a property in a protocol packet. When a set of comparison data is required, a pointer to the **SET** structure is specified in the **lpSet** member of the [PROPERTYINFO](propertyinfo.md) structure.

The parser DLL can provide a value set and a label set. The member of the **UNION** that you select in a **SET** structure points to an array of structures that define each member of a set.

-   Value set

    A value set is used when you want Network Monitor to include an in-set or not-in-set indicator with the value found in the protocol packet. For example, if a DWORD set is specified, Network Monitor displays a label for each DWORD value found in the protocol packet, indicating that the DWORD is or is not specified in the set.

    A value set can be based on BYTE, WORD, DWORD, LARGEINT, and SYSTEMTIME data types.

-   Label set

    A label set is used when you want Network Monitor to display a user-defined label instead of the property values specified in a set.

    A label set can be based on BYTE, WORD, DWORD, LARGEINT, SYSTEMTIME and BIT label pairs.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[LABELED\_BIT](labeled-bit.md)
</dt> <dt>

[PROPERTYINFO](propertyinfo.md)
</dt> </dl>

 

 




