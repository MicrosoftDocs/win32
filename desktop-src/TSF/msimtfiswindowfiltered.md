---
title: MsimtfIsWindowFiltered function
description: The MsimtfIsWindowFiltered function tests if the given window is filtered by AIMM (Active Input Method Manager).
ms.assetid: 1f5e98f1-3626-4aa5-b2da-b6bc48d02184
keywords:
- MsimtfIsWindowFiltered function Text Services Framework
topic_type:
- apiref
api_name:
- MsimtfIsWindowFiltered
api_location:
- msimtf.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MsimtfIsWindowFiltered function

The **MsimtfIsWindowFiltered** function tests if the given window is filtered by AIMM (Active Input Method Manager).

## Syntax


```C++
BOOL CALLBACK MsimtfIsWindowFiltered(
  _In_ HWND hwnd
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

A window handle to be tested.

</dd> </dl>

## Return value



| Return code                                                                          | Description                                                               |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | If this window is filtered by Active Input Method Manager.<br/>     |
| <dl> <dt>**FALSE**</dt> </dl> | If this window is not filtered by Active Input Method Manager.<br/> |



 

## Remarks

A window can be filtered by IActiveIMMApp::FilterClientWindows.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Msimtf.dll</dt> </dl> |



 

 





