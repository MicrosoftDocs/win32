---
Description: Proxy function for creating the IWICImagingFactory.
ms.assetid: e4f575b0-878f-461e-92e7-9494e505ea6f
title: WICCreateImagingFactory\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WICCreateImagingFactory\_Proxy function

Proxy function for creating the [**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master).

## Syntax


```C++
HRESULT WICCreateImagingFactory_Proxy(
  _In_  UINT               SDKVersion,
  _Out_ IWICImagingFactory **ppIImagingFactory
);
```



## Parameters

<dl> <dt>

*SDKVersion* \[in\]
</dt> <dd>

Type: **UINT**

</dd> <dt>

*ppIImagingFactory* \[out\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/win32/Wincodec/nn-wincodec-iwicimagingfactory?branch=master)\*\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




