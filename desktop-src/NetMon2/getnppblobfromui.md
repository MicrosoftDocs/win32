---
description: Selects a register NIC.
ms.assetid: 27814a40-6933-498b-a0d2-535698b1e402
title: GetNPPBlobFromUI function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetNPPBlobFromUI
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetNPPBlobFromUI function

The **GetNPPBlobFromUI** function selects a register NIC.

## Syntax


```C++
DWORD GetNPPBlobFromUI(
  _In_  HWND  hwnd,
  _In_  HBLOB hFilterBlob,
  _Out_ HBLOB *phBlob
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

A handle to a window that displays the **Select a network** dialog box.

</dd> <dt>

*hFilterBlob* \[in\]
</dt> <dd>

A handle to a [*filter BLOB*](f.md) used to limit which NICs are displayed.

</dd> <dt>

*phBlob* \[out\]
</dt> <dd>

A pointer to the handle of the BLOB that represents the selected NIC.

</dd> </dl>

## Return value

If the function is successful (the user selects a NIC), the return value is NMERR\_SUCCESS, and the BLOB that *phBlob* points to is filled in.

If the user does not select an NIC, the return value is **NMERR\_NO\_NPP\_SELECTED**.

If the function is unsuccessful, the return value is another NMERR value.

## Remarks

When called, Network Monitor displays the **Select a network** dialog box, which you can use to select a NIC. The NPP BLOB that represents the NIC is returned to the calling application.

If the BLOB named by *hFilterBlob* is a [*special BLOB*](s.md), the finder will attempt to process it. An example would be a call that had previously returned a special BLOB from the remote NPP. The application inserted the required tag, MACHINE\_NAME. In this situation, the finder would pass this BLOB to the remote NPP, which would then return a table of NPP BLOBs representing the machine requested. These remote NPP BLOBs would appear in the dialog box.

The caller must call the [DestroyBlob](destroyblob.md) function, which destroys the returned BLOB when it is no longer required.



| For more information about | See                                                                          |
|----------------------------|------------------------------------------------------------------------------|
| Three ways to select NICs  | [Selecting a Network Interface Card](selecting-a-network-interface-card.md) |
| Specifying a filter BLOB   | [Specifying a Filter BLOB](specifying-a-filter-blob.md)                     |



 

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

[GetNPPBlobTable](getnppblobtable.md)
</dt> <dt>

[SelectNPPBlobFromTable](selectnppblobfromtable.md)
</dt> </dl>

 

 




