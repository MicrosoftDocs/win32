---
Description: A printer interface DLL's DrvDevicePropertySheets function is responsible for creating property sheet pages that describe a printer's properties.
ms.assetid: 46f39e36-8915-4ccf-97ef-45dbacdfbe0a
title: DrvDevicePropertySheets function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvDevicePropertySheets function

A printer interface DLL's **DrvDevicePropertySheets** function is responsible for creating property sheet pages that describe a printer's properties.

## Syntax


```C++
LONG DrvDevicePropertySheets(
  _In_opt_ PPROPSHEETUI_INFO pPSUIInfo,
           LPARAM            lParam
);
```



## Parameters

<dl> <dt>

*pPSUIInfo* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

Caller-supplied integer value that is dependent on the contents of the **Reason** member of the PROPSHEETUI\_INFO structure, as listed in the following table.



| Reason value                         | Definition of *lParam*                                                                                                                                                                                                                                                                                                       |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROPSHEETUI\_REASON\_INIT<br/> | Pointer to a [**DEVICEPROPERTYHEADER**](devicepropertyheader.md) structure.<br/>                                                                                                                                                                                                                                      |
| All other reason values<br/>   | See the description of the *lParam* parameter for the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type.<br/> (The [**DEVICEPROPERTYHEADER**](devicepropertyheader.md) structure's address is contained in the **lParamInit** member of the [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure.)<br/> |



 

</dd> </dl>

## Return value

See the ReturnValue section in the description of the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type.

## Remarks

All [printer interface DLLs](https://www.bing.com/search?q=printer+interface+DLLs) must provide a **DrvDevicePropertySheets** function, which is defined using the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type. The function's purpose is to call the [**ComPropSheet**](compropsheet.md) function, provided by [CPSUI](https://www.bing.com/search?q=CPSUI), to specify a property sheet page containing user-modifiable properties for the printer.

The function should perform operations as described for the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type. The function should create the printer's DeviceSettings property sheet page (see the **pDlgPage** member of the [**COMPROPSHEETUI**](compropsheetui.md) structure).

Printer device settings should be stored in the registry. If a user with administrator privilege modifies options on the DeviceSettings page, the **DrvDevicePropertySheets** function should write the updated values to the registry by calling SetPrinterData (described in the Microsoft Windows SDK documentation).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md)
</dt> <dt>

[**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvDevicePropertySheets%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





