---
description: The CreateHandoffTable function creates a handoff table that includes the handoff set information stored in the INI file of the parser.
ms.assetid: 6dbca2fa-33fb-48e8-b663-be59aec6264b
title: CreateHandoffTable function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreateHandoffTable
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CreateHandoffTable function

The **CreateHandoffTable** function creates a [*handoff table*](h.md) that includes the handoff set information stored in the INI file of the parser.

## Syntax


```C++
DWORD WINAPI CreateHandoffTable(
  _In_  LPSTR          secName,
  _In_  LPSTR          iniFile,
  _Out_ LPHANDOFFTABLE *hTable,
  _In_  DWORD          nMaxProtocolEntries,
  _In_  DWORD          base
);
```



## Parameters

<dl> <dt>

*secName* \[in\]
</dt> <dd>

String that indicates the section of the INI file where the handoff set information is located.

</dd> <dt>

*iniFile* \[in\]
</dt> <dd>

String that includes the name of the parser INI file.

</dd> <dt>

*hTable* \[out\]
</dt> <dd>

Handle to a **HANDOFFTABLE** structure created and maintained by Network Monitor.

</dd> <dt>

*nMaxProtocolEntries* \[in\]
</dt> <dd>

Number that specifies the maximum number of entries that the handoff table can process.

</dd> <dt>

*base* \[in\]
</dt> <dd>

Numerical base of handoff set numbers stored in the INI file.

</dd> </dl>

## Return value

If the function is successful, the return value is the number of entries in the handoff table.

If the function is unsuccessful, the return value is zero.

## Remarks

The handoff table created by Network Monitor is based on information provided in the parser INI. The returned handle to the handoff table can then be used to obtain a handle to one of the protocols included in the table. To obtain a handle of one of these protocols, call [GetProtocolFromTable](getprotocolfromtable.md).

Notice that the parser application never accesses the **HANDOFFTABLE** structure directly. This structure is created and maintained by Network Monitor.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[GetProtocolFromTable](getprotocolfromtable.md)
</dt> <dt>

[HANDOFFTABLE](handofftable.md)
</dt> </dl>

 

 




