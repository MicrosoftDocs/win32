---
title: SystemState CheckRegistryValueString method
description: Retrieves an unsigned 64-bit (unsigned REG\_QWORD) value from the registry.
ms.assetid: '5C022B58-01B0-4051-92DE-FC601EEC6DB1'
keywords: ["CheckRegistryValueString method Access Execution Engine", "CheckRegistryValueString method Access Execution Engine , SystemState interface", "SystemState interface Access Execution Engine , CheckRegistryValueString method"]
topic_type:
- apiref
api_name:
- SystemState.CheckRegistryValueString
api_location:
- AxeCore.dll
api_type:
- COM
---

# SystemState::CheckRegistryValueString method

Retrieves an unsigned 64-bit (unsigned REG\_QWORD) value from the registry.

## Syntax


```C++
virtual HRESULT CheckRegistryValueString(
  [in]  HKEY    keyRoot,
  [in]  LPCWSTR keyPath,
  [in]  LPCWSTR valueName,
  [out] LPCWSTR *data
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

A pointer to a string buffer to receive the registry string value.

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

 

 





