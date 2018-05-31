---
Description: The FaxLoggingOptions configuration object is used by a fax client application to access and configure the event logging categories and the activity logging options that the fax service is using.
ms.assetid: 438e4e89-88c9-431d-b774-98e65cf57064
title: FaxLoggingOptions object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxLoggingOptions object

The **FaxLoggingOptions** configuration object is used by a fax client application to access and configure the event logging categories and the activity logging options that the fax service is using.

A **FaxLoggingOptions** object is accessed through a [**FaxServer**](-mfax-faxserver.md) object. **FaxLoggingOptions** objects provide access to [**FaxActivityLogging**](-mfax-faxactivitylogging.md) objects and [**FaxEventLogging**](-mfax-faxeventlogging.md) objects.

![faxserver, faxloggingoptions, faxactivitylogging, and faxeventlogging objects](images/faxloggingoptions.png)

## Members

The **FaxLoggingOptions** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxLoggingOptions** object has these properties.



| Property                                                                         | Access type          | Description                                                                                                                                                                              |
|:---------------------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivityLogging**](-mfax-faxloggingoptions-activitylogging-vb.md)<br/> | Read-only<br/> | The [**ActivityLogging**](-mfax-faxloggingoptions-activitylogging-vb.md) property retrieves the [**FaxActivityLogging**](-mfax-faxactivitylogging.md) configuration object.<br/> |
| [**EventLogging**](-mfax-faxloggingoptions-eventlogging-vb.md)<br/>       | Read-only<br/> | The [**EventLogging**](-mfax-faxloggingoptions-eventlogging-vb.md) property retrieves the [**FaxEventLogging**](-mfax-faxeventlogging.md) configuration object.<br/>             |



 

## Remarks

To create a **FaxLoggingOptions** object in Microsoft Visual Basic, call the [**LoggingOptions**](-mfax-faxserver-loggingoptions.md) property of the [**FaxServer**](-mfax-faxserver.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxLoggingOptions<br/>                                                     |



## See also

<dl> <dt>

[Fax Service Extended COM Object Model](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxLoggingOptions**](-mfax-faxloggingoptions-cpp.md)
</dt> </dl>

 

 




