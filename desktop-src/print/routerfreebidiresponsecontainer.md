---
Description: RouterFreeBidiResponseContainer frees a BIDI\_RESPONSE\_CONTAINER structure previously allocated by RouterAllocBidiResponseContainer.
ms.assetid: 3998eed5-398e-4835-b917-54f5ae814ddf
title: RouterFreeBidiResponseContainer function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RouterFreeBidiResponseContainer function

`RouterFreeBidiResponseContainer` frees a [**BIDI\_RESPONSE\_CONTAINER**](bidi-response-container.md) structure previously allocated by [**RouterAllocBidiResponseContainer**](routerallocbidiresponsecontainer.md).

## Syntax


```C++
DWORD RouterFreeBidiResponseContainer(
  _In_ PBIDI_RESPONSE_CONTAINER pData
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to the BIDI\_RESPONSE\_CONTAINER structure to be freed.

</dd> </dl>

## Return value

`RouterFreeBidiResponseContainer` normally returns ERROR\_SUCCESS, unless it throws an exception. In that case it returns an appropriate error code.

## Remarks

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Version<br/>         | This function is available in Windows XP and later operating systems.<br/>                         |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>WinSpool.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>WinSpool.drv</dt> </dl>                  |



## See also

<dl> <dt>

[**BIDI\_RESPONSE\_CONTAINER**](bidi-response-container.md)
</dt> <dt>

[**RouterAllocBidiResponseContainer**](routerallocbidiresponsecontainer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RouterFreeBidiResponseContainer%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





