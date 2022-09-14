---
title: TsViewCookie (Textstor.h)
description: The TsViewCookie data type identifies a context view.
ms.assetid: e649b799-d0d6-4f2d-b9f1-28070eea9b16
keywords:
- TsViewCookie
ms.topic: reference
ms.date: 05/31/2018
---

# TsViewCookie

The **TsViewCookie** data type identifies a context view.


```C++
typedef DWORD TsViewCookie;
```



## Remarks

An application must supply a unique **TsViewCookie** value for each view it creates.

The TSF manager obtains this value from the application by calling [ITextStoreACP::GetActiveView](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-getactiveview) or [ITextStoreAnchor::GetActiveView](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-getactiveview). The TSF manager uses this value to identify the view when calling various [ITextStoreACP](/windows/desktop/api/Textstor/nn-textstor-itextstoreacp) or [ITextStoreAnchor](/windows/desktop/api/Textstor/nn-textstor-itextstoreanchor) methods.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                             |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                         |
| Header<br/>                   | <dl> <dt>Textstor.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Textstor.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITextStoreACP**](/windows/desktop/api/Textstor/nn-textstor-itextstoreacp)
</dt> <dt>

[**ITextStoreACP::GetActiveView**](/windows/desktop/api/Textstor/nf-textstor-itextstoreacp-getactiveview)
</dt> <dt>

[**ITextStoreAnchor::GetActiveView**](/windows/desktop/api/Textstor/nf-textstor-itextstoreanchor-getactiveview)
</dt> </dl>

 

 





