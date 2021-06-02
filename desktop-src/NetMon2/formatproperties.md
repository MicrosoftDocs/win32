---
description: The FormatProperties export function formats the data that is displayed in the details pane of the Network Monitor UI. If you want to display data in the details pane, you must implement the FormatProperties export function in all parser DLLs.
ms.assetid: 78e0b4b9-f19e-41cb-8504-635f3f9ac1ee
title: FormatProperties callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FormatProperties
api_type: 
- UserDefined
api_location: 
- Netmon.h
---

# FormatProperties callback function

The **FormatProperties** export function formats the data that is displayed in the details pane of the Network Monitor UI. If you want to display data in the details pane, you must implement the **FormatProperties** export function in all parser DLLs.

## Syntax


```C++
DWORD FormatProperties(
  _In_ HFRAME         hFrame,
  _In_ LPBYTE         lpFrame,
  _In_ LPBYTE         lpProtocol,
  _In_ DWORD          nPropertyInsts,
  _In_ LPPROPERTYINST lpPropInst
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame that is being parsed.

</dd> <dt>

*lpFrame* \[in\]
</dt> <dd>

Pointer to the first byte of a frame.

</dd> <dt>

*lpProtocol* \[in\]
</dt> <dd>

Pointer to the beginning of the protocol data in a frame.

</dd> <dt>

*nPropertyInsts* \[in\]
</dt> <dd>

Number of [PROPERTYINST](propertyinst.md) structures provided by *lpPropInst*.

</dd> <dt>

*lpPropInst* \[in\]
</dt> <dd>

Pointer to an array of [PROPERTYINST](propertyinst.md) structures.

</dd> </dl>

## Return value

If the function is successful, the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Remarks

Network Monitor calls the **FormatProperties** function to display data in the details pane of the Network Monitor UI. Typically, **FormatProperties** is called to format the summary line for a protocol, and then to format all the property instances of the protocol within a frame. However, Network Monitor does not guarantee the number of times it calls **FormatProperties** for a specific parser.

During the implementation of the **FormatProperties** function, the parser indirectly calls the [FormatPropertyInstance](formatpropertyinstance.md) function to use the generic formatter that Network Monitor provides, or it can call a custom formatter procedure that is defined by the parser. One of the formatters must be called for each [PROPERTYINST](propertyinst.md) structure passed to the parser DLL in the *lpPropInst* parameter.



| For Information on                                          | See                                                                |
|-------------------------------------------------------------|--------------------------------------------------------------------|
| What parsers are, and how they work with Network Monitor.   | [Parsers](parsers.md)                                             |
| Which entry points are included in the parser DLL.          | [Parser DLL Architecture](parser-dll-architecture.md)             |
| How to implement **FormatProperties**  includes an example. | [Implementing FormatProperties](implementing-formatproperties.md) |
| How the generic formatter formats different types of data.  | [Generic Formatter Output](generic-formatter-output.md)           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[FormatPropertyInstance](formatpropertyinstance.md)
</dt> <dt>

[PROPERTYINFO](propertyinfo.md)
</dt> <dt>

[PROPERTYINST](propertyinst.md)
</dt> </dl>

 

 




