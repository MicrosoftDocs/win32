---
title: Player.KeyDown event
description: The KeyDown event occurs when a key is pressed. | Player.KeyDown event
ms.assetid: a34dafca-5db2-4065-bcfe-d66e633b26fb
keywords:
- KeyDown event Windows Media Player
- KeyDown event Windows Media Player , Player class
- Player class Windows Media Player , KeyDown event
topic_type:
- apiref
api_name:
- Player.KeyDown
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.KeyDown event

The **KeyDown** event occurs when a key is pressed.

## Syntax


```JScript
Player.KeyDown(
  nKeyCode,
  nShiftState
)
```



## Parameters

<dl> <dt>

*nKeyCode* 
</dt> <dd>

**Number** (**int**) specifying which physical key is pressed. For possible values, see the Remarks section.

</dd> <dt>

*nShiftState* 
</dt> <dd>

**Number** (**int**) specifying a bitfield with the least significant bits corresponding to the SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. The shift argument indicates the state of these keys. Some, all, or none of the bits can be set, indicating that some, all, or none of the keys are pressed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The *nKeyCode* argument specifies a physical key. The following tables show the possible values for the major keys on a standard keyboard.

Values for the main keys.



| Key                     | Value   |
|-------------------------|---------|
| A-Z                     | 65-90   |
| 0-9                     | 48-56   |
| F1-F12                  | 112-123 |
| ESC                     | 27      |
| TAB                     | 9       |
| CAPS LOCK               | 20      |
| SHIFT (left or right)   | 16      |
| CTRL (left or right)    | 17      |
| ALT (left or right)     | 18      |
| SPACE                   | 32      |
| BACKSPACE               | 8       |
| ENTER                   | 13      |
| Windows logo key, left  | 91      |
| Windows logo key, right | 92      |
| Application key         | 93      |



 

Values for the number pad keys.



| Key               | Value  |
|-------------------|--------|
| 0-9               | 96-105 |
| NUM LOCK          | 144    |
| DIVIDE (/)        | 111    |
| MULTIPLY (\*)     | 106    |
| SUBTRACT (-)      | 109    |
| ADD (+)           | 107    |
| SEPARATOR (Enter) | 108    |
| DECIMAL (.)       | 110    |



 

Values for the navigation keys.



| Key         | Value |
|-------------|-------|
| INSERT      | 45    |
| DELETE      | 46    |
| HOME        | 36    |
| END         | 35    |
| PAGE UP     | 33    |
| PAGE DOWN   | 34    |
| UP ARROW    | 38    |
| DOWN ARROW  | 40    |
| LEFT ARROW  | 37    |
| RIGHT ARROW | 39    |



 

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





