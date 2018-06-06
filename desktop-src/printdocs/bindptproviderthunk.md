---
Description: Opens an instance of a print ticket provider.
ms.assetid: 815cc360-8dcd-4c58-a64d-5d77436a8623
title: BindPTProviderThunk function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BindPTProviderThunk function

\[This function is not supported and might be disabled or deleted in future versions of Windows. [**PTOpenProviderEx**](/windows/desktop/api/prntvpt/nf-prntvpt-ptopenproviderex) provides equivalent functionality and should be used instead.\]

Opens an instance of a print ticket provider.

## Syntax


```C++
HRESULT BindPTProviderThunk(
  _In_  LPTSTR      pszPrinterName,
  _In_  INT         maxVersion,
  _In_  INT         prefVersion,
  _Out_ HPTPROVIDER *phProvider,
  _Out_ INT         *usedVersion
);
```



## Parameters

<dl> <dt>

*pszPrinterName* \[in\]
</dt> <dd>

The full name of a print queue.

</dd> <dt>

*maxVersion* \[in\]
</dt> <dd>

The latest version of the [Print Schema](https://www.bing.com/search?q=Print+Schema) that the caller supports.

</dd> <dt>

*prefVersion* \[in\]
</dt> <dd>

The version of the [Print Schema](https://www.bing.com/search?q=Print+Schema) requested by the caller.

</dd> <dt>

*phProvider* \[out\]
</dt> <dd>

A pointer to a handle to the print ticket provider.

</dd> <dt>

*usedVersion* \[out\]
</dt> <dd>

The version of the [Print Schema](https://www.bing.com/search?q=Print+Schema) that the print ticket provider will use.

</dd> </dl>

## Return value

If the method succeeds, it returns **S\_OK**; otherwise, it returns an **HRESULT** error code. For more information about COM error codes, see [Error Handling](https://www.bing.com/search?q=Error+Handling).

## Remarks

Before calling this function, the calling thread must initialize COM by calling [**CoInitializeEx**](https://msdn.microsoft.com/library/windows/desktop/ms695279).

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

[**PTOpenProviderEx**](/windows/desktop/api/prntvpt/nf-prntvpt-ptopenproviderex)
</dt> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

 




