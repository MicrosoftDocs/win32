---
Description: RouterAllocBidiMem allocates a block of memory of a specified size. This function is used by the port monitor to allocate memory for strings and binary objects.
ms.assetid: 39042c66-3db1-41bd-b06d-12aefcb007d3
title: RouterAllocBidiMem function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RouterAllocBidiMem function

`RouterAllocBidiMem` allocates a block of memory of a specified size. This function is used by the port monitor to allocate memory for strings and binary objects.

## Syntax


```C++
PVOID RouterAllocBidiMem(
  _In_ size_t NumBytes
);
```



## Parameters

<dl> <dt>

*NumBytes* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the block of memory to be allocated.

</dd> </dl>

## Return value

`RouterAllocBidiMem` returns a pointer to the block of memory if successful. If the function fails, the caller can obtain the error code by calling **GetLastError** (described in the Microsoft Windows SDK documentation).

## Remarks

When the memory allocated by this function is no longer needed, it can be returned by a call to [**RouterFreeBidiMem**](routerfreebidimem.md).

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

[**RouterFreeBidiMem**](routerfreebidimem.md)
</dt> <dt>

[**SendRecvBidiDataFromPort**](print.sendrecvbididatafromport)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RouterAllocBidiMem%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





