---
title: TS\_ATTR\_\ Constants
description: The TS\_ATTR\_\ constants are used to obtain and change the values of document attributes. These constants form possible values of bitfield flags in ITextStoreACP and ITextStoreAnchor methods.
ms.assetid: 'e99a44ba-c41a-4dd7-9475-dd37159081fd'
topic_type:
- apiref
api_name:
- TS_ATTR_FIND_BACKWARDS
- TS_ATTR_FIND_WANT_OFFSET
- TS_ATTR_FIND_UPDATESTART
- TS_ATTR_FIND_WANT_VALUE
- TS_ATTR_FIND_WANT_END
- TS_ATTR_FIND_HIDDEN
api_location:
- Textstor.h
api_type:
- HeaderDef
---

# TS\_ATTR\_\* Constants

The TS\_ATTR\_\* constants are used to obtain and change the values of document attributes. These constants form possible values of bitfield flags in [ITextStoreACP](itextstoreacp.md) and [ITextStoreAnchor](itextstoreanchor.md) methods.



| Constant/value                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                        |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TS_ATTR_FIND_BACKWARDS"></span><span id="ts_attr_find_backwards"></span><dl> <dt>**TS\_ATTR\_FIND\_BACKWARDS**</dt> <dt>( 0x1 )</dt> </dl>        | Search backward from the start character or anchor position for the position where a transition occurs in a document attribute value. The default is search forward.<br/>                                                                                                                                                                                    |
| <span id="TS_ATTR_FIND_WANT_OFFSET"></span><span id="ts_attr_find_want_offset"></span><dl> <dt>**TS\_ATTR\_FIND\_WANT\_OFFSET**</dt> <dt>( 0x2 )</dt> </dl> | Return the number of characters between the start character or anchor position (**acpStart** in [ITextStoreACP::FindNextAttrTransition](itextstoreacp-findnextattrtransition.md) or **paStart** in [ITextStoreAnchor::FindNextAttrTransition](itextstoreanchor-findnextattrtransition.md) ) and the position at which an attribute transition occurs.<br/> |
| <span id="TS_ATTR_FIND_UPDATESTART"></span><span id="ts_attr_find_updatestart"></span><dl> <dt>**TS\_ATTR\_FIND\_UPDATESTART**</dt> <dt>( 0x4 )</dt> </dl>  | Used by [ITextStoreAnchor::FindNextAttrTransition](itextstoreanchor-findnextattrtransition.md) to position the input anchor at the next attribute transition, if one is found. Otherwise the input anchor is not modified.<br/>                                                                                                                             |
| <span id="TS_ATTR_FIND_WANT_VALUE"></span><span id="ts_attr_find_want_value"></span><dl> <dt>**TS\_ATTR\_FIND\_WANT\_VALUE**</dt> <dt>( 0x8 )</dt> </dl>    | Load supported document attribute values into the [TS\_ATTRVAL](ts-attrval.md) structure.<br/>                                                                                                                                                                                                                                                              |
| <span id="TS_ATTR_FIND_WANT_END"></span><span id="ts_attr_find_want_end"></span><dl> <dt>**TS\_ATTR\_FIND\_WANT\_END**</dt> <dt>( 0x10 )</dt> </dl>         | Used by [ITextStoreACP::RequestAttrsTransitioningAtPosition](itextstoreacp-requestattrstransitioningatposition.md) and [ITextStoreAnchor::RequestAttrsTransitioningAtPosition](itextstoreanchor-requestattrstransitioningatposition.md) to obtain the document attribute values that end at the specified character or anchor position.<br/>               |
| <span id="TS_ATTR_FIND_HIDDEN"></span><span id="ts_attr_find_hidden"></span><dl> <dt>**TS\_ATTR\_FIND\_HIDDEN**</dt> <dt>( 0x20 )</dt> </dl>                | Reserved.<br/>                                                                                                                                                                                                                                                                                                                                               |



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                         |
| Header<br/>                   | <dl> <dt>Textstor.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Textstor.idl</dt> </dl> |



## See also

<dl> <dt>

[TS\_ATTRID](ts-attrid.md)
</dt> <dt>

[TS\_ATTRVAL](ts-attrval.md)
</dt> <dt>

[ITextStoreACP::FindNextAttrTransition](itextstoreacp-findnextattrtransition.md)
</dt> <dt>

[ITextStoreACP::RequestAttrsTransitioningAtPosition](itextstoreacp-requestattrstransitioningatposition.md)
</dt> <dt>

[ITextStoreAnchor::FindNextAttrTransition](itextstoreanchor-findnextattrtransition.md)
</dt> <dt>

[ITextStoreAnchor::RequestAttrsTransitioningAtPosition](itextstoreanchor-requestattrstransitioningatposition.md)
</dt> </dl>

 

 





