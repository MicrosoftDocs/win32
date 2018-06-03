---
Description: Gets a named feature from the PrintCapabilities, by name and full namespace URI.
ms.assetid: AC6434F5-0892-4426-98BB-BC02AD17917B
title: IPrintSchemaCapabilities::GetFeature method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintSchemaCapabilities::GetFeature method

Gets a named feature from the PrintCapabilities, by name and full namespace URI.

## Syntax


```C++
HRESULT GetFeature(
  [in]          BSTR                bstrName,
  [in]          BSTR                bstrNamespaceUri,
  [out, retval] IPrintSchemaFeature **ppFeature
);
```



## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

The base value of the "name" attribute of the Feature element. For example, for the Print Schema feature, the tag looks like this &lt;psf:Feature name="psk:JobOutputBin"&gt;, showing a base value of "JobOutputBin".

</dd> <dt>

*bstrNamespaceUri* \[in\]
</dt> <dd>

The namespace URI value of the "name" attribute of the Feature element. For example, for the Print Schema feature, the tag looks like this &lt;psf:Feature name="psk:JobOutputBin"&gt;, with a base name value of "JobOutputBin", and the namespace URI of the public Print Schema is "http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords". If the feature is not defined in the public Print Schema, then this should be the URI of the private namespace that defines the feature.

</dd> <dt>

*ppFeature* \[out, retval\]
</dt> <dd>

The returned feature.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Remarks

When the requested feature, option or property is not found, this method returns S\_FALSE and sets a NULL pointer on the output object of the feature, option or property.

So if the [**IPrintSchemaTicket**](iprintschematicket-interface.md) object does not contain the specified feature, option or property, the app must obtain an [**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md) object and query it via [**IPrintSchemaCapabilities::GetFeatureByKeyName**](iprintschemacapabilities-getfeaturebykeyname.md) or via **IPrintSchemaCapabilities::GetFeature**.

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

[**IPrintSchemaFeature**](iprintschemafeature-interface.md)
</dt> <dt>

[**IPrintSchemaTicket**](iprintschematicket-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaCapabilities::GetFeature%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





