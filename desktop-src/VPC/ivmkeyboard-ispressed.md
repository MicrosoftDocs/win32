---
title: IVMKeyboard IsPressed method (VPCCOMInterfaces.h)
description: Determines whether the specified key is down.
ms.assetid: 7541d678-762a-4c2e-80cd-686bb56c9cd7
keywords:
- IsPressed method Virtual PC
- IsPressed method Virtual PC , IVMKeyboard interface
- IVMKeyboard interface Virtual PC , IsPressed method
topic_type:
- apiref
api_name:
- IVMKeyboard.IsPressed
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMKeyboard::IsPressed method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Determines whether the specified key is down.

## Syntax


```C++
HRESULT IsPressed(
  [in]          BSTR         key,
  [out, retval] VARIANT_BOOL *pressed
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

The key code for the key whose state is to be queried.

</dd> <dt>

*pressed* \[out, retval\]
</dt> <dd>

**TRUE** if the key is currently pressed down, **FALSE** otherwise.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                 | Description                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                   |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>         | A parameter is **NULL**.<br/>                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>      | The specified string is empty, or contains an invalid key code.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                               |



 

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
</dt> </dl>

 

