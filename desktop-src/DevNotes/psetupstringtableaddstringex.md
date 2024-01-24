---
description: Adds a string and extra data to a table.
ms.assetid: e6f29cb0-4468-435d-9ae3-217d4f69e87e
title: pSetupStringTableAddStringEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- pSetupStringTableAddStringEx
api_type: 
- DllExport
api_location: 
- Setupapi.dll
---

# pSetupStringTableAddStringEx function

\[This function is not available in Windows Vista or Windows Server 2008.\]

Adds a string and extra data to a table.

## Syntax


```C++
LONG pSetupStringTableAddStringEx(
  _In_     PVOID StringTable,
  _In_     PTSTR String,
  _In_     DWORD Flags,
  _In_opt_ PVOID ExtraData,
  _In_opt_ UINT  ExtraDataSize
);
```



## Parameters

<dl> <dt>

*StringTable* \[in\]
</dt> <dd>

A pointer to the string table.

</dd> <dt>

*String* \[in\]
</dt> <dd>

A pointer to string to be added to the table.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

The value of this parameter can be `STRTAB_CASE_SENSITIVE | STRTAB_NEW_EXTRADATA`.



| Value                                                                                                                                                                                                                                             | Meaning                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| <span id="STRTAB_CASE_SENSITIVE"></span><span id="strtab_case_sensitive"></span><dl> <dt>**STRTAB\_CASE\_SENSITIVE**</dt> <dt>0x001</dt> </dl> | String is case sensitive.<br/> |
| <span id="STRTAB_NEW_EXTRADATA"></span><span id="strtab_new_extradata"></span><dl> <dt>**STRTAB\_NEW\_EXTRADATA**</dt> <dt>0x004</dt> </dl>    | There is extra data.<br/>      |



 

</dd> <dt>

*ExtraData* \[in, optional\]
</dt> <dd>

A optional pointer to an extra data object.

</dd> <dt>

*ExtraDataSize* \[in, optional\]
</dt> <dd>

The size of the extra data.

</dd> </dl>

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 
