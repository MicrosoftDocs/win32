---
description: The AttachPropertyInstanceEx function maps an existing property to a specific location in the recognized data, and modifies the value of the property data.
ms.assetid: 08bd1959-5ce8-4cb8-af8b-abbf4839c484
title: AttachPropertyInstanceEx function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AttachPropertyInstanceEx
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# AttachPropertyInstanceEx function

The **AttachPropertyInstanceEx** function maps an existing property to a specific location in the recognized data, and modifies the value of the property data.

## Syntax


```C++
BOOL WINAPI AttachPropertyInstanceEx(
  _In_ HFRAME    hFrame,
  _In_ HPROPERTY hProperty,
  _In_ DWORD     Length,
  _In_ ULPVOID   lpData,
  _In_ DWORD     LengthEx,
  _In_ ULPVOID   lpDataEx,
  _In_ DWORD     HelpID,
  _In_ DWORD     IndentLevel,
  _In_ DWORD     IFlags
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame that is being parsed. Use the handle passed to the parser DLL in the *hFrame* parameter of the [**AttachProperties**](attachproperties.md) function.

</dd> <dt>

*hProperty* \[in\]
</dt> <dd>

Handle to a [**PROPERTYINFO**](propertyinfo.md) structure that defines the property. When you implement the [**Register**](register-parser.md) export function you specify the **PROPERTYINFO** structure that defines the property.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

Length of the data for this instance of the property.

</dd> <dt>

*lpData* \[in\]
</dt> <dd>

Pointer to the location in the recognized data where the property value is located. Use the pointer passed to the parser DLL in the *lpProtocol* parameter of the [**AttachProperties**](attachproperties.md) function.

</dd> <dt>

*LengthEx* \[in\]
</dt> <dd>

Length of the extended data   length in bytes.

</dd> <dt>

*lpDataEx* \[in\]
</dt> <dd>

Pointer to the extended data, which is typically a stack variable that contains the extend data.

</dd> <dt>

*HelpID* \[in\]
</dt> <dd>

Identifier (from 0 to 2047) used to set context-sensitive Help for a property.

The *HelpID* number is relative to the Help file associated with the protocol [*property database*](p.md).

</dd> <dt>

*IndentLevel* \[in\]
</dt> <dd>

Indentation level (from 0 to 15) used to display a property hierarchically.

Network Monitor uses levels 0 through 9. Level 15 is a special value that allows the parser to attach a hidden property that is not visible.

</dd> <dt>

*IFlags* \[in\]
</dt> <dd>

A BIT field value that indicates the order of the BITs within a property. Previous parsers that set *fError* to 0 or 1, should now set *fError* to IFLAG\_ERROR. Set this parameter to one of the following values.



| Value                                                                                                                                                         | Meaning                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <span id="IFLAG_ERROR"></span><span id="iflag_error"></span><dl> <dt>**IFLAG\_ERROR**</dt> </dl>       | Data in the frame has an error.<br/>                      |
| <span id="IFLAG_SWAPPED"></span><span id="iflag_swapped"></span><dl> <dt>**IFLAG\_SWAPPED**</dt> </dl> | At attach time, **WORD** byte is a non-Intel format.<br/> |
| <span id="IFLAG_UNICODE"></span><span id="iflag_unicode"></span><dl> <dt>**IFLAG\_UNICODE**</dt> </dl> | At attach time, **STRING** is Unicode.<br/>               |



 

</dd> </dl>

## Return value

If the function is successful, the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Remarks

The **AttachPropertyInstanceEx** function is called during the implementation of the [**AttachProperties**](attachproperties.md) export function. When a property is attached to the data using AttachPropertyInstanceEx, Network Monitor creates a [**PROPERTYINST**](propertyinst.md) structure that defines the instance of the attached property and a [**PROPERTYINSTEX**](propertyinstex.md) structure that defines the extended data.

If **AttachPropertyInstanceEx** is called and no extended data is provided, the *lpDataEx* parameter is **NULL** or the *LengthEx* parameter is 0, the **AttachPropertyInstanceEx** call is functionally equivalent to an [**AttachPropertyInstance**](attachpropertyinstance.md) call.

During the implementation of [**AttachProperties**](attachproperties.md), call [**AttachPropertyInstance**](attachpropertyinstance.md) to use the data as it exists in the capture. You can also call **AttachPropertyInstanceEx** function to modify the property data. However, it is advised that you use the data as it exists in the capture.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




