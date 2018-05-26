---
Description: The FlushData method flushes buffered data to a data stream while leaving the stream open, allowing the caller to write additional data to the stream.
ms.assetid: F0E31AA1-47BD-4294-89BA-27B02FC8125B
title: IPrintWriteStreamFlushFlushData method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintWriteStreamFlush::FlushData method

The FlushData method flushes buffered data to a data stream while leaving the stream open, allowing the caller to write additional data to the stream.Writing to the stream is done using the [**IPrintWriteStream::WriteBytes**](iprintwritestream-writebytes.md) method.

## Syntax


```C++
HRESULT FlushData(
    None
);
```



## Parameters

<dl> <dt>

*None* 
</dt> <dd>

None

</dd> </dl>

## Return value

The FlushData method returns an HRESULT value.

## Remarks

Only the last filter in the print filter pipeline benefits from the flush. The data is flushed to the port monitor. However, the port monitor has the option of using buffers.

## Examples

The following code snippet shows how to flush data to a data stream. Note that error checking has been omitted for clarity.


```
// Flushing data to a data stream
// ------------------------------
// Declare a pointer to an IPrintWriteStreamFlush interface
IPrintWriteStreamFlush *pIFlush;

// Retireve a pointer to an IPrintWriteStream interface 
// by using the RequestWriter() method in InitializeFilter()
IPrintWriteStream      *pIWrite;

HRESULT hr = pIWrite->QueryInterface(IID_IPrintWriteStreamFlush, reinterpret_cast<void **>(&amp;pIFlush));

hr = pIWrite->WriteBytes(buf, cb, &amp;cbWritten);

hr = pIFlush->FlushData();
```



## Requirements



|                            |                                                                                             |
|----------------------------|---------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>          |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintWriteStreamFlush**](iprintwritestreamflush.md)
</dt> <dt>

[**IPrintWriteStream::WriteBytes**](iprintwritestream-writebytes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintWriteStreamFlush::FlushData%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





