---
title: fault_status attribute
description: The \ fault\_status\ ACF attribute specifies that an error code of type error\_status\_t indicates a failure of the remote procedure, rather than other types of problems such as communication errors.
ms.assetid: 9da7bd3d-cef0-4ad4-b2a4-3f8aa156e8e0
keywords:
- fault_status attribute MIDL
topic_type:
- apiref
api_name:
- fault_status
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# fault\_status attribute

The **\[fault\_status\]** ACF attribute specifies that an error code of type [**error\_status\_t**](error-status-t.md) indicates a failure of the remote procedure, rather than other types of problems such as communication errors.

``` syntax
[fault_status [ , ACF-function-attributes ] ] function-name(
    [ [ ACF-parameter-attributes ] ] parameter-name
    , ... );

[ [ ACF-function-attributes ] ] function-name(
    [fault_status [ , ACF-parameter-attributes ] ] parameter-name
    , ... );
```

## Parameters

<dl> <dt>

*ACF-function-attributes* 
</dt> <dd>

Specifies zero or more ACF function attributes such as **\[fault\_status\]** and **\[**[**nocode**](nocode.md)**\]**. Function attributes are enclosed in square brackets. Note that zero or more attributes can be applied to a function. Separate multiple function attributes with commas. Also note that if **\[fault\_status\]** appears as a function attribute, it cannot also appear as a parameter attribute.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function as defined in the IDL file.

</dd> <dt>

*ACF-parameter-attributes* 
</dt> <dd>

Specifies attributes that apply to a parameter. Note that zero or more attributes can be applied to the parameter. Parameter attributes are enclosed in square brackets. Separate multiple parameter attributes with commas. IDL parameter attributes, such as directional attributes, are not allowed in the ACF. Note that if **\[fault\_status\]** appears as a parameter attribute, it cannot also appear as a function attribute.

</dd> <dt>

*parameter-name* 
</dt> <dd>

Specifies the parameter for the function as defined in the IDL file. Each parameter for the function must be specified in the same sequence, using the same name as defined in the IDL file.

</dd> </dl>

## Remarks

The **\[fault\_status\]** attribute can be used as either a function attribute or as a parameter attribute, but it can appear only once per function. It can be applied either to the function itself or to one parameter in each function.

The **\[fault\_status\]** attribute can be applied only to functions that return the type [**error\_status\_t**](error-status-t.md). When the remote procedure fails in a way that causes a fault PDU to be returned, an error code is returned.

When **\[fault\_status\]** is used as a parameter attribute, the parameter must be an **\[**[**out**](out-idl.md)**\]** parameter of type [**error\_status\_t**](error-status-t.md). If a server error occurs, the parameter is set to the error code. When the remote call is successfully completed, the procedure sets the value.

The parameter associated with the **\[fault\_status\]** attribute does not have to be specified in the IDL file. When the parameter is not specified, a new [**out**](out-idl.md) parameter of type [**error\_status\_t**](error-status-t.md) is generated following the last parameter defined in the DCE IDL file.

It is possible for both the **\[fault\_status\]** and **\[**[**comm\_status**](comm-status.md)**\]** attributes to appear in a single function, either as function attributes or parameter attributes. If both attributes are function attributes, or if they apply to the same parameter and no error occurs, the function or parameter has the value **error\_status\_ok**. Otherwise, it contains the appropriate status code value. Because values returned for **\[fault\_status\]** are different from the values returned for **\[comm\_status\]**, the returned values are readily interpreted.

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**comm\_status**](comm-status.md)
</dt> <dt>

[**error\_status\_t**](error-status-t.md)
</dt> <dt>

[**nocode**](nocode.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> </dl>

 

 




