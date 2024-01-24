---
description: The read-only ConfigurableItems property of the Merge object returns a collection ConfigurableItem objects, each of which represents a single row from the ModuleConfiguration table.
ms.assetid: 4d1a64f7-fbd0-4358-8911-112e43f1be4a
title: Merge.ConfigurableItems property (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.ConfigurableItems
- IMsmMerge.get_ConfigurableItems
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.ConfigurableItems property

The read-only **ConfigurableItems** property of the [**Merge**](merge-object.md) object returns a collection [**ConfigurableItem**](configurableitem-object.md) objects, each of which represents a single row from the [ModuleConfiguration table](moduleconfiguration-table.md). Semantically, each interface in the enumerator represents an item that can be configured by the module consumer. The collection is a read-only collection and implements the standard read-only collection interfaces of Item(), Count() and \_NewEnum(). The **IEnumMsmConfigItems** enumerator implements Next(), Skip(), Reset(), and Clone() with the standard semantics.

This property is read-only.

## Syntax


```JScript
propVal = Merge.ConfigurableItems
```



## Property value

## C++

See [**get\_ConfigurableItems**](/windows/desktop/api/Mergemod/nf-mergemod-imsmmerge2-get_configurableitems) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




