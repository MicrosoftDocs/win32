---
title: TS_SD_ Constants (Textstor.h)
description: The TS\_SD\_\ constants describe dynamic document states used by an application at runtime.
ms.assetid: fb673e42-bee7-484e-872a-d709d5ca12f2
topic_type:
- apiref
api_name:
- TS_SD_READONLY
- TS_SD_LOADING
- TS_SD_MASKALL
api_location:
- Textstor.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TS\_SD\_\* Constants

The TS\_SD\_\* constants describe dynamic document states used by an application at runtime.



| Constant/value                                                                                                                                                                                                                                              | Description                                                  |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| <span id="TS_SD_READONLY"></span><span id="ts_sd_readonly"></span><dl> <dt>**TS\_SD\_READONLY**</dt> <dt>( 0x1 )</dt> </dl>                              | The document is read-only and cannot be modified.<br/> |
| <span id="TS_SD_LOADING"></span><span id="ts_sd_loading"></span><dl> <dt>**TS\_SD\_LOADING**</dt> <dt>( 0x2 )</dt> </dl>                                 | The document is loading and might be incomplete.<br/>  |
| <span id="TS_SD_MASKALL"></span><span id="ts_sd_maskall"></span><dl> <dt>**TS\_SD\_MASKALL**</dt> <dt>( TS\_SD\_READONLY \| TS\_SD\_LOADING )</dt> </dl> | The document is both read-only and loading.<br/>       |



## Remarks

The **dwDynamicFlags** member of the [TS\_STATUS](/windows/desktop/api/Textstor/ns-textstor-ts_status) structure uses these constants.

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

[TS\_STATUS](/windows/desktop/api/Textstor/ns-textstor-ts_status)
</dt> <dt>

[TF\_SD\_\* Constants](tf-sd--constants.md)
</dt> </dl>

 

 





