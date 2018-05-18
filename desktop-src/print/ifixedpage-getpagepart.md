---
Description: 'The GetPagePart method gets the images, thumbnails, fonts, and so on in a page by using the URI.'
ms.assetid: '6ec8d282-eedb-419e-84cb-8f4776ea7650'
title: 'IFixedPage::GetPagePart method'
---

# IFixedPage::GetPagePart method

The **GetPagePart** method gets the images, thumbnails, fonts, and so on in a page by using the URI.

## Syntax


```C++
HRESULT GetPagePart(
  [in]  const wchar_t  *uri,
  [out]       IUnknown **ppUnk
);
```



## Parameters

<dl> <dt>

*uri* \[in\]
</dt> <dd>

The URI for a part. For example, the filter might parse the page markup and find a referenced font. The filter can use the font URI in a call to **GetPagePart**. The filter could then retrieve the font object that is associated with the page.

</dd> <dt>

*ppUnk* \[out\]
</dt> <dd>

The object that is to be queried.

</dd> </dl>

## Return value

**GetPagePart** returns an **HRESULT**.

## Remarks

A filter must use QueryInterface on the return value to see what part types reside in the page.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IFixedPage::GetPagePart%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




