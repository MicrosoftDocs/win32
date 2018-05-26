---
title: SystemState CheckRegistryValueUInt64 method
description: Retrieves an unsigned 64-bit (unsigned REG\_QWORD) value from the registry.
ms.assetid: F02F2CF4-F164-4368-8EF3-0696EA93AEEC
keywords:
- CheckRegistryValueUInt64 method Access Execution Engine
- CheckRegistryValueUInt64 method Access Execution Engine , SystemState interface
- SystemState interface Access Execution Engine , CheckRegistryValueUInt64 method
topic_type:
- apiref
api_name:
- SystemState.CheckRegistryValueUInt64
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

# SystemState::CheckRegistryValueUInt64 method

Retrieves an unsigned 64-bit (unsigned REG\_QWORD) value from the registry.

## Syntax


```C++
virtual HRESULT CheckRegistryValueUInt64(
  [in]  HKEY      keyRoot,
  [in]  LPCWSTR   keyPath,
  [in]  LPCWSTR   valueName,
  [out] ULONGLONG *data
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

A pointer to an item to receive the registry value.

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

 

 





