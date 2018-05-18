---
title: SystemState SetRegistryValueUInt64 method
description: Sets an unsigned 64-bit (unsigned REG\_QWORD) value Into the registry.
ms.assetid: 'FA123397-1D8F-4462-B031-C0C5F1ADDBBD'
keywords: ["SetRegistryValueUInt64 method Access Execution Engine", "SetRegistryValueUInt64 method Access Execution Engine , SystemState interface", "SystemState interface Access Execution Engine , SetRegistryValueUInt64 method"]
topic_type:
- apiref
api_name:
- SystemState.SetRegistryValueUInt64
api_location:
- AxeCore.dll
api_type:
- COM
---

# SystemState::SetRegistryValueUInt64 method

Sets an unsigned 64-bit (unsigned REG\_QWORD) value Into the registry.

## Syntax


```C++
virtual HRESULT SetRegistryValueUInt64(
  [in] HKEY      keyRoot,
  [in] LPCWSTR   keyPath,
  [in] LPCWSTR   valueName,
  [in] ULONGLONG data
) = 0;
```



## Parameters

<dl> <dt>

*keyRoot* \[in\]
</dt> <dd>

A handle to the root of the registry key.

</dd> <dt>

*keyPath* \[in\]
</dt> <dd>

The registry value path.

</dd> <dt>

*valueName* \[in\]
</dt> <dd>

The registry value name.

</dd> <dt>

*data* \[in\]
</dt> <dd>

A pointer to an item to set the registry value.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**SystemState**](systemstate.md)
</dt> </dl>

 

 





