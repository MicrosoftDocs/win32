---
description: The DocumentEvent function is an event handler for events associated with printing a document.
ms.assetid: 1250116e-55c7-470f-97f6-36f27a31a841
title: DocumentEvent function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DocumentEvent
- DocumentEventA
- DocumentEventW
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# DocumentEvent function

The **DocumentEvent** function is an event handler for events associated with printing a document.

## Syntax

```C++
HRESULT DocumentEvent(
  _In_  HANDLE hPrinter,
  _In_  HDC    hdc,
        INT    iEsc,
        ULONG  cbIn,
  _In_  PVOID  pvIn,
        ULONG  cbOut,
  _Out_ PVOID  pvOut
);
```
## Parameters

*hPrinter* \[in\]

A handle to a printer object. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

*hdc* \[in\]

A device context handle that is generated by a call of [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca). This is zero if *iEsc* is set to DOCUMENTEVENT\_CREATEDCPRE. For restrictions on printing from a 32-bit application on a 64-bit version of Windows, see Remarks.

*iEsc* 

An escape code that identifies the event to be handled. This parameter can be one of the following integer constants.

| Constant | Event |
|-|-|
| <span id="DOCUMENTEVENT_ABORTDOC"></span><span id="documentevent_abortdoc"></span><dl> <dt>**DOCUMENTEVENT\_ABORTDOC**</dt> </dl> | GDI is about to process a call to its [**AbortDoc**](/windows/desktop/api/Wingdi/nf-wingdi-abortdoc) function. |
| <span id="DOCUMENTEVENT_CREATEDCPOST"></span><span id="documentevent_createdcpost"></span><dl> <dt>**DOCUMENTEVENT\_CREATEDCPOST**</dt> </dl> | GDI has just processed a call to its [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) or [**CreateIC**](/windows/desktop/api/wingdi/nf-wingdi-createica) function.<br/> This escape code should not be used unless there has been a previous call to **DocumentEvent** with *iEsc* set to DOCUMENTEVENT\_CREATEDCPRE. |
| <span id="DOCUMENTEVENT_CREATEDCPRE"></span><span id="documentevent_createdcpre"></span><dl> <dt>**DOCUMENTEVENT\_CREATEDCPRE**</dt> </dl> | GDI is about to process a call to its [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) or [**CreateIC**](/windows/desktop/api/wingdi/nf-wingdi-createica) function. |
| <span id="DOCUMENTEVENT_DELETEDC"></span><span id="documentevent_deletedc"></span><dl> <dt>**DOCUMENTEVENT\_DELETEDC**</dt> </dl> | GDI is about to process a call to its [**DeleteDC**](/windows/desktop/api/wingdi/nf-wingdi-deletedc) function. |
| <span id="DOCUMENTEVENT_ENDDOCPOST"></span><span id="documentevent_enddocpost"></span><dl> <dt>**DOCUMENTEVENT\_ENDDOCPOST**</dt> </dl> | GDI has just processed a call to its [**EndDoc**](/windows/desktop/api/Wingdi/nf-wingdi-enddoc) function. |
| <span id="DOCUMENTEVENT_ENDDOCPRE_or_DOCUMENTEVENT_ENDDOC"></span><span id="documentevent_enddocpre_or_documentevent_enddoc"></span><span id="DOCUMENTEVENT_ENDDOCPRE_OR_DOCUMENTEVENT_ENDDOC"></span><dl> <dt>**DOCUMENTEVENT\_ENDDOCPRE or DOCUMENTEVENT\_ENDDOC**</dt> </dl> | GDI is about to process a call to its [**EndDoc**](/windows/desktop/api/Wingdi/nf-wingdi-enddoc) function. |
| <span id="DOCUMENTEVENT_ENDPAGE"></span><span id="documentevent_endpage"></span><dl> <dt>**DOCUMENTEVENT\_ENDPAGE**</dt> </dl> | GDI is about to process a call to its [**EndPage**](/windows/desktop/api/Wingdi/nf-wingdi-endpage) function. |
| <span id="DOCUMENTEVENT_ESCAPE"></span><span id="documentevent_escape"></span><dl> <dt>**DOCUMENTEVENT\_ESCAPE**</dt> </dl> | GDI is about to process a call to its [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function. |
| <span id="DOCUMENTEVENT_QUERYFILTER"></span><span id="documentevent_queryfilter"></span><dl> <dt>**DOCUMENTEVENT\_QUERYFILTER**</dt> </dl> | The DOCUMENTEVENT\_QUERYFILTER event represents an opportunity for the spooler to query the driver for a list of the DOCUMENTEVENT\_ *XXX* events to which the driver will respond. This event is issued just prior to a call to **DocumentEvent** that passes the DOCUMENTEVENT\_CREATEDCPRE event. |
| <span id="DOCUMENTEVENT_RESETDCPOST"></span><span id="documentevent_resetdcpost"></span><dl> <dt>**DOCUMENTEVENT\_RESETDCPOST**</dt> </dl> | GDI has just processed a call to its [**ResetDC**](/windows/desktop/api/wingdi/nf-wingdi-resetdca) function.<br/> This escape code should not be used unless there has been a previous call to **DocumentEvent** with *iEsc* set to DOCUMENTEVENT\_RESETDCPRE. |
| <span id="DOCUMENTEVENT_RESETDCPRE"></span><span id="documentevent_resetdcpre"></span><dl> <dt>**DOCUMENTEVENT\_RESETDCPRE**</dt> </dl> | GDI is about to process a call to its [**ResetDC**](/windows/desktop/api/wingdi/nf-wingdi-resetdca) function. |
| <span id="DOCUMENTEVENT_STARTDOCPOST"></span><span id="documentevent_startdocpost"></span><dl> <dt>**DOCUMENTEVENT\_STARTDOCPOST**</dt> </dl> | GDI has just processed a call to its [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca) function. |
| <span id="DOCUMENTEVENT_STARTDOCPRE_or_DOCUMENTEVENT_STARTDOC"></span><span id="documentevent_startdocpre_or_documentevent_startdoc"></span><span id="DOCUMENTEVENT_STARTDOCPRE_OR_DOCUMENTEVENT_STARTDOC"></span><dl> <dt>**DOCUMENTEVENT\_STARTDOCPRE or DOCUMENTEVENT\_STARTDOC**</dt> </dl> | GDI is about to process a call to its [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca) function. |
| <span id="DOCUMENTEVENT_STARTPAGE"></span><span id="documentevent_startpage"></span><dl> <dt>**DOCUMENTEVENT\_STARTPAGE**</dt> </dl> | GDI is about to process a call to its [**StartPage**](/windows/desktop/api/Wingdi/nf-wingdi-startpage) function. |

*cbIn* 

The size, in bytes, of the buffer pointed to by *pvIn*.

*pvIn* \[in\]

A pointer to a buffer. What the buffer contains depends on the value of *iEsc*, as shown in the following table.

| Constant | pvin Contents |
|-|-|
| <span id="DOCUMENTEVENT_ABORTDOC"></span><span id="documentevent_abortdoc"></span><dl> <dt>**DOCUMENTEVENT\_ABORTDOC**</dt> </dl> | Not used. |
| <span id="DOCUMENTEVENT_CREATEDCPOST"></span><span id="documentevent_createdcpost"></span><dl> <dt>**DOCUMENTEVENT\_CREATEDCPOST**</dt> </dl> | *pvIn* contains the address of a pointer to the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure specified in the *pvOut* parameter in a previous call to this function, for which the *iEsc* parameter was set to DOCUMENTEVENT\_CREATEDCPRE. |
| <span id="DOCUMENTEVENT_CREATEDCPRE"></span><span id="documentevent_createdcpre"></span><dl> <dt>**DOCUMENTEVENT\_CREATEDCPRE**</dt> </dl> | *pvIn* points to a DOCEVENT\_CREATEDCPRE structure which is documented in the [Windows Driver Development Kit](https://msdn.microsoft.com/windows/hardware/gg487428). |
| <span id="DOCUMENTEVENT_DELETEDC"></span><span id="documentevent_deletedc"></span><dl> <dt>**DOCUMENTEVENT\_DELETEDC**</dt> </dl> | Not used. |
| <span id="DOCUMENTEVENT_ENDDOCPOST"></span><span id="documentevent_enddocpost"></span><dl> <dt>**DOCUMENTEVENT\_ENDDOCPOST**</dt> </dl> | Not used. |
| <span id="DOCUMENTEVENT_ENDDOCPRE_or_DOCUMENTEVENT_ENDDOC"></span><span id="documentevent_enddocpre_or_documentevent_enddoc"></span><span id="DOCUMENTEVENT_ENDDOCPRE_OR_DOCUMENTEVENT_ENDDOC"></span><dl> <dt>**DOCUMENTEVENT\_ENDDOCPRE or DOCUMENTEVENT\_ENDDOC**</dt> </dl> | Not used. |
| <span id="DOCUMENTEVENT_ENDPAGE"></span><span id="documentevent_endpage"></span><dl> <dt>**DOCUMENTEVENT\_ENDPAGE**</dt> </dl> | Not used. |
| <span id="DOCUMENTEVENT_ESCAPE"></span><span id="documentevent_escape"></span><dl> <dt>**DOCUMENTEVENT\_ESCAPE**</dt> </dl> | *pvIn* points to a DOCEVENT\_ESCAPE structure which is documented in the [Windows Driver Development Kit](https://msdn.microsoft.com/windows/hardware/gg487428). |
| <span id="DOCUMENTEVENT_QUERYFILTER"></span><span id="documentevent_queryfilter"></span><dl> <dt>**DOCUMENTEVENT\_QUERYFILTER**</dt> </dl> | Same as for DOCUMENTEVENT\_CREATEDCPRE. |
| <span id="DOCUMENTEVENT_RESETDCPOST"></span><span id="documentevent_resetdcpost"></span><dl> <dt>**DOCUMENTEVENT\_RESETDCPOST**</dt> </dl> | *pvIn* contains the address of a pointer to the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure specified in the *pvOut* parameter in a previous call to this function, for which the *iEsc* parameter was set to DOCUMENTEVENT\_RESETDCPRE. |
| <span id="DOCUMENTEVENT_RESETDCPRE"></span><span id="documentevent_resetdcpre"></span><dl> <dt>**DOCUMENTEVENT\_RESETDCPRE**</dt> </dl> | *pvIn* contains the address of a pointer to the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure supplied by the caller of [**ResetDC**](/windows/desktop/api/wingdi/nf-wingdi-resetdca). |
| <span id="DOCUMENTEVENT_STARTDOCPOST"></span><span id="documentevent_startdocpost"></span><dl> <dt>**DOCUMENTEVENT\_STARTDOCPOST**</dt> </dl> | *pvIn* points to a LONG that specifies the print job identifier returned by [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca). |
| <span id="DOCUMENTEVENT_STARTDOCPRE_or_DOCUMENTEVENT_STARTDOC"></span><span id="documentevent_startdocpre_or_documentevent_startdoc"></span><span id="DOCUMENTEVENT_STARTDOCPRE_OR_DOCUMENTEVENT_STARTDOC"></span><dl> <dt>**DOCUMENTEVENT\_STARTDOCPRE or DOCUMENTEVENT\_STARTDOC**</dt> </dl> | *pvIn* contains the address of a pointer to a [**DOCINFO**](/windows/desktop/api/Wingdi/ns-wingdi-docinfoa) structure supplied by the caller of [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca). |
| <span id="DOCUMENTEVENT_STARTPAGE"></span><span id="documentevent_startpage"></span><dl> <dt>**DOCUMENTEVENT\_STARTPAGE**</dt> </dl> | Not used. |

*cbOut*

| Value                       | Meaning                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------|
| IDOCUMENTEVENT\_QUERYFILTER | The size, in bytes, of the buffer pointer to by *pvOut*.                             |
| DOCUMENTEVENT\_ESCAPE       | A value that is used as the *cbOutput* parameter for [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape). |
| For all other values        | *iEsc* is not used.                                                                  |

*pvOut* \[out\]

A pointer to a buffer. The contents of the buffer depend on the value supplied for *iEsc*, as shown in the following table.

| Constant                                                                                                                                                                                          | pvOut Contents                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DOCUMENTEVENT_CREATEDCPRE"></span><span id="documentevent_createdcpre"></span><dl> <dt>**DOCUMENTEVENT\_CREATEDCPRE**</dt> </dl> | A pointer to a driver-supplied [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure, which GDI uses instead of the one supplied by the [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) caller. (If **NULL**, GDI uses the caller-supplied structure.)<br/> |
| <span id="DOCUMENTEVENT_ESCAPE"></span><span id="documentevent_escape"></span><dl> <dt>**DOCUMENTEVENT\_ESCAPE**</dt> </dl>                | A pointer to a buffer that is used as the *lpszOutData* parameter for [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape).<br/>                                                                                                              |
| <span id="DOCUMENTEVENT_QUERYFILTER"></span><span id="documentevent_queryfilter"></span><dl> <dt>**DOCUMENTEVENT\_QUERYFILTER**</dt> </dl> | A pointer to buffer containing a DOCEVENT\_FILTER structure which is documented in the [Windows Driver Development Kit](https://msdn.microsoft.com/windows/hardware/gg487428).<br/>                                          |
| <span id="DOCUMENTEVENT_RESETDCPRE"></span><span id="documentevent_resetdcpre"></span><dl> <dt>**DOCUMENTEVENT\_RESETDCPRE**</dt> </dl>    | A pointer to a driver-supplied [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure, which GDI uses instead of the one supplied by the [**ResetDC**](/windows/desktop/api/wingdi/nf-wingdi-resetdca) caller. (If **NULL**, GDI uses the caller-supplied structure.)<br/>   |

## Return value

The function's return value is dependent on the escape supplied for *iEsc*. For some escape codes, the return value is not used (see below). If the function supplies a return value, it must be one of the following.

| Return Value               | Meaning                                                                           |
|----------------------------|-----------------------------------------------------------------------------------|
| DOCUMENTEVENT\_FAILURE     | The driver supports the escape code identified by *iEsc*, but a failure occurred. |
| DOCUMENTEVENT\_SUCCESS     | The driver successfully handled the escape code identified by *iEsc*.             |
| DOCUMENTEVENT\_UNSUPPORTED | The driver does not support the escape code identified by *iEsc*.                 |

The following list indicates which escape codes that require a return value and which do not, and explains the meaning of the DOCUMENTEVENT\_SUCCESS, DOCUMENTEVENT\_FAILURE, and DOCUMENTEVENT\_UNSUPPORTED return codes.

| Return Value                                          | Meaning                                                                                                                                                                                    |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DOCUMENTEVENT\_ABORTDOC                               | The return value is not used and should not be read.                                                                                                                                       |
| DOCUMENTEVENT\_CREATEDCPOST                           | The return value is not used and should not be read.                                                                                                                                       |
| DOCUMENTEVENT\_CREATEDCPRE                            | DOCUMENTEVENT\_FAILURE - GDI does not create the device context or information context, and provides a return value of 0 for [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) or [**CreateIC**](/windows/desktop/api/wingdi/nf-wingdi-createica). |
| DOCUMENTEVENT\_DELETEDC                               | The return value is not used and should not be read.                                                                                                                                       |
| DOCUMENTEVENT\_ENDDOCPOST                             | The return value is not used and should not be read.                                                                                                                                       |
| DOCUMENTEVENT\_ENDDOCPRE or DOCUMENTEVENT\_ENDDOC     | The return value is not used and should not be read.                                                                                                                                       |
| DOCUMENTEVENT\_ENDPAGE                                | The return value is not used and should not be read.                                                                                                                                       |
| DOCUMENTEVENT\_ESCAPE                                 | The return value is not used and should not be read.                                                                                                                                       |
| DOCUMENTEVENT\_QUERYFILTER                            | See Remarks.                                                                                                                                                                               |
| DOCUMENTEVENT\_RESETDCPOST                            | The return value is not used and should not be read.                                                                                                                                       |
| DOCUMENTEVENT\_RESETDCPRE                             | DOCUMENTEVENT\_FAILURE - GDI does not reset the device context, and provides a return value of 0 for [**ResetDC**](/windows/desktop/api/wingdi/nf-wingdi-resetdca).                                                           |
| DOCUMENTEVENT\_STARTDOCPOST                           | DOCUMENTEVENT\_FAILURE - GDI calls [**AbortDoc**](/windows/desktop/api/Wingdi/nf-wingdi-abortdoc) to stop the document, and then provides a return value of SP\_ERROR for [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca).                      |
| DOCUMENTEVENT\_STARTDOCPRE or DOCUMENTEVENT\_STARTDOC | DOCUMENTEVENT\_FAILURE - GDI does not start the document, and provides a return value of SP\_ERROR for [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca).                                                       |
| DOCUMENTEVENT\_STARTPAGE                              | DOCUMENTEVENT\_FAILURE - GDI does not start the page, and provides a return value of SP\_ERROR for [**StartPage**](/windows/desktop/api/Wingdi/nf-wingdi-startpage).                                                         |

## Remarks

For an *iEsc* value of DOCUMENTEVENT\_QUERYFILTER, the spooler can interpret a DOCUMENTEVENT\_SUCCESS value returned by **DocumentEvent** in two ways, depending on whether the driver modified certain members of the DOCEVENT\_FILTER structure (which is documented in the [Windows Driver Development Kit](https://msdn.microsoft.com/windows/hardware/gg487428) ). (The *pvOut* parameter points to this structure.) When the spooler allocates memory for a structure of this type, it initializes two members of this structure, **cElementsReturned** and **cElementsNeeded**, to known values. After **DocumentEvent** returns, the spooler determines whether the values of these members have changed, and uses that information to interpret the **DocumentEvent** return value. The following table summarizes this situation.

| Return Value                          | Status of cElementsReturned and cElementsNeeded    | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DOCUMENTEVENT\_SUCCESS<br/>     | Driver made no change to either member.<br/> | The spooler interprets this return value as equivalent to DOCUMENTEVENT\_UNSUPPORTED. The spooler is unable to retrieve the event filter from the driver, so it persists in calling **DocumentEvent** for all events.<br/>                                                                                                                                                                                                                         |
| DOCUMENTEVENT\_SUCCESS<br/>     | Driver wrote to one or both members.<br/>    | The spooler accepts this return value without interpretation. If the driver wrote to only one of **cElementsNeeded** and **cElementsReturned**, the spooler considers the unchanged member to have a value of zero.<br/> The spooler filters out all events listed in the **aDocEventCall** member of DOCEVENT\_FILTER (which is documented in the [Windows Driver Development Kit](https://msdn.microsoft.com/windows/hardware/gg487428) ).<br/> |
| DOCUMENTEVENT\_UNSUPPORTED<br/> | Not applicable<br/>                          | The driver does not support DOCUMENTEVENT\_QUERYFILTER.<br/> The spooler is unable to retrieve the event filter from the driver, so it persists in calling **DocumentEvent** for all events.<br/>                                                                                                                                                                                                                                            |
| DOCUMENTEVENT\_FAILURE<br/>     | Not applicable<br/>                          | The driver supports DOCUMENTEVENT\_QUERYFILTER, but encountered an internal error.<br/> The spooler is unable to retrieve the event filter from the driver, so it persists in calling **DocumentEvent** for all events.<br/>                                                                                                          

If the escape code supplied in the *iEsc* parameter is DOCUMENTEVENT\_CREATEDCPRE, the following rules apply:

-   If the job is being sent directly to the printer without spooling, pvIn->pszDevice points to the printer name. (For more information, see the documentation for the DOCEVENT\_CREATEDCPRE structure in the [Windows Driver Development Kit](https://msdn.microsoft.com/windows/hardware/gg487428).)
-   If the job is being spooled, pvIn->pszDevice points to the printer port name.

> [!NOTE]  
> The following restrictions apply when running a 32-bit application on a 64-bit version of Windows. The only GDI function that **DocumentEvent** should call is [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape), and only private escapes should be used. **DocumentEvent** calls to other GDI functions may produce undefined behavior.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **DocumentEventW** (Unicode) and **DocumentEventA** (ANSI)<br/>                                     |

## See also

* [Printing](printdocs-printing.md)
* [Print Spooler API Functions](printing-and-print-spooler-functions.md)
* [Windows Driver Development Kit](https://msdn.microsoft.com/windows/hardware/gg487428)
