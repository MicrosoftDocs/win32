---
Description: The \_CPSUICALLBACK function type is used by CPSUI applications (including printer interface DLLs) for defining a callback function intended for use as a CPSUI message handler.
ms.assetid: 7d0f1609-5a24-4d38-9e9e-0c8e2de679a2
title: '\_CPSUICALLBACK callback function'
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# \_CPSUICALLBACK callback function

The **\_CPSUICALLBACK** function type is used by CPSUI applications (including printer interface DLLs) for defining a callback function intended for use as a [CPSUI message handler](print.cpsui_message_handler).

## Syntax


```C++
LONG _CPSUICALLBACK(
   PCPSUICBPARAM pComPropSheetUICBParam
);
```



## Parameters

<dl> <dt>

*pComPropSheetUICBParam* 
</dt> <dd>

CPSUI-supplied pointer to a [**CPSUICBPARAM**](cpsuicbparam.md) structure.

</dd> </dl>

## Return value

A \_CPSUICALLBACK-typed callback function must return one of the values listed in the following table. Each value indicates an action that CPSUI should perform.



| Return code                                                                                                     | Description                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**CPSUICB\_ACTION\_ITEMS\_APPLIED**</dt> </dl>  | The [**CPSUICBPARAM**](cpsuicbparam.md) structure's **Reason** member was set to CPSUICB\_REASON\_APPLYNOW, and the callback function has successfully processed the current option values.<br/>                                                                                |
| <dl> <dt>**CPSUICB\_ACTION\_NO\_APPLY\_EXIT**</dt> </dl> | The [**CPSUICBPARAM**](cpsuicbparam.md) structure's **Reason** member was set to CPSUICB\_REASON\_APPLYNOW, but the callback function has detected invalid or incompatible option values. The callback function must display a dialog box telling the user of the problem.<br/> |
| <dl> <dt>**CPSUICB\_ACTION\_NONE**</dt> </dl>            | No action by CPSUI is required.<br/>                                                                                                                                                                                                                                             |
| <dl> <dt>**CPSUICB\_ACTION\_OPTIF\_CHANGED**</dt> </dl>  | The callback function has set the OPTIF\_CHANGED flag in an [**OPTITEM**](optitem.md) structure to indicate that the selected option has changed, or that another OPTIF-prefixed flag has changed.<br/>                                                                         |
| <dl> <dt>**CPSUICB\_ACTION\_REINIT\_ITEMS**</dt> </dl>   | The callback function has set the OPTIF\_CHANGED flag in an [**OPTITEM**](optitem.md) structure to indicate that **Flags** or **pData** members of the associated [**OPTTYPE**](opttype.md) or [**OPTPARAM**](optparam.md) structure have changed.<br/>                       |



 

## Remarks

Callback functions specified using the \_CPSUICALLBACK function type are supplied by applications that use [CPSUI](print.common_property_sheet_user_interface) to manage property sheet pages. If one of these callback functions is associated with a property sheet page, CPSUI calls it when user activity (such as changing the page's control focus, modifying option values, or clicking on **OK**) is detected.

A \_CPSUICALLBACK-typed callback function is assigned to a property sheet page by including its address in a [**COMPROPSHEETUI**](compropsheetui.md) structure, which is passed to CPSUI's [**ComPropSheet**](compropsheet.md) function when the function code is [**CPSFUNC\_ADD\_PCOMPROPSHEETUI**](print.cpsfunc_add_pcompropsheetui).

Additionally, callback functions can be assigned to extended push buttons through the use of [**EXTPUSH**](extpush.md) structures.

When one of these callback functions is called, it receives a pointer to a [**CPSUICBPARAM**](cpsuicbparam.md) structure. This structure describes the current option settings for the page and indicates the user event that caused the function to be called. The callback function is responsible for validating and processing the settings. It should display a dialog box if a setting (or a combination of settings) is invalid. The function's return value indicates to CPSUI whether the page needs to be redisplayed or reinitialized.

Callback functions specified with this function type cannot be used if the **DlgProc** member of the [**DLGPAGE**](dlgpage.md) structure specifies an application-supplied dialog box procedure. This is because \_CPSUICALLBACK-typed callbacks are called from CPSUI's dialog box procedures, which are not used if the application supplies its own procedures.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20_CPSUICALLBACK%20callback%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




