---
description: The MXDC\_S0PAGE\_DATA\_T structure holds an XPS document page to be passed to the Microsoft XPS Document Converter (MXDC) output file without any processing.
ms.assetid: 3dc8e0b9-cf63-4345-93d2-3b60dac42546
title: MXDC_S0PAGE_DATA_T structure (Mxdc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MXDC_S0PAGE_DATA_T
api_type: 
- HeaderDef
api_location: 
- mxdc.h
---

# MXDC\_S0PAGE\_DATA\_T structure

The **MXDC\_S0PAGE\_DATA\_T** structure holds an XPS document page to be passed to the Microsoft XPS Document Converter (MXDC) output file without any processing.

## Syntax


```C++
typedef struct tagMxdcS0PageData {
  ULONG dwSize;
  BYTE  bData[1];
} MXDC_S0PAGE_DATA_T, *P_MXDC_S0PAGE_DATA_T;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

The size of the output buffer, **bData**.

</dd> <dt>

**bData**
</dt> <dd>

The XPS document page.

</dd> </dl>

## Remarks

This structure is appended to an [**MXDC\_ESCAPE\_HEADER\_T**](mxdcescapeheader.md) structure (which has its **opCode** set to MXDCOP\_SET\_S0PAGE) to make an [**MXDC\_S0PAGE\_PASSTHROUGH\_ESCAPE\_T**](mxdcs0pagepassthroughescape.md) structure. That structure is then passed to the *lpszInData* parameter of the [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) function when it is called with [**MXDC\_ESCAPE**](mxdc-escape.md) as the escape. The result is that the MXDC passes the page through to the output without processing it.

The call to [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) must be between a call to [**StartPage**](/windows/desktop/api/Wingdi/nf-wingdi-startpage) and a call to [**EndPage**](/windows/desktop/api/Wingdi/nf-wingdi-endpage).

The calling application is responsible for validating the XML of the XPS document page.

Streaming consumption is more efficient if you call [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) with **MXDCOP\_SET\_S0PAGE\_RESOURCE** as **opCode** for each resource on the page before you call it with **MXDCOP\_SET\_S0PAGE**.

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

 

