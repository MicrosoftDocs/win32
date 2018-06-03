---
Description: Converts a print ticket to a DEVMODE structure.
ms.assetid: 3b0a6afd-fa9d-434e-a95f-b051296d4567
title: ConvertPrintTicketToDevModeThunk2 function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConvertPrintTicketToDevModeThunk2 function

\[This function is not supported and might be disabled or deleted in future versions of Windows. [**PTConvertPrintTicketToDevMode**](/windows/desktop/api/prntvpt/nf-prntvpt-ptconvertprinttickettodevmode) provides equivalent functionality and should be used instead.\]

Converts a print ticket to a [**DEVMODE**](/windows/desktop/api/Wingdi/ns-wingdi-_devicemodea) structure.

## Syntax


```C++
HRESULT ConvertPrintTicketToDevModeThunk2(
  _In_      HPTPROVIDER hProvider,
  _In_      BYTE        *pPrintTicket,
  _In_      ULONG       cbSize,
  _In_      INT         baseType,
  _In_      DWORD       scope,
  _Out_     BYTE        **ppDevmode,
  _Out_     ULONG       *pcbDevModeLength,
  _Out_opt_ BSTR        *errMsg
);
```



## Parameters

<dl> <dt>

*hProvider* \[in\]
</dt> <dd>

A handle to an open print ticket provider. This handle is returned by the [**BindPTProviderThunk**](bindptproviderthunk.md) function.

</dd> <dt>

*pPrintTicket* \[in\]
</dt> <dd>

The buffer that contains the print ticket to convert.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

The size, in bytes, of the buffer passed in *pPrintTicket*.

</dd> <dt>

*baseType* \[in\]
</dt> <dd>

A value indicating whether the user's default [**DEVMODE**](/windows/desktop/api/Wingdi/ns-wingdi-_devicemodea) or the print queue's default **DEVMODE** is used to provide values to the output **DEVMODE** when *pPrintTicket* does not specify every possible setting for a **DEVMODE**. The value of this parameter must be a member of the [**EDefaultDevmodeType**](/windows/desktop/api/prntvpt/ne-prntvpt-tagedefaultdevmodetype) enumeration, cast as an **INT**.

</dd> <dt>

*scope* \[in\]
</dt> <dd>

A value that specifies the scope of *pPrintTicket*. This value can specify a single page, an entire document, or all documents in the print job. The value of this parameter must be a member of the [**EPrintTicketScope**](/windows/desktop/api/prntvpt/ne-prntvpt-eprintticketscope) enumeration, cast as a **DWORD**.

</dd> <dt>

*ppDevmode* \[out\]
</dt> <dd>

The address of the newly created [**DEVMODE**](/windows/desktop/api/Wingdi/ns-wingdi-_devicemodea). This function calls [**CoTaskMemAlloc**](https://msdn.microsoft.com/library/windows/desktop/ms692727) to allocate this buffer. When the buffer is no longer needed, the caller must free it by calling [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722).

</dd> <dt>

*pcbDevModeLength* \[out\]
</dt> <dd>

The size, in bytes, of the [**DEVMODE**](/windows/desktop/api/Wingdi/ns-wingdi-_devicemodea) returned in *ppDevmode*.

</dd> <dt>

*errMsg* \[out, optional\]
</dt> <dd>

A pointer to a string that specifies what, if anything, is invalid about the print ticket in *pPrintTicket*. If it is valid, this is **NULL**. If *errMsg* is not **NULL** when the function returns, the caller must free the string with [**SysFreeString**](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3).

</dd> </dl>

## Return value

If the method succeeds, it returns **S\_OK**; otherwise, it returns an **HRESULT** error code. For more information about COM error codes, see [Error Handling](https://www.bing.com/search?q=Error Handling).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Prntvpt.dll</dt> </dl> |



## See also

<dl> <dt>

[Print Schema](https://www.bing.com/search?q=Print Schema)
</dt> <dt>

[**PTConvertPrintTicketToDevMode**](/windows/desktop/api/prntvpt/nf-prntvpt-ptconvertprinttickettodevmode)
</dt> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

 




