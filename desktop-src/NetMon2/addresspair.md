---
description: The ADDRESSPAIR structure constructs a capture filter.
ms.assetid: 0dd2bcaa-5e0f-448f-969e-14b923a01a2f
title: ADDRESSPAIR structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ADDRESSPAIR
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# ADDRESSPAIR structure

The **ADDRESSPAIR** structure constructs a capture filter.

## Syntax


```C++
typedef struct _ADDRESSPAIR {
  WORD    AddressFlags;
  WORD    NalReserved;
  ADDRESS DstAddress;
  ADDRESS SrcAddress;
} ADDRESSPAIR, *LPADDRESSPAIR;
```



## Members

<dl> <dt>

**AddressFlags**
</dt> <dd>

Flags that describe the addresses used by a capture filter. See Remarks for more information.



| Value                                                                                                                                                                                                         | Meaning                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <span id="ADDRESS_FLAGS_MATCH_DST"></span><span id="address_flags_match_dst"></span><dl> <dt>**ADDRESS\_FLAGS\_MATCH\_DST**</dt> </dl>                 | Matches the destination address.<br/>                              |
| <span id="ADDRESS_FLAGS_MATCH_SRC"></span><span id="address_flags_match_src"></span><dl> <dt>**ADDRESS\_FLAGS\_MATCH\_SRC**</dt> </dl>                 | Matches the source address.<br/>                                   |
| <span id="ADDRESS_FLAGS_EXCLUDED"></span><span id="address_flags_excluded"></span><dl> <dt>**ADDRESS\_FLAGS\_EXCLUDED**</dt> </dl>                     | Excludes the frame if this address is found.<br/>                  |
| <span id="ADDRESS_FLAGS_DST_GROUP_ADDR"></span><span id="address_flags_dst_group_addr"></span><dl> <dt>**ADDRESS\_FLAGS\_DST\_GROUP\_ADDR**</dt> </dl> | Matches group bit only. Use this for broadcast-type messages.<br/> |
| <span id="ADDRESS_FLAGS_MATCH_BOTH"></span><span id="address_flags_match_both"></span><dl> <dt>**ADDRESS\_FLAGS\_MATCH\_BOTH**</dt> </dl>              | Matches destination and source addresses.<br/>                     |



 

</dd> <dt>

**NalReserved**
</dt> <dd>

This is reserved.

</dd> <dt>

**DstAddress**
</dt> <dd>

Destination address of the address pair element.

</dd> <dt>

**SrcAddress**
</dt> <dd>

Source address of the address pair element.

</dd> </dl>

## Remarks

The flags of the **AddressFlags** member can be combined. For example the following setting excludes the frame if the specified source address is detected.

``` syntax
ADDRESS_FLAGS_MATCH_SOURCE|ADDRESS_FLAGS_EXCLUDED
```

For more information about implementing this structure, see [Capture Filters](capture-filters.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[CAPTUREFILTER](capturefilter.md)
</dt> </dl>

 

 




