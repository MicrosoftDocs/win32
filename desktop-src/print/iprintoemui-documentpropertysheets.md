---
Description: The IPrintOemUI::DocumentPropertySheets method allows a user interface plug-in to append a new page to a printer device's document property sheet.
ms.assetid: a8c7eb0d-792f-4a6c-af47-bb4558feb790
title: IPrintOemUI::DocumentPropertySheets method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI::DocumentPropertySheets method

The `IPrintOemUI::DocumentPropertySheets` method allows a user interface plug-in to append a new page to a printer device's document property sheet.

## Syntax


```C++
HRESULT DocumentPropertySheets(
   PPROPSHEETUI_INFO pPSUIInfo,
   LPARAM            lParam
);
```



## Parameters

<dl> <dt>

*pPSUIInfo* 
</dt> <dd>

Caller-supplied pointer to a [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

Caller-supplied value that depends on the reason value in *pPSUIInfo*--&gt;**Reason**. The reason value can be one of the following constants, which are defined in compstui.h. For more information about these constants, see the Remarks section and *lParam* parameter description in the [**PFNPROPSHEETUI**](pfnpropsheetui.md) function type.

PROPSHEETUI\_REASON\_DESTROY

PROPSHEETUI\_REASON\_GET\_ICON

PROPSHEETUI\_REASON\_GET\_INFO\_HEADER

PROPSHEETUI\_REASON\_INIT

PROPSHEETUI\_REASON\_SET\_RESULT

</dd> </dl>

## Return value

The return value depends on the contents of the PROPSHEETUI\_INFO structure's **Reason** member. For more information, see the description of [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md).

## Remarks

A user interface plug-in's `IPrintOemUI::DocumentPropertySheets` method performs the same types of operations as the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function that is exported by user-mode printer interface DLLs. Both functions have the same input parameters.

If you provide a user interface plug-in, the `IPrintOemUI::DocumentPropertySheets` method is called after the driver's **DrvDocumentPropertySheets** function is called.

When `IPrintOemUI::DocumentPropertySheets` is called, the **lParamInit** member of the [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure contains the address of an [**OEMUIPSPARAM**](oemuipsparam.md) structure.

If you implement this method, you typically also supply a [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback function to handle user modifications. This callback function must call [**IPrintOemDriverUI::DrvUpdateUISetting**](iprintoemdriverui-drvupdateuisetting.md) to inform the driver when the value associated with a user interface setting has been modified, if the value is stored in the driver's [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure (instead of the plug-in's private DEVMODEW members ) or in registry keys.

If `IPrintOemUI::DocumentPropertySheets` methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.

If one user interface plug-in supports several printer models, and if you only want the new page to be displayed for some of those models, the `IPrintOemUI::DocumentPropertySheets` method should just provide a success return value, without actually adding the page, for the models not requiring the page.

For more information about creating and installing user interface plug-ins, see [Customizing Microsoft's Printer Drivers](https://www.bing.com/search?q=Customizing+Microsoft's+Printer+Drivers).

## Requirements



|                            |                                                                                                                          |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                       |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h or Compstui.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI**](iprintoemui-interface.md)
</dt> <dt>

[**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md)
</dt> <dt>

[**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md)
</dt> <dt>

[**PFNPROPSHEETUI**](pfnpropsheetui.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::DocumentPropertySheets%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





