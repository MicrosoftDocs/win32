---
Description: The PFNPROPSHEETUI function type is used by CPSUI applications (including printer interface DLLs) for defining page creation callbacks, which specify property sheet pages for creation.
ms.assetid: b78d0dd7-1fe9-4b7e-8f51-4b5dc5fa2571
title: PFNPROPSHEETUI callback function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PFNPROPSHEETUI callback function

The PFNPROPSHEETUI function type is used by CPSUI applications (including printer interface DLLs) for defining [page creation callbacks](print.page_creation_callbacks), which specify property sheet pages for creation.

## Syntax


```C++
LONG PFNPROPSHEETUI(
   PPROPSHEETUI_INFO pPSUIInfo,
   LPARAM            lParam
);
```



## Parameters

<dl> <dt>

*pPSUIInfo* 
</dt> <dd>

CPSUI-supplied pointer to a [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

CPSUI-supplied integer value that is dependent on the contents of the **Reason** member of the [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure. Valid values are as follows:

<dl> <dt>

<span id="PROPSHEETUI_REASON_BEFORE_INIT"></span><span id="propsheetui_reason_before_init"></span>PROPSHEETUI\_REASON\_BEFORE\_INIT
</dt> <dd>

This value is new to Windows 8 and it is provided only to the original PFNPROPSHEETUI parameter passed to [**CommonPropertySheetUI**](commonpropertysheetui.md).

</dd> <dt>

<span id="PROPSHEETUI_REASON_DESTROY"></span><span id="propsheetui_reason_destroy"></span>PROPSHEETUI\_REASON\_DESTROY
</dt> <dd>

The *lParam* value is nonzero if the user has selected the property sheet's **OK** or **Cancel** button. Otherwise the value is zero.

</dd> </dl>

<dl> <dt>

<span id="PROPSHEETUI_REASON_GET_ICON"></span><span id="propsheetui_reason_get_icon"></span>PROPSHEETUI\_REASON\_GET\_ICON
</dt> <dd>

The *lParam* value is a pointer to a [**PROPSHEETUI\_GETICON\_INFO**](propsheetui-geticon-info.md) structure.

</dd> </dl>

<dl> <dt>

<span id="PROPSHEETUI_REASON_GET_INFO_HEADER"></span><span id="propsheetui_reason_get_info_header"></span>PROPSHEETUI\_REASON\_GET\_INFO\_HEADER
</dt> <dd>

The *lParam* value is a pointer to a [**PROPSHEETUI\_INFO\_HEADER**](propsheetui-info-header.md) structure.

</dd> </dl>

<dl> <dt>

<span id="PROPSHEETUI_REASON_INIT"></span><span id="propsheetui_reason_init"></span>PROPSHEETUI\_REASON\_INIT
</dt> <dd>

If the callback function is specified by the *pfnPropSheetUI* parameter to [**CommonPropertySheetUI**](commonpropertysheetui.md), *lParam* is the *lParam* value passed to **CommonPropertySheetUI**.

If the callback function is specified using the CPSFUNC\_ADD\_PFNPROPSHEETUI function code with CPSUI's [**ComPropSheet**](compropsheet.md) function, *lParam* is the *lParam2* value passed to **ComPropSheet**.

CPSUI copies the *lParam* value into the **lParamInit** member of the function's [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure.

The *lParam* value must not reside on the application's stack.

</dd> </dl>

<dl> <dt>

<span id="PROPSHEETUI_REASON_SET_RESULT"></span><span id="propsheetui_reason_set_result"></span>PROPSHEETUI\_REASON\_SET\_RESULT
</dt> <dd>

The *lParam* value is a pointer to a [**SETRESULT\_INFO**](setresult-info.md) structure.

</dd> </dl> </dd> </dl>

## Return value

If the operation succeeds, the function should return a value of one (or greater). Otherwise it should return a value less than one.



| Return code                                                                                    | Description                                                                                               |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**One or greater.**</dt> </dl> | The PFNPROPSHEETUI function associated with the parent of the current page will be called.<br/>     |
| <dl> <dt>**Less than 1.**</dt> </dl>    | The PFNPROPSHEETUI function associated with the parent of the current page will not be called.<br/> |



 

## Remarks

Callback functions specified using the PFNPROPSHEETUI function type are supplied by applications that use [CPSUI](print.common_property_sheet_user_interface) to manage customized property sheet pages. One such callback function must be specified when an application calls the [**CommonPropertySheetUI**](commonpropertysheetui.md) function. For example, when the NT-based operating system print spooler calls CPSUI's **CommonPropertySheetUI** function to support its **DocumentProperties** or **PrinterProperties** API functions (described in the Microsoft Windows SDK documentation), the spooler specifies an internal PFNPROPSHEETUI-typed callback function.

Applications can specify additional PFNPROPSHEETUI-typed callback functions by calling CPSUI's [**ComPropSheet**](compropsheet.md) function with a function code of [**CPSFUNC\_ADD\_PFNPROPSHEETUI**](print.cpsfunc_add_pfnpropsheetui). For example, the NT-based operating system print spooler does this to notify CPSUI of the existence of a printer interface DLL's [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) and [**DrvDevicePropertySheets**](drvdevicepropertysheets.md) functions. Likewise, Microsoft's [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) and [*Pscript*](wdkgloss.p#wdkgloss-pscript) drivers use this technique to notify CPSUI of the existence of [**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) and [**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md) methods in [user interface plug-ins](print.user_interface_plug_ins).

Each PFNPROPSHEETUI-typed callback function is called by CPSUI several times. The **Reason** member of the [**PROPSHEETUI\_INFO**](propsheetui-info.md) structure stipulates the operation that the function should perform, as follows:

<dl> <dt>

<span id="PROPSHEETUI_REASON_BEFORE_INIT"></span><span id="propsheetui_reason_before_init"></span>PROPSHEETUI\_REASON\_BEFORE\_INIT
</dt> <dd>

This *lParam* value is used between the common printer UI and the system-provided configuration module for v4 printer drivers. This value should be ignored by v3 printer drivers, which should return -1 in this case.

</dd> <dt>

<span id="PROPSHEETUI_REASON_DESTROY"></span><span id="propsheetui_reason_destroy"></span>PROPSHEETUI\_REASON\_DESTROY
</dt> <dd>

The callback function should release resources that were allocated in response to PROPSHEETUI\_REASON\_INIT.

</dd> </dl>

<dl> <dt>

<span id="PROPSHEETUI_REASON_GET_ICON"></span><span id="propsheetui_reason_get_icon"></span>PROPSHEETUI\_REASON\_GET\_ICON
</dt> <dd>

The callback function should call **LoadImage** (described in the Windows SDK documentation) to load an icon resource, using parameters specified by the [**PROPSHEETUI\_GETICON\_INFO**](propsheetui-geticon-info.md) structure pointed to be *lParam*, and it should return the icon's handle in the structure.

</dd> </dl>

<dl> <dt>

<span id="PROPSHEETUI_REASON_GET_INFO_HEADER"></span><span id="propsheetui_reason_get_info_header"></span>PROPSHEETUI\_REASON\_GET\_INFO\_HEADER
</dt> <dd>

The callback function should supply page header information in the [**PROPSHEETUI\_INFO\_HEADER**](propsheetui-info-header.md) structure pointed to by *lParam*.

</dd> </dl>

<dl> <dt>

<span id="PROPSHEETUI_REASON_INIT"></span><span id="propsheetui_reason_init"></span>PROPSHEETUI\_REASON\_INIT
</dt> <dd>

The callback function should call the [**ComPropSheet**](compropsheet.md) function to specify property sheet pages. (This is always the first reason received.)

</dd> </dl>

<dl> <dt>

<span id="PROPSHEETUI_REASON_SET_RESULT"></span><span id="propsheetui_reason_set_result"></span>PROPSHEETUI\_REASON\_SET\_RESULT
</dt> <dd>

The callback function receives result information in the [**SETRESULT\_INFO**](setresult-info.md) structure pointed to by *lParam*. This is application-supplied status information, specified by calling CPSUI's [**ComPropSheet**](compropsheet.md) function with a function code of CPSFUNC\_SET\_RESULT.

For more information about handling this reason value, see the description of [**SETRESULT\_INFO**](setresult-info.md).

</dd> </dl>

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PFNPROPSHEETUI%20callback%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




