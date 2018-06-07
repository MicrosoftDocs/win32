---
Description: Verifies a single catalog file using standard operating system code signing policy, such as driver signing.
ms.assetid: 1e2a18a5-506e-46a8-9309-666bec92182d
title: pSetupVerifyCatalogFile function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# pSetupVerifyCatalogFile function

\[This function is no longer supported by Microsoft. For an INF file (device install), developers should use **SetupVerifyInfFile**. To validate a non-INF based catalog, use **WinVerifyTrust**.\]

Verifies a single catalog file using standard operating system code signing policy, such as driver signing.

## Syntax


```C++
DWORD pSetupVerifyCatalogFile(
  _In_ LPCTSTR CatalogFullPath
);
```



## Parameters

<dl> <dt>

*CatalogFullPath* \[in\]
</dt> <dd>

The fully qualified path of the catalog file to be verified.

</dd> </dl>

## Return value

If the function succeeds, it returns **ERROR\_SUCCESS**; otherwise, it returns the error from [**WinVerifyTrust**](https://msdn.microsoft.com/b7efac6a-ac9f-477a-aada-63fe32208e6f).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SetupVerifyInfFile**](https://msdn.microsoft.com/3e64783f-6ded-498a-a994-ccd3ba217e91)
</dt> <dt>

[**WinVerifyTrust**](https://msdn.microsoft.com/b7efac6a-ac9f-477a-aada-63fe32208e6f)
</dt> </dl>

 

 




