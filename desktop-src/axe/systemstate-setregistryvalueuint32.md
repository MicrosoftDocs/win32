---
title: SystemState SetRegistryValueUInt32 method
description: Sets an unsigned 32-bit integer (unsigned REG\_DWORD) value into the registry.
ms.assetid: 8A601E4E-011E-49FE-AC6A-62FF5D3A8172
keywords:
- SetRegistryValueUInt32 method Access Execution Engine
- SetRegistryValueUInt32 method Access Execution Engine , SystemState interface
- SystemState interface Access Execution Engine , SetRegistryValueUInt32 method
topic_type:
- apiref
api_name:
- SystemState.SetRegistryValueUInt32
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SystemState::SetRegistryValueUInt32 method

Sets an unsigned 32-bit integer (unsigned REG\_DWORD) value into the registry.

## Syntax


```C++
virtual HRESULT SetRegistryValueUInt32(
  [in] HKEY    keyRoot,
  [in] LPCWSTR keyPath,
  [in] LPCWSTR valueName,
  [in] ULONG   data
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**SystemState**](systemstate.md)
</dt> </dl>

 

 





