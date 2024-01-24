---
description: The SummaryInfo object is used to read, create, and update document properties from the summary information stream of a storage object.
ms.assetid: 296e90d2-84b8-4c9e-8716-be90f94294ee
title: SummaryInfo object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SummaryInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# SummaryInfo object

The **SummaryInfo** object is used to read, create, and update document properties from the [summary information stream](summary-information-stream.md) of a storage object.

## Members

The **SummaryInfo** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SummaryInfo** object has these methods.



| Method                                 | Description                                                                                                                                    |
|:---------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**Persist**](summaryinfo-persist.md) | Formats and writes the previously stored properties into the standard [summary information stream](summary-information-stream.md).<br/> |



 

### Properties

The **SummaryInfo** object has these properties.



| Property                                                                             | Description                                                                                     |
|:-------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Property Property (SummaryInfo Object)**](summaryinfo-summaryinfo.md)<br/> | Gets or sets the value for the specified property in the summary information stream.<br/> |
| [**PropertyCount**](summaryinfo-propertycount.md)<br/>                        | Indicates the current number of property values in the summary information object.<br/>   |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISummaryInfo is defined as 000C109B-0000-0000-C000-000000000046<br/>                                                                                                                                                                         |



## See also

<dl> <dt>

[**SummaryInformation Property (Database Object)**](database-summaryinformation.md)
</dt> <dt>

[**SummaryInformation Property (Installer Object)**](installer-summaryinformation.md)
</dt> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




