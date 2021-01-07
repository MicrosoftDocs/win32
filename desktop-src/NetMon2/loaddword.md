---
description: The LoadDWORD function is called by the monitor to set a DWORD variable with a value taken from an HTML configuration string variable.
ms.assetid: 18a7beba-01f4-4f92-99bf-067f79f25db0
title: LoadDWORD function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LoadDWORD
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# LoadDWORD function

The **LoadDWORD** function is called by the monitor to set a **DWORD** variable with a value taken from an HTML configuration string variable.

## Syntax


```C++
BOOL LoadDWORD(
  _In_ const char  *pConfig,
  _In_ const char  *pVarName,
  _In_       DWORD *pValue
);
```



## Parameters

<dl> <dt>

*pConfig* \[in\]
</dt> <dd>

Pointer to the HTML configuration string passed to the monitor by the [IMonitor::DoConfigure](imonitor-doconfigure.md) method.

</dd> <dt>

*pVarName* \[in\]
</dt> <dd>

Pointer to the name of the variable in the configuration string.

</dd> <dt>

*pValue* \[in\]
</dt> <dd>

Pointer to the **DWORD** variable that is set to the value of the configuration string variable.

</dd> </dl>

## Return value

If the function is successful (if the variable name was found and had a non-zero-length string), the **DWORD** is inserted, and the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




