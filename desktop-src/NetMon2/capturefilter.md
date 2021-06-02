---
description: The CAPTUREFILTER structure contains capture filter data.
ms.assetid: 773187c6-31c7-4439-850d-1dd43d42f701
title: CAPTUREFILTER structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPTUREFILTER
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# CAPTUREFILTER structure

The **CAPTUREFILTER** structure contains capture filter data.

## Syntax


```C++
typedef struct _CAPTUREFILTER {
  DWORD          FilterFlags;
  LPBYTE         lpSapTable;
  LPWORD         lpEtypeTable;
  WORD           nSaps;
  WORD           nEtypes;
  LPADDRESSTABLE AddressTable;
  EXPRESSION     FilterExpression;
  TRIGGER        Trigger;
  DWORD          nFrameBytesToCopy;
  RESERVED       Reserved;
} CAPTUREFILTER, *LPCAPTUREFILTER;
```



## Members

<dl> <dt>

**FilterFlags**
</dt> <dd>

Flags that describe the contents of the capture filter.



| Value                                                                                                                                                                                                                                                                                                   | Meaning                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="CAPTUREFILTER_FLAGS_INCLUDE_ALL_SAPS"></span><span id="capturefilter_flags_include_all_saps"></span><dl> <dt>**CAPTUREFILTER\_FLAGS\_INCLUDE\_ALL\_SAPS**</dt> <dt>0x0001</dt> </dl>       | Includes all SAPs as acceptable frames.<br/>  |
| <span id="CAPTUREFILTER_FLAGS_INCLUDE_ALL_ETYPES"></span><span id="capturefilter_flags_include_all_etypes"></span><dl> <dt>**CAPTUREFILTER\_FLAGS\_INCLUDE\_ALL\_ETYPES**</dt> <dt>0x0002</dt> </dl> | Include all Etypes as acceptable frames.<br/> |
| <span id="CAPTUREFILTER_FLAGS_LOCAL_ONLY"></span><span id="capturefilter_flags_local_only"></span><dl> <dt>**CAPTUREFILTER\_FLAGS\_LOCAL\_ONLY**</dt> <dt>0x0008</dt> </dl>                          | No P-mode<br/>                                |
| <span id="CAPTUREFILTER_FLAGS_KEEP_RAW"></span><span id="capturefilter_flags_keep_raw"></span><dl> <dt>**CAPTUREFILTER\_FLAGS\_KEEP\_RAW**</dt> <dt>0x0020</dt> </dl>                                | Keep SMT and token ring MAC frames.<br/>      |



 

</dd> <dt>

**lpSapTable**
</dt> <dd>

Pointer to an array of SAP values. This member indicates the SAP values that are valid to pass to the driver. If CAPTUREFILTER\_FLAGS\_INCLUDE\_ALL\_SAPS is set, this becomes an exception list (include all SAPS except these).

</dd> <dt>

**lpEtypeTable**
</dt> <dd>

Pointer to an array of Etype values. This indicates those Etype values that are valid to pass to the driver. If CAPTUREFILTER\_FLAGS\_INCLUDE\_ALL\_ETYPES is set, this becomes an exception list (include all Etypes except these).

</dd> <dt>

**nSaps**
</dt> <dd>

Number of SAPs in the SAP table.

</dd> <dt>

**nEtypes**
</dt> <dd>

Number of Etypes in the Etype table.

</dd> <dt>

**AddressTable**
</dt> <dd>

Name of the address table.

</dd> <dt>

**FilterExpression**
</dt> <dd>

An EXPRESSION structure. This contains the pattern match portion of the capture filter.

</dd> <dt>

**Trigger**
</dt> <dd>

Reserved.

</dd> <dt>

**nFrameBytesToCopy**
</dt> <dd>

If this member is not 0, then it specifies how many bytes to keep of each frame received. If it is 0, then keep the whole frame.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

The combination of flags, values, and expressions determine which frames will be passed by the driver that uses this structure data. For more information about implementing a **CAPTUREFILTER** structure, see [Capture Filters](capture-filters.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[ADDRESSTABLE](addresstable.md)
</dt> <dt>

[ADDRESSPAIR](addresspair.md)
</dt> <dt>

[EXPRESSION](expression.md)
</dt> <dt>

[ANDEXP](andexp.md)
</dt> <dt>

[PATTERNMATCH](patternmatch.md)
</dt> </dl>

 

 




