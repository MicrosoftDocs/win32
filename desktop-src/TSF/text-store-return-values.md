---
title: Text Store Return Values (Textstor.h)
description: When a document manager processes a text store, it produces return values in the range from 0xHHHH0200 through 0xHHHH0300. The following table lists text store return values in alphabetical order.
ms.assetid: 20b0a89f-ab52-466f-9669-c6c29ad12de0
topic_type:
- apiref
api_name:
- Text Store Return Values
api_location:
- Textstor.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Text Store Return Values

When a document manager processes a text store, it produces return values in the range from 0x*HHHH*0200 through 0x*HHHH*0300. The following table lists text store return values in alphabetical order.



| Return code/value                                                                                                                                                                                                                          | Description                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TS_E_FORMAT"></span><span id="ts_e_format"></span><dl> <dt>**TS\_E\_FORMAT**</dt> <dt>0x8004020a</dt> </dl>                   | Application does not support the data type contained in the [**IDataObject**](/windows/desktop/api/objidl/nn-objidl-idataobject) object to be inserted using [**ITextStoreACP::InsertEmbedded**](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-insertembedded).<br/> |
| <span id="TS_E_INVALIDPOINT"></span><span id="ts_e_invalidpoint"></span><dl> <dt>**TS\_E\_INVALIDPOINT**</dt> <dt>0x80040207</dt> </dl> | Parameter is not within the bounding box of any character.<br/>                                                                                                                                        |
| <span id="TS_E_INVALIDPOS"></span><span id="ts_e_invalidpos"></span><dl> <dt>**TS\_E\_INVALIDPOS**</dt> <dt>0x80040200</dt> </dl>       | Range specified extends outside the document.<br/>                                                                                                                                                     |
| <span id="TS_E_NOINTERFACE"></span><span id="ts_e_nointerface"></span><dl> <dt>**TS\_E\_NOINTERFACE**</dt> <dt>0x80040204</dt> </dl>    | Object does not support the requested interface.<br/>                                                                                                                                                  |
| <span id="TS_E_NOLAYOUT"></span><span id="ts_e_nolayout"></span><dl> <dt>**TS\_E\_NOLAYOUT**</dt> <dt>0x80040206</dt> </dl>             | Application has not calculated a text layout.<br/>                                                                                                                                                     |
| <span id="TS_E_NOLOCK"></span><span id="ts_e_nolock"></span><dl> <dt>**TS\_E\_NOLOCK**</dt> <dt>0x80040201</dt> </dl>                   | Application does not have a read-only lock or read/write lock for the document.<br/>                                                                                                                   |
| <span id="TS_E_NOOBJECT"></span><span id="ts_e_noobject"></span><dl> <dt>**TS\_E\_NOOBJECT**</dt> <dt>0x80040202</dt> </dl>             | Embedded content offset is not positioned before a TF\_CHAR\_EMBEDDED character.<br/>                                                                                                                  |
| <span id="TS_E_NOSELECTION"></span><span id="ts_e_noselection"></span><dl> <dt>**TS\_E\_NOSELECTION**</dt> <dt>0x80040205</dt> </dl>    | Document has no selection.<br/>                                                                                                                                                                        |
| <span id="TS_E_NOSERVICE"></span><span id="ts_e_noservice"></span><dl> <dt>**TS\_E\_NOSERVICE**</dt> <dt>0x80040203</dt> </dl>          | Content cannot be returned to match the service GUID.<br/>                                                                                                                                             |
| <span id="TS_E_READONLY"></span><span id="ts_e_readonly"></span><dl> <dt>**TS\_E\_READONLY**</dt> <dt>0x80040209</dt> </dl>             | Document is read-only. Cannot modify content.<br/>                                                                                                                                                     |
| <span id="TS_E_SYNCHRONOUS"></span><span id="ts_e_synchronous"></span><dl> <dt>**TS\_E\_SYNCHRONOUS**</dt> <dt>0x00040300</dt> </dl>    | Document cannot be locked synchronously.<br/>                                                                                                                                                          |
| <span id="TS_S_ASYNC"></span><span id="ts_s_async"></span><dl> <dt>**TS\_S\_ASYNC**</dt> <dt>( 0x1 )</dt> </dl>                         | Document successfully received an asynchronous lock.<br/>                                                                                                                                              |



 

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

[**ITextStoreACP::InsertEmbedded**](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-insertembedded)
</dt> </dl>

 

