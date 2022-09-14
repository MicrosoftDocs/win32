---
title: dispinterface attribute
description: The dispinterface statement defines a set of properties and methods on which you can call IDispatch Invoke.
ms.assetid: d85a8e2b-0155-4d68-bb38-e86f4807e7de
keywords:
- dispinterface attribute MIDL
topic_type:
- apiref
api_name:
- dispinterface
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# dispinterface attribute

The **dispinterface** statement defines a set of properties and methods on which you can call **IDispatch::Invoke**. A dispinterface may be defined by explicitly listing the set of supported methods and properties (Syntax 1), or by listing a single interface (Syntax 2).

``` syntax
[
    [attributes]
]
dispinterface dispinterface-name
{
    properties:
        property-list
    methods:
        method-list
};

[
  [attributes]
]
dispinterface dispinterface-name
{
    interface interface-name
};
```

## Parameters

<dl> <dt>

*attributes* 
</dt> <dd>

Specifies attributes that apply to the entire **dispinterface**. The following attributes are accepted: **\[**[**helpstring**](helpstring.md)**\]**, **\[**[**helpcontext**](helpcontext.md)**\]**, **\[**[**helpfile**](helpfile.md)**\]**, **\[**[**hidden**](hidden.md)**\]**, **\[**[**nonextensible**](nonextensible.md)**\]**, **\[**[**oleautomation**](oleautomation.md)**\]**, **\[**[**restricted**](restricted.md)**\]**, **\[**[**uuid**](uuid.md)**\]**, and **\[**[**version**](version.md)**\]**.

</dd> <dt>

*dispinterface-name* 
</dt> <dd>

The name by which the **dispinterface** is known in the type library. This name must be unique within the type library.

</dd> <dt>

*property-list* 
</dt> <dd>

(Syntax 1) An optional list of properties supported by the object, declared in the form of variables. This is the short form for declaring the property functions in the methods list. See the comments section for details.

</dd> <dt>

*method-list* 
</dt> <dd>

(Syntax 1) A list comprising a function prototype for each method and property in the **dispinterface**. Any number of function definitions can appear in *methlist*. A function in *methlist* has the following form:

**\[***attributes***\]** *returntype methname type paramname* **(***params***);**

The following attributes are accepted on a method in a **dispinterface**: **\[helpstring\]**, **\[helpcontext\]**, **\[**[**propget**](propget.md)**\]**, **\[**[**propput**](propput.md)**\]**, **\[**[**propputref**](propputref.md)**\]**, **\[**[**string**](string.md)**\]**, and **\[**[**vararg**](vararg.md)**\]**. If **\[vararg\]** is specified, the last parameter must be a safe array of **VARIANT** type.

The parameter list is a comma-delimited list, each element of which has the following form:

**\[***attributes***\]**

The *type* can be any declared or built-in type, or a pointer to any type. Attributes on parameters are:

**\[**[**in**](in.md)**\]**, **\[**[**out**](out-idl.md)**\]**, **\[**[**optional**](optional.md)**\]**, **\[string\]**

</dd> <dt>

*interface-name* 
</dt> <dd>

(Syntax 2) The name of the interface to declare as an IDispatch interface.

</dd> </dl>

## Remarks

The MIDL compiler accepts the following parameter ordering (from left-to-right):

1.  Required parameters (parameters that do not have the \[defaultvalue\] or \[optional\] attributes),
2.  optional parameters with or without the \[defaultvalue\] attribute,
3.  parameters with the \[optional\] attribute and without the \[defaultvalue\] attribute,
4.  \[ [**lcid**](lcid.md)\] parameter, if any,
5.  \[ [**retval**](retval.md)\] parameter

Method functions are specified exactly as described in the reference page for [**module**](module.md) except that the \[ [**entry**](entry.md)\] attribute is not allowed. Note that STDOLE32.TLB (STDOLE.TLB on 16-bit systems) must be imported, because a **dispinterface** inherits from IDispatch.

You can declare properties in either the properties or methods lists. Declaring properties in the properties list does not indicate the type of access the property supports (that is, get, put, or putref). Specify the \[ [**readonly**](readonly.md)\] attribute for properties that don't support put or putref. If you declare the property functions in the methods list, functions for one property all have the same identifier.

Using the first syntax, the properties: and methods: tags are required. The \[ [**id**](id.md)\] attribute is also required on each member. For example:

``` syntax
properties: 
    [id(0)] int Value;    // Default property. 
methods: 
    [id(1)] HRESULT Show();
```

Unlike interface members, dispinterface members cannot use the [**retval**](retval.md) attribute to return a value in addition to an HRESULT error code. The \[ [**lcid**](lcid.md)\] attribute is likewise invalid for dispinterfaces, because IDispatch::Invoke passes an LCID. However, it is possible to redeclare an interface that uses these attributes.

Using the second syntax, interfaces that support IDispatch and are declared earlier in an ODL script can be redeclared as IDispatch interfaces as follows:

``` syntax
dispinterface helloPro 
{ 
    interface hello; 
};
```

The preceding example declares all the members of hello and all the members that hello inherits as supporting IDispatch. In this case, if hello were declared earlier with \[lcid\] and \[retval\] members that returned HRESULTs, MkTypLib would remove each \[lcid\] parameter and HRESULT return type, and instead mark the return type as that of the \[retval\] parameter.

> [!Note]  
> The Mktyplib.exe tool is obsolete. Use the MIDL compiler instead.

 

The properties and methods of a dispinterface are not part of the VTBL of the dispinterface. Consequently, [CreateStdDispatch](/windows/win32/api/oleauto/nf-oleauto-createstddispatch) and [DispInvoke](/windows/win32/api/oleauto/nf-oleauto-dispinvoke) cannot be used to implement IDispatch::Invoke. The dispinterface is used when an application needs to expose existing non-VTBL functions through Automation. These applications can implement IDispatch::Invoke by examining the dispidMember parameter and directly calling the corresponding function.

## Examples

``` syntax
[ 
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676), 
    version(1.0), 
    helpstring("Useful help string."), 
    helpcontext(2480)
] 
dispinterface MyDispatchObject 
{ 
    properties: 
        [id(1)] int x;    //An integer property named x 
        [id(2)] BSTR y;   //A string property named y 
    methods: 
        [id(3)] HRESULT show();    //No arguments, no result 
        [id(11)] int computeit(int inarg, double *outarg); 
}; 
 
[
    uuid(1e123456-1f3c-1069-996b-00dd010fe676)
] 
dispinterface MyObject 
{ 
    properties: 
    methods: 
        [id(1), propget, bindable, defaultbind, displaybind] long x(); 
 
        [id(1), propput, bindable, defaultbind, 
         displaybind] HRESULT x(long rhs); 
}
```

## See also

<dl> <dt>

[**bindable**](bindable.md)
</dt> <dt>

[**defaultbind**](defaultbind.md)
</dt> <dt>

[**displaybind**](displaybind.md)
</dt> <dt>

[**helpcontext**](helpcontext.md)
</dt> <dt>

[**helpfile**](helpfile.md)
</dt> <dt>

[**helpstring**](helpstring.md)
</dt> <dt>

[**hidden**](hidden.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**optional**](optional.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**nonextensible**](nonextensible.md)
</dt> <dt>

[**propget**](propget.md)
</dt> <dt>

[**propput**](propput.md)
</dt> <dt>

[**propputref**](propputref.md)
</dt> <dt>

[**oleautomation**](oleautomation.md)
</dt> <dt>

[**restricted**](restricted.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**uuid**](uuid.md)
</dt> <dt>

[**vararg**](vararg.md)
</dt> <dt>

[**version**](version.md)
</dt> </dl>

 

 
