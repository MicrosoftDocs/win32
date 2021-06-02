---
title: TS_IAS_ Constants (Textstor.h)
description: The TS\_IAS\_\ constants are used as bitfield flags to control insertion of text or embedded objects at a selection or insertion point.
ms.assetid: 58e0d13c-d90c-41d2-bd93-4eba5fe0a69a
topic_type:
- apiref
api_name:
- TS_IAS_NOQUERY
- TS_IAS_QUERYONLY
api_location:
- Textstor.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TS\_IAS\_\* Constants

The TS\_IAS\_\* constants are used as bitfield flags to control insertion of text or embedded objects at a selection or insertion point.



| Constant/value                                                                                                                                                                                                                       | Description                                                                                                                                   |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TS_IAS_NOQUERY"></span><span id="ts_ias_noquery"></span><dl> <dt>**TS\_IAS\_NOQUERY**</dt> <dt>( 0x1 )</dt> </dl>       | Text is inserted and the range pointer is set to **NULL** upon exit. Cannot be combined with the TS\_IAS\_QUERYONLY flag.<br/>          |
| <span id="TS_IAS_QUERYONLY"></span><span id="ts_ias_queryonly"></span><dl> <dt>**TS\_IAS\_QUERYONLY**</dt> <dt>( 0x2 )</dt> </dl> | Do not perform the insertion. Caller only requires the range pointer to be set. Cannot be combined with the TS\_IAS\_NOQUERY flag.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                         |
| Header<br/>                   | <dl> <dt>Textstor.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Textstor.idl</dt> </dl> |



 

 





