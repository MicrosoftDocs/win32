---
title: Manager Return Values (Msctf.h)
description: The Text Services Framework produces return values in the range from 0xHHHH0200 through 0xHHHH0507. The following table gives the manager return values in alphabetical order.
ms.assetid: 12178252-c246-4fa4-bf7b-2445b859ec01
topic_type:
- apiref
api_name:
- Manager Return Values
api_location:
- Msctf.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Manager Return Values

The Text Services Framework produces return values in the range from 0x*HHHH*0200 through 0x*HHHH*0507. The following table gives the manager return values in alphabetical order.

> [!Note]  
> The descriptions supplied are non-specific; the meaning of a return value can vary depending on the method that returned the value.

 



| Return code/value                                                                                                                                                                                                                                                   | Description                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="TF_E_ALREADY_EXISTS"></span><span id="tf_e_already_exists"></span><dl> <dt>**TF\_E\_ALREADY\_EXISTS**</dt> <dt>0x80040506</dt> </dl>                   | The preserved key is registered.<br/>                                                       |
| <span id="TF_E_COMPOSITION_REJECTED"></span><span id="tf_e_composition_rejected"></span><dl> <dt>**TF\_E\_COMPOSITION\_REJECTED**</dt> <dt>0x80040508</dt> </dl> | The context owner rejected the composition.<br/>                                            |
| <span id="TF_E_DISCONNECTED"></span><span id="tf_e_disconnected"></span><dl> <dt>**TF\_E\_DISCONNECTED**</dt> <dt>0x80040504</dt> </dl>                          | The context object is not on a document stack.<br/>                                         |
| <span id="TF_E_EMPTYCONTEXT"></span><span id="tf_e_emptycontext"></span><dl> <dt>**TF\_E\_EMPTYCONTEXT**</dt> <dt>0x80040509</dt> </dl>                          | The context is empty.<br/>                                                                  |
| <span id="TF_E_FORMAT"></span><span id="tf_e_format"></span><dl> <dt>**TF\_E\_FORMAT**</dt> <dt>0x8004020a</dt> </dl>                                            | Context owner cannot handle objects of the type provided by the pDataObject parameter.<br/> |
| <span id="TF_E_INVALIDPOINT"></span><span id="tf_e_invalidpoint"></span><dl> <dt>**TF\_E\_INVALIDPOINT**</dt> <dt>0x80040207</dt> </dl>                          | The screen coordinates are invalid.<br/>                                                    |
| <span id="TF_E_INVALIDPOS"></span><span id="tf_e_invalidpos"></span><dl> <dt>**TF\_E\_INVALIDPOS**</dt> <dt>0x80040200</dt> </dl>                                | The character position is invalid.<br/>                                                     |
| <span id="TF_E_INVALIDVIEW"></span><span id="tf_e_invalidview"></span><dl> <dt>**TF\_E\_INVALIDVIEW**</dt> <dt>0x80040505</dt> </dl>                             | The context view is invalid.<br/>                                                           |
| <span id="TF_E_LOCKED"></span><span id="tf_e_locked"></span><dl> <dt>**TF\_E\_LOCKED**</dt> <dt>0x80040500</dt> </dl>                                            | The context is already locked.<br/>                                                         |
| <span id="TF_E_NOINTERFACE"></span><span id="tf_e_nointerface"></span><dl> <dt>**TF\_E\_NOINTERFACE**</dt> <dt>0x80040204</dt> </dl>                             | The object does not support the requested interface.<br/>                                   |
| <span id="TF_E_NOLAYOUT"></span><span id="tf_e_nolayout"></span><dl> <dt>**TF\_E\_NOLAYOUT**</dt> <dt>0x80040206</dt> </dl>                                      | The text layout has not been calculated.<br/>                                               |
| <span id="TF_E_NOLOCK"></span><span id="tf_e_nolock"></span><dl> <dt>**TF\_E\_NOLOCK**</dt> <dt>0x80040201</dt> </dl>                                            | The caller does not have the necessary type of document.<br/>                               |
| <span id="TF_E_NOOBJECT"></span><span id="tf_e_noobject"></span><dl> <dt>**TF\_E\_NOOBJECT**</dt> <dt>0x80040202</dt> </dl>                                      | No embedded object exists at the specified position.<br/>                                   |
| <span id="TF_E_NOPROVIDER"></span><span id="tf_e_noprovider"></span><dl> <dt>**TF\_E\_NOPROVIDER**</dt> <dt>0x80040503</dt> </dl>                                | No function provider exists for the specified function.<br/>                                |
| <span id="TF_E_NOSELECTION"></span><span id="tf_e_noselection"></span><dl> <dt>**TF\_E\_NOSELECTION**</dt> <dt>0x80040205</dt> </dl>                             | No selection exists within the context.<br/>                                                |
| <span id="TF_E_NOSERVICE"></span><span id="tf_e_noservice"></span><dl> <dt>**TF\_E\_NOSERVICE**</dt> <dt>0x80040203</dt> </dl>                                   | The specified service does not exists or cannot be created.<br/>                            |
| <span id="TF_E_NOTOWNEDRANGE"></span><span id="tf_e_notownedrange"></span><dl> <dt>**TF\_E\_NOTOWNEDRANGE**</dt> <dt>0x80040502</dt> </dl>                       | The TSF manager does not own the range.<br/>                                                |
| <span id="TF_E_RANGE_NOT_COVERED"></span><span id="tf_e_range_not_covered"></span><dl> <dt>**TF\_E\_RANGE\_NOT\_COVERED**</dt> <dt>0x80040507</dt> </dl>         | The range is not within an active composition.<br/>                                         |
| <span id="TF_E_READONLY"></span><span id="tf_e_readonly"></span><dl> <dt>**TF\_E\_READONLY**</dt> <dt>0x80040209</dt> </dl>                                      | The edit context is read-only.<br/>                                                         |
| <span id="TF_E_STACKFULL"></span><span id="tf_e_stackfull"></span><dl> <dt>**TF\_E\_STACKFULL**</dt> <dt>0x80040501</dt> </dl>                                   | The context stack is full.<br/>                                                             |
| <span id="TF_E_SYNCHRONOUS"></span><span id="tf_e_synchronous"></span><dl> <dt>**TF\_E\_SYNCHRONOUS**</dt> <dt>0x80040208</dt> </dl>                             | A synchronous read-only lock cannot be obtained.<br/>                                       |
| <span id="TF_S_ASYNC"></span><span id="tf_s_async"></span><dl> <dt>**TF\_S\_ASYNC**</dt> <dt>0x00040300</dt> </dl>                                               | The data will be obtained asynchronously.<br/>                                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



 

 





