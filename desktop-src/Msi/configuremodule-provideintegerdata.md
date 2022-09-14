---
description: The ProvideIntegerData method of the ConfigureModule object is called by Mergemod.dll to retrieve integer data from the client tool.
ms.assetid: 13d48301-bd63-432c-b663-85a840886dda
title: ConfigureModule.ProvideIntegerData method (Mergemod.h)
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

# ConfigureModule.ProvideIntegerData method

The **ProvideIntegerData** method of the [**ConfigureModule object**](configuremodule-object.md) is called by Mergemod.dll to retrieve integer data from the client tool.

Mergemod.dll provides the *Name* from the corresponding entry in the [ModuleConfiguration table](moduleconfiguration-table.md).

The tool should return S\_OK and provide the appropriate customization integer in *ConfigData*.

If the tool does not provide any configuration data for this *Name* value, the function should return S\_FALSE. In this case Mergemod.dll ignores the value of the *ConfigData* argument and uses the Default value from the ModuleConfiguration table.

## Syntax


```JScript
ConfigureModule.ProvideIntegerData(
  Name,
  ConfigData
)
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

Name of item for which data is being retrieved.

</dd> <dt>

*ConfigData* 
</dt> <dd>

Pointer to customization text.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The client may be called no more than once for each record in the [ModuleConfiguration table](moduleconfiguration-table.md). Note that Mergemod.dll never makes multiple calls to the client for the same "Name" value. If no record in the ModuleSubstitution table uses the property, an entry in the ModuleConfiguration table causes no calls to the client.

### C++

See [**ProvideIntegerData function**](/windows/desktop/api/Mergemod/nf-mergemod-imsmconfiguremodule-provideintegerdata).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




