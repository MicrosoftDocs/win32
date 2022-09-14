---
description: Merges two print tickets and returns a valid, viable print ticket.
ms.assetid: 4aa7b9de-abf2-4781-942e-0b992a6bffed
title: MergeAndValidatePrintTicketThunk2 function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MergeAndValidatePrintTicketThunk2
api_type: 
- DllExport
api_location: 
- prntvpt.dll
---

# MergeAndValidatePrintTicketThunk2 function

\[This function is not supported and might be disabled or deleted in future versions of Windows. [**PTMergeAndValidatePrintTicket**](/windows/desktop/api/prntvpt/nf-prntvpt-ptmergeandvalidateprintticket) provides equivalent functionality and should be used instead.\]

Merges two print tickets and returns a valid, viable print ticket.

## Syntax


```C++
HRESULT MergeAndValidatePrintTicketThunk2(
  _In_      HPTPROVIDER hProvider,
  _In_      BYTE        *pBasePrintTicket,
  _In_      INT         basePrintTicketLength,
  _In_opt_  BYTE        *pDeltaPrintTicket,
  _In_      INT         deltaPrintTicketLength,
  _In_      DWORD       scope,
  _Out_     BYTE        **ppValidatedPrintTicket,
  _Out_     INT         *pValidatedPrintTicketLength,
  _Out_opt_ BSTR        *pbstrErrorMessage
);
```



## Parameters

<dl> <dt>

*hProvider* \[in\]
</dt> <dd>

A handle to an open print ticket provider. This handle is returned by the [**BindPTProviderThunk**](bindptproviderthunk.md) function.

</dd> <dt>

*pBasePrintTicket* \[in\]
</dt> <dd>

The buffer that contains the base print ticket data, expressed in XML as described in the [Print Schema](./printschema.md).

</dd> <dt>

*basePrintTicketLength* \[in\]
</dt> <dd>

The size, in bytes, of the buffer referenced by *pBasePrintTicket*.

</dd> <dt>

*pDeltaPrintTicket* \[in, optional\]
</dt> <dd>

The buffer that contains the print ticket to merge. The print ticket data is expressed in XML as described in the [Print Schema](./printschema.md). The value of this parameter can be **NULL**.

</dd> <dt>

*deltaPrintTicketLength* \[in\]
</dt> <dd>

The size, in bytes, of the buffer referenced by *pDeltaPrintTicket*.

</dd> <dt>

*scope* \[in\]
</dt> <dd>

The value that specifies whether the scope of *pDeltaPrintTicket* and *ppValidatedPrintTicket* is a single page, an entire document, or all documents in the print job. The value of this parameter must be a member of the [**EPrintTicketScope**](/windows/desktop/api/prntvpt/ne-prntvpt-eprintticketscope) enumeration, cast as a **DWORD**.

</dd> <dt>

*ppValidatedPrintTicket* \[out\]
</dt> <dd>

The address of the buffer that contains the merged and validated print ticket. This function calls [**CoTaskMemAlloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemalloc) to allocate this buffer. When the buffer is no longer needed, the caller must free it by calling [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree).

</dd> <dt>

*pValidatedPrintTicketLength* \[out\]
</dt> <dd>

The size, in bytes, of the buffer referenced by *ppValidatedPrintTicket*.

</dd> <dt>

*pbstrErrorMessage* \[out, optional\]
</dt> <dd>

A pointer to a string that specifies what, if anything, is invalid about the print ticket in *pBasePrintTicket* or *pDeltaPrintTicket*. If they are both valid, this value is **NULL**. If *pbstrErrorMessage* is not **NULL** when the function returns, the caller must free the string with [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring).

</dd> </dl>

## Return value

If the method succeeds, it returns **S\_OK**; otherwise, it returns an **HRESULT** error code. For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Prntvpt.dll</dt> </dl> |



## See also

<dl> <dt>

[Print Schema](./printschema.md)
</dt> <dt>

[**PTMergeAndValidatePrintTicket**](/windows/desktop/api/prntvpt/nf-prntvpt-ptmergeandvalidateprintticket)
</dt> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

