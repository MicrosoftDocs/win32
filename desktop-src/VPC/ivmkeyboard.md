---
title: IVMKeyboard interface (VPCCOMInterfaces.h)
description: Controls the keyboard device within a virtual machine. The IVMKeyboard for a virtual machine can be retrieved using the IVMVirtualMachine Keyboard property.
ms.assetid: a64a23b6-3937-40c6-af9d-fb341c04fbf7
keywords:
- IVMKeyboard interface Virtual PC
- IVMKeyboard interface Virtual PC , described
topic_type:
- apiref
api_name:
- IVMKeyboard
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMKeyboard interface

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Controls the keyboard device within a virtual machine. The **IVMKeyboard** for a virtual machine can be retrieved using the [**IVMVirtualMachine::Keyboard**](ivmvirtualmachine-keyboard.md) property.

## Members

The **IVMKeyboard** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IVMKeyboard** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMKeyboard** interface has these methods.



| Method                                                       | Description                                                                   |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**IsPressed**](ivmkeyboard-ispressed.md)                   | Determines whether the specified key is down.<br/>                      |
| [**PressAndReleaseKey**](ivmkeyboard-pressandreleasekey.md) | Simulates a key being pressed down and then released.<br/>              |
| [**PressKey**](ivmkeyboard-presskey.md)                     | Simulates a key being pressed down.<br/>                                |
| [**ReleaseKey**](ivmkeyboard-releasekey.md)                 | Simulates a key being released.<br/>                                    |
| [**TypeAsciiText**](ivmkeyboard-typeasciitext.md)           | Simulates a series of ASCII keys being typed into the guest.<br/>       |
| [**TypeKeySequence**](ivmkeyboard-typekeysequence.md)       | Simulates a comma-delimited list of keys being typed in the guest.<br/> |



 

### Properties

The **IVMKeyboard** interface has these properties.



| Property                                                                | Access type           | Description                                                                                                |
|:------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------|
| [**HasExclusiveAccess**](ivmkeyboard-hasexclusiveaccess.md)<br/> | Read/write<br/> | Indicates whether this object has exclusive control over the virtual machine's keyboard device.<br/> |



 

## Remarks

Keys can be typed into the virtual machine in several ways. To type a normal ASCII sequence of characters, use the [**TypeAsciiText**](ivmkeyboard-typeasciitext.md) method. If greater flexibility is required, **IVMKeyboard** has several methods that are designed to be used with the key codes in the following list. The [**TypeKeySequence**](ivmkeyboard-typekeysequence.md) method can accept a comma-delimited string of key codes, which will be pressed and released, in order, within the virtual machine. In addition to these key codes, the keywords UP and DOWN can be used to force a key to only be pressed, or only be released. The UP and DOWN keywords only apply to the key code directly following the keyword.

To avoid multiple scripts, applications, or users from simultaneously attempting to access the same keyboard device, set the [**HasExclusiveAccess**](ivmkeyboard-hasexclusiveaccess.md) property to **TRUE**. If exclusive access is acquired by one process, any attempts by other processes to send input to the keyboard device will be ignored until exclusive access has been released.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMKeyboard is defined as 00695f2e-c5ad-4d6e-b1ab-336ed121f8c4<br/>                |



## See also

<dl> <dt>

[Windows Virtual PC Interfaces](virtual-pc-interfaces.md)
</dt> <dt>

[Key Sequences](key-sequences.md)
</dt> </dl>

 

