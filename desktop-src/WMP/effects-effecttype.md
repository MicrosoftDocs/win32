---
title: EFFECTS.effectType
description: The effectType method retrieves the registry name of the visualization with the specified registry index. This name is a unique ID defined by the visualization author.
ms.assetid: 47da4f3f-8552-4404-ad46-5dc6afca849a
keywords:
- EFFECTS.effectType Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.effectType
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# EFFECTS.effectType

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **effectType** method retrieves the registry name of the visualization with the specified registry index. This name is a unique ID defined by the visualization author.

``` syntax
        elementID.effectType(index)
```

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number** (**long**) containing the registry index of a visualization.

</dd> </dl>

## Return Value

This method returns a **String**.

## Remarks

This method is useful for switching between visualizations in script. A user interface could display the set of titles, but when the user selects one, the script must use **currentEffectType** to switch visualizations.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> <dt>

[**EFFECTS.currentEffectType**](effects-currenteffecttype.md)
</dt> </dl>

 

 





