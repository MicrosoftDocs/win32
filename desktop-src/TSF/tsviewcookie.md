---
title: TsViewCookie
description: The TsViewCookie data type identifies a context view.
ms.assetid: e649b799-d0d6-4f2d-b9f1-28070eea9b16
keywords:
- TsViewCookie
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TsViewCookie

The **TsViewCookie** data type identifies a context view.


```C++
typedef DWORD TsViewCookie;
```



## Remarks

An application must supply a unique **TsViewCookie** value for each view it creates.

The TSF manager obtains this value from the application by calling [ITextStoreACP::GetActiveView](/windows/win32/Textstor/nf-textstor-itextstoreacp-getactiveview?branch=master) or [ITextStoreAnchor::GetActiveView](/windows/win32/Textstor/nf-textstor-itextstoreanchor-getactiveview?branch=master). The TSF manager uses this value to identify the view when calling various [ITextStoreACP](/windows/win32/Textstor/nn-textstor-itextstoreacp?branch=master) or [ITextStoreAnchor](/windows/win32/Textstor/nn-textstor-itextstoreanchor?branch=master) methods.

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

[**ITextStoreACP**](/windows/win32/Textstor/nn-textstor-itextstoreacp?branch=master)
</dt> <dt>

[**ITextStoreACP::GetActiveView**](/windows/win32/Textstor/nf-textstor-itextstoreacp-getactiveview?branch=master)
</dt> <dt>

[**ITextStoreAnchor::GetActiveView**](/windows/win32/Textstor/nf-textstor-itextstoreanchor-getactiveview?branch=master)
</dt> </dl>

 

 





