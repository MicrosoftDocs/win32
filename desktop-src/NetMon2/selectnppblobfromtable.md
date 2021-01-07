---
description: The SelectNPPBlobFromTable function selects a NIC from a supplied NPP BLOB table.
ms.assetid: 7f8010ed-472a-49b2-8d97-92851b6c14cd
title: SelectNPPBlobFromTable function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SelectNPPBlobFromTable
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# SelectNPPBlobFromTable function

The **SelectNPPBlobFromTable** function selects a NIC from a supplied NPP BLOB table.

## Syntax


```C++
DWORD SelectNPPBlobFromTable(
  _In_  HWND        hwnd,
  _In_  PBLOB_TABLE pBlobTable,
  _Out_ HBLOB       *hBlob
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Handle to the window that displays the **Select a network** dialog box.

</dd> <dt>

*pBlobTable* \[in\]
</dt> <dd>

Pointer to the supplied BLOB table. Network Monitor uses this table to populate the **Select a network** dialog box.

</dd> <dt>

*hBlob* \[out\]
</dt> <dd>

Handle to the BLOB that represents the selected NIC.

</dd> </dl>

## Return value

If the function is successful and the user selects a NIC, the return value is NMERR\_SUCCESS; the BLOB pointed to by *hBlob* is filled in.

If the user does not select a NIC, the return value is NMERR\_NO\_NPP\_SELECTED.

If the function is unsuccessful, the return value is another NMERR value.

## Remarks

When called, Network Monitor displays the **Select a network** dialog box, which you can use to select a NIC. The NPP BLOB that represents the selected NIC returns to the calling application.

To learn the various ways you can select NICs, see [Selecting a Network Interface Card](selecting-a-network-interface-card.md)

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

[GetNPPBlobFromUI](getnppblobfromui.md)
</dt> <dt>

[GetNPPBlobTable](getnppblobtable.md)
</dt> <dt>

[Special BLOB Entries](special-blob-entries.md)
</dt> </dl>

 

 




