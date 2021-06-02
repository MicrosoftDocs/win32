---
description: The SummaryInformation property of the Database object returns a SummaryInfo object that can be used to examine, update, and add properties to the summary information stream.
ms.assetid: 6892a8c0-c99e-4dcb-b6cb-d470ffceab69
title: Database.SummaryInformation property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.SummaryInformation
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.SummaryInformation property

The **SummaryInformation** property of the [**Database**](database-object.md) object returns a [**SummaryInfo**](summaryinfo-object.md) object that can be used to examine, update, and add properties to the [summary information stream](summary-information-stream.md).

This property is read-only.

## Syntax


```JScript
propVal = Database.SummaryInformation
```



## Property value

The maximum number of properties to be added or modified. This parameter is required and used to allocate sufficient working memory during the stream generation. It is not required to store this number of properties. A value of zero must be used if the database is opened read-only to prevent the stream from being updated.

## Remarks

If a value of *maxProperties* greater than 0 is used to open an existing summary information stream, the [**Persist**](summaryinfo-persist.md) method must be called before closing the object. Failing to do this will lose the existing stream information.

If the property fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



 

 




