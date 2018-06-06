---
Description: Converts a DEVMODE structure to a print ticket.
ms.assetid: c03371f8-a978-4fb7-82cc-f76a65f3904c
title: ConvertDevModeToPrintTicketThunk2 function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConvertDevModeToPrintTicketThunk2 function

\[This function is not supported and might be disabled or deleted in future versions of Windows. [**PTConvertDevModeToPrintTicket**](/windows/desktop/api/prntvpt/nf-prntvpt-ptconvertdevmodetoprintticket) provides equivalent functionality and should be used instead.\]

Converts a [**DEVMODE**](/windows/desktop/api/Wingdi/ns-wingdi-_devicemodea) structure to a print ticket.

## Syntax


```C++
HRESULT ConvertDevModeToPrintTicketThunk2(
  _In_  HPTPROVIDER hProvider,
  _In_  BYTE        *pDevmode,
  _In_  ULONG       cbSize,
  _In_  DWORD       scope,
  _Out_ BYTE        **ppPrintTicket,
  _Out_ INT         *pcbPrintTicketLength
);
```



## Parameters

<dl> <dt>

*hProvider* \[in\]
</dt> <dd>

A handle to an open print ticket provider. This handle is returned by the [**BindPTProviderThunk**](bindptproviderthunk.md) function.

</dd> <dt>

*pDevmode* \[in\]
</dt> <dd>

A pointer to the [**DEVMODE**](/windows/desktop/api/Wingdi/ns-wingdi-_devicemodea) to convert.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

The size, in bytes, of the [**DEVMODE**](/windows/desktop/api/Wingdi/ns-wingdi-_devicemodea) passed in *pDevmode*.

</dd> <dt>

*scope* \[in\]
</dt> <dd>

A value that specifies the scope of *ppPrintTicket*. This value can specify a single page, an entire document, or all documents in the print job. The value of this parameter must be a member of the [**EPrintTicketScope**](/windows/desktop/api/prntvpt/ne-prntvpt-eprintticketscope) enumeration, cast as a **DWORD**.

</dd> <dt>

*ppPrintTicket* \[out\]
</dt> <dd>

The address of the buffer that contains a print ticket that represents the [**DEVMODE**](/windows/desktop/api/Wingdi/ns-wingdi-_devicemodea) passed in *pDevmode*. This function calls [**CoTaskMemAlloc**](https://msdn.microsoft.com/library/windows/desktop/ms692727) to allocate this buffer. When the buffer is no longer needed, the caller must free it by calling [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722).

</dd> <dt>

*pcbPrintTicketLength* \[out\]
</dt> <dd>

The size, in bytes, of the print ticket returned in *ppPrintTicket*.

</dd> </dl>

## Return value

If the method succeeds, it returns **S\_OK**; otherwise, it returns an **HRESULT** error code. For more information about COM error codes, see [Error Handling](https://www.bing.com/search?q=Error+Handling).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Prntvpt.dll</dt> </dl> |



## See also

<dl> <dt>

[Print Schema](https://www.bing.com/search?q=Print+Schema)
</dt> <dt>

[**PTConvertDevModeToPrintTicket**](/windows/desktop/api/prntvpt/nf-prntvpt-ptconvertdevmodetoprintticket)
</dt> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

 




