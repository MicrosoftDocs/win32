---
Description: Disables features.
ms.assetid: 2ea2dcfb-84e6-4f83-9afd-c3050b53f37c
title: pSetupSetGlobalFlags function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# pSetupSetGlobalFlags function

\[This function is not available in Windows Vista or Windows Server 2008.\]

Disables features.

## Syntax


```C++
VOID pSetupSetGlobalFlags(
  _In_ DWORD Value
);
```



## Parameters

<dl> <dt>

*Value* \[in\]
</dt> <dd>

The flags used to disable user interface or automatic backup.



| Value                                                                                                                                                                                                                                         | Meaning                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <span id="PSPGF_NONINTERACTIVE"></span><span id="pspgf_noninteractive"></span><dl> <dt>**PSPGF\_NONINTERACTIVE**</dt> <dt>0x004</dt> </dl> | Set to disable user interface.<br/>   |
| <span id="PSPGF_NO_BACKUP"></span><span id="pspgf_no_backup"></span><dl> <dt>**PSPGF\_NO\_BACKUP**</dt> <dt>0x002</dt> </dl>               | Set to disable automatic backup.<br/> |



 

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Setupapi.dll</dt> </dl> |



 

 




