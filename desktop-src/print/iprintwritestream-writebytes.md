---
Description: 'The WriteBytes method writes a specified number of bytes to a stream.'
ms.assetid: 'd47c836e-a291-4cc2-9688-82526f8bfb8b'
title: 'IPrintWriteStream::WriteBytes method'
---

# IPrintWriteStream::WriteBytes method

The `WriteBytes` method writes a specified number of bytes to a stream.

## Syntax


```C++
HRESULT WriteBytes(
  [in]  void  pvBuffer,
  [in]  ULONG cbBuffer,
  [out] ULONG *pcbWritten
);
```



## Parameters

<dl> <dt>

*pvBuffer* \[in\]
</dt> <dd>

A pointer to the buffer that the bytes will be written from.

</dd> <dt>

*cbBuffer* \[in\]
</dt> <dd>

The size of the buffer to be read from.

</dd> <dt>

*pcbWritten* \[out\]
</dt> <dd>

A pointer to the number of bytes actually written.

</dd> </dl>

## Return value

`WriteBytes` returns an **HRESULT** value.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintWriteStream::WriteBytes%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




