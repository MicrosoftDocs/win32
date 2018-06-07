---
Description: Gets a feature from the PrintCapabilities based on a given key name.
ms.assetid: 053BFE59-FDC6-42F3-BE14-CE63D5637D62
title: IPrintSchemaCapabilities::GetFeatureByKeyName method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintSchemaCapabilities::GetFeatureByKeyName method

Gets a feature from the PrintCapabilities based on a given key name.

## Syntax


```C++
HRESULT GetFeatureByKeyName(
  [in]          BSTR                bstrKeyName,
  [out, retval] IPrintSchemaFeature **ppFeature
);
```



## Parameters

<dl> <dt>

*bstrKeyName* \[in\]
</dt> <dd>

The key name of the feature.

</dd> <dt>

*ppFeature* \[out, retval\]
</dt> <dd>

The returned feature.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Remarks

Only the following feature key names are recognized. The key names are equivalent to public Print Schema feature names as shown in the following table. The table also shows the features that have specialized option types (by default the option type is [**IPrintSchemaOption**](iprintschemaoption-interface.md)).



| Name              | Print schema feature public name              | Specialized option type                                                              |
|-------------------|-----------------------------------------------|--------------------------------------------------------------------------------------|
| DocumentBinding   | DocumentBinding or JobBindAllDocuments        |                                                                                      |
| DocumentCollate   | DocumentCollate                               |                                                                                      |
| DocumentDuplex    | JobDuplexAllDocumentsContiguously             |                                                                                      |
| DocumentHolePunch | DocumentHolePunch or JobHolePunch             |                                                                                      |
| DocumentInputBin  | JobInputBin, DocumentInputBin or PageInputBin |                                                                                      |
| DocumentNUp       | JobNUpAllDocumentsContiguously                | [**IPrintSchemaNUpOption**](iprintschemanupoption-interface.md)                     |
| DocumentStaple    | JobStapleAllDocuments or DocumentStaple       |                                                                                      |
| PageMediaSize     | PageMediaSize                                 | [**IPrintSchemaPageMediaSizeOption**](iprintschemapagemediasizeoption-interface.md) |
| PageMediaType     | PageMediaType                                 |                                                                                      |
| PageOrientation   | PageOrientation                               |                                                                                      |
| PageOutputColor   | PageOutputColor                               |                                                                                      |
| PageOutputQuality | PageOutputQuality                             |                                                                                      |



 

When the requested feature, option or property is not found, this method returns S\_FALSE and sets a NULL pointer on the output object of the feature, option or property.

So if the [**IPrintSchemaTicket**](iprintschematicket-interface.md) object does not contain the specified feature, option or property, the app must obtain an [**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md) object and query it via **IPrintSchemaCapabilities::GetFeatureByKeyName** or via [**IPrintSchemaCapabilities::GetFeature**](iprintschemacapabilities-getfeature.md).

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Version<br/>         | Windows 8<br/>                                                                          |
| Header<br/>          | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md)
</dt> <dt>

[**IPrintSchemaNUpOption**](iprintschemanupoption-interface.md)
</dt> <dt>

[**IPrintSchemaOption**](iprintschemaoption-interface.md)
</dt> <dt>

[**IPrintSchemaPageMediaSizeOption**](iprintschemapagemediasizeoption-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaCapabilities::GetFeatureByKeyName%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





