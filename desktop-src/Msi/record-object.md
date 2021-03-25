---
description: The Record object is a container for holding and transferring a variable number of values.
ms.assetid: e832c19f-61a6-4e42-a10a-b7bb1705af59
title: Record object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Record
api_type: 
- COM
api_location: 
- Msi.dll
---

# Record object

The **Record** object is a container for holding and transferring a variable number of values. Fields within the record are numerically indexed and can contain strings, integers, objects, and null values. Fields beyond the allocated record size are treated as having permanently null values. Field number 0 is reserved.

## Members

The **Record** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Record** object has these methods.



| Method                                  | Description                                                                                          |
|:----------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**ClearData**](record-cleardata.md)   | Clears the data in all fields, setting them to null.<br/>                                      |
| [**FormatText**](record-formattext.md) | Formats fields according to the template in field 0.<br/>                                      |
| [**ReadStream**](record-readstream.md) | Reads a specified number of bytes from a record field holding stream data.<br/>                |
| [**SetStream**](record-setstream.md)   | Copies the content of the specified file into the designated record field as stream data.<br/> |



 

### Properties

The **Record** object has these properties.



| Property                                             | Access type           | Description                                                                                   |
|:-----------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------|
| [**DataSize**](record-datasize.md)<br/>       |                       | Returns the size of the data for the designated field.<br/>                             |
| [**FieldCount**](record-fieldcount.md)<br/>   |                       | Returns the number of fields in the record.<br/>                                        |
| [**IntegerData**](record-integerdata.md)<br/> | Read/write<br/> | Transfers 32-bit integer data in to or out of a specified field within the record.<br/> |
| [**IsNull**](record-isnull.md)<br/>           |                       | Returns True if the indicated field is null and False if the field contains data.<br/>  |
| [**StringData**](record-stringdata.md)<br/>   | Read/write<br/> | Transfers string data in to or out of a specified field within the record.<br/>         |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecord is defined as 000C1093-0000-0000-C000-000000000046<br/>                                                                                                                                                                              |



## See also

<dl> <dt>

[**CreateRecord Method**](installer-createrecord.md)
</dt> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




