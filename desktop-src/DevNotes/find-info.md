---
description: Contains search context information.
ms.assetid: 4b865563-98c2-459b-bb2b-75420d51d6a7
title: FIND_INFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FIND_INFO
api_type: 
- NA
api_location: 
---

# FIND\_INFO structure

Contains search context information.

## Syntax


```C++
typedef struct _FIND_INFO {
  TAGID     tiIndex;
  TAGID     tiCurrent;
  TAGID     tiEndIndex;
  TAG       tName;
  DWORD     dwIndexRec;
  DWORD     dwFlags;
  ULONGLONG ullKey;
  union {
    LPCTSTR szName;
    DWORD   dwName;
    GUID    *pguidName;
  };
} FIND_INFO, *PFIND_INFO;
```



## Members

<dl> <dt>

**tiIndex**
</dt> <dd>

The **TAGID** for the index to be searched.

</dd> <dt>

**tiCurrent**
</dt> <dd>

The **TAGID** for the current item that was located.

</dd> <dt>

**tiEndIndex**
</dt> <dd>

The **TAGID** for the last record after FindFirst if the index is UNIQUE.

</dd> <dt>

**tName**
</dt> <dd>

The type of the item to be located. See [TAG Types](tag-types.md).

</dd> <dt>

**dwIndexRec**
</dt> <dd>

An internal counter used to track where in the index the next find operation should start.

</dd> <dt>

**dwFlags**
</dt> <dd>

This member can be 0 or **SHIMDB\_INDEX\_UNIQUE\_KEY** (0x00000001), which indicates that this is a unique-key index.

</dd> <dt>

**ullKey**
</dt> <dd>

The key for the current entry.

</dd> <dt>

**szName**
</dt> <dd>

The current string (if the tag type is **TAG\_TYPE\_STRINGREF**).

</dd> <dt>

**dwName**
</dt> <dd>

The current **DWORD** value (if the tag type is **TAG\_TYPE\_DWORD**).

</dd> <dt>

**pguidName**
</dt> <dd>

The current GUID value (if the tag type is **TAG\_TYPE\_BINARY** and the TAG is **TAG\_DATABASE\_ID**).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SdbFindFirstDWORDIndexedTag**](sdbfindfirstdwordindexedtag.md)
</dt> </dl>

 

 




