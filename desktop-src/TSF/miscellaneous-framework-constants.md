---
title: Miscellaneous Framework Constants
description: Miscellaneous framework constants indicate settings for clients, processes, or text.
ms.assetid: 'fa53c1f1-50eb-45eb-b2ea-f236a376d41a'
topic_type:
- apiref
api_name:
- TF_CLIENTID_NULL
- TF_INVALID_GUIDATOM
- TF_DEFAULT_SELECTION
- TF_GTP_INCL_TEXT
- TF_HF_OBJECT
- TF_IE_CORRECTION
- TF_INVALID_COOKIE
- TF_INVALID_EDIT_COOKIE
- TF_POPF_ALL
- TF_ST_CORRECTION
- TF_TU_CORRECTION
- TF_US_HIDETIPUI
api_location:
- Msctf.h
api_type:
- HeaderDef
---

# Miscellaneous Framework Constants

Miscellaneous framework constants indicate settings for clients, processes, or text.



| Constant/value                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_CLIENTID_NULL"></span><span id="tf_clientid_null"></span><dl> <dt>**TF\_CLIENTID\_NULL**</dt> <dt>((TfClientId)0)</dt> </dl>                        | Indicates to a text service that the client is deactivated. See [TfClientId](tfclientid.md).<br/>                                                                                                                                                      |
| <span id="TF_INVALID_GUIDATOM"></span><span id="tf_invalid_guidatom"></span><dl> <dt>**TF\_INVALID\_GUIDATOM**</dt> <dt>((TfGuidAtom)0)</dt> </dl>               | The [TfGuidAtom](tfguidatom.md) value for the current process is invalid.<br/>                                                                                                                                                                         |
| <span id="TF_DEFAULT_SELECTION"></span><span id="tf_default_selection"></span><dl> <dt>**TF\_DEFAULT\_SELECTION**</dt> <dt>( TS\_DEFAULT\_SELECTION )</dt> </dl> | Use the default selection. Used by [ITfContext::GetSelection](itfcontext-getselection.md), [ITextStoreACP::GetSelection](itextstoreacp-getselection.md), and [ITextStoreAnchor::GetSelection](itextstoreanchor-getselection.md).<br/>                |
| <span id="TF_GTP_INCL_TEXT"></span><span id="tf_gtp_incl_text"></span><dl> <dt>**TF\_GTP\_INCL\_TEXT**</dt> <dt>( 0x1 )</dt> </dl>                               | Specifies that the [ITfEditRecord::GetTextAndPropertyUpdates](itfeditrecord-gettextandpropertyupdates.md) method will obtain the collection of range objects that cover the text changed during the edit session.<br/>                                 |
| <span id="TF_HF_OBJECT"></span><span id="tf_hf_object"></span><dl> <dt>**TF\_HF\_OBJECT**</dt> <dt>( 1 )</dt> </dl>                                              | The range shift stops if an embedded object is encountered. Used in **dwFlags** member of [TF\_HALTCOND](tf-haltcond.md) structure.<br/>                                                                                                               |
| <span id="TF_IE_CORRECTION"></span><span id="tf_ie_correction"></span><dl> <dt>**TF\_IE\_CORRECTION**</dt> <dt>( 1 )</dt> </dl>                                  | The text is a transform (correction) of existing content, so that other text services can preserve data associated with the original text. Used in *dwFlags* parameter of [ITfRange::InsertEmbedded](itfrange-insertembedded.md).<br/>                 |
| <span id="TF_INVALID_COOKIE"></span><span id="tf_invalid_cookie"></span><dl> <dt>**TF\_INVALID\_COOKIE**</dt> <dt>( 0xffffffff )</dt> </dl>                      | Not used.<br/>                                                                                                                                                                                                                                          |
| <span id="TF_INVALID_EDIT_COOKIE"></span><span id="tf_invalid_edit_cookie"></span><dl> <dt>**TF\_INVALID\_EDIT\_COOKIE**</dt> <dt>( 0 )</dt> </dl>               | Not used.<br/>                                                                                                                                                                                                                                          |
| <span id="TF_POPF_ALL"></span><span id="tf_popf_all"></span><dl> <dt>**TF\_POPF\_ALL**</dt> <dt>( 0x1 )</dt> </dl>                                               | All contexts are removed from the stack. Used in *dwFlags* parameter of [ITfDocumentMgr::Pop](itfdocumentmgr-pop.md).<br/>                                                                                                                             |
| <span id="TF_ST_CORRECTION"></span><span id="tf_st_correction"></span><dl> <dt>**TF\_ST\_CORRECTION**</dt> <dt>( 1 )</dt> </dl>                                  | The text is a transform (correction) of existing content, so that other text services can preserve data associated with the original text. Used in *dwFlags* parameter of [ITfRange::SetText](itfrange-settext.md).<br/>                               |
| <span id="TF_TU_CORRECTION"></span><span id="tf_tu_correction"></span><dl> <dt>**TF\_TU\_CORRECTION**</dt> <dt>( 0x1 )</dt> </dl>                                | The text change is the result of a transform (correction) of existing content. This implies that the semantics of the text have not changed. Used in *dwFlags* parameter of [ITfPropertyStore::OnTextUpdated](itfpropertystore-ontextupdated.md).<br/> |
| <span id="TF_US_HIDETIPUI"></span><span id="tf_us_hidetipui"></span><dl> <dt>**TF\_US\_HIDETIPUI**</dt> <dt>0x00000001</dt> </dl>                                | Not used.<br/>                                                                                                                                                                                                                                          |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[ITextStoreACP::GetSelection](itextstoreacp-getselection.md)
</dt> <dt>

[ITextStoreAnchor::GetSelection](itextstoreanchor-getselection.md)
</dt> <dt>

[ITfContext::GetSelection](itfcontext-getselection.md)
</dt> <dt>

[ITfDocumentMgr::Pop](itfdocumentmgr-pop.md)
</dt> <dt>

[ITfEditRecord::GetTextAndPropertyUpdates](itfeditrecord-gettextandpropertyupdates.md)
</dt> <dt>

[ITfPropertyStore::OnTextUpdated](itfpropertystore-ontextupdated.md)
</dt> <dt>

[ITfRange::InsertEmbedded](itfrange-insertembedded.md)
</dt> <dt>

[ITfRange::SetText](itfrange-settext.md)
</dt> <dt>

[TfClientId](tfclientid.md)
</dt> <dt>

[TfGuidAtom](tfguidatom.md)
</dt> <dt>

[TF\_HALTCOND](tf-haltcond.md)
</dt> </dl>

 

 





