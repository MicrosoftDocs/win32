---
description: The ReadStream method of the Record object reads a specified number of bytes from a record field that contains stream data.
ms.assetid: 845e23e5-6379-4592-aee4-cd6832baf335
title: Record.ReadStream method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Record.ReadStream
api_type: 
- COM
api_location: 
- Msi.dll
---

# Record.ReadStream method

The **ReadStream** method of the [**Record**](record-object.md) object reads a specified number of bytes from a record field that contains stream data.

## Syntax


```JScript
Record.ReadStream(
  field,
  length,
  format
)
```



## Parameters

<dl> <dt>

*field* 
</dt> <dd>

The required field number of the value within the record, 1-based.

</dd> <dt>

*length* 
</dt> <dd>

The required number of bytes to read from the stream.

</dd> <dt>

*format* 
</dt> <dd>

Required interpretation and return of the data bytes.



| Parameter name                                                                                                                                                                                                                                                                  | Meaning                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <span id="msiReadStreamInteger"></span><span id="msireadstreaminteger"></span><span id="MSIREADSTREAMINTEGER"></span><dl> <dt>**msiReadStreamInteger**</dt> <dt>0</dt> </dl> | As a long integer the length must be 1 to 4.<br/>             |
| <span id="msiReadStreamBytes"></span><span id="msireadstreambytes"></span><span id="MSIREADSTREAMBYTES"></span><dl> <dt>**msiReadStreamBytes**</dt> <dt>1</dt> </dl>         | The data as a **BSTR**—one byte per character.<br/>           |
| <span id="msiReadStreamAnsi"></span><span id="msireadstreamansi"></span><span id="MSIREADSTREAMANSI"></span><dl> <dt>**msiReadStreamAnsi**</dt> <dt>2</dt> </dl>             | The ANSI bytes translated to a Unicode **BSTR**.<br/>         |
| <span id="msiReadStreamDirect"></span><span id="msireadstreamdirect"></span><span id="MSIREADSTREAMDIRECT"></span><dl> <dt>**msiReadStreamDirect**</dt> <dt>3</dt> </dl>     | The byte pairs that are returned directly as a **BSTR**.<br/> |



 

</dd> </dl>

## Return value

This method returns a string that contains the requested number of bytes read from a record field.

## Remarks

The returned value of a nonexistent field is an Empty value. If the stream has fewer bytes that the count requested, the returned string is shortened appropriately.

For an example of this method, see [Copy ANSI File Into a Database Field](copy-ansi-file-into-a-database-field.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecord is defined as 000C1093-0000-0000-C000-000000000046<br/>                                                                                                                                                                              |



 

 




