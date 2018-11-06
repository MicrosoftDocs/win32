---
title: Targeting Stubs for Specific 32-bit or 64-bit Platforms
description: Some of the features of Microsoft RPC and the MIDL 3.0 and later compilers are platform-specific.
ms.assetid: bb1bee56-7f39-406c-bdbf-b73bda568247
keywords:
- 32-bit platforms MIDL
- 64-bit platforms MIDL
- stubs MIDL
ms.topic: article
ms.date: 05/31/2018
---

# Targeting Stubs for Specific 32-bit or 64-bit Platforms

Some of the features of Microsoft RPC and the MIDL 3.0 and later compilers are platform-specific.

As a precaution, the MIDL 3.0 and later compilers generate guards that facilitate compatibility checking during the C-compilation phase. MIDL generates two types of guards: a platform-dependent guard (32-bit versus 64-bit) and a release-dependent guard (feature set dependency). For example, MIDL generates the following guard to prevent C-compiling of a 32-bit stub for other platforms:

``` syntax
#if !defined(__RPC_WIN32__)
#error  Invalid build platform for this stub.
#endif
```

The release-dependent guard is triggered by a set of features found in the processed IDL file(s) and by the [**/target**](-target.md) switch. For example, if the interface uses features supported only on WindowsÂ 2000 or later, MIDL generates a guard with the TARGET\_IS\_NT50\_OR\_LATER macro.

The guard macros, defined in Rpcndr.h, depend on the setting of WINVER and \_WIN32\_WINNT and are evaluated by the C/C++ compiler.

If, at C-compile time, you get an error message indicating that you need a specific platform to run a stub, first check to make sure you have not used a feature that is not available on this platform. The features triggering a particular guard are listed in the body of the guard. In the previous example, the -Oicf compiler switch triggered the guard. Notable features of this kind include the [**/robust**](-robust.md) switch and the \[[**async**](async.md)\] attribute available on WindowsÂ 2000 and later, the [**pipe**](pipe.md) type constructor, the /Oif compiler option, and the \[[**user\_marshal**](user-marshal.md)\] and \[[**wire\_marshal**](wire-marshal.md)\] attributes. Stubs using these features will not run on earlier systems.

If you know that your target platform is correct for the features you are using and still receive an error, you may need to set the environment variables appropriately.

**To build for WindowsÂ 2000 or later releases**

-   Add this line to your makefile:

    ``` syntax
    CFLAGS = $(CFLAGS) -D_WIN32_WINNT=0x500
    ```

## Related topics

<dl> <dt>

[**/target**](-target.md)
</dt> <dt>

[**/robust**](-robust.md)
</dt> <dt>

[**async**](async.md)
</dt> <dt>

[**async\_uuid**](async-uuid.md)
</dt> <dt>

[**/Oi**](-oi.md)
</dt> <dt>

[**pipe**](pipe.md)
</dt> <dt>

[**wire\_marshal**](wire-marshal.md)
</dt> <dt>

[**user\_marshal**](user-marshal.md)
</dt> <dt>

[Marshaling OLE Data Types](marshaling-ole-data-types.md)
</dt> </dl>

 

 




