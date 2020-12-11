---
title: TF_SD_ Constants (Msctf.h)
description: The TF\_SD\_\ constants describe the document status.
ms.assetid: 953d39cd-8af1-4c86-8fb8-8b8ec917c631
topic_type:
- apiref
api_name:
- TF_SD_READONLY
- TF_SD_LOADING
api_location:
- Msctf.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_SD\_\* Constants

The TF\_SD\_\* constants describe the document status.



| Constant/value                                                                                                                                                                                                                              | Description                                                  |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| <span id="TF_SD_READONLY"></span><span id="tf_sd_readonly"></span><dl> <dt>**TF\_SD\_READONLY**</dt> <dt>( TS\_SD\_READONLY )</dt> </dl> | The document is read-only and cannot be modified.<br/> |
| <span id="TF_SD_LOADING"></span><span id="tf_sd_loading"></span><dl> <dt>**TF\_SD\_LOADING**</dt> <dt>( TS\_SD\_LOADING )</dt> </dl>     | The document is loading and can be incomplete.<br/>    |



## Remarks

The **dwDynamicFlags** member of the [TF\_STATUS](/previous-versions/windows/desktop/legacy/ms629192(v=vs.85)) structure uses these constants.

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

[TF\_STATUS](/previous-versions/windows/desktop/legacy/ms629192(v=vs.85))
</dt> <dt>

[TS\_SD\_\* Constants](ts-sd--constants.md)
</dt> <dt>

[ITfContextOwner::GetStatus](/windows/desktop/api/Msctf/nf-msctf-itfcontextowner-getstatus)
</dt> <dt>

[ITfContextOwnerServices::OnStatusChange](/windows/desktop/api/Msctf/nf-msctf-itfcontextownerservices-onstatuschange)
</dt> <dt>

[ITextStoreACP::GetStatus](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-getstatus)
</dt> <dt>

[ITfStatusSunk::OnStatusChange](/windows/desktop/api/Msctf/nf-msctf-itfstatussink-onstatuschange)
</dt> </dl>

 

