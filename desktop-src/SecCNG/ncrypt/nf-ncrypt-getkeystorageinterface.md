---
title: GetKeyStorageInterface function
description: Retrieves the key storage interface for the specified provider.
ms.topic: reference
ms.date: 08/10/2022
req.lib: Ncrypt.lib
req.dll: Ncrypt.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- Ncrypt.dll
api_name:
- GetKeyStorageInterface
targetos: Windows
---

# GetKeyStorageInterface function

Retrieves the key storage interface for the specified provider.

## Syntax

```cpp
HRESULT WINAPI GetKeyStorageInterface(
  _In_ LPCWSTR pszProviderName,
  _Out_ NCRYPT_KEY_STORAGE_FUNCTION_TABLE** ppFunctionTable,
  _In_ DWORD dwFlags
);
```

## Parameters

`pszProviderName`

The provider name.

`ppFunctionTable`

Used to retrieve the key storage interface.

`dwFlags`

Flags.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Remarks

**GetKeyStorageInterface** isn't associated with a header file. You can call it by first using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw) function (to load `Ncrypt.dll`), and then by calling the [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) function to retrieve the address of **GetKeyStorageInterface**.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
| **Library** | Ncrypt.lib |
| **DLL** | Ncrypt.dll |
