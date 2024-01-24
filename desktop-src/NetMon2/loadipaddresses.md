---
description: The LoadIPAddresses function is called by the monitor to fill in an IP address list with addresses taken from an HTML configuration string variable.
ms.assetid: d0b5d686-5a98-4d61-aa28-24ea71fcb06b
title: LoadIPAddresses function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LoadIPAddresses
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# LoadIPAddresses function

The **LoadIPAddresses** function is called by the monitor to fill in an IP address list with addresses taken from an HTML configuration string variable.

## Syntax


```C++
BOOL LoadIPAddresses(
  _In_  const char  *pConfig,
  _In_  const char  *pVarName,
  _Out_       DWORD **ppAddresses,
  _Out_       DWORD *pNumAddresses
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

Pointer to a pointer to an array of addresses. If the variable specified in *pVarName* is found and has a non-zero-length, the function allocates sufficient space and stores all the IP addresses as an array.

</dd> <dt>

*pNumAddresses* \[out\]
</dt> <dd>

Pointer to the **DWORD** variable that is set to the number of IP addresses taken from the configuration string.

</dd> </dl>

## Return value

If the function is successful (the variable name was found and had a non-zero-length string that represented IP addresses), the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Remarks

The IP addresses must be in x.x.x.x format (for example, 127.0.0.1).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




