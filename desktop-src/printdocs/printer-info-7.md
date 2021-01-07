---
description: The PRINTER\_INFO\_7 structure specifies directory services printer information.
ms.assetid: 9443855e-df7d-41a1-a0df-5649a97b2915
title: PRINTER_INFO_7 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_INFO_7
- _PRINTER_INFO_7A
- _PRINTER_INFO_7W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_INFO\_7 structure

The **PRINTER\_INFO\_7** structure specifies directory services printer information. Use this structure with the [**SetPrinter**](setprinter.md) function to publish a printer's data in the directory service (DS), or to update or remove a printer's published data from the DS. Use this structure with the [**GetPrinter**](getprinter.md) function to determine whether a printer is published in the DS.

## Syntax


```C++
typedef struct _PRINTER_INFO_7 {
  LPTSTR pszObjectGUID;
  DWORD  dwAction;
} PRINTER_INFO_7, *PPRINTER_INFO_7;
```



## Members

<dl> <dt>

**pszObjectGUID**
</dt> <dd>

A pointer to a null-terminated string containing the GUID of the directory service print queue object associated with a published printer. Use the [**GetPrinter**](getprinter.md) function to retrieve this GUID.

Before calling [**SetPrinter**](setprinter.md), set **pszObjectGUID** to **NULL**.

</dd> <dt>

**dwAction**
</dt> <dd>

Indicates the action for the [**SetPrinter**](setprinter.md) function to perform. For the [**GetPrinter**](getprinter.md) function, this member indicates whether the specified printer is published. This member can be a combination of the following values.



| Value                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DSPRINT_PENDING"></span><span id="dsprint_pending"></span><dl> <dt>**DSPRINT\_PENDING**</dt> <dt>0x80000000</dt> </dl>       | [**GetPrinter**](getprinter.md): Indicates that the system is attempting to complete a publish or unpublish operation started by a [**SetPrinter**](setprinter.md) call.<br/> [**SetPrinter**](setprinter.md): This value is not valid. <br/>                                                |
| <span id="DSPRINT_PUBLISH"></span><span id="dsprint_publish"></span><dl> <dt>**DSPRINT\_PUBLISH**</dt> <dt>0x00000001</dt> </dl>       | [**SetPrinter**](setprinter.md): Publishes the printer's data in the DS.<br/> [**GetPrinter**](getprinter.md): Indicates the printer is published. <br/>                                                                                                                                      |
| <span id="DSPRINT_REPUBLISH"></span><span id="dsprint_republish"></span><dl> <dt>**DSPRINT\_REPUBLISH**</dt> <dt>0x00000008</dt> </dl> | [**SetPrinter**](setprinter.md): The DS data for the printer is unpublished and then published again, refreshing all properties in the published printer. Re-publishing also changes the GUID of the published printer.<br/> [**GetPrinter**](getprinter.md): Never returns this value. <br/> |
| <span id="DSPRINT_UNPUBLISH"></span><span id="dsprint_unpublish"></span><dl> <dt>**DSPRINT\_UNPUBLISH**</dt> <dt>0x00000004</dt> </dl> | [**SetPrinter**](setprinter.md): Removes the printer's published data from the DS.<br/> [**GetPrinter**](getprinter.md): Indicates the printer is not published. <br/>                                                                                                                        |
| <span id="DSPRINT_UPDATE"></span><span id="dsprint_update"></span><dl> <dt>**DSPRINT\_UPDATE**</dt> <dt>0x00000002</dt> </dl>          | [**SetPrinter**](setprinter.md): Updates the printer's published data in the DS.<br/> [**GetPrinter**](getprinter.md): Never returns this value. <br/>                                                                                                                                        |



 

</dd> </dl>

## Remarks

The **PRINTER\_INFO\_7** structure is used in a [**SetPrinter**](setprinter.md) call to publish printer information to the directory service. The published data includes all values and data for the specified printer found under the SPLDS\_SPOOLER\_KEY, SPLDS\_DRIVER\_KEY, or SPLDS\_USER\_KEY keys created by [**SetPrinterDataEx**](setprinterdataex.md).

For [**SetPrinter**](setprinter.md), *pszObjectGUID* should be set to **NULL**. For [**GetPrinter**](getprinter.md), *pszObjectGUID* returns the GUID of the directory services print queue object associated with a published printer. You can use this GUID with Active Directory Services Interface (ADSI) methods to retrieve published data for the printer. However, the recommended method for retrieving published data is to call the [**GetPrinterDataEx**](getprinterdataex.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PRINTER\_INFO\_7W** (Unicode) and **\_PRINTER\_INFO\_7A** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> </dl>

 

 




