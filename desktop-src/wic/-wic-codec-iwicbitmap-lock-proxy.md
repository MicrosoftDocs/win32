---
Description: Proxy function for the Lock method.
ms.assetid: c9d67b35-092b-4f0b-a292-879576a046bf
title: IWICBitmap\_Lock\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICBitmap\_Lock\_Proxy function

Proxy function for the [**Lock**](/windows/win32/Wincodec/nf-wincodec-iwicbitmap-lock?branch=master) method.

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

Type: **[**IWICBitmap**](/windows/win32/Wincodec/nn-wincodec-iwicbitmap?branch=master)\***

Pointer to this [**IWICBitmap**](/windows/win32/Wincodec/nn-wincodec-iwicbitmap?branch=master) object.

</dd> <dt>

*prcLock* \[in\]
</dt> <dd>

Type: **const [**WICRect**](/windows/win32/Wincodec/ns-wincodec-wicrect?branch=master)\***

The rectangle to be accessed.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Type: **DWORD**

The access mode you wish to obtain for the lock.

</dd> <dt>

*ppILock* \[out\]
</dt> <dd>

Type: **[**IWICBitmapLock**](/windows/win32/Wincodec/nn-wincodec-iwicbitmaplock?branch=master)\*\***

A pointer that receives the locked memory location.

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



 

 




