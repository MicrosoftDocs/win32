---
title: SystemState CheckRegistryValueMultistring method
description: Retrieves a multi-string (REG\_MULTI\_SZ) value from the registry.
ms.assetid: '72C78E4A-1A33-4D34-92BF-07636FB4F87C'
keywords: ["CheckRegistryValueMultistring method Access Execution Engine", "CheckRegistryValueMultistring method Access Execution Engine , SystemState interface", "SystemState interface Access Execution Engine , CheckRegistryValueMultistring method"]
topic_type:
- apiref
api_name:
- SystemState.CheckRegistryValueMultistring
api_location:
- AxeCore.dll
api_type:
- COM
---

# SystemState::CheckRegistryValueMultistring method

Retrieves a multi-string (REG\_MULTI\_SZ) value from the registry.

## Syntax


```C++
virtual HRESULT CheckRegistryValueMultistring(
  [in]  HKEY    keyRoot,
  [in]  LPCWSTR keyPath,
  [in]  LPCWSTR valueName,
  [out] LPCWSTR *data,
  [out] ULONG   *length
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

A pointer to a string buffer to receive the registry multi-string value.

</dd> <dt>

*length* \[out\]
</dt> <dd>

The length of the returned strings (including the zero at the end to indicate the last string).

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

 

 





