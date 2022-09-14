---
description: The ConfigureModule object is an interface implemented by the client.
ms.assetid: f6240837-7685-4bfe-8a2f-b4428014702a
title: ConfigureModule object (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ConfigureModule
- IMsmConfigureModule
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# ConfigureModule object

The **ConfigureModule object** is an interface implemented by the client. Mergemod.dllcalls methods on the **IMsmConfigureModule** interface to request that the client tool provide configuration information. The module is configured based on the client's responses to calls on this interface.

## Members

The **ConfigureModule** object has these types of members:

-   [Methods](#methods)

### Methods

The **ConfigureModule** object has these methods.



| Method                                                           | Description                                                                        |
|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| [**ProvideIntegerData**](configuremodule-provideintegerdata.md) | Called by Mergemod.dll to obtain integers used to configure the module.<br/> |
| [**ProvideTextData**](configuremodule-providetextdata.md)       | Called by Mergemod.dll to obtain text used to configure the module.<br/>     |



 

## Remarks

### C++

interface **IMsmConfigureModule : IDispatch**

### Interface ID



| Constant                     | Value                                  |
|------------------------------|----------------------------------------|
| **IID\_IMsmConfigureModule** | {AC013209-18A7-4851-8A21-2353443D70A0} |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




