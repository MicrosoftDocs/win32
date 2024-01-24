---
description: The PORT\_INFO\_1 structure identifies a supported printer port.
ms.assetid: e474fe9c-e554-406a-a5bf-de07f9a72b32
title: PORT_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PORT_INFO_1
- _PORT_INFO_1A
- _PORT_INFO_1W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PORT\_INFO\_1 structure

The **PORT\_INFO\_1** structure identifies a supported printer port.

## Syntax


```C++
typedef struct _PORT_INFO_1 {
  LPTSTR pName;
} PORT_INFO_1, *PPORT_INFO_1;
```



## Members

<dl> <dt>

**pName**
</dt> <dd>

Pointer to a null-terminated string that identifies a supported printer port (for example, "LPT1:").

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PORT\_INFO\_1W** (Unicode) and **\_PORT\_INFO\_1A** (ANSI)<br/>                                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**EnumPorts**](enumports.md)
</dt> </dl>

 

 




