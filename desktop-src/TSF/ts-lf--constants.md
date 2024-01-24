---
title: TS_LF_ Constants (Textstor.h)
description: The TS\_LF\_\ constants specify the type of document lock.
ms.assetid: f0bb6ef9-a8fc-4331-9210-6c5ba1721a73
topic_type:
- apiref
api_name:
- TS_LF_SYNC
- TS_LF_READ
- TS_LF_READWRITE
api_location:
- Textstor.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TS\_LF\_\* Constants

The TS\_LF\_\* constants specify the type of document lock.



| Constant/value                                                                                                                                                                                                                    | Description                                                                               |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| <span id="TS_LF_SYNC"></span><span id="ts_lf_sync"></span><dl> <dt>**TS\_LF\_SYNC**</dt> <dt>( 0x1 )</dt> </dl>                | The document has a synchronous-lock if this flag is combined with other flags.<br/> |
| <span id="TS_LF_READ"></span><span id="ts_lf_read"></span><dl> <dt>**TS\_LF\_READ**</dt> <dt>( 0x2 )</dt> </dl>                | The document has a read-only lock and cannot be modified.<br/>                      |
| <span id="TS_LF_READWRITE"></span><span id="ts_lf_readwrite"></span><dl> <dt>**TS\_LF\_READWRITE**</dt> <dt>( 0x6 )</dt> </dl> | The document has a read/write lock and can be modified.<br/>                        |



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

[Document Locks](document-locks.md)
</dt> <dt>

[ITextStoreACP::RequestLock](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-requestlock)
</dt> <dt>

[ITextStoreACPSink::OnLockGranted](/windows/desktop/api/Textstor/nf-textstor-itextstoreacpsink-onlockgranted)
</dt> <dt>

[ITextStoreAnchor::RequestLock](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-requestlock)
</dt> <dt>

[ITextStoreAnchorSink::OnLockGranted](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchorsink-onlockgranted)
</dt> </dl>

 

 





