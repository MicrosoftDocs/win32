---
description: The ADDRESSTABLE structure contains a table of address pairs.
ms.assetid: 84577b6c-9d43-4e53-9f8d-33685329b11d
title: ADDRESSTABLE structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ADDRESSTABLE
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# ADDRESSTABLE structure

The **ADDRESSTABLE** structure contains a table of address pairs.

## Syntax


```C++
typedef struct _ADDRESSTABLE {
  DWORD       nAddressPairs;
  DWORD       nNonMacAddressPairs;
  ADDRESSPAIR AddressPair[MAX_ADDRESS_PAIRS];
} ADDRESSTABLE, *LPADDRESSTABLE;
```



## Members

<dl> <dt>

**nAddressPairs**
</dt> <dd>

Number of address pairs in the **AddressPair** array.

</dd> <dt>

**nNonMacAddressPairs**
</dt> <dd>

Number of non-MAC address pairs.

</dd> <dt>

**AddressPair**
</dt> <dd>

Array of address pairs. Note that you may only store up to eight address pairs per ADDRESSTABLE structure.

</dd> </dl>

## Remarks

Use this structure as part of the capture filter construction process. For more information about implementing this structure, see [Capture Filters](capture-filters.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[ADDRESSPAIR](addresspair.md)
</dt> <dt>

[CAPTUREFILTER](capturefilter.md)
</dt> </dl>

 

 




