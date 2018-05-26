---
Description: Proxy function for the GetLocation method.
ms.assetid: 2dc4767b-9992-4e5a-a171-2de19178d912
title: IWICMetadataQueryReader\_GetLocation\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICMetadataQueryReader\_GetLocation\_Proxy function

Proxy function for the [**GetLocation**](/windows/win32/Wincodec/nf-wincodec-iwicmetadataqueryreader-getlocation?branch=master) method.

## Syntax


```C++
HRESULT IWICMetadataQueryReader_GetLocation_Proxy(
  _In_    IWICMetadataQueryReader *THIS_PTR,
  _In_    UINT                    cchMaxLength,
  _Inout_ WCHAR                   *wzNamespace,
  _Out_   UINT                    *pcchActualLength
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master)\***

Pointer to this [**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master) object.

</dd> <dt>

*cchMaxLength* \[in\]
</dt> <dd>

Type: **UINT**

The length of the *wzNamespace* buffer.

</dd> <dt>

*wzNamespace* \[in, out\]
</dt> <dd>

Type: **WCHAR\***

Pointer that receives the current namespace location.

</dd> <dt>

*pcchActualLength* \[out\]
</dt> <dd>

Type: **UINT\***

The actual buffer length needed to retrieve the current namespace location.

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



 

 




