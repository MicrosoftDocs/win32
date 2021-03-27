---
description: The GetFiles object retrieves the files needed in a particular language of the module. Requires certain actions be performed through the Merge object before all parts of this interface returns valid results.
ms.assetid: f3bf64ec-75f7-43a6-bbd8-a51508c57002
title: GetFiles object (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFiles
- IMsmGetFiles
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# GetFiles object

The **GetFiles** object retrieves the files needed in a particular language of the module. Requires certain actions be performed through the [Merge object](merge-object.md) before all parts of this interface returns valid results.

## Members

The **GetFiles** object has these types of members:

-   [Properties](#properties)

### Properties

The **GetFiles** object has these properties.



| Property                                               | Description                                                                                                                                                     |
|:-------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ModuleFiles**](getfiles-modulefiles.md)<br/> | [**ModuleFiles**](getfiles-modulefiles.md) property returns all the primary keys of the [File table](file-table.md) for the currently open module.<br/> |



 

## C++

interface **IMsmGetFiles : IDispatch**

## Interface ID



| Constant              | Value                                  |
|-----------------------|----------------------------------------|
| **IID\_IMsmGetFiles** | {7041AE26-2D78-11D2-888A-00A0C981B015} |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




