---
title: nocode attribute
description: The \ nocode\ attribute is used in ACF headers or with individual functions to prevent the generation of client stub code.
ms.assetid: d3b6e4c8-103c-4ea2-8748-11d844fdda97
keywords:
- nocode attribute MIDL
topic_type:
- apiref
api_name:
- nocode
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# nocode attribute

The **\[nocode\]** attribute is used in ACF headers or with individual functions to prevent the generation of client stub code.

``` syntax
[ 
    nocode 
    [ , ACF-interface-attributes ] 
] 
interface interface-name
{
  [ include filename-list ; ]
  [ typedef [type-attribute-list] typename; ] 
  [ [ nocode [ , ACF-function-attributes ] ] function-name (
        [ ACF-parameter-attributes ] parameter-name ;
        ...);
  ]
    ...
}
```

## Parameters

<dl> <dt>

*ACF-interface-attributes* 
</dt> <dd>

Specifies a list of one or more attributes that apply to the interface as a whole. Valid attributes include either **\[**[**auto\_handle**](auto-handle.md)**\]** or **\[**[**implicit\_handle**](implicit-handle.md)**\]** and either **\[**[**code**](code.md)**\]** or **\[nocode\]**. When two or more interface attributes are present, they must be separated by commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface. In DCE-compatibility mode, the interface name must match the name of the interface specified in the IDL file. When you use the MIDL compiler switch [**/acf**](-acf.md), the interface name in the ACF and the interface name in the IDL file can be different.

</dd> <dt>

*filename-list* 
</dt> <dd>

Specifies a list of one or more C-language header file names, separated by commas. The full file name, including the extension, must be supplied.

</dd> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies a list of one or more attributes, separated by commas, that apply to the specified type. Valid type attributes include **\[**[**allocate**](allocate.md)**\]**.

</dd> <dt>

*typename* 
</dt> <dd>

Specifies a type defined in the IDL file. Type attributes in the ACF can only be applied to types previously defined in the IDL file.

</dd> <dt>

*ACF-function-attributes* 
</dt> <dd>

Specifies attributes that apply to the function as a whole, such as **\[**[**comm\_status**](comm-status.md)**\]**. Function attributes are enclosed in square brackets. Separate multiple function attributes with commas.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function as defined in the IDL file.

</dd> <dt>

*ACF-parameter-attributes* 
</dt> <dd>

Specifies ACF attributes that apply to a parameter. Note that zero or more attributes can be applied to the parameter. Separate multiple parameter attributes with commas. ACF parameter attributes are enclosed in square brackets.

</dd> <dt>

*parameter-name* 
</dt> <dd>

Specifies a parameter of the function as defined in the IDL file. Each parameter for the function must be specified in the same sequence and using the same name as defined in the IDL file.

</dd> </dl>

## Remarks

The **\[nocode\]** attribute can appear in the ACF header, or it can be applied to an individual function.

When the **\[nocode\]** attribute appears in the ACF header, client stub code is not generated for any remote function unless it has the **\[**[**code**](code.md)**\]** function attribute. You can override the **\[nocode\]** attribute in the header for an individual function by specifying the **\[code\]** attribute as a function attribute.

When the **\[nocode\]** attribute appears in the function's attribute list, no client stub code is generated for the function.

Client stub code is not generated when:

-   The ACF header includes the **\[nocode\]** attribute.
-   The **\[nocode\]** attribute is applied to the function.
-   The **\[**[**local**](local.md)**\]** attribute applies to the function in the interface file.

Either **\[**[**code**](code.md)**\]** or **\[nocode\]** can appear in a function's attribute list, and the one you choose can appear exactly once.

The **\[nocode\]** attribute is ignored when server stubs are generated. You cannot apply it when generating server stubs in DCE-compatibility mode.

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**/acf**](-acf.md)
</dt> <dt>

[**allocate**](allocate.md)
</dt> <dt>

[**auto\_handle**](auto-handle.md)
</dt> <dt>

[**code**](code.md)
</dt> <dt>

[**comm\_status**](comm-status.md)
</dt> <dt>

[**implicit\_handle**](implicit-handle.md)
</dt> </dl>

 

 




