---
description: Sends a message to the specified control in a dialog box.
ms.assetid: 7c91e432-662c-4dd0-980c-892ce1092077
title: '_SendDlgItemMessage function'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _SendDlgItemMessage
api_type: 
- DllExport
api_location: 
- Sqlunirl.dll
---

# \_SendDlgItemMessage function

\[This function is a wrapper over the **SendDlgItemMessage** function. This function may be altered or unavailable in the future. Applications should call **SendDlgItemMessage** directly.\]

Sends a message to the specified control in a dialog box. See [**SendDlgItemMessage**](/windows/win32/api/winuser/nf-winuser-senddlgitemmessagea).

## Syntax


```C++
LRESULT _SendDlgItemMessage(
    ...
);
```



## Parameters

<dl> <dt>

*...* 
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Sqlunirl.dll</dt> </dl> |



## See also

<dl> <dt>

[**SendDlgItemMessage**](/windows/win32/api/winuser/nf-winuser-senddlgitemmessagea)
</dt> </dl>

 

 
