---
Description: The put\_Luminance method specifies the luminance value on which to key. This property applies only when the key type is DXTKEY\_LUMINANCE.
ms.assetid: 3e255423-1724-49fe-b1a1-49bc1d5fa6ae
title: IDxtKey::put\_Luminance method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IDxtKey::put\_Luminance method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_Luminance` method specifies the luminance value on which to key. This property applies only when the key type is DXTKEY\_LUMINANCE.

## Syntax


```C++
HRESULT put_Luminance(
  [in] int newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

The luminance value on which to key. The valid range is from 0 to 100.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IDxtKey Interface**](idxtkey.md)
</dt> <dt>

[**IDxtKey::put\_KeyType**](idxtkey-put-keytype.md)
</dt> </dl>

 

 




