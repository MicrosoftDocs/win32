---
description: The Dependency object returns a module that the current module is dependent upon and which has not yet been merged into the current installation database.
ms.assetid: 3157f07d-99de-4628-9b03-eb86eb4896a4
title: Dependency object (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Dependency
- IMsmDependency
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Dependency object

The **Dependency** object returns a module that the current module is dependent upon and which has not yet been merged into the current installation database.

## Members

The **Dependency** object has these types of members:

-   [Properties](#properties)

### Properties

The **Dependency** object has these properties.



| Property                                           | Description                                             |
|:---------------------------------------------------|:--------------------------------------------------------|
| [**Language**](dependency-language.md)<br/> | Return the language of the module.<br/>           |
| [**Module**](dependency-module.md)<br/>     | Return the module ID of the required module.<br/> |
| [**Version**](dependency-version.md)<br/>   | Return the version of the required module.<br/>   |



 

## C++

interface **IMsmDependency : IDispatch**

## Interface ID



| Constant                | Value                                  |
|-------------------------|----------------------------------------|
| **IID\_IMsmDependency** | {0ADDA82D-2C26-11D2-AD65-00A0C9AF11A6} |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




