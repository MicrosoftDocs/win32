---
description: The FilterAddObject function adds a single object to a display filter.
ms.assetid: 796216f4-a407-4a8c-98b3-8c3761d91913
title: FilterAddObject function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FilterAddObject
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# FilterAddObject function

The **FilterAddObject** function adds a single object to a [*display filter*](d.md).

## Syntax


```C++
DWORD WINAPI FilterAddObject(
  _In_  HFILTER        hFilter,
  _Out_ LPFILTEROBJECT lpFilterObject
);
```



## Parameters

<dl> <dt>

*hFilter* \[in\]
</dt> <dd>

Handle to the display filter.

</dd> <dt>

*lpFilterObject* \[out\]
</dt> <dd>

Pointer to a [FILTEROBJECT](filterobject.md) structure that defines the object to be added to the filter. Each object can be an operator, value, or property.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is an error code.



| Return code                                                                                              | Description                                                                  |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_INVALID\_PARAMETER**</dt> </dl> | The *hFilter* parameter has an invalid value.<br/>                     |
| <dl> <dt>**NMERR\_OUT\_OF\_MEMORY**</dt> </dl>    | Network Monitor does not have enough memory to create the object.<br/> |



 

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **FilterAddObject** function.

The **FilterAddObject** function is called each time a filter object is added to the display filter. The display filter is a postfix stack of objects that can be an operator, value, or property.

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

[FILTEROBJECT](filterobject.md)
</dt> </dl>

 

 




