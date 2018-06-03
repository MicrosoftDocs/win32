---
Description: The IPrintOemUI::DeviceCapabilities method enables a user interface plug-in to specify customized device capabilities.
ms.assetid: a3d3e986-41ab-489a-a930-b10e9989553f
title: IPrintOemUI::DeviceCapabilities method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI::DeviceCapabilities method

The `IPrintOemUI::DeviceCapabilities` method enables a user interface plug-in to specify customized device capabilities.

## Syntax


```C++
HRESULT DeviceCapabilities(
   POEMUIOBJ poemuiobj,
   HANDLE    hPrinter,
   PWSTR     pDeviceName,
   WORD      wCapability,
   PVOID     pOutput,
   PDEVMODE  pPublicDM,
   PVOID     pOEMDM,
   DWORD     dwOld,
   DWORD     *dwResult
);
```



## Parameters

<dl> <dt>

*poemuiobj* 
</dt> <dd>

Caller-supplied pointer to an [**OEMUIOBJ**](oemuiobj.md) structure.

</dd> <dt>

*hPrinter* 
</dt> <dd>

Caller-supplied handle to the printer device.

</dd> <dt>

*pDeviceName* 
</dt> <dd>

Caller-supplied pointer to a string representing the device name.

</dd> <dt>

*wCapability* 
</dt> <dd>

Caller-supplied flag indicating the type of information the method should return. For a list of flags, see the description of the [**DrvDeviceCapabilities**](drvdevicecapabilities.md) function.

</dd> <dt>

*pOutput* 
</dt> <dd>

Caller-supplied pointer to a buffer to receive the requested information. The type of information returned is dependent on the flag specified by *wCapability*.

</dd> <dt>

*pPublicDM* 
</dt> <dd>

Caller-supplied pointer to a validated [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure.

</dd> <dt>

*pOEMDM* 
</dt> <dd>

Caller-supplied pointer to the user interface plug-in's private DEVMODEW structure members.

</dd> <dt>

*dwOld* 
</dt> <dd>

Caller-supplied return value from the printer driver's [**DrvDeviceCapabilities**](drvdevicecapabilities.md) function, or from another user interface plug-in. For more information, see the following Remarks section.

</dd> <dt>

*dwResult* 
</dt> <dd>

A return value that is dependent on the flag specified by *wCapability*. For more information, see the description of the [**DrvDeviceCapabilities**](drvdevicecapabilities.md) function and the following Remarks section.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                                                         | Description                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                | The operation succeeded.<br/>                                                                                                                                                                                                                           |
| <dl> <dt>**S\_DEVCAP\_OUTPUT\_FULL\_REPLACEMENT**</dt> </dl> | The plug-in intends to use the buffer that is pointed to by the *pOutput* parameter for its own purposes. This return value is defined in prcomoem.h. For more information about when to use this return value, see the following Remarks section.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                              | The operation failed.<br/>                                                                                                                                                                                                                              |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                           | The method is not implemented.<br/>                                                                                                                                                                                                                     |



 

## Remarks

A user interface plug-in's `IPrintOemUI::DeviceCapabilities` method performs the same types of operations as the [**DrvDeviceCapabilities**](drvdevicecapabilities.md) function that is exported by user-mode printer interface DLLs. The method specifies capabilities provided by the printer.

You can use the `IPrintOemUI::DeviceCapabilities` method to preempt Unidrv support for a capability, or to add a capability that the printer driver doesn't provide. The driver calls `IPrintOemUI::DeviceCapabilities` from within its [**DrvDeviceCapabilities**](drvdevicecapabilities.md) function.

If the `IPrintOemUI::DeviceCapabilities` method indicates customized support for a capability (by setting appropriate bits in response to a received DC\_FIELDS flag), customized code must completely support the capability. Complete support typically includes returning information about the capability in response to calls to the `IPrintOemUI::DeviceCapabilities` method, plus providing appropriate user-mode or kernel-mode code to implement the capability.

If `IPrintOemUI::DeviceCapabilities` methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation. Each time a plug-in's `IPrintOemUI::DeviceCapabilities` method is called, its *dwOld* input value is the return value from the previously called plug-in's `IPrintOemUI::DeviceCapabilities` method. For the first plug-in called, *dwOld* contains the return value from the printer driver's **DrvDeviceCapabilities** function. Likewise, the buffer pointed to by *pOutput* contains, on input, any contents placed there by a previously called `IPrintOemUI::DeviceCapabilities` method or **DrvDeviceCapabilities** function.

For multiple user interface plug-ins to work in conjunction with each other, each `IPrintOemUI::DeviceCapabilities` method must obey the following rules:

-   If a user interface plug-in does not support a specified capability, its `IPrintOemUI::DeviceCapabilities` method should just return the contents of the *dwOld* parameter in *dwResult*.

-   If a user interface plug-in supports the capability, its `IPrintOemUI::DeviceCapabilities` method should ignore *dwOld* and the contents of the buffer pointed to by *pOutput*. It should provide a return value and buffer contents appropriate for indicating that it supports the specified capability. If the method detects an error, it should return GDI\_ERROR in *dwResult*.

-   If you want a user interface plug-in to modify the capabilities information received in the buffer pointed to by *pOutput*, its `IPrintOemUI::DeviceCapabilities` method should modify the buffer contents and return an appropriate return value in *dwResult*. For example, if *wCapability* is DC\_FIELDS, the method should OR the bits it needs to set with the bits that are set in *dwOld*, and return the result of the OR operation in *dwResult*.

-   The preceding rules should be followed even if the received contents of *dwOld* is GDI\_ERROR.

When the driver's **DrvDeviceCapabilities** function is called with the DC\_FIELDS flag set, the function calls all `IPrintOemUI::DeviceCapabilities` methods, also specifying DC\_FIELDS, and returns the union of all set bits to the caller.

The S\_DEVCAP\_OUTPUT\_FULL\_REPLACEMENT return value is new in Windows Vista, and applies to both Unidrv and Pscript5 user interface plug-ins. A plug-in should use the S\_DEVCAP\_OUTPUT\_FULL\_REPLACEMENT return value only if it requires complete control over what is placed in the buffer that is pointed to by the *pOutput* parameter. Neither the Unidrv nor the Pscript5 core driver will place data in the *pOutput* buffer when the plug-in returns S\_DEVCAP\_OUTPUT\_FULL\_REPLACEMENT. A plug-in might need to return this value when a setting in the [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure (which is pointed to by the *pPublicDM* and *pOEMDM* parameters) indicates to the user interface plug-in that it should report device capability data that is different from that specified in the GPD or PPD file. For example, a DEVMODEW structure that specifies photo printing might require a different set of paper types than those that are specified in the GPD or PPD file. In such a situation, and regardless of the values of the *pOutput* and *dwOld* parameters, the plug-in should return S\_DEVCAP\_OUTPUT\_FULL\_REPLACEMENT, and should set the *dwResult* parameter to the number of paper types that it intends to report. If *pOutput* is not **NULL**, the plug-in should also fill the buffer that is pointed to by *pOutput* with the desired set of paper types, and should set *dwResult* to the number of paper types that the plug-in intends to report.

When multiple user interface plug-ins are active at the same time, and one of them returns S\_DEVCAP\_OUTPUT\_FULL\_REPLACEMENT, the Unidrv or Pscript5 core driver interprets this return value to mean that the plug-ins intend to provide full replacement output data. As a result, the core driver does not place any data into the *pOutput* buffer before it calls the plug-ins. (The core driver calls the plug-ins in the same order that was specified for their installation.)

In situations where the values that the core driver places in the *pOutput* buffer do not need to be replaced, the plug-in should return S\_OK. The Unidrv and Pscript5 core drivers recognize the S\_DEVCAP\_OUTPUT\_FULL\_REPLACEMENT return value only for device capabilities that use the *pOutput* buffer--in other words, when the *wCapability* parameter is set to one of the following flags:

<dl> DC\_PAPERNAMES  
DC\_PAPERS  
DC\_PAPERSIZE  
DC\_BINNAMES  
DC\_BINS  
DC\_NUP  
DC\_PERSONALITY  
DC\_MEDIAREADY  
DC\_MEDIATYPENAMES  
DC\_MEDIATYPES  
DC\_ENUMRESOLUTIONS  
</dl>

For more information about creating and installing user interface plug-ins, see [Customizing Microsoft's Printer Drivers](https://www.bing.com/search?q=Customizing Microsoft's Printer Drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI**](iprintoemui-interface.md)
</dt> <dt>

[**DrvDeviceCapabilities**](drvdevicecapabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::DeviceCapabilities%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





