---
title: IMimeObjResolver MimeOleObjectFromMoniker method
description: See MimeOleObjectFromMoniker.
ms.assetid: '31149734-dfa8-4060-9354-25bc7911775d'
keywords: ["MimeOleObjectFromMoniker method Windows Mail (formerly Outlook Express)", "MimeOleObjectFromMoniker method Windows Mail (formerly Outlook Express) , IMimeObjResolver interface", "IMimeObjResolver interface Windows Mail (formerly Outlook Express) , MimeOleObjectFromMoniker method"]
topic_type:
- apiref
api_name:
- IMimeObjResolver.MimeOleObjectFromMoniker
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeObjResolver::MimeOleObjectFromMoniker method

\[**IMimeObjResolver::MimeOleObjectFromMoniker** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

See [**MimeOleObjectFromMoniker**](oe-mimeoleobjectfrommoniker.md).

## Syntax


```C++
HRESULT MimeOleObjectFromMoniker(
  [in]  BINDF    bindf,
  [in]  IMoniker *pmkOriginal,
  [in]  IBindCtx *pBindCtx,
  [in]  REFIID   riid,
  [out] LPVOID   *ppvObject,
  [out] IMoniker **ppmkNew
);
```



## Parameters

<dl> <dt>

*bindf* \[in\]
</dt> <dd>

Type: **[**BINDF**](https://msdn.microsoft.com/library/ms775130)**

Contains the values that determine how a resource should be bound to a moniker.

</dd> <dt>

*pmkOriginal* \[in\]
</dt> <dd>

Type: **[IMoniker](http://msdn.microsoft.com/library/com/htm/cmi_m_8otu.asp)\***

Pointer to the original [IMoniker](http://msdn.microsoft.com/library/com/htm/cmi_m_8otu.asp) interface.

</dd> <dt>

*pBindCtx* \[in\]
</dt> <dd>

Type: **[IBindCtx](http://msdn.microsoft.com/library/com/htm/cmi_a2b_06bc.asp)\***

Pointer to the [IBindCtx](http://msdn.microsoft.com/library/com/htm/cmi_a2b_06bc.asp) interface on the bind context object.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies the IID of the interface the client wishes to use to communicate with the object that the moniker identifies.

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Type: **LPVOID\***

Receives the address of a pointer to the specified interface.

</dd> <dt>

*ppmkNew* \[out\]
</dt> <dd>

Type: **[IMoniker](http://msdn.microsoft.com/library/com/htm/cmi_m_8otu.asp)\*\***

Specifies address of new [IMoniker](http://msdn.microsoft.com/library/com/htm/cmi_m_8otu.asp) pointer variable.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





