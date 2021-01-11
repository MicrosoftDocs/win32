---
description: Retrieves data from the specified entries belonging to an EXE entry.
ms.assetid: 355eecd6-a0c9-4448-9aed-a9c3eb3b2071
title: SdbQueryDataExTagID function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbQueryDataExTagID
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbQueryDataExTagID function

Retrieves data from the specified entries belonging to an EXE entry.

## Syntax


```C++
DWORD WINAPI SdbQueryDataExTagID(
  _In_        PDB     pdb,
  _In_        TAGID   tiExe,
  _In_opt_    LPCTSTR lpszDataName,
  _Out_opt_   LPDWORD lpdwDataType,
  _Out_       LPVOID  lpBuffer,
  _Inout_opt_ LPDWORD lpcbBufferSize,
  _Out_       TAGID   *ptiData
);
```



## Parameters

<dl> <dt>

*pdb* \[in\]
</dt> <dd>

A handle to the shim database.

</dd> <dt>

*tiExe* \[in\]
</dt> <dd>

The [**TAGID**](tagid.md) of the EXE entry.

</dd> <dt>

*lpszDataName* \[in, optional\]
</dt> <dd>

The name of the data entry to be retrieved. To specify multiple entries, separate the names with the backslash character ("\\"). If this parameter is **NULL**, the function attempts to return all data entries.

</dd> <dt>

*lpdwDataType* \[out, optional\]
</dt> <dd>

The data type of the returned entries. This parameter can be one of the following values:

<dl><span id="REG_BINARY"></span><span id="reg_binary"></span><dt>

**REG\_BINARY**
</dt><span id="REG_DWORD"></span><span id="reg_dword"></span><dt>

**REG\_DWORD**
</dt><span id="REG_MULTI_SZ"></span><span id="reg_multi_sz"></span><dt>

**REG\_MULTI\_SZ**
</dt><span id="REG_NONE"></span><span id="reg_none"></span><dt>

**REG\_NONE**
</dt><span id="REG_QWORD"></span><span id="reg_qword"></span><dt>

**REG\_QWORD**
</dt><span id="REG_SZ"></span><span id="reg_sz"></span><dt>

**REG\_SZ**
</dt> </dl> </dd> <dt>

*lpBuffer* \[out\]
</dt> <dd>

The buffer that receives the data. If buffer is not large enough to contain the data, the function fails and returns **ERROR\_INSUFFICIENT\_BUFFER**.

</dd> <dt>

*lpcbBufferSize* \[in, out, optional\]
</dt> <dd>

The size of the *lpBuffer* buffer, in bytes.

</dd> <dt>

*ptiData* \[out\]
</dt> <dd>

The [**TAGID**](tagid.md) of the data entry.

</dd> </dl>

## Return value

This function returns one of the following values.



| Return code                                                                                                    | Description                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>       | One or more input parameters is incorrect.<br/>                  |
| <dl> <dt>**ERROR\_INTERNAL\_DB\_CORRUPTION**</dt> </dl> | No data entries were found for the EXE entry.<br/>               |
| <dl> <dt>**ERROR\_INSUFFICIENT\_BUFFER**</dt> </dl>     | The buffer is not large enough to contain the data entries.<br/> |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl>      | The memory allocation failed.<br/>                               |
| <dl> <dt>**ERROR\_NOT\_FOUND**</dt> </dl>               | A data entry with the name *lpszDataName* was not found.<br/>    |
| <dl> <dt>**ERROR\_SUCCESS**</dt> </dl>                  | The function completed successfully.<br/>                        |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



 

 




