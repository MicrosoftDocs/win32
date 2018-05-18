---
Description: 'The printer driver''s DrvDriverEvent function calls a user interface plug-in''s IPrintOemUI::DriverEvent method for additional processing of printer driver events.'
ms.assetid: 'aacddaea-3a6f-4018-92ac-fe4aa2ddabd3'
title: 'IPrintOemUI::DriverEvent method'
---

# IPrintOemUI::DriverEvent method

The printer driver's [**DrvDriverEvent**](drvdriverevent.md) function calls a user interface plug-in's `IPrintOemUI::DriverEvent` method for additional processing of printer driver events.

## Syntax


```C++
HRESULT DriverEvent(
   DWORD  dwDriverEvent,
   DWORD  dwLevel,
   LPBYTE pDriverInfo,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*dwDriverEvent* 
</dt> <dd>

Caller-supplied bit flag indicating the event that has occurred. Valid flags are listed in the following table.



| Flag                                 | Definition                                     |
|--------------------------------------|------------------------------------------------|
| DRIVER\_EVENT\_DELETE<br/>     | The driver is being removed.<br/>        |
| DRIVER\_EVENT\_INITIALIZE<br/> | The driver has just been installed.<br/> |



 

</dd> <dt>

*dwLevel* 
</dt> <dd>

Caller-supplied value indicating the type of structure pointed to by the *pDriverInfo* parameter, as indicated in the following table.



| *dwLevel* Value | Structure pointed to by *pDriverInfo* |
|-----------------|---------------------------------------|
| 1<br/>    | DRIVER\_INFO\_1<br/>            |
| 2<br/>    | DRIVER\_INFO\_2<br/>            |
| 3<br/>    | DRIVER\_INFO\_3<br/>            |



 

<dl> <dd>

The DRIVER\_INFO\_*N* structures are described in the Microsoft Windows SDK documentation.

</dd> </dl> </dd> <dt>

*pDriverInfo* 
</dt> <dd>

Caller-supplied pointer to a structure whose type is identified by the *dwLevel* parameter.

</dd> <dt>

*lParam* 
</dt> <dd>

Caller-supplied flags. See the following Remarks section.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

A user interface plug-in's `IPrintOemUI::DriverEvent` method performs the same types of operations as the **DrvDriverEvent** function that is exported by user-mode printer interface DLLs. For information about driver events and how they should be processed, see the description of the [**DrvDriverEvent**](drvdriverevent.md) function.

If you provide a user interface plug-in, the printer driver's **DrvDriverEvent** function calls the `IPrintOemUI::DriverEvent` method. The **DrvDriverEvent** function performs its own processing for the specified event, and then calls the `IPrintOemUI::DriverEvent` method to handle additional processing of the event.

If `IPrintOemUI::DriverEvent` methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.

For more information about creating and installing user interface plug-ins, see [Customizing Microsoft's Printer Drivers](print.customizing_microsoft_s_printer_drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI**](iprintoemui-interface.md)
</dt> <dt>

[**DrvDriverEvent**](drvdriverevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::DriverEvent%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





