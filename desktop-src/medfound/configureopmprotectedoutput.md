---
description: Configures a protected output object.
ms.assetid: d22a378e-2d4e-4ff4-a18e-136932c24d2b
title: ConfigureOPMProtectedOutput function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ConfigureOPMProtectedOutput
api_type: 
- DllExport
api_location: 
- gdi32.dll
---

# ConfigureOPMProtectedOutput function

> [!IMPORTANT]
> This function is used by [Output Protection Manager](output-protection-manager.md) (OPM) to access functionality in the display driver. Applications should not call this function.

 

Configures a protected output object.

## Syntax


```C++
NTSTATUS WINAPI ConfigureOPMProtectedOutput(
  _In_       OPM_PROTECTED_OUTPUT_HANDLE      opoOPMProtectedOutput,
  _In_ const DXGKMDT_OPM_CONFIGURE_PARAMETERS *pParameters,
  _In_       ULONG                            ulAdditionalParametersSize,
  _In_ const BYTE                             *pbAdditionalParameters
);
```



## Parameters

<dl> <dt>

*opoOPMProtectedOutput* \[in\]
</dt> <dd>

A handle to the protected output object. This handle is obtained by calling [**CreateOPMProtectedOutputs**](createopmprotectedoutputs.md).

</dd> <dt>

*pParameters* \[in\]
</dt> <dd>

A pointer to a **DXGKMDT\_OPM\_CONFIGURE\_PARAMETERS** structure that contains the configuration command.

</dd> <dt>

*ulAdditionalParametersSize* \[in\]
</dt> <dd>

The size of the *pbAdditionalParameters* buffer, in bytes.

</dd> <dt>

*pbAdditionalParameters* \[in\]
</dt> <dd>

A pointer to a buffer that contains additional information for the command.

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

Applications should call [**IOPMVideoOutput::Configure**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-configure) instead of calling this function.

This function has no associated import library. To call this function, you must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Gdi32.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Gdi32.dll</dt> </dl> |



## See also

<dl> <dt>

[OPM Functions](opm-functions.md)
</dt> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> </dl>

 

 
