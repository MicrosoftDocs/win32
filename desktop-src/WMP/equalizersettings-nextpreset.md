---
title: EQUALIZERSETTINGS.nextPreset
description: The nextPreset method applies the next equalizer preset.
ms.assetid: 67d40ec9-2744-4d63-aa56-0ee20496e896
keywords:
- EQUALIZERSETTINGS.nextPreset Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.nextPreset
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EQUALIZERSETTINGS.nextPreset

The **nextPreset** method applies the next equalizer preset.

``` syntax
        elementID.nextPreset()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Remarks

If the current preset is the last one available, the first preset is made current.

## Examples


```JScript
<SUBVIEW id="eqtray">
  <EQUALIZERSETTINGS id="eq"/>
  <BUTTON
    id="nextPreset" 
    onClick="eq.nextPreset();"
  />
  <BUTTON
    id="prevPreset" 
    onClick="eq.previousPreset();"
  />
  <TEXT
    id="currentPreset" 
    value="wmpprop:eq.currentPresetTitle" 
  />
</SUBVIEW>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.previousPreset**](equalizersettings-previouspreset.md)
</dt> </dl>

 

 





