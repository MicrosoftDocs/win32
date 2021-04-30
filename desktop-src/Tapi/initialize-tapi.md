---
description: The following code example demonstrates creation of the TAPI object.
ms.assetid: f8566e53-51c9-4424-a8bb-369455f35706
title: Initialize TAPI
ms.topic: article
ms.date: 05/31/2018
---

# Initialize TAPI

The following code example demonstrates creation of the TAPI object.

```cpp
const auto result = ITTAPI::Initialize();

if (result != S_OK) {
    switch (result) {
        case S_FALSE: {
            std::cerr << "TAPI has already been initialized.\n";
        } break;

        [[fallthrough]]
        case E_OUTOFMEMORY: {
            std::cerr << "Insufficient memory exists to perform the operation.\n";
        }

        default: {
            // TODO: Handle unrecoverable error here
        }
    }
}
```

## See Also

- [ITTAPI::Initialize](/windows/win32/api/tapi3if/nf-tapi3if-ittapi-initialize)
- [Common HRESULT Values](../seccrypto/common-hresult-values.md)
