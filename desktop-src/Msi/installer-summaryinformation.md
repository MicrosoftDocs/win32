---
description: The SummaryInformation property of the Installer object returns a SummaryInfo object that can be used to examine, update, and add properties to the summary information stream of a package or transform.
ms.assetid: 6a1d81b9-d61f-4bff-92c3-35fc436a6a41
title: Installer.SummaryInformation property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.SummaryInformation
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.SummaryInformation property

The **SummaryInformation** property of the [**Installer**](installer-object.md) object returns a [**SummaryInfo**](summaryinfo-object.md) object that can be used to examine, update, and add properties to the summary information stream of a package or transform.

This property is read-only.

## Syntax


```JScript
propVal = Installer.SummaryInformation
```



## Property value

## Remarks

If a value of *maxProperties* greater than 0 is used to open an existing summary information stream, the [**Persist**](summaryinfo-persist.md) method must be called before closing the object. Failing to do this loses the existing stream information.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




