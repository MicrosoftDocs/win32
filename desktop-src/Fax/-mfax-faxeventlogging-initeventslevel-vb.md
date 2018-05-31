---
Description: The InitEventsLevel property indicates the level of detail at which the fax service logs initialization (starting the server) and termination (shutting down the server) events in the application log.
ms.assetid: 73a4d3cf-4972-4ec3-9cd4-338ab8a7f123
title: FaxEventLogging.InitEventsLevel property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxEventLogging.InitEventsLevel property

The **InitEventsLevel** property indicates the level of detail at which the fax service logs initialization (starting the server) and termination (shutting down the server) events in the application log.

This property is read/write.

## Syntax


```VB
Property InitEventsLevel As Integer
```



## Property value

A variable of type [**FAX\_LOG\_LEVEL\_ENUM**](-mfax-fax-log-level-enum.md) that specifies or receives the logging level. For possible values, see [**FAX\_LOG\_LEVEL\_ENUM**](-mfax-fax-log-level-enum.md).

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-setting-logging-options.md)
</dt> <dt>

[**FaxEventLogging**](-mfax-faxeventlogging.md)
</dt> <dt>

[**IFaxEventLogging**](-mfax-faxeventlogging-cpp.md)
</dt> </dl>

 

 




