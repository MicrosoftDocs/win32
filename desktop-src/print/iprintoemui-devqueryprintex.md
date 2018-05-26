---
Description: The IPrintOemUIDevQueryPrintEx method allows a user interface plug-in to help determine if a print job is printable.
ms.assetid: a1bc9be3-53ec-4506-a409-94a65d7136e1
title: IPrintOemUIDevQueryPrintEx method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemUI::DevQueryPrintEx method

The `IPrintOemUI::DevQueryPrintEx` method allows a user interface plug-in to help determine if a print job is printable.

## Syntax


```C++
HRESULT DevQueryPrintEx(
   POEMUIOBJ           poemuiobj,
   PDEVQUERYPRINT_INFO pDQPInfo,
   PDEVMODE            pPublicDM,
   PVOID               pOEMDM
);
```



## Parameters

<dl> <dt>

*poemuiobj* 
</dt> <dd>

Caller-supplied pointer to an [**OEMUIOBJ**](oemuiobj.md) structure.

</dd> <dt>

*pDQPInfo* 
</dt> <dd>

Caller-supplied pointer to a [**DEVQUERYPRINT\_INFO**](devqueryprint-info.md) structure.

</dd> <dt>

*pPublicDM* 
</dt> <dd>

Caller-supplied pointer to a validated [**DEVMODEW**](display.devmodew) structure.

</dd> <dt>

*pOEMDM* 
</dt> <dd>

Caller-supplied pointer to the user interface plug-in's private DEVMODEW structure members.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

A user interface plug-in's `IPrintOemUI::DevQueryPrintEx` method performs the same types of operations as the [**DevQueryPrintEx**](devqueryprintex.md) function that is exported by user-mode printer interface DLLs. You can use this method to enhance the functionality provided by the **DevQueryPrintEx** function. Like the **DevQueryPrintEx** function, the `IPrintOemUI::DevQueryPrintEx` method's responsibility is to determine if the print job described by the supplied DEVMODEW structure can be printed.

When the driver's **DevQueryPrintEx** function is called, it checks the DEVMODEW structure, along with the currently selected printer options, to determine if the job is printable. If it is not, the function returns **FALSE**. If the job appears to be printable, the function calls the `IPrintOemUI::DevQueryPrintEx` method in each user interface plug-in associated with the driver. If all `IPrintOemUI::DevQueryPrintEx` methods return S\_OK, then **DevQueryPrintEx** returns **TRUE**. Thus, a job is not printable unless the **DevQueryPrintEx** function and all `IPrintOemUI::DevQueryPrintEx` methods declare it to be printable.

If `IPrintOemUI::DevQueryPrintEx` methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.

For more information about creating and installing user interface plug-ins, see [Customizing Microsoft's Printer Drivers](print.customizing_microsoft_s_printer_drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**DevQueryPrintEx**](devqueryprintex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::DevQueryPrintEx%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





