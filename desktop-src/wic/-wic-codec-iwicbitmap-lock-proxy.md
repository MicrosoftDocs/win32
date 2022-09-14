---
description: Proxy function for the Lock method.
ms.assetid: c9d67b35-092b-4f0b-a292-879576a046bf
title: IWICBitmap_Lock_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICBitmap_Lock_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICBitmap\_Lock\_Proxy function

Proxy function for the [**Lock**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmap-lock) method.

## Syntax


```C++
HRESULT IWICBitmap_Lock_Proxy(
  _In_        IWICBitmap     *THIS_PTR,
  _In_  const WICRect        *prcLock,
  _In_        DWORD          flags,
  _Out_       IWICBitmapLock **ppILock
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmap**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmap)\***

Pointer to this [**IWICBitmap**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmap) object.

</dd> <dt>

*prcLock* \[in\]
</dt> <dd>

Type: **const [**WICRect**](/windows/desktop/api/Wincodec/ns-wincodec-wicrect)\***

The rectangle to be accessed.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Type: **DWORD**

The access mode you wish to obtain for the lock.

</dd> <dt>

*ppILock* \[out\]
</dt> <dd>

Type: **[**IWICBitmapLock**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmaplock)\*\***

A pointer that receives the locked memory location.

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



 

 




