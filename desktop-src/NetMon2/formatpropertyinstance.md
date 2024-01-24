---
description: Formats the property instance data using the generic formatter that Network Monitor provides.
ms.assetid: 36206601-7519-45c8-a14e-707b318c539d
title: FormatPropertyInstance function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FormatPropertyInstance
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# FormatPropertyInstance function

The **FormatPropertyInstance** function formats the property instance data using the generic formatter that Network Monitor provides.

## Syntax


```C++
DWORD WINAPIV FormatPropertyInstance(
  _Inout_ LPPROPERTYINST lpPropertyInst
);
```



## Parameters

<dl> <dt>

*lpPropertyInst* \[in, out\]
</dt> <dd>

A pointer to a [PROPERTYINST](propertyinst.md) structure that contains the instance data.

On input, the generic formatter takes the instance data from one of the **PROPERTYINST** union members and converts that data to a predefined formatted string.

On output, the generic formatter sets the **szPropertyText** member of the **PROPERTYINST** structure to a pointer to the formatted string.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is an error code from NMerr.h.

## Remarks

The parser DLL indirectly calls the **FormatPropertyInstance** function when the generic formatter is required to format data for display in the details pane of the Network Monitor UI. To call **FormatPropertyInstance** specify it in the **InstanceData** member of the [PROPERTYINFO](propertyinfo.md) structure when you define the property.

> [!Note]  
> The parser does not recognize which function is called when it must format an instance of a property. The function can be **FormatPropertyInstance** or a custom format function defined by the parser. The parser calls whatever format function is specified by the **InstanceData** member of the **PROPERTYINFO** structure for the property.

 

For more information and an example of how to implement [formatproperties](formatproperties.md), see [Implementing FormatProperties](implementing-formatproperties.md). For more information about how the generic formatter formats different types of data, see [Generic Formatter Output](generic-formatter-output.md).

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

[PROPERTYINFO](propertyinfo.md)
</dt> <dt>

[PROPERTYINST](propertyinst.md)
</dt> </dl>

 

 




