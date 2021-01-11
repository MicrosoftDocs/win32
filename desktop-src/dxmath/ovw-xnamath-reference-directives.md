---
description: Compiler directives tune the functionality that the DirectXMath library uses.
ms.assetid: c1746b7b-7e7e-2453-77eb-17f859a38fe2
title: DirectXMath Library compiler directives
ms.topic: reference
ms.date: 05/31/2018
---

# DirectXMath Library compiler directives

Compiler directives tune the functionality that the DirectXMath library uses.



| Directive                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \_XM\_NO\_INTRINSICS\_        | When \_XM\_NO\_INTRINSICS\_ is defined, DirectXMath operations are implemented without using any platform-specific intrinsics. Instead, DirectXMath uses only standard floating point operations.<br/> By default, \_XM\_NO\_INTRINSICS\_ is not defined.<br/> This directive overrides all other directives. Therefore, we recommend that you check for \_XM\_NO\_INTRINSICS\_ before you determine the status of \_XM\_ARM\_NEON\_INTRINSICS\_ or \_XM\_SSE\_INTRINSICS\_.<br/>                                                                              |
| \_XM\_SSE\_INTRINSICS\_       | When \_XM\_SSE\_INTRINSICS\_ is defined, code is compiled to use supporting SSE and SSE2 on platforms that support these instruction sets.<br/> The Windows versions providing SSE intrinsics support both SSE and SSE2.<br/> \_XM\_SSE\_INTRINSICS\_ has no effect on systems that do not support SSE and SSE2.<br/> By default, \_XM\_SSE\_INTRINSICS\_ is defined when users compile for a Windows platform.<br/> DirectXMath uses the standard compiler defines (\_M\_IX86 / \_M\_AMD64) to determine Windows x86 or Windows x64 targets.<br/> |
| \_XM\_ARM\_NEON\_INTRINSICS\_ | This indicates the DirectXMath implementation uses of the ARM-NEON intrinsics. By default, \_XM\_ARM\_NEON\_INTRINSICS\_ is defined when users compile for a Windows RT platform. DirectXMath uses the standard compiler define (\_M\_ARM, \_M\_ARM64) to determine this binary target.<br/> ARM-NEON intrinsics support is new to DirectXMath and is not supported by XNAMath 2.x.<br/>                                                                                                                                                                             |
| \_XM\_SSE3\_INTRINSICS\_      | New for Windows 10 Creators Update SDK. <br/> When you specify this compiler directive, DirectXMath functions are implemented to make use of SSE3 intrinsics where applicable; otherwise it uses SSE/SSE2.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| \_XM\_SSE4\_INTRINSICS\_      | New for Windows 10 Anniversary SDK.<br/> When you specify this compiler directive, DirectXMath functions are implemented to make use of SSE3 and SSE4.1 intrinsics where applicable; otherwise it uses SSE/SSE2. When you specify this compiler directive, it also implies \_XM\_SSE3\_INTRINSICS\_ and \_XM\_SSE\_INTRINSICS\_.<br/>                                                                                                                                                                                                                                |
| \_XM\_AVX\_INTRINSICS\_       | New for Windows 10 Anniversary SDK.<br/> Use of /arch:AVX will enable this directive. <br/> When you specify this compiler directive, DirectXMath functions are implemented to make use of SSE3, SSE4.1, and AVX 128-bit intrinsics where applicable; otherwise DirectXMath uses SSE/SSE2. When you specify this compiler directive, it also implies \_XM\_SSE3\_INTRINSICS, \_XM\_SSE4\_INTRINSICS\_, and \_XM\_SSE\_INTRINSICS\_, and includes a small subset of SSE3 instructions. <br/>                                                                    |
| XM\_AVX2\_INTRINSICS\_        | New for Windows 10 Fall Creators Update SDK<br/> Use of /arch:AVX2 enables this directive. When you specify this compiler directive, DirectXMath functions make use of AVX2, F16C/CVT16, FMA3, AVX 128-bit, SSE4.1, and SSE3 intrinsics where applicable. When you use \_XM\_AVX2\_INTRINSICS\_, it implies \_XM\_F16C\_INTRINSICS\_, \_XM\_FMA3\_INTRINSICS\_, \_XM\_AVX\_INTRINSICS\_, \_XM\_SSE\_INTRINSICS\_, \_XM\_SSE3\_INTRINSICS\_, and \_XM\_SSE4\_INTRINSICS\_.<br/>                                                                                       |
| \_XM\_F16C\_INTRINSICS\_      | New for Windows 10 Anniversary SDK.<br/> When you specify this compiler directive, DirectXMath functions are implemented to make use of SSE3, SSE4.1, AVX 128-bit, and F16C/CVT16 intrinsics where applicable; otherwise DirectXMath uses SSE/SSE2. When you use \_XM\_F16C\_INTRINSICS\_, it implies \_XM\_AVX\_INTRINSICS\_, \_XM\_SSE\_INTRINSICS\_, \_XM\_SSE3\_INTRINSICS\_, and \_XM\_SSE4\_INTRINSICS\_.<br/>                                                                                                                                                 |
| \_XM\_FMA3\_INTRINSICS\_      | New for Windows 10 Fall Creators Update SDK<br/> When you specify this compiler directive, DirectXMath functions will make use of SSE3, SSE4.1, AVX 128-bit, and FMA3 intrinsics where applicable; otherwise DirectXMath uses SSE/SSE2. When you use \_XM\_FMA3\_INTRINSICS\_, it implies \_XM\_AVX\_INTRINSICS\_, \_XM\_SSE\_INTRINSICS\_, \_XM\_SSE3\_INTRINSICS\_, and \_XM\_SSE4\_INTRINSICS\_. <br/>                                                                                                                                                            |
| \_XM\_VECTORCALL\_            | This enables the use of the new \_\_vectorcall calling convention for Windows x86 or Windows x64 targets. It defaults to \_XM\_VECTORCALL\_=1 when the compiler supports this feature. You can manually set it to \_XM\_VECTORCALL\_=0 to always disable it. <br/> \_\_vectorcall is not supported for the Windows RT platform or Managed C++. <br/>                                                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[DirectXMath Programming Reference](ovw-xnamath-reference.md)
</dt> </dl>

 

 




