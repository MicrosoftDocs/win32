---
title: TF\_IAS\_\ Constants
description: The TF\_IAS\_\ constants are used as bitfield flags in methods that insert text or embedded objects at a selection or insertion point.
ms.assetid: adc5c539-fdb1-4829-ad17-2f54ec179c47
topic_type:
- apiref
api_name:
- TF_IAS_NOQUERY
- TF_IAS_QUERYONLY
- TF_IAS_NO_DEFAULT_COMPOSITION
api_location:
- Msctf.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TF\_IAS\_\* Constants

The TF\_IAS\_\* constants are used as bitfield flags in methods that insert text or embedded objects at a selection or insertion point.



| Constant/value                                                                                                                                                                                                                                                                       | Description                                                                                                                                |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TF_IAS_NOQUERY"></span><span id="tf_ias_noquery"></span><dl> <dt>**TF\_IAS\_NOQUERY**</dt> <dt>( 0x1 )</dt> </dl>                                                       | Text is inserted and the range pointer is set to **NULL** upon exit. Cannot be combined with the TF\_IAS\_QUERYONLY flag.<br/>       |
| <span id="TF_IAS_QUERYONLY"></span><span id="tf_ias_queryonly"></span><dl> <dt>**TF\_IAS\_QUERYONLY**</dt> <dt>( 0x2 )</dt> </dl>                                                 | Do not perform the insert. Caller only requires the range pointer to be set. Cannot be combined with the TF\_IAS\_NOQUERY flag.<br/> |
| <span id="TF_IAS_NO_DEFAULT_COMPOSITION"></span><span id="tf_ias_no_default_composition"></span><dl> <dt>**TF\_IAS\_NO\_DEFAULT\_COMPOSITION**</dt> <dt>( 0x80000000 )</dt> </dl> | TSF will not create a default composition if a composition is required. Caller must start a composition over the range.<br/>         |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[ITextStoreACP::InsertEmbeddedAtSelection](/windows/win32/Textstor/nf-textstor-itextstoreacp-insertembeddedatselection?branch=master)
</dt> <dt>

[ITextStoreACP::InsertTextAtSelection](/windows/win32/Textstor/nf-textstor-itextstoreacp-inserttextatselection?branch=master)
</dt> <dt>

[ITextStoreAnchor::InsertEmbeddedAtSelection](/windows/win32/Textstor/nf-textstor-itextstoreanchor-insertembeddedatselection?branch=master)
</dt> <dt>

[ITextStoreAnchor::InsertTextAtSelection](/windows/win32/Textstor/nf-textstor-itextstoreanchor-inserttextatselection?branch=master)
</dt> <dt>

[ITfInsertAtSelection::InsertEmbeddedAtSelection](/windows/win32/Msctf/nf-msctf-itfinsertatselection-insertembeddedatselection?branch=master)
</dt> <dt>

[ITfInsertAtSelection::InsertTextAtSelection](/windows/win32/Msctf/nf-msctf-itfinsertatselection-inserttextatselection?branch=master)
</dt> </dl>

 

 





