---
title: KeyDown Event of the AxWindowsMediaPlayer Object
description: The KeyDown event occurs when a key is pressed. | KeyDown Event of the AxWindowsMediaPlayer Object
ms.assetid: e67b9628-6c53-4893-921a-9487ebfc1cd5
keywords:
- KeyDown Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- KeyDown Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# KeyDown Event of the AxWindowsMediaPlayer Object

The KeyDown event occurs when a key is pressed.

``` syntax
[C#]
private void player_KeyDownEvent(
  object sender,
  _WMPOCXEvents_KeyDownEvent e
)

[Visual Basic]
Private Sub player_KeyDownEvent(  
  sender As Object, 
  e As _WMPOCXEvents_KeyDownEvent
) Handles player.KeyDownEvent
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_KeyDownEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_KeyDownEvent**, which contains the following properties related to this event.



| Property    | Description                                                                                                                                                                                                                                                                                                                                                                          |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nKeyCode    | System.Int16Specifies which physical key is pressed. For possible values, see Remarks.<br/>                                                                                                                                                                                                                                                                                    |
| nShiftState | System.Int16A bitfield with the least significant bits corresponding to the SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. The shift argument indicates the state of these keys. Some, all, or none of the bits can be set, indicating that some, all, or none of the keys are pressed.<br/> |



 

## Remarks

The **nKeyCode** property specifies a physical key. The following tables show the possible values for the major keys on a standard keyboard.

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



 

## Requirements



|                      |                                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> </dl>

 

 





