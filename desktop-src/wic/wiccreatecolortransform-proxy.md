---
description: Creates an color transform object that implements IWICColorTransform. This COM object supports the free-threaded object model.
ms.assetid: 43DCC3FB-B687-45F0-AAC6-DED76214716C
title: WICCreateColorTransform_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WICCreateColorTransform_Proxy
api_type: 
- DllExport
api_location: 
- WindowsCodecsExt.dll
---

# WICCreateColorTransform\_Proxy function

Creates an color transform object that implements [**IWICColorTransform**](/windows/win32/api/wincodec/nn-wincodec-iwiccolortransform). This COM object supports the free-threaded object model.

## Syntax


```C++
HRESULT WINAPI WICCreateColorTransform_Proxy(
  _Out_  **ppIColorTransform
);
```



## Parameters

<dl> <dt>

*ppIColorTransform* \[out\]
</dt> <dd>

The color transform created.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>WindowsCodecsExt.dll</dt> </dl> |



 

 
