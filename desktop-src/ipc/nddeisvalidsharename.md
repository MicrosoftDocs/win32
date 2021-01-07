---
description: Determines whether a share name uses the proper syntax.
ms.assetid: 4ffcff5d-0db5-4761-a31a-acefd2b8d9e2
title: NDdeIsValidShareName function (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDdeIsValidShareName
- NDdeIsValidShareNameA
- NDdeIsValidShareNameW
api_type: 
- DllExport
api_location: 
- Nddeapi.dll
---

# NDdeIsValidShareName function

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Determines whether a share name uses the proper syntax.

## Syntax


```C++
BOOL NDdeIsValidShareName(
  _In_ LPTSTR shareName
);
```



## Parameters

<dl> <dt>

*shareName* \[in\]
</dt> <dd>

The share name to be validated. This parameter cannot be **NULL**.

</dd> </dl>

## Return value

If the share name has valid syntax, the return value is nonzero.

If the share name does not have valid syntax, the return value is zero.

## Remarks

This function is also called by [**NDdeShareAdd**](nddeshareadd.md) when it creates the DDE share.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Nddeapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nddeapi.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **NDdeIsValidShareNameW** (Unicode) and **NDdeIsValidShareNameA** (ANSI)<br/>    |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Functions](network-dde-functions.md)
</dt> <dt>

[**NDdeShareAdd**](nddeshareadd.md)
</dt> </dl>

 

 




