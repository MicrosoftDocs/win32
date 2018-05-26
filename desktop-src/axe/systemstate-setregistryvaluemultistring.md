---
title: SystemState SetRegistryValueMultistring method
description: Sets a multi-string (REG\_MULTI\_SZ) value into the registry.
ms.assetid: 20B968DB-DC19-4ED2-B072-47613A8E0A55
keywords:
- SetRegistryValueMultistring method Access Execution Engine
- SetRegistryValueMultistring method Access Execution Engine , SystemState interface
- SystemState interface Access Execution Engine , SetRegistryValueMultistring method
topic_type:
- apiref
api_name:
- SystemState.SetRegistryValueMultistring
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

# SystemState::SetRegistryValueMultistring method

Sets a multi-string (REG\_MULTI\_SZ) value into the registry.

## Syntax


```C++
virtual HRESULT SetRegistryValueMultistring(
  [in] HKEY    keyRoot,
  [in] LPCWSTR keyPath,
  [in] LPCWSTR valueName,
  [in] LPCWSTR data,
  [in] ULONG   length
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

A pointer to a buffer to set the registry string value.

</dd> <dt>

*length* \[in\]
</dt> <dd>

The length of multi-string (including the zero that marks the end of the multi-string).

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

 

 





