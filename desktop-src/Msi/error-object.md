---
description: The Error object returns the information of a single merge error.
ms.assetid: 38025e21-2d31-40f8-a088-2d3912c2893e
title: Error object (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Error
- IMsmError
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Error object

The **Error** object returns the information of a single merge error.

## Members

The **Error** object has these types of members:

-   [Properties](#properties)

### Properties

The **Error** object has these properties.



| Property                                                | Description                                                                                 |
|:--------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**DatabaseKeys**](error-databasekeys.md)<br/>   | Returns the primary keys of the row in the database table that caused the error.<br/> |
| [**DatabaseTable**](error-databasetable.md)<br/> | Returns the table name of the table in the database causing the error.<br/>           |
| [**Language**](error-language.md)<br/>           | Return the language of the error.<br/>                                                |
| [**ModuleKeys**](error-modulekeys.md)<br/>       | Returns the primary keys of the row in the module table that caused the error.<br/>   |
| [**ModuleTable**](error-moduletable.md)<br/>     | Returns the table name of the table in the module causing the error.<br/>             |
| [**Path**](error-path.md)<br/>                   | Return the path to the file or directory causing the error. Currently unused.<br/>    |
| [**Type**](error-type.md)<br/>                   | Return the type of error.<br/>                                                        |



 

## C++

interface **IMsmError : IDispatch**

## Interface ID



| Constant           | Value                                  |
|--------------------|----------------------------------------|
| **IID\_IMsmError** | {0ADDA828-2C26-11D2-AD65-00A0C9AF11A6} |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




