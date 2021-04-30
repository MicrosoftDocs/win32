---
title: TF_SS_ Constants (Msctf.h)
description: The TF\_SS\_\ constants, defined before run time in the TF\_STATUS structure, describe static document states.
ms.assetid: 371aeeda-f081-4506-ba51-79c6a8bc8768
topic_type:
- apiref
api_name:
- TF_SS_DISJOINTSEL
- TF_SS_REGIONS
- TF_SS_TRANSITORY
- TF_SS_TKBAUTOCORRECTENABLE
- TF_SS_TKBPREDICTIONENABLE
api_location:
- Msctf.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_SS\_\* Constants

The TF\_SS\_\* constants, defined before run time in the [**TF\_STATUS**](/previous-versions/windows/desktop/legacy/ms629192(v=vs.85)) structure, describe static document states.



| Constant/value                                                                                                                                                                                                                                                                              | Description                                                                                                    |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| <span id="TF_SS_DISJOINTSEL"></span><span id="tf_ss_disjointsel"></span><dl> <dt>**TF\_SS\_DISJOINTSEL**</dt> <dt>( TS\_SS\_DISJOINTSEL )</dt> </dl>                                     | The document supports multiple selections.<br/>                                                          |
| <span id="TF_SS_REGIONS"></span><span id="tf_ss_regions"></span><dl> <dt>**TF\_SS\_REGIONS**</dt> <dt>( TS\_SS\_REGIONS )</dt> </dl>                                                     | The document can contain multiple regions.<br/>                                                          |
| <span id="TF_SS_TRANSITORY"></span><span id="tf_ss_transitory"></span><dl> <dt>**TF\_SS\_TRANSITORY**</dt> <dt>( TS\_SS\_TRANSITORY )</dt> </dl>                                         | The document is expected to have a short usage cycle.<br/>                                               |
| <span id="TF_SS_TKBAUTOCORRECTENABLE"></span><span id="tf_ss_tkbautocorrectenable"></span><dl> <dt>**TF\_SS\_TKBAUTOCORRECTENABLE**</dt> <dt>( TS\_SS\_TKBAUTOCORRECTENABLE )</dt> </dl> | **Starting with Windows 8:** The document supports autocorrection provided by the touch keyboard.<br/>   |
| <span id="TF_SS_TKBPREDICTIONENABLE"></span><span id="tf_ss_tkbpredictionenable"></span><dl> <dt>**TF\_SS\_TKBPREDICTIONENABLE**</dt> <dt>( TS\_SS\_TKBPREDICTIONENABLE )</dt> </dl>     | **Starting with Windows 8:** The document supports text suggestions provided by the touch keyboard.<br/> |



## Remarks

The **dwStaticFlags** member of the TF\_STATUS structure uses these constants.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**TF\_STATUS**](/previous-versions/windows/desktop/legacy/ms629192(v=vs.85))
</dt> </dl>

 

