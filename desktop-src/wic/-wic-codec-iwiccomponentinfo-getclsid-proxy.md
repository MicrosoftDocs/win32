---
description: Proxy function for the GetCLSID method.
ms.assetid: c6a8d752-590f-43d6-bac8-72b5bd259ad0
title: IWICComponentInfo_GetCLSID_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICComponentInfo_GetCLSID_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICComponentInfo\_GetCLSID\_Proxy function

Proxy function for the [**GetCLSID**](/windows/desktop/api/Wincodec/nf-wincodec-iwiccomponentinfo-getclsid) method.

## Syntax


```C++
HRESULT IWICComponentInfo_GetCLSID_Proxy(
  _In_  IWICComponentInfo *THIS_PTR,
  _Out_ CLSID             *pclsid
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICComponentInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwiccomponentinfo)\***

Pointer to this [**IWICComponentInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwiccomponentinfo) object.

</dd> <dt>

*pclsid* \[out\]
</dt> <dd>

Type: **CLSID\***

A pointer that receives the component's CLSID.

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



 

 




