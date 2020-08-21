---
title: Loading and Registering a Type Library
description: The Automation dynamic link library, Oleaut32.dll, provides several functions that you can call to load and register a type library. Calling LoadTypeLibEx, as shown in the following example, both loads the library and creates the registry entries.
ms.assetid: b7404919-fa0a-4de8-8c85-41b7bc7c5a52
ms.topic: article
ms.date: 05/31/2018
---

# Loading and Registering a Type Library

The Automation dynamic link library, Oleaut32.dll, provides several functions that you can call to load and register a type library. Calling [LoadTypeLibEx](/windows/win32/api/oleauto/nf-oleauto-loadtypelibex), as shown in the following example, both loads the library and creates the registry entries.

## Example

``` syntax
ITypeLib *pTypeLib;
HRESULT hr;
hr = LoadTypeLibEx("example.tlb", REGKIND_REGISTER, &pTypeLib);
if(SUCCEEDED(hr))
{
    pTypeLib->Release();
} else {
    exit(0); // Handle errors here.
}
```

 

 