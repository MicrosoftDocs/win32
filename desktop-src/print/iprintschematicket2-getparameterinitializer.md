---
Description: The GetParameterInitializer method retrieves the IPrintSchemaParameterInitializer object, and it represents the &lt;psfParameterInit&gt; element in the PrintTicket XML.
ms.assetid: E5403359-A757-4530-B17B-C80E8A45AA92
title: IPrintSchematicket2GetParameterInitializer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintSchematicket2::GetParameterInitializer method

The **GetParameterInitializer** method retrieves the [**IPrintSchemaParameterInitializer**](iprintschemaparameterinitializer.md) object, and it represents the &lt;psf:ParameterInit&gt; element in the PrintTicket XML.

The keyword name and keyword namespace URI specify the **IPrintSchemaParameterInitializer** object to be retrieved.

## Syntax


```C++
HRESULT GetParameterInitializer(
  [in]          BSTR                             bstrName,
  [in]          BSTR                             bstrNamespaceUri,
  [out, retval] IPrintSchemaParameterInitializer **ppParameterInitializer
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

*ppParameterInitializer* \[out, retval\]
</dt> <dd>

The [**IPrintSchemaParameterInitializer**](iprintschemaparameterinitializer.md) object.

</dd> </dl>

## Return value

The **GetParameterInitializer** method returns an **HRESULT** value. If the property call was not successful, it returns the appropriate **HRESULT** error code.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchematicket2**](iprintschematicket2.md)
</dt> <dt>

[**IPrintSchemaParameterInitializer**](iprintschemaparameterinitializer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchematicket2::GetParameterInitializer%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





