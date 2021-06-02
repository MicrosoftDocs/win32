---
description: The LoadIPXAddresses function is called by the monitor to fill in an IPX address list taken from an HTML configuration string variable.
ms.assetid: d8ffd00b-2741-49e8-a90d-d41e56ee7101
title: LoadIPXAddresses function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LoadIPXAddresses
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# LoadIPXAddresses function

The **LoadIPXAddresses** function is called by the monitor to fill in an IPX address list taken from an HTML configuration string variable.

## Syntax


```C++
BOOL LoadIPXAddresses(
  _In_  const char        *pConfig,
  _In_  const char        *pVarName,
  _Out_       IPX_ADDRESS **ppAddresses,
  _Out_       DWORD       *pNumAddresses
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

*ppAddresses* \[out\]
</dt> <dd>

Pointer to a pointer to an array of addresses. If the variable specified in *pVarName* is found and has a non-zero-length, sufficient space is allocated (by using **HeapAllocMemory**), and all the IPX addresses are stored as an array.

</dd> <dt>

*pNumAddresses* \[out\]
</dt> <dd>

Pointer to the **DWORD** variable that is set to the number of IPX addresses taken from the configuration string.

</dd> </dl>

## Return value

If the function is successful (the variable name was found and had a non-zero-length string that represented IPX addresses), the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




