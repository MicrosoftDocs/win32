---
description: The ProvideTextData method is called by Mergemod.dll to retrieve text data from the client tool. Mergemod.dll provides the Name from the corresponding entry in the ModuleConfiguration table.
ms.assetid: 286b0b58-1b6a-4d41-89e1-eb9c23bdd788
title: ConfigureModule.ProvideTextData method (Mergemod.h)
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

# ConfigureModule.ProvideTextData method

The **ProvideTextData** method is called by Mergemod.dll to retrieve text data from the client tool. Mergemod.dll provides the *Name* from the corresponding entry in the ModuleConfiguration table.

The tool should return S\_OK and provide the appropriate customization text in ConfigData. The client tool is responsible for allocating the data, but Mergemod.dllis responsible for releasing the memory. This argument MUST be a **BSTR** object. **LPCWSTR** is NOT accepted.

If the tool does not provide any configuration data for this *Name* value, the function should return S\_FALSE. In this case Mergemod.dll ignores the value of the ConfigData argument and uses the Default value from the ModuleConfiguration table.

Any return code other than S\_OK or S\_FALSE will cause an error to be logged (if a log is open) and will result in the merge failing.

Because this function follows standard **BSTR** convention, null is equivalent to the empty string.

## Syntax


```JScript
ConfigureModule.ProvideTextData(
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

See [**ProvideTextData function**](/windows/desktop/api/Mergemod/nf-mergemod-imsmconfiguremodule-providetextdata).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




