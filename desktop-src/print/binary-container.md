---
Description: The BINARY\_CONTAINER structure is a container for binary data.
ms.assetid: bac960c5-7c29-4550-9b82-5adb6a0cc243
title: BINARY\_CONTAINER structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# BINARY\_CONTAINER structure

The BINARY\_CONTAINER structure is a container for binary data.

## Syntax


```C++
typedef struct _BINARY_CONTAINER {
  DWORD  cbBuf;
  LPBYTE pData;
} BINARY_CONTAINER, *PBINARY_CONTAINER;
```



## Members

<dl> <dt>

**cbBuf**
</dt> <dd>

Specifies the number of bytes of binary data in the **pData** member.

</dd> <dt>

**pData**
</dt> <dd>

Pointer to a buffer that contains the binary data.

</dd> </dl>

## Remarks

The BINARY\_CONTAINER structure is used in a [**BIDI\_DATA**](bidi-data.md) structure when the bidi data consists of binary data, as opposed to integer, float, or string data.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | This structure is available in Windows XP and later operating systems.<br/>                          |
| Header<br/>  | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



## See also

<dl> <dt>

[**BIDI\_DATA**](bidi-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BINARY_CONTAINER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





