---
title: TF_ES_ Constants (Msctf.h)
description: The following are constants used by the ITfContext RequestEditSession method.
ms.assetid: 5498329f-3302-4f66-bdec-cab7db0cdc0e
topic_type:
- apiref
api_name:
- TF_ES_ASYNCDONTCARE
- TF_ES_SYNC
- TF_ES_READ
- TF_ES_READWRITE
- TF_ES_ASYNC
api_location:
- Msctf.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TF\_ES\_\* Constants

The following are constants used by the [ITfContext::RequestEditSession](/windows/desktop/api/Msctf/nf-msctf-itfcontext-requesteditsession) method.



| Constant/value                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                             |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_ES_ASYNCDONTCARE"></span><span id="tf_es_asyncdontcare"></span><dl> <dt>**TF\_ES\_ASYNCDONTCARE**</dt> <dt>( 0 )</dt> </dl> | The edit session can occur synchronously or asynchronously, at the discretion of the manager. The manager will attempt to schedule a synchronous edit session for improved performance. This value cannot be combined with the TF\_ES\_ASYNC or TF\_ES\_SYNC values.<br/>                                                                         |
| <span id="TF_ES_SYNC"></span><span id="tf_es_sync"></span><dl> <dt>**TF\_ES\_SYNC**</dt> <dt>( 0x1 )</dt> </dl>                          | The edit session must be synchronous or the request will fail (with TF\_E\_SYNCHRONOUS). This flag should only be used in documented situations (such as keystroke handling) where it can be expected to succeed. Otherwise the call will likely fail. This value cannot be combined with the TF\_ES\_ASYNCDONTCARE or TF\_ES\_ASYNC values.<br/> |
| <span id="TF_ES_READ"></span><span id="tf_es_read"></span><dl> <dt>**TF\_ES\_READ**</dt> <dt>( 0x2 )</dt> </dl>                          | Requests read-only access to the context.<br/>                                                                                                                                                                                                                                                                                                    |
| <span id="TF_ES_READWRITE"></span><span id="tf_es_readwrite"></span><dl> <dt>**TF\_ES\_READWRITE**</dt> <dt>( 0x6 )</dt> </dl>           | Requests read/write access to the context.<br/>                                                                                                                                                                                                                                                                                                   |
| <span id="TF_ES_ASYNC"></span><span id="tf_es_async"></span><dl> <dt>**TF\_ES\_ASYNC**</dt> <dt>( 0x8 )</dt> </dl>                       | The edit session must be asynchronous or the request will fail. This value cannot be combined with the TF\_ES\_ASYNCDONTCARE or TF\_ES\_SYNC values.<br/>                                                                                                                                                                                         |



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

[ITfContext::RequestEditSession](/windows/desktop/api/Msctf/nf-msctf-itfcontext-requesteditsession)
</dt> </dl>

 

 





