---
description: Represents information about a connection to a printer.
ms.assetid: afac3f91-74eb-46f7-94b4-d37b2b8a32a4
title: PRINTER_CONNECTION_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_CONNECTION_INFO_1
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_CONNECTION\_INFO\_1 structure

Represents information about a connection to a printer.

## Syntax


```C++
typedef struct _PRINTER_CONNECTION_INFO_1 {
  DWORD  dwFlags;
  LPTSTR pszDriverName;
} PRINTER_CONNECTION_INFO_1, *PPRINTER_CONNECTION_INFO_1;
```



## Members

<dl> <dt>

**dwFlags**
</dt> <dd>

The following values are defined:



| Value                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRINTER\_CONNECTION\_MISMATCH (0x00000020) | If this bit-flag is set, the printer connection is mismatched. The user can supply a local print driver as *pszDriverName* and use it to do the rendering instead of using the driver installed on the server printer to which the user is connected.<br/>                                                                                                                                                                                                                                    |
| PRINTER\_CONNECTION\_NO\_UI (0x00000040)   | If this bit-flag is set then this call cannot display a dialog box. If a dialog box must be displayed to install a printer driver from the server and this bit-flag is set, the printer driver will not be installed, the printer connection will not be added, and the call will fail.<br/> **Windows 7:** In Windows 7 and later versions of Windows, if this flag is set and the user is running in elevated mode, the **Do you trust this printer?** dialog will not be shown.<br/> |



 

</dd> <dt>

**pszDriverName**
</dt> <dd>

A pointer to the name of the driver.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> </dl>

 

 




