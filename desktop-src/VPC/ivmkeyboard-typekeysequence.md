---
title: IVMKeyboard TypeKeySequence method (VPCCOMInterfaces.h)
description: Simulates a comma-delimited list of keys being typed.
ms.assetid: ba4d4e43-cb2e-49ae-940d-2e81286d3473
keywords:
- TypeKeySequence method Virtual PC
- TypeKeySequence method Virtual PC , IVMKeyboard interface
- IVMKeyboard interface Virtual PC , TypeKeySequence method
topic_type:
- apiref
api_name:
- IVMKeyboard.TypeKeySequence
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMKeyboard::TypeKeySequence method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Simulates a comma-delimited list of keys being typed.

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

The comma-delimited sequence of key codes to be typed.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                 | Description                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                   |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>      | The specified string is empty, or contains an invalid key code.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                               |



 

## Remarks

A key sequence string is a comma-delimited set of key identifiers which are used to simulate the key press and release sequence of a standard U.S. 101-key AT-style keyboard.

If a key identifier appears in the string without a preceding modifier, a key-pressed code is sent to the virtual machine session, followed immediately by its corresponding key-released code. Key modifiers can be used to change this behavior.

For example, the DOWN modifier will send the key-pressed code for the following key identifier without sending the key-released code. This is useful for simulating Ctrl, Alt, and Shift keys when they are held down while other keys are being sent. To release the key, it must be included in the key string again along with a preceding UP modifier.

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

[**IVMKeyboard**](ivmkeyboard.md)
</dt> <dt>

[Key Sequences](key-sequences.md)
</dt> </dl>

 

