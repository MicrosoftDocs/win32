---
description: The Persist method of the SummaryInfo object formats and writes the previously stored properties into the standard SummaryInformation stream.
ms.assetid: 77ec1754-73b1-416e-9c9d-72fdbabe16ae
title: SummaryInfo.Persist method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SummaryInfo.Persist
api_type: 
- COM
api_location: 
- Msi.dll
---

# SummaryInfo.Persist method

The **Persist** method of the [**SummaryInfo**](summaryinfo-object.md) object formats and writes the previously stored properties into the standard SummaryInformation stream. It generates an error if the stream cannot be successfully written. This method may only be called once after all the property values have been set. Properties may still be read after the stream is written.

## Syntax


```JScript
SummaryInfo.Persist()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISummaryInfo is defined as 000C109B-0000-0000-C000-000000000046<br/>                                                                                                                                                                         |



 

 




