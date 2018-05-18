---
Description: 'The Format property of the ConfigurableItem object returns the value from the Format column of the ModuleConfiguration table.'
ms.assetid: 'e75ed650-7309-4e24-9c35-82ebf27d011b'
title: 'ConfigurableItem.Format property'
---

# ConfigurableItem.Format property

The **Format** property of the [**ConfigurableItem**](configurableitem-object.md) object returns the value from the Format column of the [ModuleConfiguration table](moduleconfiguration-table.md).

This property is read-only.

## Syntax


```JScript
propVal = ConfigurableItem.Format
```



## Property value

## Remarks

This property can only have the following values.



| Constant                        | Value |
|---------------------------------|-------|
| **msmConfigurableItemText**     | 0     |
| **msmConfigurableItemKey**      | 1     |
| **msmConfigurableItemInteger**  | 2     |
| **msmConfigurableItemBitfield** | 3     |



 

### C++

See [**get\_Format**](imsmconfigurableitem-get-format.md) function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




