---
Description: Sets the seek pointer.
ms.assetid: 82080353-2252-4BF2-B7F4-F297DCA99FA0
title: IPrinterScriptableStream::Seek method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrinterScriptableStream::Seek method

Sets the seek pointer.

## Syntax


```C++
HRESULT Seek(
  [in]          LONG        lOffset,
  [in]          STREAM_SEEK streamSeek,
  [out, retval] LONG        *plPosition
);
```



## Parameters

<dl> <dt>

*lOffset* \[in\]
</dt> <dd>

The displacement to be added to the location indicated by the *streamSeek* parameter.

</dd> <dt>

*streamSeek* \[in\]
</dt> <dd>

The origin for the displacement specified *lOffset*.

</dd> <dt>

*plPosition* \[out, retval\]
</dt> <dd>

The new pointer position.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterScriptableStream**](iprinterscriptablestream.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptableStream::Seek%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





