---
title: TS\_ATTRID
description: The TS\_ATTRID data type is used to identify a text attribute.
ms.assetid: '5e375609-3d3c-4c12-ae05-dcaa70779162'
keywords: ["TS_ATTRID"]
---

# TS\_ATTRID

The **TS\_ATTRID** data type is used to identify a text attribute.


```C++
typedef GUID TS_ATTRID;
```



## Remarks

A list of predefined GUIDs for TS\_ATTRID is in tsattrs.h.

The GUIDs TSATTRID\_Text\_VerticalWriting and TSATTRID\_Text\_Orientation are useful for applications to match input text that is to be corrected. Additional user-defined GUIDs can be created.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                             |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                         |
| Header<br/>                   | <dl> <dt>Textstor.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Textstor.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITextStoreACP::FindNextAttrTransition**](itextstoreacp-findnextattrtransition.md)
</dt> <dt>

[**ITextStoreACP::RequestAttrsAtPosition**](itextstoreacp-requestattrsatposition.md)
</dt> <dt>

[**ITextStoreACP::RequestAttrsTransitioningAtPosition**](itextstoreacp-requestattrstransitioningatposition.md)
</dt> <dt>

[**ITextStoreACP::RequestSupportedAttrs**](itextstoreacp-requestsupportedattrs.md)
</dt> <dt>

[**ITextStoreACPSink::OnAttrsChange**](itextstoreacpsink-onattrschange.md)
</dt> <dt>

[**ITextStoreAnchor::FindNextAttrTransition**](itextstoreanchor-findnextattrtransition.md)
</dt> <dt>

[**ITextStoreAnchor::RequestAttrsAtPosition**](itextstoreanchor-requestattrsatposition.md)
</dt> <dt>

[**ITextStoreAnchor::RequestAttrsTransitioningAtPosition**](itextstoreanchor-requestattrstransitioningatposition.md)
</dt> <dt>

[**ITextStoreAnchor::RequestSupportedAttrs**](itextstoreanchor-requestsupportedattrs.md)
</dt> <dt>

[**ITextStoreAnchorSink::OnAttrsChange**](itextstoreanchorsink-onattrschange.md)
</dt> <dt>

[**TS\_ATTRVAL**](ts-attrval.md)
</dt> </dl>

 

 





