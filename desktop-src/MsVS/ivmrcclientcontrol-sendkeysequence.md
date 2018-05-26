---
title: IVMRCClientControl SendKeySequence method
description: The SendKeySequence method simulates a sequence of keys typed in the guest with the current input focus.
ms.assetid: c06860aa-a90e-4bd7-8441-04c15bb375a3
keywords:
- SendKeySequence method Virtual Server
- SendKeySequence method Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , SendKeySequence method
- SendKeySequence method Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , SendKeySequence method
topic_type:
- apiref
api_name:
- IVMRCClientControl.SendKeySequence
- VMRCClientControl.SendKeySequence
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMRCClientControl::SendKeySequence method

The **SendKeySequence** method simulates a sequence of keys typed in the guest with the current input focus.

## Syntax


```C++
HRESULT SendKeySequence(
  [in] BSTR keySequence
);
```



## Parameters

<dl> <dt>

*keySequence* \[in\]
</dt> <dd>

A comma-delimited sequence of key identifiers.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                  | Description                                                                                             |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The operation was successful.<br/>                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *keySequence* parameter was **NULL** or contained an invalid key identifier or sequence.<br/> |



 

## Remarks

A key sequence string is a comma-delimited set of key identifiers which are used to simulate the key press and release sequence of a standard U.S. 101-key AT-style keyboard.

If a key identifier appears in the string without a preceding modifier, a key-pressed code is sent to the VMRC server, followed immediately by its corresponding key-released code. Key modifiers can be used to change this behavior.

For example, the **DOWN** modifier will send the key-pressed code for the following key identifier without sending the key-released code. This is useful for simulating Ctrl, Alt, and Shift keys when they are held down while other keys are being sent. To release the key, it must be included in the key string again along with a preceding **UP** modifier.

The [Key Identifiers Reference](key-identifiers-reference.md) topic contains a list of valid key identifier and key modifier strings.

## Examples

The following example will cause the control to send "Hello World!" to the VMRC server.


```C++
BSTR bHello = (BSTR) "DOWN,Key_LeftShift,Key_H,UP,Key_LeftShift,Key_E,"
              "Key_L,Key_L,Key_O,Key_Space,DOWN,Key_LeftShift,"
              "Key_W,UP,Key_LeftShift,Key_O,Key_R,Key_L,Key_D,"
              "DOWN,Key_LeftShift,Key_1,UP,Key_Left_Shift";

HRESULT hr = pIVMRCClientControl->SendKeySequence(bHello);
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> <dt>

[Key Identifiers Reference](key-identifiers-reference.md)
</dt> </dl>

 

 





