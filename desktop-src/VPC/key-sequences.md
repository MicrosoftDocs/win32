---
title: Key Sequences
description: A key sequence string is a comma-delimited set of key identifiers which are used to simulate the key press and release sequence of a standard U.S. 101-key AT-style keyboard.
ms.assetid: 6f5301d1-af6e-4b43-8884-c76b2300ba92
keywords:
- Windows Virtual PC Virtual PC , key sequences
ms.topic: article
ms.date: 05/31/2018
---

# Key Sequences

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

A key sequence string is a comma-delimited set of key identifiers which are used to simulate the key press and release sequence of a standard U.S. 101-key AT-style keyboard.

If a key identifier appears in the string without a preceding modifier, a key-pressed code is simulated, followed immediately by its corresponding key-released code. Key modifiers can be used to change this behavior.

For example, the **DOWN** modifier will send the key-pressed code for the following key identifier without sending the key-released code. This is useful for simulating Ctrl, Alt, and Shift keys when they are held down while other keys are being sent. To release the key, it must be included in the key string again along with a preceding **UP** modifier.

## Key Identifiers

The following list details the valid key identifier strings. 

| Key identifier string | Meaning                         |
|-----------------------|---------------------------------|
| Key\_Escape           | the **Esc** key                 |
| Key\_F1               | the **F1** key                  |
| Key\_F2               | the **F2** key                  |
| Key\_F3               | the **F3** key                  |
| Key\_F4               | the **F4** key                  |
| Key\_F5               | the **F5** key                  |
| Key\_F6               | the **F6** key                  |
| Key\_F7               | the **F7** key                  |
| Key\_F8               | the **F8** key                  |
| Key\_F9               | the **F9** key                  |
| Key\_F10              | the **F10** key                 |
| Key\_F11              | the **F11** key                 |
| Key\_F12              | the **F12** key                 |
| Key\_SysReq           | the **SysReq** key              |
| Key\_ScrollLock       | the **ScrollLock** key          |
| Key\_Break            | the **Break** key               |
| Key\_LeftApostrophe   | the **\`** key                  |
| Key\_1                | the **1** key                   |
| Key\_2                | the **2** key                   |
| Key\_3                | the **3** key                   |
| Key\_4                | the **4** key                   |
| Key\_5                | the **5** key                   |
| Key\_6                | the **6** key                   |
| Key\_7                | the **7** key                   |
| Key\_8                | the **8** key                   |
| Key\_9                | the **9** key                   |
| Key\_0                | the **0** key                   |
| Key\_Hyphen           | the **-** key                   |
| Key\_Equals           | the **=** key                   |
| Key\_Backspace        | the **Backspace** key           |
| Key\_Insert           | the **Ins** key                 |
| Key\_Home             | the **Home** key                |
| Key\_PageUp           | the **PageUp** key              |
| Key\_NumLock          | the **NumLock** key             |
| KeyPad\_Divide        | the **/** key on the keypad     |
| KeyPad\_Multiply      | the **\*** key on the keypad    |
| KeyPad\_Minus         | the **-** key on the keypad     |
| Key\_Tab              | the **Tab** key                 |
| Key\_Q                | the **Q** key                   |
| Key\_W                | the **W** key                   |
| Key\_E                | the **E** key                   |
| Key\_R                | the **R** key                   |
| Key\_T                | the **T** key                   |
| Key\_Y                | the **Y** key                   |
| Key\_U                | the **U** key                   |
| Key\_I                | the **I** key                   |
| Key\_O                | the **O** key                   |
| Key\_P                | the **P** key                   |
| Key\_LeftBracket      | the **\[** key                  |
| Key\_RightBracket     | the **\]** key                  |
| Key\_Backslash        | the **\\** key                  |
| Key\_Delete           | the **Delete** key              |
| Key\_End              | the **End** key                 |
| Key\_PageDown         | the **PageDown** key            |
| KeyPad\_7             | the **7** key on the keypad     |
| KeyPad\_8             | the **8** key on the keypad     |
| KeyPad\_9             | the **9** key on the keypad     |
| KeyPad\_Plus          | the **+** key on the keypad     |
| Key\_A                | the **A** key                   |
| Key\_S                | the **S** key                   |
| Key\_D                | the **D** key                   |
| Key\_F                | the **F** key                   |
| Key\_G                | the **G** key                   |
| Key\_H                | the **H** key                   |
| Key\_J                | the **J** key                   |
| Key\_K                | the **K** key                   |
| Key\_L                | the **L** key                   |
| Key\_SemiColon        | the **;** key                   |
| Key\_SingleQuote      | the **'** key                   |
| Key\_Enter            | the **Enter** key               |
| KeyPad\_4             | the **4** key on the keypad     |
| KeyPad\_5             | the **5** key on the keypad     |
| KeyPad\_6             | the **6** key on the keypad     |
| Key\_LeftShift        | the **Left Shift** key          |
| Key\_Z                | the **Z** key                   |
| Key\_X                | the **X** key                   |
| Key\_C                | the **C** key                   |
| Key\_V                | the **V** key                   |
| Key\_B                | the **B** key                   |
| Key\_N                | the **N** key                   |
| Key\_M                | the **M** key                   |
| Key\_Comma            | the **,** key                   |
| Key\_Period           | the **.** key                   |
| Key\_Slash            | the **/** key                   |
| Key\_RightShift       | the **Right Shift** key         |
| Key\_Up               | the **Up** key                  |
| KeyPad\_1             | the **1** key on the keypad     |
| KeyPad\_2             | the **2** key on the keypad     |
| KeyPad\_3             | the **3** key on the keypad     |
| KeyPad\_Enter         | the **Enter** key on the keypad |
| Key\_LeftCtrl         | the **Left Ctrl** key           |
| Key\_LeftWindows      | the **Left Windows** key        |
| Key\_LeftAlt          | the **Left Alt** key            |
| Key\_Space            | the **Space** key               |
| Key\_RightAlt         | the **Right Alt** key           |
| Key\_RightWindows     | the **Right Windows** key       |
| Key\_RightCtrl        | the **Right Ctrl** key          |
| Key\_Application      | the **Application** key         |
| Key\_Left             | the **Left** key                |
| Key\_Down             | the **Down** key                |
| Key\_Right            | the **Right** key               |
| KeyPad\_0             | the **0** key on the keypad     |
| KeyPad\_DecimalPoint  | the **.** key on the keypad     |



 

## Key Modifiers

The following list details the valid key modifier strings. 

| Key modifier string | Meaning                                                                                       |
|---------------------|-----------------------------------------------------------------------------------------------|
| DOWN                | Send a key-pressed code for the following key identifier without sending a key-released code. |
| UP                  | Send a key-released code for the following key identifier.                                    |
| HOLD                | Pause 200 milliseconds before continuing to process the remainder of the key sequence string. |



 

## Related topics

<dl> <dt>

[**IVMKeyboard**](ivmkeyboard.md)
</dt> </dl>

 

 