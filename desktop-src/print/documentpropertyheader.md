---
Description: The DOCUMENTPROPERTYHEADER structure is used as an input parameter to a printer interface DLLs DrvDocumentPropertySheets function.
ms.assetid: 5aaf1f90-fb75-4e5a-9316-9212a21b8fed
title: DOCUMENTPROPERTYHEADER structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DOCUMENTPROPERTYHEADER structure

The DOCUMENTPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function.

## Syntax


```C++
typedef struct _DOCUMENTPROPERTYHEADER {
  WORD     cbSize;
  WORD     Reserved;
  HANDLE   hPrinter;
  LPTSTR   pszPrinterName;
  PDEVMODE pdmIn;
  PDEVMODE pdmOut;
  DWORD    cbOut;
  DWORD    fMode;
} DOCUMENTPROPERTYHEADER, *PDOCUMENTPROPERTYHEADER;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the DOCUMENTPROPERTYHEADER structure.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**hPrinter**
</dt> <dd>

Printer handle.

</dd> <dt>

**pszPrinterName**
</dt> <dd>

Pointer to a NULL-terminated string representing the printer's name.

</dd> <dt>

**pdmIn**
</dt> <dd>

Pointer to an input [**DEVMODEW**](display.devmodew) structure that the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function should copy into the printer interface DLL's internal DEVMODEW structure (before the property sheet is displayed, if applicable). If DM\_IN\_BUFFER or DM\_MODIFY is not set in **fMode**, this pointer is **NULL**.

</dd> <dt>

**pdmOut**
</dt> <dd>

Pointer to an output DEVMODEW structure into which the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function should copy the printer interface DLL's internal DEVMODEW contents (after the property sheet has been displayed, if applicable). If DM\_OUT\_BUFFER or DM\_COPY is not set in **fMode**, this pointer is **NULL**.

</dd> <dt>

**cbOut**
</dt> <dd>

Specifies the size, in bytes, of the buffer to which **pdmOut** points. For more information, see the following Remarks section.

</dd> <dt>

**fMode**
</dt> <dd>

One or more of the bit flags listed in the following table. (The flags are defined in header files Wingdi.h and Winddiui.h.)



| Flag                                                 | Definition                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No flags set (that is, **fMode** is 0).<br/>   | The [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function should return the size, in bytes, of its DEVMODEW structure, including all public and private members, in the **cbOut** member.<br/>                                                                                                                                                                                                                |
| DM\_ADVANCED<br/>                              | If set, the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function should only create the Advanced document page.<br/> If not set, the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function should create both the PageSetup and Advanced document pages.<br/> (See the description of the **pDlgPage** member of the [**COMPROPSHEETUI**](compropsheetui.md) structure.)<br/> |
| DM\_IN\_BUFFER or<br/> DM\_MODIFY<br/>   | The caller has supplied a DEVMODEW structure pointer in **pdmIn**, and the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function should update its internal DEVMODEW structure to reflect the contents of the supplied DEVMODEW.<br/>                                                                                                                                                                         |
| DM\_IN\_PROMPT or<br/> DM\_PROMPT<br/>   | The [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function should create its property sheet pages.<br/> (This flag is never set if the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function's *pPSUIInfo* parameter is **NULL**.)<br/>                                                                                                                                                |
| DM\_NOPERMISSION<br/>                          | The printer interface DLL's [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback should not allow the user to modify properties on the displayed property sheet pages.<br/>                                                                                                                                                                                                                                                 |
| DM\_OUT\_BUFFER or<br/> DM\_COPY<br/>    | The caller has supplied a DEVMODEW structure pointer in **pdmOut**, and the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md)function should copy the contents of its internal DEVMODEW structure into the supplied DEVMODEW.<br/>                                                                                                                                                                                 |
| DM\_PROMPT\_NON\_MODAL<br/>                    | The [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function should create its property sheet pages, and launch a non-modal UI.<br/> (This flag is never set if the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function's *pPSUIInfo* parameter is **NULL**.)<br/>                                                                                                                     |
| DM\_USER\_DEFAULT<br/>                         | Not used.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DM\_OUT\_DEFAULT or<br/> DM\_UPDATE<br/> | Not used.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                  |



 

</dd> </dl>

## Remarks

The input value in the **cbOut** member is not necessarily equal to the size of the buffer pointed to by the **pdmOut** member. For example, when the *pPSUInfo* parameter of the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function is **NULL**, and if either the **fMode** member of the DOCUMENTPROPERTYHEADER structure is zero, or the **pdmOut** member of the same structure is **NULL**, a driver should write the total size of the printer's [**DEVMODEW**](display.devmodew) structure (including the public and private structure members) in the **cbOut** member. In such a case, a driver should treat the **cbOut** member as a "write-only" member. The "plotter" sample that ships with the Windows Driver Kit (WDK) demonstrates how to use the **cbOut** member correctly.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md)
</dt> <dt>

[**COMPROPSHEETUI**](compropsheetui.md)
</dt> <dt>

[**DEVMODEW**](display.devmodew)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DOCUMENTPROPERTYHEADER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





