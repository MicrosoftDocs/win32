---
title: comm_status attribute
description: The \ comm\_status\ ACF attribute causes an error code to be returned when a communication error occurs during the execution of a function.
ms.assetid: 3ea9ce62-8bd4-40fe-b838-bfebd52b5a15
keywords:
- comm_status attribute MIDL
topic_type:
- apiref
api_name:
- comm_status
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# comm\_status attribute

The **\[comm\_status\]** ACF attribute causes an error code to be returned when a communication error occurs during the execution of a function.

``` syntax
[comm_status [ , ACF-function-attributes ] ] 
    error_status_t function-name(
        [ [ ACF-parameter-attributes ] ] parameter-name
        , ...);

[ [ ACF-function-attributes ] ] function-name(
    [comm_status [ , ACF-parameter-attributes ] ] error_status_t name
    , ...);
```

## Parameters

<dl> <dt>

*ACF-function-attributes* 
</dt> <dd>

Specifies zero or more ACF function attributes, such as **\[comm\_status\]** and **\[**[**nocode**](nocode.md)**\]**. Function attributes are enclosed in square brackets. Zero or more attributes can be applied to a function. Separate multiple function attributes with commas. Note that if **\[comm\_status\]** appears as a function attribute, it cannot also appear as a parameter attribute.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function as defined in the IDL file.

</dd> <dt>

*ACF-parameter-attributes* 
</dt> <dd>

Specifies attributes that apply to a parameter. Note that zero, one, or more attributes can be applied to the parameter. Separate multiple parameter attributes with commas. Parameter attributes are enclosed in square brackets. IDL parameter attributes, such as directional attributes, are not allowed in the ACF. Note that if **\[comm\_status\]** appears as a parameter attribute, it cannot also appear as a function attribute.

</dd> <dt>

*parameter-name* 
</dt> <dd>

Specifies the parameter for the function as defined in the IDL file. Each parameter for the function must be specified in the same sequence, using the same name as defined in the IDL file.

</dd> </dl>

## Remarks

The **\[comm\_status\]** attribute can be used as either a function attribute or as a parameter attribute, but it can appear only once per function. It can be applied either to the function or to one parameter in each function.

The **\[comm\_status\]** attribute can be applied only to functions that return the type [**error\_status\_t**](error-status-t.md). When a communication error occurs during the execution of the function, an error code is returned.

When **\[comm\_status\]** is used as a parameter attribute, the parameter must be defined in the IDL file and must be an **\[**[**out**](out-idl.md)**\]** parameter of type [**error\_status\_t**](error-status-t.md). When a communication error occurs during the execution of the function, the parameter is set to the error code. When the remote call is completed successfully, the procedure sets the value.

It is possible for both the **\[comm\_status\]** and **\[**[**fault\_status**](fault-status.md)**\]** attributes to appear in a single function, either as function attributes or parameter attributes. If both attributes are function attributes or if they apply to the same parameter and no error occurs, the function or parameter has the value **error\_status\_ok**. Otherwise, it contains the appropriate **\[comm\_status\]** or **\[fault\_status\]** value. Because values returned for **\[comm\_status\]** are different from the values returned for **\[fault\_status\]**, the returned values are readily interpreted.

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**error\_status\_t**](error-status-t.md)
</dt> <dt>

[**fault\_status**](fault-status.md)
</dt> <dt>

[**nocode**](nocode.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> </dl>

 

 




