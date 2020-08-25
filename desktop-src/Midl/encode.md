---
title: encode attribute
description: The \ encode\ ACF attribute specifies that a procedure or a data type needs serialization support.
ms.assetid: 2661021d-8a26-4216-935b-ca40b6f8b9ec
keywords:
- encode attribute MIDL
topic_type:
- apiref
api_name:
- encode
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# encode attribute

The **\[encode\]** ACF attribute specifies that a procedure or a data type needs serialization support.

``` syntax
[ 
    encode 
    [ , interface-attribute-list] 
] 
interface interface-name
{
    interface-definition
}

[ encode [ , op-attribute-list] ] proc-name

typedef [encode [ , type-attribute-list] ] type-name
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

Specifies other operational attributes that apply to the procedure such as **\[**[**decode**](decode.md)**\]**.

</dd> <dt>

*proc-name* 
</dt> <dd>

Specifies the name of the procedure.

</dd> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies other attributes that apply to the type such as **\[**[**decode**](decode.md)**\]** and **\[**[**allocate**](allocate.md)**\]**.

</dd> <dt>

*type-name* 
</dt> <dd>

Specifies a type defined in the IDL file.

</dd> </dl>

## Remarks

The **\[encode\]** attribute causes the MIDL compiler to generate code that an application can use to serialize data into a buffer. The **\[**[**decode**](decode.md)**\]** attribute generates the code for unmarshaling data from a buffer.

Use the **\[encode\]** and **\[**[**decode**](decode.md)**\]** attributes in an ACF to generate serialization code for procedures or types defined in the IDL file of an interface. When used as an interface attribute, **\[encode\]** applies to all the types and procedures defined in the IDL file. When used as an operational attribute, **\[encode\]** applies only to the specified procedure. When used as a type attribute, **\[encode\]** applies only to the specified type.

When the **\[encode\]** or **\[**[**decode**](decode.md)**\]** attribute is applied to a procedure, the MIDL compiler generates a serialization stub in a similar fashion as remote stubs are generated for remote routines. A procedure can be either a remote or a serializing procedure, but it cannot be both. The prototype of the generated routine is sent to the STUB.H file while the stub itself goes into the STUB\_C.C file.

The MIDL compiler generates two functions for each type the **\[encode\]** attribute applies to, and one additional function for each type the **\[**[**decode**](decode.md)**\]** attribute applies to. For example, for a user-defined type named MyType, the compiler generates code for the MyType\_Encode, MyType\_Decode, and MyType\_AlignSize functions. For these functions, the compiler writes prototypes to STUB.H and source code to STUB\_C.C.

For additional information about serialization handles and encoding or decoding data, see [Serialization Services](/windows/desktop/Rpc/serialization-services).

## Examples

``` syntax
/* 
    ACF file example; 
    Assumes MyType1, MyType2, MyType3, MyProc1, MyProc2, MyProc3 defined 
    in IDL file  
    MyType1, MyType2, MyProc1, MyProc2 have encode and decode 
    serialization support 
    MyType3 and MyProc3 have encode serialization support only 
*/ 
[ 
    encode, 
    implicit_handle(handle_t bh) 
]    
interface regress 
{ 
    typedef [ decode ] MyType1; 
    typedef [ encode, decode ] MyType2; 
    [ decode ] MyProcc1(); 
    [ encode ] MyProc2(); 
}
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**allocate**](allocate.md)
</dt> <dt>

[**decode**](decode.md)
</dt> </dl>

 

 