---
description: The LoadMACAddresses function is called by the monitor to fill in a MAC address list with addresses taken from an HTML configuration string variable.
ms.assetid: cb7d2812-e234-4858-8b25-f8fc72aeee79
title: LoadMACAddresses function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LoadMACAddresses
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# LoadMACAddresses function

The **LoadMACAddresses** function is called by the monitor to fill in a MAC address list with addresses taken from an HTML configuration string variable.

## Syntax


```C++
BOOL LoadMACAddresses(
  _In_  const char   *pConfig,
  _In_  const char   *pVarName,
  _Out_       LPBYTE *ppAddresses,
  _Out_       DWORD  *pNumAddresses
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

Pointer to a pointer to an array of addresses. If the variable specified in *pVarName* is found and has a non-zero-length, the function allocates sufficient space (by using **HeapAllocMemory**) and stores all the MAC addresses as an array.

</dd> <dt>

*pNumAddresses* \[out\]
</dt> <dd>

Pointer to the **DWORD** variable that is set to the number of MAC addresses taken from the configuration string.

</dd> </dl>

## Return value

If the function is successful, (the variable name was found and had a non-zero-length string that represented MAC addresses), the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




