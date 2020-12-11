---
title: TS_CHAR_ Constants (Textstor.h)
description: The TS\_CHAR\_\ constants describe the type of character.
ms.assetid: b40ca931-d45c-4101-9380-bb2b3ad25fba
topic_type:
- apiref
api_name:
- TS_CHAR_EMBEDDED
- TS_CHAR_REGION
- TS_CHAR_REPLACEMENT
api_location:
- Textstor.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TS\_CHAR\_\* Constants

The TS\_CHAR\_\* constants describe the type of character.



| Constant/value                                                                                                                                                                                                                                   | Description                                                                                         |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| <span id="TS_CHAR_EMBEDDED"></span><span id="ts_char_embedded"></span><dl> <dt>**TS\_CHAR\_EMBEDDED**</dt> <dt>( 0xfffc )</dt> </dl>          | The character is a Unicode 2.1 object-replacement character.<br/>                             |
| <span id="TS_CHAR_REGION"></span><span id="ts_char_region"></span><dl> <dt>**TS\_CHAR\_REGION**</dt> <dt>( 0 )</dt> </dl>                     | The character is a region boundary.<br/>                                                      |
| <span id="TS_CHAR_REPLACEMENT"></span><span id="ts_char_replacement"></span><dl> <dt>**TS\_CHAR\_REPLACEMENT**</dt> <dt>( 0xfffd )</dt> </dl> | The character is a hidden-text placeholder character or a Unicode replacement character.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                         |
| Header<br/>                   | <dl> <dt>Textstor.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Textstor.idl</dt> </dl> |



## See also

<dl> <dt>

[Embedded Objects](embedded-objects.md)
</dt> </dl>

 

 





