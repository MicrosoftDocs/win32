---
title: SystemState CheckRegistryValueUInt32 method
description: Retrieves an unsigned 32-bit integer (unsigned REG\_DWORD) value from the registry.
ms.assetid: 'B9708C52-965B-45C1-8347-D2DAB15ACBD3'
keywords: ["CheckRegistryValueUInt32 method Access Execution Engine", "CheckRegistryValueUInt32 method Access Execution Engine , SystemState interface", "SystemState interface Access Execution Engine , CheckRegistryValueUInt32 method"]
topic_type:
- apiref
api_name:
- SystemState.CheckRegistryValueUInt32
api_location:
- AxeCore.dll
api_type:
- COM
---

# SystemState::CheckRegistryValueUInt32 method

Retrieves an unsigned 32-bit integer (unsigned REG\_DWORD) value from the registry.

## Syntax


```C++
virtual HRESULT CheckRegistryValueUInt32(
  [in]  HKEY    keyRoot,
  [in]  LPCWSTR keyPath,
  [in]  LPCWSTR valueName,
  [out] ULONG   *data
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

*data* \[out\]
</dt> <dd>

A pointer to an item to receive the registry string value.

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

 

 





