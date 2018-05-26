---
title: TS\_ATTRID
description: The TS\_ATTRID data type is used to identify a text attribute.
ms.assetid: 5e375609-3d3c-4c12-ae05-dcaa70779162
keywords:
- TS_ATTRID
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                             |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                         |
| Header<br/>                   | <dl> <dt>Textstor.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Textstor.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITextStoreACP::FindNextAttrTransition**](/windows/win32/Textstor/nf-textstor-itextstoreacp-findnextattrtransition?branch=master)
</dt> <dt>

[**ITextStoreACP::RequestAttrsAtPosition**](/windows/win32/Textstor/nf-textstor-itextstoreacp-requestattrsatposition?branch=master)
</dt> <dt>

[**ITextStoreACP::RequestAttrsTransitioningAtPosition**](/windows/win32/Textstor/nf-textstor-itextstoreacp-requestattrstransitioningatposition?branch=master)
</dt> <dt>

[**ITextStoreACP::RequestSupportedAttrs**](/windows/win32/Textstor/nf-textstor-itextstoreacp-requestsupportedattrs?branch=master)
</dt> <dt>

[**ITextStoreACPSink::OnAttrsChange**](/windows/win32/Textstor/nf-textstor-itextstoreacpsink-onattrschange?branch=master)
</dt> <dt>

[**ITextStoreAnchor::FindNextAttrTransition**](/windows/win32/Textstor/nf-textstor-itextstoreanchor-findnextattrtransition?branch=master)
</dt> <dt>

[**ITextStoreAnchor::RequestAttrsAtPosition**](/windows/win32/Textstor/nf-textstor-itextstoreanchor-requestattrsatposition?branch=master)
</dt> <dt>

[**ITextStoreAnchor::RequestAttrsTransitioningAtPosition**](/windows/win32/Textstor/nf-textstor-itextstoreanchor-requestattrstransitioningatposition?branch=master)
</dt> <dt>

[**ITextStoreAnchor::RequestSupportedAttrs**](/windows/win32/Textstor/nf-textstor-itextstoreanchor-requestsupportedattrs?branch=master)
</dt> <dt>

[**ITextStoreAnchorSink::OnAttrsChange**](/windows/win32/Textstor/nf-textstor-itextstoreanchorsink-onattrschange?branch=master)
</dt> <dt>

[**TS\_ATTRVAL**](/windows/win32/Textstor/ns-textstor-ts_attrval?branch=master)
</dt> </dl>

 

 





