---
Description: 'Gets a pointer to an IPrinterExtensionContext object.'
ms.assetid: '5E3DC6C7-E370-4120-81B7-2093812AD009'
title: 'IPrinterExtensionContextCollection::GetAt method'
---

# IPrinterExtensionContextCollection::GetAt method

Gets a pointer to an [**IPrinterExtensionContext**](iprinterextensioncontext-interface.md) object.

## Syntax


```C++
HRESULT GetAt(
  [in]          ULONG                    ulIndex,
  [out, retval] IPrinterExtensionContext **ppContext
);
```



## Parameters

<dl> <dt>

*ulIndex* \[in\]
</dt> <dd>

The index of the [**IPrinterExtensionContext**](iprinterextensioncontext-interface.md) object within the collection.

</dd> <dt>

*ppContext* \[out, retval\]
</dt> <dd>

Pointer to an [**IPrinterExtensionContext**](iprinterextensioncontext-interface.md) interface.

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

[**IPrinterExtensionContext**](iprinterextensioncontext-interface.md)
</dt> <dt>

[**IPrinterExtensionContextCollection**](iprinterextensioncontextcollection.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterExtensionContextCollection::GetAt%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





