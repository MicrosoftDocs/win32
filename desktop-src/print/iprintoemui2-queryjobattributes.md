---
Description: The IPrintOemUI2::QueryJobAttributes method allows a UI plug-in to postprocess the core driver's results after a call to the DrvQueryJobAttributes DDI.
ms.assetid: cb510aa6-7156-4b02-bab1-6951becbc1a0
title: IPrintOemUI2::QueryJobAttributes method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI2::QueryJobAttributes method

The `IPrintOemUI2::QueryJobAttributes` method allows a UI plug-in to postprocess the core driver's results after a call to the [**DrvQueryJobAttributes**](drvqueryjobattributes.md) DDI. The plug-in can choose to overwrite the values that the core driver placed in the *lpAttributeInfo* output buffer.

## Syntax


```C++
HRESULT QueryJobAttributes(
   HANDLE   hPrinter,
   PDEVMODE pDevmode,
   DWORD    dwLevel,
   LPBYTE   lpAttributeInfo
);
```



## Parameters

<dl> <dt>

*hPrinter* 
</dt> <dd>

Specifies the caller-supplied printer handle.

</dd> <dt>

*pDevmode* 
</dt> <dd>

Pointer to a caller-supplied [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure.

</dd> <dt>

*dwLevel* 
</dt> <dd>

Specifies a caller-supplied value indicating the type of structure pointed to by *lpAttributeInfo*, as indicated in the following table.



| Value        | Structure Pointed to by *lpAttributeInfo*                 |
|--------------|-----------------------------------------------------------|
| 1<br/> | [**ATTRIBUTE\_INFO\_1**](attribute-info-1.md)<br/> |
| 2<br/> | [**ATTRIBUTE\_INFO\_2**](attribute-info-2.md)<br/> |
| 3<br/> | [**ATTRIBUTE\_INFO\_3**](attribute-info-3.md)<br/> |
| 4<br/> | [**ATTRIBUTE\_INFO\_4**](attribute-info-4.md)<br/> |



 

<dl> <dd>

Note that if this method changes any dwDrv*Xxx* member of the ATTRIBUTE\_INFO\_*N* structures, the spooler assumes that the plug-in is able to support the behavior represented by that member.

</dd> </dl> </dd> <dt>

*lpAttributeInfo* 
</dt> <dd>

Pointer to a memory location that receives the address of a structure of the type identified by *dwLevel*.

</dd> </dl>

## Return value

If the UI plug-in supports this method, and the method succeeded, it should return S\_OK. This causes the core driver to return **TRUE** for the [**DrvQueryJobAttributes**](drvqueryjobattributes.md) DDI. If the UI plug-in supports this method, but the method failed, it should return E\_FAIL. This causes the core driver to return **FALSE** for the DrvQueryJobAttributes DDI. If the UI plug-in does not support this method, it should return E\_NOTIMPL.

## Remarks

When the printer has multiple UI plug-ins installed, the core driver calls the UI plug-ins in the order they were installed. The HRESULT returned by the last UI plug-in that supports this method is used to determine the core driver's DrvQueryJobAttributes DDI return value as described in the previous section.

See [**DrvQueryJobAttributes**](drvqueryjobattributes.md) for more information.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI2**](iprintoemui2-interface.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_1**](attribute-info-1.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_2**](attribute-info-2.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_3**](attribute-info-3.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_4**](attribute-info-4.md)
</dt> <dt>

[**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b)
</dt> <dt>

[**DrvQueryJobAttributes**](drvqueryjobattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI2::QueryJobAttributes%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





