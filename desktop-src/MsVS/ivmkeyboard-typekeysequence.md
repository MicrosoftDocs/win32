---
title: IVMKeyboard TypeKeySequence method
description: The TypeKeySequence method simulates the given series of keys being typed (pressed and then released) inside the virtual machine.
ms.assetid: b8c171f7-c109-4477-ac2d-655773e2036f
keywords:
- TypeKeySequence method Virtual Server
- TypeKeySequence method Virtual Server , IVMKeyboard interface
- IVMKeyboard interface Virtual Server , TypeKeySequence method
- TypeKeySequence method Virtual Server , VMKeyboard interface
- VMKeyboard interface Virtual Server , TypeKeySequence method
topic_type:
- apiref
api_name:
- IVMKeyboard.TypeKeySequence
- VMKeyboard.TypeKeySequence
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMKeyboard::TypeKeySequence method

The **TypeKeySequence** method simulates the given series of keys being typed (pressed and then released) inside the virtual machine.

## Syntax


```C++
HRESULT TypeKeySequence(
  [in] BSTR keySequence
);
```



## Parameters

<dl> <dt>

*keySequence* \[in\]
</dt> <dd>

The comma-delimited sequence of key codes to be typed inside the virtual machine.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                       | Description                                                                 |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *keySequence* parameter is **NULL**.<br/>                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>      | The given text string is empty, or contains an invalid key code.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                                    |



 

## Remarks

A key sequence string is a comma-delimited set of key identifiers which are used to simulate the key press and release sequence of a standard U.S. 101-key AT-style keyboard.

If a key identifier appears in the string without a preceding modifier, a key-pressed code is sent to the virtual machine session, followed immediately by its corresponding key-released code. Key modifiers can be used to change this behavior.

For example, the **DOWN** modifier will send the key-pressed code for the following key identifier without sending the key-released code. This is useful for simulating Ctrl, Alt, and Shift keys when they are held down while other keys are being sent. To release the key, it must be included in the key string again along with a preceding **UP** modifier.

The [Key Identifiers Reference](key-identifiers-reference.md) topic contains a list of valid key identifier and key modifier strings.

## Examples

The following example will send "Hello World!" to the virtual machine session.


```C++
BSTR bHello = (BSTR) "DOWN,Key_LeftShift,Key_H,UP,Key_LeftShift,Key_E,"
              "Key_L,Key_L,Key_O,Key_Space,DOWN,Key_LeftShift,"
              "Key_W,UP,Key_LeftShift,Key_O,Key_R,Key_L,Key_D,"
              "DOWN,Key_LeftShift,Key_1,UP,Key_Left_Shift";

HRESULT hr = pIVMKeyboard->TypeKeySequence(bHello);
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMKeyboard**](ivmkeyboard.md)
</dt> <dt>

[Key Identifiers Reference](key-identifiers-reference.md)
</dt> </dl>

 

 





