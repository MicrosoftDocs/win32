---
description: Describes the data type of the value associated with a TAG.
ms.assetid: 009ad522-35da-4053-a7f6-61d7d240b98c
title: TAG Types
ms.topic: reference
ms.date: 05/31/2018
---

# TAG Types

Describes the data type of the value associated with a TAG.



| Constant/value                                                                                                                                                                                                                            | Description                                           |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------|
| <span id="TAG_TYPE_NULL"></span><span id="tag_type_null"></span><dl> <dt>**TAG\_TYPE\_NULL**</dt> <dt>0x1000</dt> </dl>                | There is no value associated with the TAG.<br/> |
| <span id="TAG_TYPE_BYTE"></span><span id="tag_type_byte"></span><dl> <dt>**TAG\_TYPE\_BYTE**</dt> <dt>0x2000</dt> </dl>                | A **BYTE** value.<br/>                          |
| <span id="TAG_TYPE_WORD"></span><span id="tag_type_word"></span><dl> <dt>**TAG\_TYPE\_WORD**</dt> <dt>0x3000</dt> </dl>                | A **WORD** value.<br/>                          |
| <span id="TAG_TYPE_DWORD"></span><span id="tag_type_dword"></span><dl> <dt>**TAG\_TYPE\_DWORD**</dt> <dt>0x4000</dt> </dl>             | A **DWORD** value.<br/>                         |
| <span id="TAG_TYPE_QWORD"></span><span id="tag_type_qword"></span><dl> <dt>**TAG\_TYPE\_QWORD**</dt> <dt>0x5000</dt> </dl>             | A **ULONGLONG** value.<br/>                     |
| <span id="TAG_TYPE_STRINGREF"></span><span id="tag_type_stringref"></span><dl> <dt>**TAG\_TYPE\_STRINGREF**</dt> <dt>0x6000</dt> </dl> | A tokenized string value.<br/>                  |
| <span id="TAG_TYPE_LIST"></span><span id="tag_type_list"></span><dl> <dt>**TAG\_TYPE\_LIST**</dt> <dt>0x7000</dt> </dl>                | A list of TAG values.<br/>                      |
| <span id="TAG_TYPE_STRING"></span><span id="tag_type_string"></span><dl> <dt>**TAG\_TYPE\_STRING**</dt> <dt>0x8000</dt> </dl>          | A string value.<br/>                            |
| <span id="TAG_TYPE_BINARY"></span><span id="tag_type_binary"></span><dl> <dt>**TAG\_TYPE\_BINARY**</dt> <dt>0x9000</dt> </dl>          | A binary value.<br/>                            |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**TAG**](tag.md)
</dt> <dt>

[**TAGID**](tagid.md)
</dt> <dt>

[**TAGREF**](tagref.md)
</dt> </dl>

 

 




