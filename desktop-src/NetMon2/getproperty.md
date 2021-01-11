---
description: The GetProperty function returns a handle to a given property.
ms.assetid: e77ca20a-55df-4d31-aa6d-2c00695f1d6e
title: GetProperty function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetProperty
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetProperty function

The **GetProperty** function returns a handle to a given property.

## Syntax


```C++
HPROPERTY WINAPI GetProperty(
  _In_ HPROTOCOL hProtocol,
  _In_ LPSTR     PropertyName
);
```



## Parameters

<dl> <dt>

*hProtocol* \[in\]
</dt> <dd>

Handle to the protocol.

</dd> <dt>

*PropertyName* \[in\]
</dt> <dd>

Name of the property (for example, **Checksum**).

</dd> </dl>

## Return value

If the function is successful, the return value is the handle to the property.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

The **GetProperty** function can be used to obtain the property handle needed to locate instances of the property. The functions used to locate property instances are [FindPropertyInstance](findpropertyinstance.md) (which locates the first instance) and [FindPropertyInstanceRestart](findpropertyinstancerestart.md) (which locates the next instance).

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetProperty** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[FindPropertyInstance](findpropertyinstance.md)
</dt> <dt>

[FindPropertyInstanceRestart](findpropertyinstancerestart.md)
</dt> </dl>

 

 




