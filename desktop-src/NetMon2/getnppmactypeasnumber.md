---
description: Retrieves the MAC type from the NetworkInfo category of the NPP section of the BLOB and converts the type data into a MAC type number.
ms.assetid: 53aa538c-69ee-4b34-93fb-9e61c6baadea
title: GetNPPMacTypeAsNumber function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetNPPMacTypeAsNumber
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetNPPMacTypeAsNumber function

The **GetNPPMacTypeAsNumber** function retrieves the MAC type from the NetworkInfo category of the NPP section of the BLOB and converts the type data into a MAC type number.

## Syntax


```C++
DWORD GetNPPMacTypeAsNumber(
  _In_  HBLOB   hBlob,
  _Out_ LPDWORD lpMacType
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

A handle to the specified BLOB.

</dd> <dt>

*lpMacType* \[out\]
</dt> <dd>

A pointer to the MAC type.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the tag is unavailable, the return value is MAC\_TYPE\_UNKNOWN.

## Remarks

This function maps the tag, **NPP:NetworkInfo:MacType** to the **MAC\_TYPE\_\*** as defined in the Npptypes.h file.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



 

 




