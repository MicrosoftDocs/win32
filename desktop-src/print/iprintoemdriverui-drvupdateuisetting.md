---
Description: 'The IPrintOemDriverUI::DrvUpdateUISetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can notify the driver of a modified user interface option.'
ms.assetid: 'f5dec76e-16ad-4df0-b3c9-f0cbfb9b8c41'
title: 'IPrintOemDriverUI::DrvUpdateUISetting method'
---

# IPrintOemDriverUI::DrvUpdateUISetting method

The `IPrintOemDriverUI::DrvUpdateUISetting` method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can notify the driver of a modified user interface option.

## Syntax


```C++
HRESULT DrvUpdateUISetting(
   PVOID pci,
   PVOID pOptItem,
   DWORD dwPreviousSelection,
   DWORD dwMode
);
```



## Parameters

<dl> <dt>

*pci* 
</dt> <dd>

Caller-supplied pointer to an [**OEMUIOBJ**](oemuiobj.md) structure.

</dd> <dt>

*pOptItem* 
</dt> <dd>

Caller-supplied pointer to an [**OPTITEM**](optitem.md) structure describing a user interface option item.

</dd> <dt>

*dwPreviousSelection* 
</dt> <dd>

Not used.

</dd> <dt>

*dwMode* 
</dt> <dd>

Caller-supplied integer constant indicating to which property sheet page the supplied option item belongs. The following constants are valid.



| Value                       | Definition                                                                                             |
|-----------------------------|--------------------------------------------------------------------------------------------------------|
| OEMCUIP\_DOCPROP<br/> | The supplied option item belongs to the Advanced page of the document property sheet.<br/>       |
| OEMCUIP\_PRNPROP<br/> | The supplied option item belongs to the Device Settings page of the printer property sheet.<br/> |



 

For more information, see the following Remarks section.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

If you are providing a user interface plug-in that implements the [**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) method or the [**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md) method, you typically also supply a [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback function to handle user modifications. This callback function must call `IPrintOemDriverUI::DrvUpdateUISetting` to inform the driver when the value associated with a user interface setting has been modified, if the value is stored in the driver's [**DEVMODEW**](display.devmodew) structure (instead of the plug-in's private DEVMODEW members ) or in registry keys.

The value specified for *dwMode* should be based on which method specified the callback function.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUI::DrvUpdateUISetting%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




