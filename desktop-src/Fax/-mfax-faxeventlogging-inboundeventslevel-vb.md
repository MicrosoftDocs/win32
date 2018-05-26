---
Description: The InboundEventsLevel property indicates the level of detail at which the fax service logs events about inbound fax transmissions in the application log.
ms.assetid: c89bf14b-f6c6-4782-a14a-41dabbe5e349
title: FaxEventLogging.InboundEventsLevel property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxEventLogging.InboundEventsLevel property

The **InboundEventsLevel** property indicates the level of detail at which the fax service logs events about inbound fax transmissions in the application log.

This property is read/write.

## Syntax


```VB
Property InboundEventsLevel As Integer
```



## Property value

A variable of type [**FAX\_LOG\_LEVEL\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_log_level_enum?branch=master) that specifies or receives the logging level. For possible values, see [**FAX\_LOG\_LEVEL\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_log_level_enum?branch=master).

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

[**IFaxEventLogging**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxeventlogging?branch=master)
</dt> </dl>

 

 




