---
title: WMDM_TAG_DATATYPE enumeration
description: The WMDM\_TAG\_DATATYPE enumeration type defines a data type.
ms.assetid: 9c300814-5610-4e46-b441-e7f2fc78a47b
keywords:
- WMDM_TAG_DATATYPE enumeration windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDM_TAG_DATATYPE
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDM\_TAG\_DATATYPE enumeration

The **WMDM\_TAG\_DATATYPE** enumeration type defines a data type.

## Syntax


```C++
typedef enum tagWMDM_TAG_DATATYPE { 
  WMDM_TYPE_DWORD,
  WMDM_TYPE_STRING,
  WMDM_TYPE_BINARY,
  WMDM_TYPE_BOOL,
  WMDM_TYPE_QWORD,
  WMDM_TYPE_WORD,
  WMDM_TYPE_GUID,
  WMDM_TYPE_DATE
} WMDM_TAG_DATATYPE;
```



## Constants

<dl> <dt>

<span id="WMDM_TYPE_DWORD"></span><span id="wmdm_type_dword"></span>**WMDM\_TYPE\_DWORD**
</dt> <dd>

Specifies a 4-byte **DWORD** value.

</dd> <dt>

<span id="WMDM_TYPE_STRING"></span><span id="wmdm_type_string"></span>**WMDM\_TYPE\_STRING**
</dt> <dd>

Specifies a null-terminated Unicode string (2 bytes per character).

</dd> <dt>

<span id="WMDM_TYPE_BINARY"></span><span id="wmdm_type_binary"></span>**WMDM\_TYPE\_BINARY**
</dt> <dd>

Specifies an array of bytes.

</dd> <dt>

<span id="WMDM_TYPE_BOOL"></span><span id="wmdm_type_bool"></span>**WMDM\_TYPE\_BOOL**
</dt> <dd>

Specifies a 4-byte Boolean value.

</dd> <dt>

<span id="WMDM_TYPE_QWORD"></span><span id="wmdm_type_qword"></span>**WMDM\_TYPE\_QWORD**
</dt> <dd>

Specifies an 8-byte **QWORD** value.

</dd> <dt>

<span id="WMDM_TYPE_WORD"></span><span id="wmdm_type_word"></span>**WMDM\_TYPE\_WORD**
</dt> <dd>

Specifies a 2-byte **WORD** value.

</dd> <dt>

<span id="WMDM_TYPE_GUID"></span><span id="wmdm_type_guid"></span>**WMDM\_TYPE\_GUID**
</dt> <dd>

Specifies a 128-bit (16-byte) GUID.

</dd> <dt>

<span id="WMDM_TYPE_DATE"></span><span id="wmdm_type_date"></span>**WMDM\_TYPE\_DATE**
</dt> <dd>

Specifies a date.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 





