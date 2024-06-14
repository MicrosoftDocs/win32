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

By default, the **RPC_WSTR** type is a pointer to a null-terminated UTF-16 Unicode string represented
as a sequence of unsigned short values,
and the **RPC_CWSTR** type is a pointer to a non-modifiable string in the same format.

When compiling for C++ where [`wchar_t`](/cpp/cpp/fundamental-types-cpp#character-types)
is a native type
(by using the [/Zc:wchar_t](/cpp/build/reference/zc-wchar-t-wchar-t-is-native-type)
compiler option),
you can define the preprocessor macro **RPC_USE_NATIVE_WCHAR**
to change the definitions of **RPC_WSTR** and **RPC_CWSTR** to use the native `wchar_t` type
instead of [`unsigned short`](/cpp/cpp/fundamental-types-cpp##sizes-of-built-in-types).

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

 

 





