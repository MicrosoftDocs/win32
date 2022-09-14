---
description: The GetNPPBlobTable function retrieves an NPP BLOB table that represents the register NICs on the local computer.
ms.assetid: 9e61faf5-1f06-40b5-bf47-f258ffb5151a
title: GetNPPBlobTable function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetNPPBlobTable
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetNPPBlobTable function

The **GetNPPBlobTable** function retrieves an NPP BLOB table that represents the register NICs on the local computer.

## Syntax


```C++
DWORD GetNPPBlobTable(
  _In_  HBLOB       hFilterBlob,
  _Out_ PBLOB_TABLE *ppBlobTable
);
```



## Parameters

<dl> <dt>

*hFilterBlob* \[in\]
</dt> <dd>

Handle to a filter BLOB that limits the NPP BLOBs returned in the table.

</dd> <dt>

*ppBlobTable* \[out\]
</dt> <dd>

Pointer to a [BLOB\_TABLE](blob-table.md) structure that contains at least one BLOB pointer.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is one of the following error codes:



| Return code                                                                                                | Description                                                            |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_NO\_NPP\_DLL**</dt> </dl>         | No DLLs were found in the NPP directory.<br/>                    |
| <dl> <dt>**NMERR\_NO\_VALID\_NPP\_DLLS**</dt> </dl> | None of the DLLs in the NPP directory were valid NPP DLLs.<br/>  |
| <dl> <dt>**NMERR\_NO\_MATCHING\_NPPS**</dt> </dl>   | NPP BLOBs were discovered, but none passed the filter test.<br/> |
| <dl> <dt>**NMERR\_OUT\_OF\_MEMOR**</dt> </dl>       | Network Monitor was not able to allocate memory.<br/>            |



 

## Remarks

The BLOB named by *hFilterBlob* can also be a special BLOB.

If you set the flag in the filter BLOB to **TRUE**, the returned BLOB table can also include special BLOBs .

If the BLOB named by *hFilterBlob* is a special BLOB, the Network Monitor UI will attempt to process it. For example, suppose that a previous call returns a special BLOB from the remote NPP. The application inserts the required tag, MACHINE\_NAME. The finder then passes this BLOB to the remote NPP, which then returns a table of the NPP BLOBs associated with the machine name.

To destroy all returned BLOBs and the BLOB table, the caller is responsible for calling the **DestroyBlob** function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



 

 




