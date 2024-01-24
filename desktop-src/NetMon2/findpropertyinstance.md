---
description: The FindPropertyInstance function finds the first instance of the property specified by the hProperty parameter.
ms.assetid: e994503d-2f32-4fa2-bba9-ff66c9d558dc
title: FindPropertyInstance function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FindPropertyInstance
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# FindPropertyInstance function

The **FindPropertyInstance** function finds the first instance of the property specified by the *hProperty* parameter.

## Syntax


```C++
LPPROPERTYINST WINAPI FindPropertyInstance(
  _In_ HFRAME    hFrame,
  _In_ HPROPERTY hProperty
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame. The frame handle can be retrieved by a call to the [GetFrame](getframe.md) function.

</dd> <dt>

*hProperty* \[in\]
</dt> <dd>

Handle to the property you want to find. The property handle can be retrieved by a call to the [GetProperty](getproperty.md) function.

</dd> </dl>

## Return value

If the function is successful (that is, if the property is found), the return value is a pointer to the first instance of the property.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

To retrieve the next instance of the property, call [FindPropertyInstanceRestart](findpropertyinstancerestart.md).

[*Experts*](e.md) and [*parsers*](p.md)can call the **FindPropertyInstance** function.

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

[FindPropertyInstanceRestart](findpropertyinstancerestart.md)
</dt> </dl>

 

 




