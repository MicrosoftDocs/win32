---
Description: The FaxEventLogging configuration object is used by a fax client application to configure the event logging categories used by the fax service. You can specify the level of detail at which the fax service logs events in the application log.
ms.assetid: c46f1b55-8211-4c9b-a622-356f2ea2db36
title: FaxEventLogging object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxEventLogging object

The **FaxEventLogging** configuration object is used by a fax client application to configure the event logging categories used by the fax service. You can specify the level of detail at which the fax service logs events in the application log.

## Members

The **FaxEventLogging** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxEventLogging** object has these methods.



| Method                                              | Description                                                                                                                                     |
|:----------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Refresh**](-mfax-faxeventlogging-refresh-vb.md) | The [**Refresh**](-mfax-faxeventlogging-refresh-vb.md) method refreshes **FaxEventLogging** object information from the fax server.<br/> |
| [**Save**](-mfax-faxeventlogging-save-vb.md)       | The [**Save**](-mfax-faxeventlogging-save-vb.md) method saves the **FaxEventLogging** object's data.<br/>                                |



 

### Properties

The **FaxEventLogging** object has these properties.



| Property                                                                               | Access type           | Description                                                                                                                                                                                                                                                                                                                        |
|:---------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GeneralEventsLevel**](-mfax-faxeventlogging-generaleventslevel-vb.md)<br/>   | Read/write<br/> | The [**GeneralEventsLevel**](-mfax-faxeventlogging-generaleventslevel-vb.md) property indicates the level of detail at which the fax service logs general events in the application log. General events include those that are not related to initialization and termination or to inbound and outbound transmissions.<br/> |
| [**InboundEventsLevel**](-mfax-faxeventlogging-inboundeventslevel-vb.md)<br/>   | Read/write<br/> | The [**InboundEventsLevel**](-mfax-faxeventlogging-inboundeventslevel-vb.md) property indicates the level of detail at which the fax service logs events about inbound fax transmissions in the application log.<br/>                                                                                                       |
| [**InitEventsLevel**](-mfax-faxeventlogging-initeventslevel-vb.md)<br/>         | Read/write<br/> | The [**InitEventsLevel**](-mfax-faxeventlogging-initeventslevel-vb.md) property indicates the level of detail at which the fax service logs initialization (starting the server) and termination (shutting down the server) events in the application log.<br/>                                                             |
| [**OutboundEventsLevel**](-mfax-faxeventlogging-outboundeventslevel-vb.md)<br/> | Read/write<br/> | The [**OutboundEventsLevel**](-mfax-faxeventlogging-outboundeventslevel-vb.md) property indicates the level of detail at which the fax service logs events about outbound fax transmissions in the application log.<br/>                                                                                                    |



 

## Remarks

> [!Note]  
> Changes made to the **FaxEventLogging** object will not be saved until you call the [**Save**](-mfax-faxeventlogging-save-vb.md) method.

 

A **FaxEventLogging** object is accessed through a [**FaxLoggingOptions**](-mfax-faxloggingoptions.md) object.

![faxserver, faxloggingoptions, faxactivitylogging, and faxeventlogging objects](images/faxeventlogging.png)

To create a **FaxEventLogging** object in Microsoft Visual Basic, call the [**EventLogging**](-mfax-faxloggingoptions-eventlogging-vb.md) property of the [**FaxLoggingOptions**](-mfax-faxloggingoptions.md) object.

To create a **FaxEventLogging** object in C++, call the [**EventLogging**](-mfax-faxloggingoptions-eventlogging-vb.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxEventLogging<br/>                                                       |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxEventLogging**](-mfax-faxeventlogging-cpp.md)
</dt> </dl>

 

 




