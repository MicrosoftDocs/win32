---
Description: The LogIncoming property is a Boolean value that indicates whether the fax service logs entries for incoming faxes in the activity log database.
ms.assetid: ba8e21f5-1284-4088-aa57-4111e03615b6
title: FaxActivityLogging.LogIncoming property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxActivityLogging.LogIncoming property

The **LogIncoming** property is a Boolean value that indicates whether the fax service logs entries for incoming faxes in the activity log database.

This property is read/write.

## Syntax


```VB
Property LogIncoming As Boolean
```



## Property value

A **Boolean** that specifies or receives a value indicating whether the fax service logs entries for incoming faxes in the activity log database.

## Remarks

If this property is equal to **True**, the fax service logs entries for incoming fax jobs in the activity log database. If this property is equal to **False**, the fax service does not log entries.

To read or write to this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**FaxActivityLogging**](-mfax-faxactivitylogging.md)
</dt> <dt>

[**IFaxActivityLogging**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxactivitylogging)
</dt> </dl>

 

 




