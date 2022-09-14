---
description: Proxy function for the GetAuthor method.
ms.assetid: fb76009e-cc01-4dec-9403-04bf6b53db80
title: IWICComponentInfo_GetAuthor_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICComponentInfo_GetAuthor_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICComponentInfo\_GetAuthor\_Proxy function

Proxy function for the [**GetAuthor**](/windows/desktop/api/Wincodec/nf-wincodec-iwiccomponentinfo-getauthor) method.

## Syntax


```C++
HRESULT IWICComponentInfo_GetAuthor_Proxy(
  _In_    IWICComponentInfo *THIS_PTR,
  _In_    UINT              cchAuthor,
  _Inout_ WCHAR             *wzAuthor,
  _Out_   UINT              *pcchActual
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICComponentInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwiccomponentinfo)\***

Pointer to this [**IWICComponentInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwiccomponentinfo) object.

</dd> <dt>

*cchAuthor* \[in\]
</dt> <dd>

Type: **UINT**

The size of the *wzAuthor* buffer.

</dd> <dt>

*wzAuthor* \[in, out\]
</dt> <dd>

Type: **WCHAR\***

A pointer that receives the name of the component's author.

The string returned is locale specific, 1033 by default.

</dd> <dt>

*pcchActual* \[out\]
</dt> <dd>

Type: **UINT\***

A pointer that receives the actual length of the component's authors name.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




