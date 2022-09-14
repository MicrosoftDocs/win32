---
description: Proxy function for the InitializeFromIStream method.
ms.assetid: 3ab780bb-7fe7-4abe-9ea7-86f54ea15d91
title: IWICStream_InitializeFromIStream_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICStream_InitializeFromIStream_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICStream\_InitializeFromIStream\_Proxy function

Proxy function for the [**InitializeFromIStream**](/windows/desktop/api/Wincodec/nf-wincodec-iwicstream-initializefromistream) method.

## Syntax


```C++
HRESULT IWICStream_InitializeFromIStream_Proxy(
  _In_ IWICStream *THIS_PTR,
  _In_ IStream    *pIStream
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICStream**](/windows/desktop/api/Wincodec/nn-wincodec-iwicstream)\***

Pointer to this [**IWICStream**](/windows/desktop/api/Wincodec/nn-wincodec-iwicstream) object.

</dd> <dt>

*pIStream* \[in\]
</dt> <dd>

Type: **[IStream](/windows/desktop/api/objidl/nn-objidl-istream)\***

The initialize stream.

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



 

