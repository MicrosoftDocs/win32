---
description: The RecordList object is a collection of Record objects. You must verify that the RecordList object exists and is not empty before referencing its properties.
ms.assetid: 7f5ac153-8da1-4dc8-9bb7-defd4e821142
title: RecordList object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RecordList
api_type: 
- COM
api_location: 
- Msi.dll
---

# RecordList object

The **RecordList** object is a collection of [**Record**](record-object.md) objects. You must verify that the **RecordList** object exists and is not empty before referencing its properties.

## Members

The **RecordList** object has these types of members:

-   [Properties](#properties)

### Properties

The **RecordList** object has these properties.



| Property                                     | Description                                                          |
|:---------------------------------------------|:---------------------------------------------------------------------|
| [**Count**](recordlist-count.md)<br/> | Returns the number of items in the **RecordList** object.<br/> |
| [**Item**](recordlist-item.md)<br/>   | Returns a record in a **RecordList** object collection.<br/>   |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecordList is defined as 000C1096-0000-0000-C000-000000000046<br/>                                                                                                                                                                          |



## See also

<dl> <dt>

[**Record**](record-object.md)
</dt> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




