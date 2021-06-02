---
title: THEME.loadPreference
description: The loadPreference method loads a preference from the registry.
ms.assetid: 51d6b0f8-f1fd-4999-a575-0b7c177b2bc8
keywords:
- THEME.loadPreference Windows Media Player
topic_type:
- apiref
api_name:
- THEME.loadPreference
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# THEME.loadPreference

The **loadPreference** method loads a preference from the registry.

``` syntax
        theme.loadPreference(theKey)
```

## Parameters

<dl> <dt>

<span id="theKey"></span><span id="thekey"></span><span id="THEKEY"></span>*theKey*
</dt> <dd>

A **String** specifying the key of the preference value to load.

</dd> </dl>

## Return Value

This method returns a **String**.

## Remarks

A preference is a key/value pair that can be stored in the registry to retain information about the state of the Windows Media Player between runs. This feature can be used, for example, to save customization settings so that they won't have to be re-entered each time Windows Media Player is started.

Preferences are not encrypted and therefore are not a secure method for persisting data. Do not use preferences to store private data.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**THEME Element**](theme-element.md)
</dt> <dt>

[**THEME.savePreference**](theme-savepreference.md)
</dt> </dl>

 

 





