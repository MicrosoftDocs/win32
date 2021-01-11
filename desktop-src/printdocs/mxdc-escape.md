---
description: The MXDC\_ESCAPE printer escape function enables applications to write documents to a file or to a printer in XML Paper Specification (XPS) format by means of the Microsoft XPS Document Converter (MXDC).
ms.assetid: 79aeb32e-94b1-4806-8ebf-a9d0956f4667
title: MXDC_ESCAPE function (Mxdc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MXDC_ESCAPE
api_type: 
- HeaderDef
api_location: 
- mxdc.h
---

# MXDC\_ESCAPE function

The **MXDC\_ESCAPE** printer escape function enables applications to write documents to a file or to a printer in XML Paper Specification (XPS) format by means of the Microsoft XPS Document Converter (MXDC).

To perform this operation, call the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function with the following parameters.

## Syntax


```C++
int MXDC_ESCAPE(
    hdc,
    cbInput,
    lpszInData,
    cbOutput,
    lpszOutData
);
```



## Parameters

<dl> <dt>

*hdc* 
</dt> <dd>

A handle to the printer device context.

</dd> <dt>

*cbInput* 
</dt> <dd>

The size, in bytes, of the data pointed to by the *lpszInData* parameter.

</dd> <dt>

*lpszInData* 
</dt> <dd>

A pointer to a buffer containing the input data, which is always stored in one of the following structures.

<dl> <dd><a href="mxdcescapeheader.md">**MxdcEscapeHeader**</a></dd> <dd><a href="mxdcprintticketescape.md">**MxdcPrintTicketEscape**</a></dd> <dd><a href="mxdcs0pagepassthroughescape.md">**MxdcS0PagePassthroughEscape**</a></dd> <dd><a href="mxdcs0pageresourceescape.md">**MxdcS0PageResourceEscape**</a></dd> </dl>

Each of these structures has an opcode member that specifies what the MXDC is supposed to do. See MxdcEscapeHeader for detailed remarks about these codes.



| Operations code (opcode)                                                                                                                                                                                                  | Action                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MXDCOP_GET_FILENAME"></span><span id="mxdcop_get_filename"></span><dl> <dt>**MXDCOP\_GET\_FILENAME**</dt> </dl>                                          | Sets the *lpszOutData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function to, either the full path of the output file as a zero-terminated string or else the size of that string.<br/>                               |
| <span id="MXDCOP_PRINTTICKET_FIXED_DOC_SEQ"></span><span id="mxdcop_printticket_fixed_doc_seq"></span><dl> <dt>**MXDCOP\_PRINTTICKET\_FIXED\_DOC\_SEQ**</dt> </dl> | Associates a print ticket with an XPS fixed document sequence.<br/>                                                                                                                                                         |
| <span id="MXDCOP_PRINTTICKET_FIXED_DOC"></span><span id="mxdcop_printticket_fixed_doc"></span><dl> <dt>**MXDCOP\_PRINTTICKET\_FIXED\_DOC**</dt> </dl>              | Associates a print ticket with an XPS document.<br/>                                                                                                                                                                        |
| <span id="MXDCOP_PRINTTICKET_FIXED_PAGE"></span><span id="mxdcop_printticket_fixed_page"></span><dl> <dt>**MXDCOP\_PRINTTICKET\_FIXED\_PAGE**</dt> </dl>           | Associates a print ticket with an XPS page.<br/>                                                                                                                                                                            |
| <span id="MXDCOP_SET_S0PAGE"></span><span id="mxdcop_set_s0page"></span><dl> <dt>**MXDCOP\_SET\_S0PAGE**</dt> </dl>                                                | Sends the XPS markup of the current page to the output.<br/>                                                                                                                                                                |
| <span id="MXDCOP_SET_S0PAGE_RESOURCE"></span><span id="mxdcop_set_s0page_resource"></span><dl> <dt>**MXDCOP\_SET\_S0PAGE\_RESOURCE**</dt> </dl>                    | Sends a resource on the page, such as an image or font, to the output.<br/>                                                                                                                                                 |
| <span id="MXDCOP_SET_XPSPASSTHRU_MODE"></span><span id="mxdcop_set_xpspassthru_mode"></span><dl> <dt>**MXDCOP\_SET\_XPSPASSTHRU\_MODE**</dt> </dl>                 | Puts the MXDC into a pass through state, enabling an application to write XPS directly to the output file without any processing by the MXDC. An entire document or even document sequence can be written in this way.<br/> |



 

</dd> <dt>

*cbOutput* 
</dt> <dd>

The size, in bytes, of the data pointed to by the *lpszOutData* parameter.

</dd> <dt>

*lpszOutData* 
</dt> <dd>

A pointer to a buffer containing the output data.

</dd> </dl>

## Return value

If the function succeeds, the return value is greater than zero. If the function fails or is not supported, the return value is less than or equal to zero.

## Remarks

This escape is supported by MXDC and XPSDrv, but not by GDI.

To determine if the printer driver is the MXDC, call [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) with the [**GETTECHNOLOGY**](/previous-versions/windows/desktop/legacy/dd144931(v=vs.85)) escape. If the driver is the MXDC, the **ExtEscape** will return the zero-terminated string, "http://schemas.microsoft.com/xps/2005/06". Be sure the buffer referenced by the *lpszOutData* parameter is large enough to hold this string.

To determine if the printer driver is the Windows in-box Microsoft XPS Document Writer driver, confirm that the printer driver is the MXDC, and then determine whether the name of the printer driver is "Microsoft XPS Document Writer".

To get the printer driver name, use one of the following techniques. <dl> Call [**GetPrinterDriver**](getprinterdriver.md) with the *Level* parameter value set to 1. The printer driver name is returned in the **pName** member of the [**DRIVER\_INFO\_1**](driver-info-1.md) structure.  
or  
Call [**GetPrinter**](getprinter.md) with the *Level* parameter value set to 2. The printer driver name is returned in the **pDriverName** member of the [**PRINTER\_INFO\_2**](printer-info-2.md) structure.  
</dl>

The following table shows where to find various objects in the XPS file various types of objects will be written.



| Object       | Location in the output file    |
|--------------|--------------------------------|
| Fixed Page   | /Documents/1/Pages/Esc%d.fpage |
| Thumbnail    | /Documents/1/Metadata          |
| Print Ticket | /Documents/1/Metadata          |
| Font         | /Documents/1/Resources/Fonts   |
| Image        | /Documents/1/Resources/Images  |



 

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

[Printer Escape Functions](/previous-versions/windows/desktop/legacy/dd162843(v=vs.85))
</dt> <dt>

[**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape)
</dt> </dl>

 

