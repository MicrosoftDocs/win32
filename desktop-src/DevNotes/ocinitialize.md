---
description: Initializes the optional component manager.
ms.assetid: 9a7ddca6-a6c8-4d96-81bb-66158b83ab68
title: OcInitialize function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OcInitialize
api_type: 
- DllExport
api_location: 
- OcManage.dll
---

# OcInitialize function

Initializes the optional component manager.

## Syntax


```C++
PVOID OcInitialize(
  _In_  POCM_CLIENT_CALLBACKS Callbacks,
  _In_  LPCTSTR               MasterOcInfName,
  _In_  UINT                  Flags,
  _Out_ PBOOL                 ShowError,
  _In_  PVOID                 Log
);
```



## Parameters

<dl> <dt>

*Callbacks* \[in\]
</dt> <dd>

A pointer to an [**OCM\_CLIENT\_CALLBACKS**](ocm-client-callbacks.md) structure that specifies the callback functions to be used by the OC manager to perform various tasks.

</dd> <dt>

*MasterOcInfName* \[in\]
</dt> <dd>

The path of the master OC .inf file.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter can be one or more of the following values.

<dl> <dt>

<span id="OCINIT_FORCENEWINF"></span><span id="ocinit_forcenewinf"></span>**OCINIT\_FORCENEWINF** (0x00000001)
</dt> <dt>

<span id="OCINIT_KILLSUBCOMPS"></span><span id="ocinit_killsubcomps"></span>**OCINIT\_KILLSUBCOMPS** (0x00000002)
</dt> <dt>

<span id="OCINIT_RUNQUIET"></span><span id="ocinit_runquiet"></span>**OCINIT\_RUNQUIET** (0x00000004)
</dt> <dt>

<span id="OCINIT_LANGUAGEAWARE"></span><span id="ocinit_languageaware"></span>**OCINIT\_LANGUAGEAWARE** (0x00000008)
</dt> </dl> </dd> <dt>

*ShowError* \[out\]
</dt> <dd>

If the function fails, this parameter indicates whether to display an error message.

</dd> <dt>

*Log* \[in\]
</dt> <dd>

A handle to the log.

</dd> </dl>

## Return value

The function returns the OC manager context value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>OcManage.dll</dt> </dl> |



## See also

<dl> <dt>

[**OCM\_CLIENT\_CALLBACKS**](ocm-client-callbacks.md)
</dt> <dt>

[**OcTerminate**](octerminate.md)
</dt> </dl>

 

 
