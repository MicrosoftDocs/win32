---
title: SystemState SetRegistryValueString method
description: Sets a string (REG\_SZ) value into the registry.
ms.assetid: '14BB1967-65A9-45D3-B3FF-877BE11ACC39'
keywords: ["SetRegistryValueString method Access Execution Engine", "SetRegistryValueString method Access Execution Engine , SystemState interface", "SystemState interface Access Execution Engine , SetRegistryValueString method"]
topic_type:
- apiref
api_name:
- SystemState.SetRegistryValueString
api_location:
- AxeCore.dll
api_type:
- COM
---

# SystemState::SetRegistryValueString method

Sets a string (REG\_SZ) value into the registry.

## Syntax


```C++
virtual HRESULT SetRegistryValueString(
  [in] HKEY    keyRoot,
  [in] LPCWSTR keyPath,
  [in] LPCWSTR valueName,
  [in] LPCWSTR data
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

A pointer to a string buffer to set the registry string value.

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

 

 





