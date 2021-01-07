---
description: The MXDC\_ESCAPE\_HEADER\_T structure holds the operation code for a call to ExtEscape with MXDC\_ESCAPE as the nEscape parameter. It also provides the sizes of the input and output buffers.
ms.assetid: 3d1f909c-0c3c-49ac-b530-4ce077ad6d94
title: MXDC_ESCAPE_HEADER_T structure (Mxdc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MXDC_ESCAPE_HEADER_T
api_type: 
- HeaderDef
api_location: 
- mxdc.h
---

# MXDC\_ESCAPE\_HEADER\_T structure

The **MXDC\_ESCAPE\_HEADER\_T** structure holds the operation code for a call to [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) with [**MXDC\_ESCAPE**](mxdc-escape.md) as the *nEscape* parameter. It also provides the sizes of the input and output buffers.

## Syntax


```C++
typedef struct tagMxdcEscapeHeader {
  ULONG cbInput;
  ULONG cbOutput;
  ULONG opCode;
} MXDC_ESCAPE_HEADER_T, *P_MXDC_ESCAPE_HEADER_T;
```



## Members

<dl> <dt>

**cbInput**
</dt> <dd>

The size of the input buffer that will be passed to the *lpszOutData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function.

</dd> <dt>

**cbOutput**
</dt> <dd>

The size of the output buffer. This is the same value as the *cbOutput* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function.

</dd> <dt>

**opCode**
</dt> <dd>

The code constant that tells MXDC what to do.



| Operations code                      | Description                                                                                                                                                                                                            |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MXDCOP\_GET\_FILENAME                | Returns, in the *lpszOutData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function, either the full path of the output file as a zero-terminated string or the size of that string. See Remarks.                   |
| MXDCOP\_PRINTTICKET\_FIXED\_DOC\_SEQ | Associates a print ticket with an XPS fixed document sequence.                                                                                                                                                         |
| MXDCOP\_PRINTTICKET\_FIXED\_DOC      | Associates a print ticket with an XPS document.                                                                                                                                                                        |
| MXDCOP\_PRINTTICKET\_FIXED\_PAGE     | Associates a print ticket with an XPS page.                                                                                                                                                                            |
| MXDCOP\_SET\_S0PAGE                  | Sends the XPS markup of the current page to the output.                                                                                                                                                                |
| MXDCOP\_SET\_S0PAGE\_RESOURCE        | Sends a resource on the page, such as an image or font, to the output.                                                                                                                                                 |
| MXDCOP\_SET\_XPSPASSTHRU\_MODE       | Puts the MXDC into a pass-through state, enabling an application to write XPS directly to the output file without any processing by the MXDC. An entire document or even document sequence can be written in this way. |



 

</dd> </dl>

## Remarks

Before calling [**MXDC\_ESCAPE**](mxdc-escape.md),\_applications should first verify that the driver is MXDC by calling [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) with the [**GETTECHNOLOGY**](/previous-versions/windows/desktop/legacy/dd144931(v=vs.85)) escape. If the driver is the MXDC the function returns the zero-terminated string "http://schemas.microsoft.com/xps/2005/06".

This structure is always at the beginning of the data passed to the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function in its *lpszInData* parameter.

When **opCode** is MXDCOP\_GET\_FILENAME:

-   The *lpszInData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function consists of only the **MXDC\_ESCAPE\_HEADER\_T** structure.
-   Obtain the output filename by calling [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) twice.
    1.  The first time, pass 4 to the *cbOutput* parameter of [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape). Set the *lpszOutData* parameter to point to any allocated 4 bytes of memory. The size of the fully qualified file path will be returned in the *lpszOutData* parameter of **ExtEscape**.
    2.  Then call the function again. This time set both *cbOutput* and *cbInput* to 4+ *DataSize*. The fully qualified file path will be returned in an [**MxdcGetFileNameData**](mxdcgetfilenamedata.md) structure.

When **opCode** is MXDCOP\_PRINTTICKET\_FIXED\_DOC\_SEQ or MXDCOP\_PRINTTICKET\_FIXED\_DOC:

-   The *lpszInData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function consists of the **MXDC\_ESCAPE\_HEADER\_T** structure and an [**MxdcPrintTicketPassthrough**](mxdcprintticketpassthrough.md) structure concatenated into an [**MxdcPrintTicketEscape**](mxdcprintticketescape.md) structure.
-   The call to [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) must occur between a call to [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca) and a call to [**EndDoc**](/windows/desktop/api/Wingdi/nf-wingdi-enddoc).

When **opCode** is MXDCOP\_PRINTTICKET\_FIXED\_PAGE:

-   The *lpszInData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function consists of the **MXDC\_ESCAPE\_HEADER\_T** structure and an [**MxdcPrintTicketPassthrough**](mxdcprintticketpassthrough.md) structure concatenated into an [**MxdcPrintTicketEscape**](mxdcprintticketescape.md) structure.
-   The call to [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) must occur between a call to [**StartPage**](/windows/desktop/api/Wingdi/nf-wingdi-startpage) and a call to [**EndPage**](/windows/desktop/api/Wingdi/nf-wingdi-endpage).

When **opCode** is MXDCOP\_SET\_S0PAGE:

-   The *lpszInData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function consists of the **MXDC\_ESCAPE\_HEADER\_T** structure and an [**MxdcS0PageData**](mxdcs0pagedata.md) structure concatenated into an [**MxdcS0PagePassthroughEscape**](mxdcs0pagepassthroughescape.md) structure.
-   The call to [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) must occur between a call to [**StartPage**](/windows/desktop/api/Wingdi/nf-wingdi-startpage) and a call to [**EndPage**](/windows/desktop/api/Wingdi/nf-wingdi-endpage).
-   The calling application is responsible for validating the XML.
-   Streaming consumption is more efficient if you call [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) with MXDCOP\_SET\_S0PAGE\_RESOURCE as **opCode** for each resource on the page before you call it with MXDCOP\_SET\_S0PAGE.

When **opCode** is MXDCOP\_SET\_S0PAGE\_RESOURCE:

-   The *lpszInData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function consists of the **MXDC\_ESCAPE\_HEADER\_T** structure and an [**MxdcXpsS0PageResource**](mxdcxpss0pageresource.md) structure concatenated into an [**MxdcS0PageResourceEscape**](mxdcs0pageresourceescape.md) structure.
-   The call to [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) must occur between a call to [**StartPage**](/windows/desktop/api/Wingdi/nf-wingdi-startpage) and a call to [**EndPage**](/windows/desktop/api/Wingdi/nf-wingdi-endpage), but there can be multiple such calls between the **StartPage** and **EndPage** calls.
-   Streaming consumption is more efficient if you call [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) with MXDCOP\_SET\_S0PAGE\_RESOURCE as **opCode** for each resource on the page before you call it with MXDCOP\_SET\_S0PAGE.

When **opCode** is MXDCOP\_SET\_XPSPASSTHRU\_MODE:

-   The *lpszInData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function consists of only the **MXDC\_ESCAPE\_HEADER\_T** structure.
-   This call must occur before the call to [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mxdc.h</dt> </dl> |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[GDI Printer Escape Functions](/previous-versions/windows/desktop/legacy/dd162843(v=vs.85))
</dt> <dt>

[**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape)
</dt> <dt>

[**MXDC\_ESCAPE**](mxdc-escape.md)
</dt> </dl>

 

