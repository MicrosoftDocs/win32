---
title: error_status_t attribute
description: The error\_status\_t keyword designates a type for an object that contains communication-status or fault-status information.
ms.assetid: 7eff0d20-c058-4f16-a3db-0b4c82303135
keywords:
- error_status_t attribute MIDL
topic_type:
- apiref
api_name:
- error_status_t
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# error\_status\_t attribute

The **error\_status\_t** keyword designates a type for an object that contains communication-status or fault-status information.

``` syntax
[ [ , ACF-function-attributes ] ] error_status_t function-name(
        [ [ ACF-parameter-attributes ] ] parameter-name
        , ...);

[ [ ACF-function-attributes ] ] function-name(
    [ [ ACF-parameter-attributes ] ] error_status_t parameter-name
    , ...);
```

## Parameters

<dl> <dt>

*ACF-function-attributes* 
</dt> <dd>

Specifies zero or more ACF function attributes, such as **\[**[**comm\_status**](comm-status.md)**\]**, **\[**[**fault\_status**](fault-status.md)**\]**, or **\[**[**nocode**](nocode.md)**\]**. Function attributes are enclosed in square brackets. Zero or more attributes can be applied to a function. Separate multiple function attributes with commas.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function as defined in the IDL file.

</dd> <dt>

*ACF-parameter-attributes* 
</dt> <dd>

Specifies attributes that apply to a parameter. Note that zero, one, or more attributes can be applied to the parameter. Separate multiple parameter attributes with commas. Parameter attributes are enclosed in square brackets. IDL parameter attributes, such as directional attributes, are not allowed in the ACF.

</dd> <dt>

*parameter-name* 
</dt> <dd>

Specifies the parameter for the function as defined in the IDL file. Each parameter for the function must be specified in the same sequence, using the same name as defined in the IDL file.

</dd> </dl>

## Remarks

The **error\_status\_t** type is used as a part of the exception handling architecture in IDL. This type maps to an [**unsigned**](unsigned.md) [**long**](long.md). Applications that catch error situations have an **\[**[**out**](out-idl.md)**\]** parameter or a return type of a procedure specified as **error\_status\_t**, and qualify the **error\_status\_t** with the **\[**[**comm\_status**](comm-status.md)**\]** or **\[**[**fault\_status**](fault-status.md)**\]** attributes in the ACF. If the parameter or return type was not qualified with the **\[comm\_status\]** or **\[fault\_status\]** attributes, then the parameter operates as though it were an unsigned long.

Beginning with version 2.0, the MIDL compiler generates stubs that contain the proper error handling architecture. However, earlier versions of the MIDL compiler handled a parameter or return type of **error\_status\_t** as though the **\[**[**comm\_status**](comm-status.md)**\]** and **\[**[**fault\_status**](fault-status.md)**\]** attributes were applied, even if they were not. With MIDL 2.0 or later, you must explicitly apply the **\[comm\_status\]** and **\[fault\_status\]** attributes to the parameter or procedure in the ACF.

The **error\_status\_t** type is one of the predefined types of the interface definition language. Predefined types can appear as type specifiers in [**typedef**](typedef.md) declarations, in general declarations, and in function declarators (either as the function-return-type or as parameter-type specifiers).

## See also

<dl> <dt>

[**comm\_status**](comm-status.md)
</dt> <dt>

[**fault\_status**](fault-status.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**long**](long.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> </dl>

 

 




