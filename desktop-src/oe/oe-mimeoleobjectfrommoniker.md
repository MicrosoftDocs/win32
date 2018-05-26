---
title: MimeOleObjectFromMoniker function
description: Do not use. Creates a new message object and loads its state from the supplied moniker.
ms.assetid: b084ab3a-84d4-4bd5-a3bd-38ee145d6ca9
keywords:
- MimeOleObjectFromMoniker function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleObjectFromMoniker
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleObjectFromMoniker function

Do not use. Creates a new message object and loads its state from the supplied moniker.

## Syntax


```C++
HRESULT MimeOleObjectFromMoniker(
  _In_  BINDF    bindf,
  _In_  IMoniker *pmkOriginal,
  _In_  IBindCtx *pBindCtx,
  _In_  REFIID   riid,
  _Out_ LPVOID   *ppvObject,
  _Out_ IMoniker **ppmkNew
);
```



## Parameters

<dl> <dt>

*bindf* \[in\]
</dt> <dd>

Type: **[**BINDF**](https://msdn.microsoft.com/library/ms775130)**

Contains the [**BINDF**](https://msdn.microsoft.com/library/ms775130) value that determines how a resource should be bound to a moniker.

</dd> <dt>

*pmkOriginal* \[in\]
</dt> <dd>

Type: **[**IMoniker**](https://msdn.microsoft.com/library/windows/desktop/ms679705)\***

Pointer to original [**IMoniker**](https://msdn.microsoft.com/library/windows/desktop/ms679705) interface.

</dd> <dt>

*pBindCtx* \[in\]
</dt> <dd>

Type: **[**IBindCtx**](https://msdn.microsoft.com/library/windows/desktop/ms693755)\***

Pointer to the [**IBindCtx**](https://msdn.microsoft.com/library/windows/desktop/ms693755) interface on the bind context object.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies IID of the interface client used to communicate with object that moniker identifies.

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Type: **LPVOID\***

Receives address of a pointer to specified interface.

</dd> <dt>

*ppmkNew* \[out\]
</dt> <dd>

Type: **[**IMoniker**](https://msdn.microsoft.com/library/windows/desktop/ms679705)\*\***

Receives address of new [**IMoniker**](https://msdn.microsoft.com/library/windows/desktop/ms679705) pointer variable.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> Not applicable to Macintosh.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





