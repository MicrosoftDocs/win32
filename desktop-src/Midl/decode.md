---
title: decode attribute
description: The \ decode\ ACF attribute specifies that a procedure or a type needs de-serialization support.
ms.assetid: 78cd855f-6731-4ef8-9097-e8da5a9b3bdc
keywords:
- decode attribute MIDL
topic_type:
- apiref
api_name:
- decode
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# decode attribute

The **\[decode\]** ACF attribute specifies that a procedure or a type needs de-serialization support.

``` syntax
[ 
    decode 
    [ , interface-attribute-list] 
] 
interface interface-name
{
    interface-definition
}

[ decode [ , op-attribute-list] ] proc-name(...);

typedef [decode [ , type-attribute-list] ] type-name;
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies other attributes that apply to the interface as a whole.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*interface-definition* 
</dt> <dd>

Specifies IDL statements which form the definition of the interface.

</dd> <dt>

*op-attribute-list* 
</dt> <dd>

Specifies other operational attributes that apply to the procedure such as **\[**[**encode**](encode.md)**\]**.

</dd> <dt>

*proc-name* 
</dt> <dd>

Specifies the name of the procedure.

</dd> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies other attributes such as **\[**[**encode**](encode.md)**\]** and **\[**[**allocate**](allocate.md)**\]**.

</dd> <dt>

*type-name* 
</dt> <dd>

Specifies a type defined in the IDL file.

</dd> </dl>

## Remarks

The **\[decode\]** attribute causes the MIDL compiler to generate code that an application can use to retrieve serialized data from a buffer. The **\[**[**encode**](encode.md)**\]** attribute provides serialization support, generating the code to serialize data into a buffer.

Use the **\[**[**encode**](encode.md)**\]** and **\[decode\]** attributes in an ACF to generate serialization code for procedures or types defined in the IDL file of an interface. When used as an interface attribute, **\[decode\]** applies to all types and procedures defined in the IDL file. When used as a type attribute, **\[decode\]** applies only to the specified type. When used as an operational attribute, **\[decode\]** applies only to that procedure.

For more information about using this serialization support, see [Serialization Services](/windows/desktop/Rpc/serialization-services) and **\[**[**encode**](encode.md)**\]**.

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**allocate**](allocate.md)
</dt> <dt>

[**encode**](encode.md)
</dt> </dl>

 

 