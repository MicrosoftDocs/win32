---
description: Proxy function for the GetVersion method.
ms.assetid: b064b065-bc02-4943-b208-ce5e40c12aa2
title: IWICComponentInfo_GetVersion_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICComponentInfo_GetVersion_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICComponentInfo\_GetVersion\_Proxy function

Proxy function for the [**GetVersion**](/windows/desktop/api/Wincodec/nf-wincodec-iwiccomponentinfo-getversion) method.

## Syntax


```C++
HRESULT IWICComponentInfo_GetVersion_Proxy(
  _In_    IWICComponentInfo *THIS_PTR,
  _In_    UINT              cchVersion,
  _Inout_ WCHAR             *wzVersion,
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

*cchVersion* \[in\]
</dt> <dd>

Type: **UINT**

The size of the *wzVersion* buffer.

</dd> <dt>

*wzVersion* \[in, out\]
</dt> <dd>

Type: **WCHAR\***

A pointer that receives a culture invariant string of the component's version.

</dd> <dt>

*pcchActual* \[out\]
</dt> <dd>

Type: **UINT\***

A pointer that receives the actual length of the component's version.

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



 

 




