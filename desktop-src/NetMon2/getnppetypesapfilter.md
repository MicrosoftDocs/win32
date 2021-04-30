---
description: The GetNPPEtypeSapFilter function retrieves the Etype/Sap filter from a given BLOB.
ms.assetid: c4891eff-ab2d-43ff-8d2b-3aa299570c0a
title: GetNPPEtypeSapFilter function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetNPPEtypeSapFilter
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetNPPEtypeSapFilter function

The **GetNPPEtypeSapFilter** function retrieves the Etype/Sap filter from a given BLOB.

## Syntax


```C++
DWORD GetNPPEtypeSapFilter(
  _In_  HBLOB  hBlob,
  _Out_ WORD   *pnSaps,
  _Out_ WORD   *pnEtypes,
  _Out_ LPBYTE *ppSapTable,
  _Out_ LPWORD *ppEtypeTable,
  _Out_ DWORD  *pFilterFlags,
  _Out_ HBLOB  hErrorBlob
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to the BLOB.

</dd> <dt>

*pnSaps* \[out\]
</dt> <dd>

Pointer to the returned number of protocols in the SAP table.

</dd> <dt>

*pnEtypes* \[out\]
</dt> <dd>

Pointer to the returned number of Etypes in the Etype table.

</dd> <dt>

*ppSapTable* \[out\]
</dt> <dd>

Pointer to the returned SAP table.

</dd> <dt>

*ppEtypeTable* \[out\]
</dt> <dd>

Pointer to the returned Etype table.

</dd> <dt>

*pFilterFlags* \[out\]
</dt> <dd>

Pointer to the returned filter flags.

</dd> <dt>

*hErrorBlob* \[out\]
</dt> <dd>

Handle to an error BLOB, which specifies the location in the original BLOB where the error (if any) occurred.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the error.

## Remarks

The Etype/Sap information is stored in the **Config** category of the NPP **Owner** section.

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

[SetNPPEtypeSapFilter](setnppetypesapfilter.md)
</dt> </dl>

 

 




