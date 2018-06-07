---
Description: The ExpsCompressionOptions enumeration describes compression options for an XPS part.
ms.assetid: 7df53803-4e01-4d00-b7a4-2f2d1dde5ad8
title: EXpsCompressionOptions enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# EXpsCompressionOptions enumeration

The ExpsCompressionOptions enumeration describes compression options for an XPS part.

## Syntax


```C++
typedef enum  { 
  Compression_NotCompressed,
  Compression_Normal,
  Compression_Small,
  Compression_Fast
} EXpsCompressionOptions;
```



## Constants

<dl> <dt>

<span id="Compression_NotCompressed"></span><span id="compression_notcompressed"></span><span id="COMPRESSION_NOTCOMPRESSED"></span>**Compression\_NotCompressed**
</dt> <dd>

The part is not compressed.

</dd> <dt>

<span id="Compression_Normal"></span><span id="compression_normal"></span><span id="COMPRESSION_NORMAL"></span>**Compression\_Normal**
</dt> <dd>

The part is compressed normally.

</dd> <dt>

<span id="Compression_Small"></span><span id="compression_small"></span><span id="COMPRESSION_SMALL"></span>**Compression\_Small**
</dt> <dd>

The compression for the part is optimized for size.

</dd> <dt>

<span id="Compression_Fast"></span><span id="compression_fast"></span><span id="COMPRESSION_FAST"></span>**Compression\_Fast**
</dt> <dd>

The compression for the part is optimized for speed.

</dd> </dl>

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |
| IDL<br/>    | <dl> <dt>Filterpipeline.idl</dt> </dl>                          |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EXpsCompressionOptions%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




