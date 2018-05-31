---
Description: The OutboundEventsLevel property indicates the level of detail at which the fax service logs events about outbound fax transmissions in the application log.
ms.assetid: 1181ebb8-c860-4241-8ddc-d64c0ae9183c
title: FaxEventLogging.OutboundEventsLevel property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxEventLogging.OutboundEventsLevel property

The **OutboundEventsLevel** property indicates the level of detail at which the fax service logs events about outbound fax transmissions in the application log.

This property is read/write.

## Syntax


```VB
Property OutboundEventsLevel As Integer
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

 

 




