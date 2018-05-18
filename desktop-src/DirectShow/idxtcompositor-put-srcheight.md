---
Description: 'The put\_SrcHeight method specifies the height of the source rectangle.'
ms.assetid: '80c8cf92-36e2-4e57-8ce7-6a114bc8bab4'
title: 'IDxtCompositor::put\_SrcHeight method'
---

# IDxtCompositor::put\_SrcHeight method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_SrcHeight` method specifies the height of the source rectangle.

## Syntax


```C++
HRESULT put_SrcHeight(
  [in] long newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

The height of the source rectangle, in pixels.

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

[**IDxtCompositor Interface**](idxtcompositor.md)
</dt> </dl>

 

 




