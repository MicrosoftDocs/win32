---
Description: The GetParameterDefinition method retrieves the IPrintSchemaParameterDefinition object, and it represents the &lt;psfParameterDef&gt; element in the PrintCapabilites XML.
ms.assetid: 19C3A3C5-446B-48FD-8E77-2E0F787B16B1
title: IPrintSchemaCapabilities2GetParameterDefinition method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintSchemaCapabilities2::GetParameterDefinition method

The **GetParameterDefinition** method retrieves the [**IPrintSchemaParameterDefinition**](iprintschemaparameterdefinition.md) object, and it represents the &lt;psf:ParameterDef&gt; element in the PrintCapabilites XML.

The keyword name and keyword namespace URI specify the **IPrintSchemaParameterDefinition** object to be retrieved.

## Syntax


```C++
HRESULT GetParameterDefinition(
  [in]          BSTR                            bstrName,
  [in]          BSTR                            bstrNamespaceUri,
  [out, retval] IPrintSchemaParameterDefinition **ppParameterDefinition
);
```



## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

The keyword name.

</dd> <dt>

*bstrNamespaceUri* \[in\]
</dt> <dd>

The keyword namespace URI.

</dd> <dt>

*ppParameterDefinition* \[out, retval\]
</dt> <dd>

The **IPrintSchemaParameterDefinition** object.

</dd> </dl>

## Return value

The **GetParameterDefinition** method returns an **HRESULT** value. If the property call was not successful, it returns the appropriate **HRESULT** error code.

## Remarks

To be consistent with [**IPrintSchemaCapabilities::GetFeature**](iprintschemacapabilities-getfeature.md), the **GetParameterDefinition** method works for any &lt;psf:ParameterDef&gt; element that is defined in the public keyword namespaces. The **GetParameterDefinition** method also works for any IHV-defined private keyword namespace that uses either the StringParamType or the IntegerParamType data type.

When you use the &lt;psf:ParameterDef&gt; element with the QNameParamType or the DecimalParamType data type, **GetParameterDefinition** will return HRESULT\_FROM\_WIN32 (ERROR\_NOT\_SUPPORTED).

For more information about the data types that you can use with the &lt;psf:ParameterDef&gt; element, see section 2.1.3.1 of the [Print Schema Specification](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx).

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaCapabilities2**](iprintschemacapabilities2.md)
</dt> <dt>

[**IPrintSchemaParameterDefinition**](iprintschemaparameterdefinition.md)
</dt> <dt>

[Print Schema Specification](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaCapabilities2::GetParameterDefinition%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





