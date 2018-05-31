---
Description: The GeneralEventsLevel property indicates the level of detail at which the fax service logs general events in the application log.
ms.assetid: 2906d487-b4fc-4821-872b-ab1702bf17be
title: FaxEventLogging.GeneralEventsLevel property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxEventLogging.GeneralEventsLevel property

The **GeneralEventsLevel** property indicates the level of detail at which the fax service logs general events in the application log. General events include those that are not related to initialization and termination or to inbound and outbound transmissions.

This property is read/write.

## Syntax


```VB
Property GeneralEventsLevel As Integer
```



## Property value

A variable of type [**FAX\_LOG\_LEVEL\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_log_level_enum) that specifies or receives the logging level. For possible values, see [**FAX\_LOG\_LEVEL\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_log_level_enum).

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**IFaxEventLogging**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxeventlogging)
</dt> </dl>

 

 




