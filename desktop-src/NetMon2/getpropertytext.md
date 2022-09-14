---
description: The GetPropertyText function returns a pointer to the property text.
ms.assetid: 1bcbdbb8-4ec5-4cea-a1c6-4a1f37476f50
title: GetPropertyText function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetPropertyText
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetPropertyText function

The **GetPropertyText** function returns a pointer to the property text.

## Syntax


```C++
LPSTR WINAPI GetPropertyText(
  _In_ HFRAME         hFrame,
  _In_ LPPROPERTYINST lpPI,
  _In_ LPSTR          szBuffer,
  _In_ DWORD          BufferSize
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame.

</dd> <dt>

*lpPI* \[in\]
</dt> <dd>

Pointer to a property instance.

</dd> <dt>

*szBuffer* \[in\]
</dt> <dd>

Pointer to the property text string.

</dd> <dt>

*BufferSize* \[in\]
</dt> <dd>

Size of the text string buffer.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the property text.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetPropertyText** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




