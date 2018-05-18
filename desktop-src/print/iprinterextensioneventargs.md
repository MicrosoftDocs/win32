---
Description: 'Represents the context for the desktop printer extension activation.'
ms.assetid: '77850B5A-4E24-4057-B87F-D964620ABF94'
title: IPrinterExtensionEventArgs interface
---

# IPrinterExtensionEventArgs interface

Represents the context for the desktop printer extension activation.

## Members

The **IPrinterExtensionEventArgs** interface inherits from [**IPrinterExtensionContext**](iprinterextensioncontext-interface.md). **IPrinterExtensionEventArgs** also has these types of members:

-   [Properties](#properties)

### Properties

The **IPrinterExtensionEventArgs** interface has these properties.



| Property                                                                             | Access type          | Description                                                                                                                                |
|:-------------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**BidiNotification**](iprinterextensioneventargs-bidinotification.md)<br/>   | Read-only<br/> | Gets the text of the bidirectional communication (Bidi) notification, if applicable.<br/>                                            |
| [**DetailedReasonId**](iprinterextensioneventargs-detailedreasonid.md)<br/>   | Read-only<br/> | Gets a more detailed activation reason than what can be retrieved from [**ReasonId**](iprinterextensioneventargs-reasonid.md).<br/> |
| [**ReasonId**](iprinterextensioneventargs-reasonid.md)<br/>                   | Read-only<br/> | Gets the reason why the printer extension was activated.<br/>                                                                        |
| [**Request**](iprinterextensioneventargs-request.md)<br/>                     | Read-only<br/> | Gets the [**IPrinterExtensionRequest**](iprinterextensionrequest-interface.md) object for the current event.<br/>                   |
| [**SourceApplication**](iprinterextensioneventargs-sourceapplication.md)<br/> | Read-only<br/> | Gets the name of the application that invoked the printer extension.<br/>                                                            |
| [**WindowModal**](iprinterextensioneventargs-windowmodal.md)<br/>             | Read-only<br/> | Gets the run mode parameter that determines whether or not the printer extension should be run as modal.<br/>                        |
| [**WindowParent**](iprinterextensioneventargs-windowparent.md)<br/>           | Read-only<br/> | Gets the handle of the parent window.<br/>                                                                                           |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterExtensionContext**](iprinterextensioncontext-interface.md)
</dt> <dt>

[V4 Printer Driver Property Bags](print.v4_driver_property_bags)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterExtensionEventArgs%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





