---
title: GetCMMInfo function
description: The GetCMMInfo function retrieves various information about the color management module (CMM) that created the specified color transform.
ms.assetid: 60fe282c-ed52-45c8-ac64-03c2c684679c
keywords:
- GetCMMInfo function Windows Color System
topic_type:
- apiref
api_name:
- GetCMMInfo
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# GetCMMInfo function

The **GetCMMInfo** function retrieves various information about the color management module (CMM) that created the specified color transform.

## Syntax


```C++
DWORD WINAPI GetCMMInfo(
   HTRANSFORM hColorTransform,
   DWORD      dwInfo
);
```



## Parameters

<dl> <dt>

*hColorTransform* 
</dt> <dd>

Identifies the transform for which to find CMM information.

</dd> <dt>

*dwInfo* 
</dt> <dd>

Specifies the information to be retrieved. This parameter can take one of the following constant values.

 



| Value                                                                                                                                                                | Meaning                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <span id="CMM_WIN_VERSION"></span><span id="cmm_win_version"></span><dl> <dt>**CMM\_WIN\_VERSION**</dt> </dl> | Retrieves the version of Windows targeted by the color management module (CMM).<br/>       |
| <span id="CMM_DLL_VERSION"></span><span id="cmm_dll_version"></span><dl> <dt>**CMM\_DLL\_VERSION**</dt> </dl> | Retrieves the version number of the CMM.<br/>                                              |
| <span id="CMM_IDENT"></span><span id="cmm_ident"></span><dl> <dt>**CMM\_IDENT**</dt> </dl>                    | Retrieves the CMM signature registered with the International Color Consortium (ICC).<br/> |



 

</dd> </dl>

## Return value

If this function succeeds, the return value is the information specified in *dwInfo.*

If this function fails, the return value is zero.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





