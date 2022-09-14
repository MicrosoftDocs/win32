---
description: Retrieves the printers capabilities formatted in compliance with the XML Print Schema.
ms.assetid: 15219c19-b64c-4c51-9357-15a797557693
title: GetPrintCapabilitiesThunk2 function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetPrintCapabilitiesThunk2
api_type: 
- DllExport
api_location: 
- prntvpt.dll
---

# GetPrintCapabilitiesThunk2 function

\[This function is not supported and might be disabled or deleted in future versions of Windows. [**PTGetPrintCapabilities**](/windows/desktop/api/prntvpt/nf-prntvpt-ptgetprintcapabilities) provides equivalent functionality and should be used instead.\]

Retrieves the printer's capabilities formatted in compliance with the XML [Print Schema](./printschema.md).

## Syntax


```C++
HRESULT GetPrintCapabilitiesThunk2(
  _In_      HPTPROVIDER hProvider,
  _In_      BYTE        *pPrintTicket,
  _In_      INT         cbPrintTicket,
  _Out_     BYTE        **ppbPrintCapabilities,
  _Out_     INT         *pcbPrintCapabilitiesLength,
  _Out_opt_ BSTR        *pbstrErrorMessage
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

The buffer that contains the print ticket data, expressed in XML as described in the [Print Schema](./printschema.md).

</dd> <dt>

*cbPrintTicket* \[in\]
</dt> <dd>

The size, in bytes, of the buffer referenced by *pPrintTicket*.

</dd> <dt>

*ppbPrintCapabilities* \[out\]
</dt> <dd>

The address of the buffer that is allocated by this function and contains the valid print capabilities information, encoded as XML. This function calls [**CoTaskMemAlloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemalloc) to allocate this buffer. When the buffer is no longer needed, the caller must free it by calling [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree).

</dd> <dt>

*pcbPrintCapabilitiesLength* \[out\]
</dt> <dd>

The size, in bytes, of the buffer referenced by *ppbPrintCapabilities*.

</dd> <dt>

*pbstrErrorMessage* \[out, optional\]
</dt> <dd>

A pointer to a string that specifies what, if anything, is invalid about *pPrintTicket*. If it is valid, this value is **NULL**. If *pbstrErrorMessage* is not **NULL** when the function returns, the caller must free the string with [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring).

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

[**PTGetPrintCapabilities**](/windows/desktop/api/prntvpt/nf-prntvpt-ptgetprintcapabilities)
</dt> <dt>

[Print Schema](./printschema.md)
</dt> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

