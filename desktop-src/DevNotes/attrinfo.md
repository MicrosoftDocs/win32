---
description: Contains the attribute data for a file.
ms.assetid: f23f801c-826c-4269-bf96-0e01430484f4
title: ATTRINFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ATTRINFO
api_type: 
- NA
api_location: 
---

# ATTRINFO structure

Contains the attribute data for a file.

## Syntax


```C++
typedef struct tagATTRINFO {
  TAG   tAttrID;
  DWORD dwFlags;
  union {
    ULONGLONG ullAttr;
    DWORD     dwAttr;
    TCHAR     *lpAttr;
  };
} ATTRINFO, *PATTRINFO;
```



## Members

<dl> <dt>

**tAttrID**
</dt> <dd>

The attribute type. See [TAG Types](tag-types.md).

</dd> <dt>

**dwFlags**
</dt> <dd>

The flags for this attribute.



| Value                                                                                                                                                                                                                                           | Meaning                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <span id="ATTRIBUTE_AVAILABLE"></span><span id="attribute_available"></span><dl> <dt>**ATTRIBUTE\_AVAILABLE**</dt> <dt>0x00000001</dt> </dl> | The attribute is available.<br/>                             |
| <span id="ATTRIBUTE_FAILED"></span><span id="attribute_failed"></span><dl> <dt>**ATTRIBUTE\_FAILED**</dt> <dt>0x00000002</dt> </dl>          | The call failed because the attribute is not available.<br/> |



 

</dd> <dt>

**ullAttr**
</dt> <dd>

A **QWORD** value (if the tag type is **TAG\_TYPE\_QWORD**).

</dd> <dt>

**dwAttr**
</dt> <dd>

A **DWORD** value (if the tag type is **TAG\_TYPE\_DWORD**).

</dd> <dt>

**lpAttr**
</dt> <dd>

A pointer to a string (if the tag type is **TAG\_TYPE\_STRINGREF**).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SdbFormatAttribute**](sdbformatattribute.md)
</dt> <dt>

[**SdbFreeFileAttributes**](sdbfreefileattributes.md)
</dt> <dt>

[**SdbGetFileAttributes**](sdbgetfileattributes.md)
</dt> </dl>

 

 




