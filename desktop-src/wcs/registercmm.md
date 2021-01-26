---
title: RegisterCMM function
description: RegisterCMM associates a specified identification value with the specified color management module dynamic link library (CMM DLL). When this ID appears in a color profile, Windows can then locate the corresponding CMM so as to create a transform.
ms.assetid: e26a98be-2165-437d-a197-08e07952d043
keywords:
- RegisterCMM function Windows Color System
topic_type:
- apiref
api_name:
- RegisterCMM
- RegisterCMMA
- RegisterCMMW
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# RegisterCMM function

**RegisterCMM** associates a specified identification value with the specified color management module dynamic link library (CMM DLL). When this ID appears in a color profile, Windows can then locate the corresponding CMM so as to create a transform.

## Syntax


```C++
BOOL WINAPI RegisterCMM(
   PCTSTR pMachineName,
   DWORD  cmmID,
   PCTSTR pCMMdll
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved; must currently be set to **NULL**, until non-local registration is supported. This parameter is intended to point to the name of the machine on which a CMM DLL should be registered. A **NULL** pointer indicates the local machine.

</dd> <dt>

*cmmID* 
</dt> <dd>

Specifies the ID signature of the CMM registered with the International Color Consortium (ICC).

</dd> <dt>

*pCMMdll* 
</dt> <dd>

Pointer to the fully qualified path name of the CMM DLL.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **RegisterCMMW** (Unicode) and **RegisterCMMA** (ANSI)<br/>                    |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





