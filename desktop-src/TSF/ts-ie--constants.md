---
title: TS_IE_ Constants (Textstor.h)
description: The TS\_IE\_\ constants describe how to insert text that can contain embedded objects used by text services.
ms.assetid: a455d712-42d5-472e-862d-85ae3ba9149f
topic_type:
- apiref
api_name:
- TS_IE_CORRECTION
- TS_IE_COMPOSITION
api_location:
- Textstor.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TS\_IE\_\* Constants

The TS\_IE\_\* constants describe how to insert text that can contain embedded objects used by text services.



| Constant/value                                                                                                                                                                                                                          | Description                                                                                                                                                                           |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TS_IE_CORRECTION"></span><span id="ts_ie_correction"></span><dl> <dt>**TS\_IE\_CORRECTION**</dt> <dt>( 0x1 )</dt> </dl>    | The text is a transform (correction) of existing content, and any special text markup information (metadata) is retained, such as .wav file data or a language identifier.<br/> |
| <span id="TS_IE_COMPOSITION"></span><span id="ts_ie_composition"></span><dl> <dt>**TS\_IE\_COMPOSITION**</dt> <dt>( 0x2 )</dt> </dl> | Not used.<br/>                                                                                                                                                                  |



## Remarks

These constants are used in the *dwFlags* parameter of [ITextStoreACP::InsertEmbedded](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-insertembedded) and [ITextStoreAnchor::InsertEmbedded](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-insertembedded).

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

[ITextStoreACP::InsertEmbedded](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-insertembedded)
</dt> <dt>

[ITextStoreAnchor::InsertEmbedded](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-insertembedded)
</dt> </dl>

 

 





