---
Description: RouterAllocBidiResponseContainer allocates a BIDI\_RESPONSE\_CONTAINER structure containing a list of bidi responses. The bidi response list is an array of BIDI\_RESPONSE\_DATA structures.
ms.assetid: ca10f0d5-62d6-451a-96e5-38aca18cf5b0
title: RouterAllocBidiResponseContainer function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RouterAllocBidiResponseContainer function

`RouterAllocBidiResponseContainer` allocates a [**BIDI\_RESPONSE\_CONTAINER**](bidi-response-container.md) structure containing a list of bidi responses. The bidi response list is an array of [**BIDI\_RESPONSE\_DATA**](bidi-response-data.md) structures.

## Syntax


```C++
PBIDI_RESPONSE_CONTAINER RouterAllocBidiResponseContainer(
  _In_ DWORD cSize
);
```



## Parameters

<dl> <dt>

*cSize* \[in\]
</dt> <dd>

Specifies the number of BIDI\_RESPONSE\_DATA structures to be allocated.

</dd> </dl>

## Return value

`RouterAllocBidiResponseContainer` returns a pointer to the allocated structure, on success. If the function fails to allocate the structure, the caller can obtain the error code from **GetLastError** (described in the Microsoft Windows SDK documentation).

## Remarks

When the memory allocated by this function is no longer needed, use [**RouterFreeBidiResponseContainer**](routerfreebidiresponsecontainer.md).

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Version<br/>         | This function is available in Windows XP and later operating systems.<br/>                         |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**BIDI\_RESPONSE\_DATA**](bidi-response-data.md)
</dt> <dt>

[**BIDI\_RESPONSE\_CONTAINER**](bidi-response-container.md)
</dt> <dt>

[**RouterFreeBidiResponseContainer**](routerfreebidiresponsecontainer.md)
</dt> <dt>

[**SendRecvBidiDataFromPort**](https://www.bing.com/search?q=**SendRecvBidiDataFromPort**)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RouterAllocBidiResponseContainer%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





