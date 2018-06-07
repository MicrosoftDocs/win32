---
Description: The Seek method changes the seek pointer to a new location in the stream.
ms.assetid: b563e080-32ab-47b7-94f4-1d3dd19f3311
title: IPrintReadStream::Seek method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintReadStream::Seek method

The `Seek` method changes the seek pointer to a new location in the stream.

## Syntax


```C++
HRESULT Seek(
  [in]  LONGLONG  dlibMove,
  [in]  DWORD     dwOrigin,
  [out] ULONGLONG *plibNewPosition
);
```



## Parameters

<dl> <dt>

*dlibMove* \[in\]
</dt> <dd>

The displacement that is added to the location that *dwOrigin* specifies.

</dd> <dt>

*dwOrigin* \[in\]
</dt> <dd>

The origin for the displacement that *dlibMove* specifies. The origin can be the beginning of the file (STREAM\_SEEK\_SET), the current seek pointer (STREAM\_SEEK\_CUR), or the end of the file (STREAM\_SEEK\_END).

</dd> <dt>

*plibNewPosition* \[out\]
</dt> <dd>

A pointer to the location where `Seek` writes the value of the new seek pointer from the beginning of the stream.

</dd> </dl>

## Return value

`Seek` returns an **HRESULT** value.

## Remarks

The `Seek` method might block, for example, if seeking to the end of the stream.

This method is similar to the **IStream::Seek** and **SetFilePointerEx** methods. For more information about these methods, see the Microsoft Windows SDK documentation.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintReadStream::Seek%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




