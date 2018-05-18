---
Description: 'The GetNewEmptyPart method creates a new XPS part.'
ms.assetid: 'cc0911da-46ca-4cf7-a59e-da0d53e1d10c'
title: 'IXpsDocumentConsumer::GetNewEmptyPart method'
---

# IXpsDocumentConsumer::GetNewEmptyPart method

The `GetNewEmptyPart` method creates a new XPS part.

## Syntax


```C++
HRESULT GetNewEmptyPart(
  [in]  const wchar_t           *uri,
  [in]        REFIID            riid,
  [out]       void              **ppNewObject,
  [out]       IPrintWriteStream **ppWriteStream
);
```



## Parameters

<dl> <dt>

*uri* \[in\]
</dt> <dd>

The URI for the new part to be created.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

A reference identifier (REFIID) for one of the following interfaces:

-   [IFixedDocument](ifixeddocument.md)

-   [IFixedPage](ifixedpage.md)

-   [IPartImage](ipartimage.md)

-   [IPartThumbnail](ipartthumbnail.md)

-   [IPartFont](ipartfont.md)

-   [IPartPrintTicket](ipartprintticket.md)

-   [IPartColorProfile](ipartcolorprofile.md)

</dd> <dt>

*ppNewObject* \[out\]
</dt> <dd>

A pointer to the new object to be created.

</dd> <dt>

*ppWriteStream* \[out\]
</dt> <dd>

A data stream object that the part will be written to. Each part is associated with a data stream object.

</dd> </dl>

## Return value

`GetNewEmptyPart` returns an **HRESULT**.

## Remarks

A filter can create new XPS parts by using the `GetNewEmptyPart` method. Typically, the filter receives XPS parts from the inter-filter object.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



## See also

<dl> <dt>

[**IXpsDocumentConsumer**](ixpsdocumentconsumer.md)
</dt> <dt>

[IFixedDocument](ifixeddocument.md)
</dt> <dt>

[IFixedPage](ifixedpage.md)
</dt> <dt>

[IPartColorProfile](ipartcolorprofile.md)
</dt> <dt>

[IPartFont](ipartfont.md)
</dt> <dt>

[IPartImage](ipartimage.md)
</dt> <dt>

[IPartPrintTicket](ipartprintticket.md)
</dt> <dt>

[IPartThumbnail](ipartthumbnail.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsDocumentConsumer::GetNewEmptyPart%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





