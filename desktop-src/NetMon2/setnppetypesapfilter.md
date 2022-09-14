---
description: Sets the BLOB Etype/Sap filter.
ms.assetid: cd659c93-3415-4737-b848-936e80318544
title: SetNPPEtypeSapFilter function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetNPPEtypeSapFilter
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# SetNPPEtypeSapFilter function

The **SetNPPEtypeSapFilter** function sets the BLOB Etype/Sap filter.

## Syntax


```C++
DWORD SetNPPEtypeSapFilter(
  _In_  HBLOB  hBlob,
  _In_  WORD   nSaps,
  _In_  WORD   nEtypes,
  _In_  LPBYTE lpSapTable,
  _In_  LPWORD lpEtypeTable,
  _In_  DWORD  FilterFlags,
  _Out_ HBLOB  hErrorBlob
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

A handle to the BLOB.

</dd> <dt>

*nSaps* \[in\]
</dt> <dd>

The number of SAPs.

</dd> <dt>

*nEtypes* \[in\]
</dt> <dd>

The number of Etypes in the Etype table being set.

</dd> <dt>

*lpSapTable* \[in\]
</dt> <dd>

A pointer to the SAP table that is set.

</dd> <dt>

*lpEtypeTable* \[in\]
</dt> <dd>

A pointer to the Etype table that is set.

</dd> <dt>

*FilterFlags* \[in\]
</dt> <dd>

The filter flags that are set.

</dd> <dt>

*hErrorBlob* \[out\]
</dt> <dd>

The handle to an error BLOB that specifies where in the original BLOB the error (if any) occurred.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the error.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



## See also

<dl> <dt>

[GetNPPEtypeSapFilter](getnppetypesapfilter.md)
</dt> </dl>

 

 




