---
title: IVMKeyboard interface
description: The IVMKeyboard interface controls the keyboard device within a virtual machine. The IVMKeyboard for a virtual machine can be retrieved using the IVMVirtualMachine Keyboard property.
ms.assetid: 8a764387-5daa-44e3-bb54-ceafe2f7d7db
keywords:
- IVMKeyboard interface Virtual Server
- IVMKeyboard interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMKeyboard
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMKeyboard interface

The **IVMKeyboard** interface controls the keyboard device within a virtual machine. The **IVMKeyboard** for a virtual machine can be retrieved using the [**IVMVirtualMachine::Keyboard**](ivmvirtualmachine-keyboard.md) property.

## When to use

Keys can be typed into the virtual machine in several ways. To type a normal ASCII sequence of characters, use the [**TypeAsciiText**](ivmkeyboard-typeasciitext.md) method. If greater flexibility is required, **IVMKeyboard** has several methods that are designed to be used with the key codes in the following list. The [**TypeKeySequence**](ivmkeyboard-typekeysequence.md) method can accept a comma-delimited string of key codes, which will be pressed and released, in order, within the virtual machine. In addition to these key codes, the keywords UP and DOWN can be used to force a key to only be pressed, or only be released. The UP and DOWN keywords only apply to the key code directly following the keyword. The following examples illustrate the use of **TypeAsciiText** and **TypeKeySequence**:


```C++
keyboard.TypeKeySequence("DOWN, Key_LeftShift, Key_M, UP, Key_LeftShift, Key_I, Key_C, Key_R, Key_O, Key_S, Key_O, Key_F, Key_T, Key_Space");
    keyboard.TypeAsciiText("Virtual Server");
```



The previous code will type "Microsoft Virtual Server" into the virtual machine. Also, to press or release a single key, the [**PressKey**](ivmkeyboard-presskey.md), [**ReleaseKey**](ivmkeyboard-releasekey.md), and [**PressAndReleaseKey**](ivmkeyboard-pressandreleasekey.md) methods may be used with the following key codes.

To avoid multiple scripts, applications, or users from simultaneously attempting to access the same keyboard device, set the [**HasExclusiveAccess**](ivmkeyboard-hasexclusiveaccess.md) property to **TRUE**. If exclusive access is acquired by one process, any attempts by other processes to send input to the keyboard device will be ignored until exclusive access has been released.

A list of valid key identifier codes and modifiers can be found in the [Key Identifiers Reference](key-identifiers-reference.md) topic.

## Members

The **IVMKeyboard** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMKeyboard** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMKeyboard** interface has these methods.



| Method                                                       | Description                                                                                                         |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**IsPressed**](ivmkeyboard-ispressed.md)                   | Retrieves the current state (pressed or released) of the specified key within the virtual machine.<br/>       |
| [**PressAndReleaseKey**](ivmkeyboard-pressandreleasekey.md) | Simulates the given key being pressed down and then released inside the virtual machine.<br/>                 |
| [**PressKey**](ivmkeyboard-presskey.md)                     | Simulates the given key being pressed down inside the virtual machine.<br/>                                   |
| [**ReleaseKey**](ivmkeyboard-releasekey.md)                 | Simulates the given key being released inside the virtual machine.<br/>                                       |
| [**TypeAsciiText**](ivmkeyboard-typeasciitext.md)           | Simulates the given series of ASCII keys being typed (pressed and then released) in the virtual machine.<br/> |
| [**TypeKeySequence**](ivmkeyboard-typekeysequence.md)       | Simulates the given series of keys being typed (pressed and then released) inside the virtual machine.<br/>   |



 

### Properties

The **IVMKeyboard** interface has these properties.



| Property                                                                | Access type           | Description                                                                                                                |
|:------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------|
| [**HasExclusiveAccess**](ivmkeyboard-hasexclusiveaccess.md)<br/> | Read/write<br/> | Indicates whether this **IVMKeyboard** object has exclusive control over the virtual machine's keyboard device.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





