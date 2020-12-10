---
title: TS_SS_ Constants (Textstor.h)
description: The TS\_SS\_\ constants, defined before run time in the TS\_STATUS structure, describe static document states.
ms.assetid: 17264527-946a-4648-a4eb-30db751602ab
topic_type:
- apiref
api_name:
- TS_SS_DISJOINTSEL
- TS_SS_REGIONS
- TS_SS_TRANSITORY
- TS_SS_NOHIDDENTEXT
- TS_SS_TKBAUTOCORRECTENABLE
- TS_SS_TKBPREDICTIONENABLE
api_location:
- Textstor.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TS\_SS\_\* Constants

The TS\_SS\_\* constants, defined before run time in the [**TS\_STATUS**](/windows/desktop/api/Textstor/ns-textstor-ts_status) structure, describe static document states.



| Constant/value                                                                                                                                                                                                                                                      | Description                                                                                                    |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| <span id="TS_SS_DISJOINTSEL"></span><span id="ts_ss_disjointsel"></span><dl> <dt>**TS\_SS\_DISJOINTSEL**</dt> <dt>( 0x1 )</dt> </dl>                             | The document supports multiple selections.<br/>                                                          |
| <span id="TS_SS_REGIONS"></span><span id="ts_ss_regions"></span><dl> <dt>**TS\_SS\_REGIONS**</dt> <dt>( 0x2 )</dt> </dl>                                         | The document can contain multiple regions.<br/>                                                          |
| <span id="TS_SS_TRANSITORY"></span><span id="ts_ss_transitory"></span><dl> <dt>**TS\_SS\_TRANSITORY**</dt> <dt>( 0x4 )</dt> </dl>                                | The document is expected to have a short usage cycle.<br/>                                               |
| <span id="TS_SS_NOHIDDENTEXT"></span><span id="ts_ss_nohiddentext"></span><dl> <dt>**TS\_SS\_NOHIDDENTEXT**</dt> <dt>( 0x8 )</dt> </dl>                          | The document will never contain hidden text.<br/>                                                        |
| <span id="TS_SS_TKBAUTOCORRECTENABLE"></span><span id="ts_ss_tkbautocorrectenable"></span><dl> <dt>**TS\_SS\_TKBAUTOCORRECTENABLE**</dt> <dt>( 0x10 )</dt> </dl> | **Starting with Windows 8:** The document supports autocorrection provided by the touch keyboard.<br/>   |
| <span id="TS_SS_TKBPREDICTIONENABLE"></span><span id="ts_ss_tkbpredictionenable"></span><dl> <dt>**TS\_SS\_TKBPREDICTIONENABLE**</dt> <dt>( 0x20 )</dt> </dl>    | **Starting with Windows 8:** The document supports text suggestions provided by the touch keyboard.<br/> |



## Remarks

The **dwStaticFlags** member of the **TS\_STATUS** structure uses these constants.

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

[**TS\_STATUS**](/windows/desktop/api/Textstor/ns-textstor-ts_status)
</dt> <dt>

[**TF\_STATUS**](/previous-versions/windows/desktop/legacy/ms629192(v=vs.85))
</dt> </dl>

 

