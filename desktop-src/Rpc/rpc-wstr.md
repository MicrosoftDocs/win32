---
title: RPC_WSTR (Rpcdce.h)
description: The data type RPC\_WSTR represents a platform-specific wide character string.
keywords:
- RPC_WSTR
- RPC_WSTR
ms.topic: reference
ms.date: 06/10/2023
---

# RPC\_WSTR

The data type RPC\_WSTR represents a platform-specific wide character string.


```C++
#if defined(RPC_USE_NATIVE_WCHAR) && defined(_NATIVE_WCHAR_T_DEFINED)
typedef _Null_terminated_ wchar_t __RPC_FAR * RPC_WSTR;
typedef _Null_terminated_ const wchar_t * RPC_CWSTR;
#else
typedef _Null_terminated_ unsigned short __RPC_FAR * RPC_WSTR;
typedef _Null_terminated_ const unsigned short * RPC_CWSTR;
#endif

```



## Remarks

If the preprocessor macros **RPC_USE_NATIVE_WCHAR** and **_NATIVE_WCHAR_T_DEFINED** are defined, **RPC_WSTR** and **RPC_CWSTR** are defined to use [wchar_t](/windows/win32/midl/wchar-t) as the underlying type. Otherwise, the underlying type used is unsigned short.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Rpcdce.h (include Rpc.h)</dt> </dl> |



## See also

<dl> <dt>

[**RPC\_OBJECT\_INQ\_FN**](/windows/desktop/api/Rpcdce/nc-rpcdce-rpc_object_inq_fn)
</dt> </dl>

 

 





