---
description: Enclaves are used to create trusted execution environments. These libvcruntime.lib APIs are available to to be statically linked into developers' code in VBS enclaves.
ms.assetid: 659f28af-ed6c-46f6-b8c5-bb5784bc6c6b
title: libvcruntime APIs available in VBS enclaves
titleSuffix: Secure Enclaves
ms.topic: reference
ms.date: 11/20/2024
---

# libvcruntime APIs available in VBS enclaves

[!INCLUDE [enclaves-os-reqs.md](../includes/enclaves-os-reqs.md)]

Enclaves are used to create trusted execution environments. These `libvcruntime.lib` APIs are available to be statically linked into code running in VBS enclaves.

## Functions linked from libvcruntime.lib

[`_get_purecall_handler`](/cpp/c-runtime-library/reference/get-purecall-handler-set-purecall-handler)

[`_get_unexpected`](/cpp/c-runtime-library/reference/get-unexpected)

[`_set_purecall_handler`](/cpp/c-runtime-library/reference/get-purecall-handler-set-purecall-handler)

[`_set_se_translator`](/cpp/c-runtime-library/reference/set-se-translator)

[`longjmp`](/cpp/c-runtime-library/reference/longjmp)

[`memchr`](/cpp/c-runtime-library/reference/memchr-wmemchr)

[`memcmp`](/cpp/c-runtime-library/reference/memcmp-wmemcmp)

[`memcpy`](/cpp/c-runtime-library/reference/memcpy-wmemcpy)

[`memmove`](/cpp/c-runtime-library/reference/memmove-wmemmove)

[`memset`](/cpp/c-runtime-library/reference/memset-wmemset)

[`set_unexpected`](/cpp/c-runtime-library/reference/set-unexpected-crt)

[`strchr`](/cpp/c-runtime-library/reference/strchr-wcschr-mbschr-mbschr-l)

[`strrchr`](/cpp/c-runtime-library/reference/strrchr-wcsrchr-mbsrchr-mbsrchr-l)

[`strstr`](/cpp/c-runtime-library/reference/strstr-wcsstr-mbsstr-mbsstr-l)

[`unexpected`](/cpp/c-runtime-library/reference/unexpected-crt)

[`wcschr`](/cpp/c-runtime-library/reference/strchr-wcschr-mbschr-mbschr-l)

[`wcsrchr`](/cpp/c-runtime-library/reference/strrchr-wcsrchr-mbsrchr-mbsrchr-l)

[`wcsstr`](/cpp/c-runtime-library/reference/strstr-wcsstr-mbsstr-mbsstr-l)

## Internal functions and function macros

These internal [functions and function macros](/cpp/c-runtime-library/internal-crt-globals-and-functions#internal-crt-functions-and-function-macros) that can be linked from `libvcruntime.lib` are used to implement the CRT. They are not intended to be called directly from your code.

- `__AdjustPointer`
- `__BuildCatchObject`
- `__BuildCatchObjectHelper`
- [`__C_specific_handler`](/windows/win32/devnotes/--c-specific-handler2)
- `__C_specific_handler_noexcept`
- `_CreateFrameInfo`
- `__CxxDetectRethrow`
- `__CxxExceptionFilter`
- [`__CxxFrameHandler`](/cpp/c-runtime-library/cxxframehandler)
- `__CxxFrameHandler2`
- [`__CxxFrameHandler3`](../Memory/cxxframehandler3.md)
- `__CxxFrameHandler4`
- `__CxxQueryExceptionSize`
- `__CxxRegisterExceptionObject`
- [`_CxxThrowException`](/cpp/c-runtime-library/reference/cxxthrowexception)
- `__CxxUnregisterExceptionObject`
- `__DestructExceptionObject`
- `_FindAndUnlinkFrame`
- `__FrameUnwindFilter`
- `__GetPlatformExceptionInfo`
- `_IsExceptionObjectToBeDestroyed`
- `_is_exception_typeof`
- `__NLG_Dispatch2`
- `__NLG_Return2`
- `__RTCastToVoid`
- `__RTtypeid`
- `__TypeMatch`
- `__current_exception`
- `__current_exception_context`
- `__intrinsic_setjmp`
- `__intrinsic_setjmpex`
- `_local_unwind`
- `__processing_throw`
- [`_purecall`](/cpp/c-runtime-library/reference/purecall)
- `__report_gsfailure`
- [`__RTDynamicCast`](/cpp/c-runtime-library/rtdynamiccast)
- `_SetWinRTOutOfMemoryExceptionCallback`
- [`__std_exception_copy`](../Memory/stdexceptioncopy.md)
- [`__std_exception_destroy`](../Memory/stdexceptiondestroy.md)
- [`__std_terminate`](../Memory/stdterminate.md)
- `__std_type_info_compare`
- [`__std_type_info_destroy_list`](../Memory/stdtypeinfodestroylist.md)
- `__std_type_info_hash`
- `__std_type_info_name`
- `__telemetry_main_invoke_trigger`
- `__telemetry_main_return_trigger`
- `__unDName`
- `__unDNameEx`
- [`__uncaught_exception`](/cpp/c-runtime-library/reference/uncaught-exception)
- `__uncaught_exceptions`
- `__vcrt_GetModuleFileNameW`
- `__vcrt_GetModuleHandleW`
- `__vcrt_InitializeCriticalSectionEx`
- `__vcrt_LoadLibraryExW`

## See also

- [UCRT APIs Available in VBS Enclaves](enclaves-available-in-ucrt.md)
- [Bcrypt APIs Available in VBS Enclaves](enclaves-available-in-bcrypt.md)
- [Vertdll APIs Available in VBS Enclaves](enclaves-available-in-vertdll.md)
- [Secure Enclaves (Trusted Execution)](enclaves.md)
