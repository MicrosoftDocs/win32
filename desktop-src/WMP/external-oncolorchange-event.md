---
title: External.OnColorChange Event
description: Note This topic describes functionality designed for use by online stores. | External.OnColorChange Event
ms.assetid: f2cd44b1-c813-479b-b847-96ddb9572697
keywords:
- External.OnColorChange Event Windows Media Player
topic_type:
- apiref
api_name:
- External.OnColorChange Event
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.OnColorChange Event

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **OnColorChange** event occurs when the color of the Windows Media Player user interface changes.

``` syntax
window.external.OnColorChange = FunctionName
```

## Possible Values

This is a write-only property that specifies the name of the function in script that Windows Media Player calls when the event occurs.

## Parameters

The function that handles this event takes no parameters.

## Remarks

Users can change the color of the Windows Media Player user interface. You can use this event to customize the appearance of your hosted webpage to match the Player.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 2 Online Stores**](external-object-for-type-2-online-stores.md)
</dt> </dl>

 

 





