---
title: code attribute
description: The \ code\ ACF attribute causes client stub code to be generated for remote functions.
ms.assetid: 735a8c25-29d4-4073-a2db-88bc8615ccc1
keywords:
- code attribute MIDL
topic_type:
- apiref
api_name:
- code
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# code attribute

The **\[code\]** ACF attribute causes client stub code to be generated for remote functions.

``` syntax
[
    code [ , ACF-interface-attributes ] 
] 
interface interface-name
{
  [ include filename-list ; ]
  [ typedef [type-attribute-list] typenam; ]
  [ [code [ , ACF-function-attributes ]] function-name (
            [ ACF-parameter-attributes ] parameter-name,
        ...);
  ]
    ...
}
```

## Parameters

<dl> <dt>

*ACF-interface-attributes* 
</dt> <dd>

Specifies a list of one or more attributes that apply to the interface as a whole. Valid attributes include either [**\[auto\_handle\]**](auto-handle.md) or [**\[implicit\_handle\]**](implicit-handle.md) and either **\[code\]**, [**\[nocode\]**](nocode.md), or [**\[optimize\]**](optimize.md). When two or more interface attributes are present, they must be separated by commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*filename-list* 
</dt> <dd>

Specifies a list of one or more C-header file names, separated by commas. You must supply the full file name, including the extension.

</dd> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies a list of one or more attributes, separated by commas, that apply to the specified type. Valid type attributes include [**\[allocate\]**](allocate.md) and [**\[represent\_as\]**](represent-as.md).

</dd> <dt>

*typename* 
</dt> <dd>

Specifies a type defined in the IDL file. Type attributes in the ACF can be applied only to types previously defined in the IDL file.

</dd> <dt>

*ACF-function-attributes* 
</dt> <dd>

Specifies zero or more attributes that apply to the function as a whole, such as [**\[comm\_status\]**](comm-status.md). Function attributes are enclosed in square brackets. Separate multiple function attributes with commas.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function as defined in the IDL file.

</dd> <dt>

*ACF-parameter-attributes* 
</dt> <dd>

Specifies ACF attributes that apply to a parameter. Note that zero, one, or more attributes can be applied to the parameter. Separate multiple parameter attributes with commas. ACF parameter attributes are enclosed in square brackets.

</dd> <dt>

*parameter-name* 
</dt> <dd>

Specifies a parameter of the function as defined in the IDL file. Each parameter for the function must be specified in the same sequence and with the same name as defined in the IDL file.

</dd> </dl>

## Remarks

The **\[code\]** attribute can appear in the ACF header or be applied to an individual function.

When the **\[code\]** attribute appears in the ACF header, client stub code is generated for all remote functions that do not have the [**\[nocode\]**](nocode.md) function attribute. You can override the **\[code\]** attribute in the header for an individual function by specifying the **\[nocode\]** attribute as a function attribute.

When the **\[code\]** attribute appears in the remote function's attribute list, client stub code is generated for the function. Client stub code is not generated when:

-   The ACF header includes the [**\[nocode\]**](nocode.md) attribute.
-   The [**\[nocode\]**](nocode.md) attribute is applied to the function.
-   The [**\[local\]**](local.md) attribute applies to the function in the interface file.

Either **\[code\]** or [**\[nocode\]**](nocode.md) can appear in the interface or function attribute list, but the one you choose can appear only once in the list.

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**allocate**](allocate.md)
</dt> <dt>

[**auto\_handle**](auto-handle.md)
</dt> <dt>

[**comm\_status**](comm-status.md)
</dt> <dt>

[**implicit\_handle**](implicit-handle.md)
</dt> <dt>

[**local**](local.md)
</dt> <dt>

[**nocode**](nocode.md)
</dt> <dt>

[**optimize**](optimize.md)
</dt> <dt>

[**represent\_as**](represent-as.md)
</dt> </dl>

 

 




