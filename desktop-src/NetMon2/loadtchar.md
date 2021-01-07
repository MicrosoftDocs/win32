---
description: The LoadTCHAR function is called by monitors to set a string variable to a string taken from an HTML configuration string.
ms.assetid: 515a1053-d575-4b7c-92a7-4a8039f1b2ac
title: LoadTCHAR function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LoadTCHAR
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# LoadTCHAR function

The **LoadTCHAR** function is called by monitors to set a string variable to a string taken from an HTML configuration string.

## Syntax


```C++
BOOL LoadTCHAR(
  _In_  const char *pConfig,
  _In_  const char *pVarName,
  _Out_       char **ppszString
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

*ppszString* \[out\]
</dt> <dd>

Pointer to a string pointer. If the requested variable name is found, the string is allocated and assigned to this pointer. It is the user's responsibly to free the memory associated with the string.

</dd> </dl>

## Return value

If the function is successful (if the variable name was found and had a non-zero-length string), the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




