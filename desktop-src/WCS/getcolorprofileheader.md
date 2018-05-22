---
title: GetColorProfileHeader function
description: The GetColorProfileHeader function retrieves or derives ICC header structure from either ICC color profile or WCS XML profile.
ms.assetid: '7006cae0-0166-4fd9-8bf9-f0f0ed249956'
keywords: ["GetColorProfileHeader function Windows Color System"]
topic_type:
- apiref
api_name:
- GetColorProfileHeader
api_location:
- mscms.dll
api_type:
- DllExport
---

# GetColorProfileHeader function

The **GetColorProfileHeader** function retrieves or derives ICC header structure from either ICC color profile or WCS XML profile. Drivers and applications should assume returning **TRUE** only indicates that a properly structured header is returned. Each tag will still need to be validated independently using either legacy ICM2 APIs or XML schema APIs.

## Syntax


```C++
BOOL WINAPI GetColorProfileHeader(
   HPROFILE       hProfile,
   PPROFILEHEADER pHeader
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the color profile in question.

</dd> <dt>

*pHeader* 
</dt> <dd>

Points to a variable in which the ICC header structure is to be placed.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. This function will fail is an invalid ICC or WCS XML profile is referenced in the hProfile parameter. For extended error information, call **GetLastError**.

## Remarks

To determine whether the header is derived from an ICC or DMP profile handle, check the header signature (header bytes 36-39). If the signature is "acsp" (big endian) then an ICC profile was used. If the signature is "cdmp" (big-endian) then a DMP was used.

The distinguishing features that identify a header as having been "synthesized" for a WCS DMP are:

pIcmProfileHeader-&gt;phSignature = 'pmdc' (little endian = big endian 'cdmp')

pIcmProfileHeader-&gt;phCMMType = '1scw' (little endian = big endian 'wcs1').

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**PROFILEHEADER**](profileheader.md)
</dt> </dl>

 

 





