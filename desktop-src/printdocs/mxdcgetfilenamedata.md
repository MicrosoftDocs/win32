---
description: The MXDC\_GET\_FILENAME\_DATA\_T structure holds the full path and file name of a Microsoft XPS Document Converter (MXDC) output file.
ms.assetid: 070bce2e-5055-47e8-9412-2094a636635f
title: MXDC_GET_FILENAME_DATA_T structure (Mxdc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MXDC_GET_FILENAME_DATA_T
api_type: 
- HeaderDef
api_location: 
- mxdc.h
---

# MXDC\_GET\_FILENAME\_DATA\_T structure

The **MXDC\_GET\_FILENAME\_DATA\_T** structure holds the full path and file name of a Microsoft XPS Document Converter (MXDC) output file.

## Syntax


```C++
typedef struct _tagMxdcGetFileNameData {
  ULONG   cbOutput;
  wchar_t wszData[1];
} MXDC_GET_FILENAME_DATA_T, *P_MXDC_GET_FILENAME_DATA_T;
```



## Members

<dl> <dt>

**cbOutput**
</dt> <dd>

The size of the output buffer, **wszData**.

</dd> <dt>

**wszData**
</dt> <dd>

The fully qualified path and file name of the output file.

</dd> </dl>

## Remarks

This structure is returned by [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape) when it is called with the [**MXDC\_ESCAPE**](mxdc-escape.md) escape and the [**MXDC\_ESCAPE\_HEADER\_T**](mxdcescapeheader.md) structure that is passed in the *lpszInData* parameter has its **opCode** set to **MXDCOP\_GET\_FILENAME**.

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

 

