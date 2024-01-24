---
description: The PROVIDOR\_INFO\_1 structure identifies a print provider.
ms.assetid: 0eff115a-b3d2-4c8f-b820-46e7f62dd295
title: PROVIDOR_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PROVIDOR_INFO_1
- _PROVIDOR_INFO_1A
- _PROVIDOR_INFO_1W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PROVIDOR\_INFO\_1 structure

The **PROVIDOR\_INFO\_1** structure identifies a print provider.

## Syntax


```C++
typedef struct _PROVIDOR_INFO_1 {
  LPTSTR pName;
  LPTSTR pEnvironment;
  LPTSTR pDLLName;
} PROVIDOR_INFO_1, *PPROVIDOR_INFO_1;
```



## Members

<dl> <dt>

**pName**
</dt> <dd>

Pointer to a null-terminated string that is the name of the print provider.

</dd> <dt>

**pEnvironment**
</dt> <dd>

Pointer to a null-terminated environment string specifying the environment the provider dynamic-link library (DLL) is designed to run in.

</dd> <dt>

**pDLLName**
</dt> <dd>

Pointer to a null-terminated string that is the name of the provider .dll.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PROVIDOR\_INFO\_1W** (Unicode) and **\_PROVIDOR\_INFO\_1A** (ANSI)<br/>                         |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**AddPrintProvidor**](addprintprovidor.md)
</dt> </dl>

 

 




