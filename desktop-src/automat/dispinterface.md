---
title: dispinterface
description: This statement defines a set of properties and methods on which IDispatch Invoke can be called. A dispinterface can be defined by explicitly listing the set of supported methods and properties (Syntax 1) or by listing a single interface (Syntax 2).
ms.assetid: e8c18ae5-3d9e-4dff-aa20-b5acc723eacf
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# dispinterface

This statement defines a set of properties and methods on which [IDispatch::Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D) can be called. A dispinterface can be defined by explicitly listing the set of supported methods and properties (Syntax 1) or by listing a single interface (Syntax 2).

## Syntax

``` syntax
[attributes]
dispinterface intfname {
   properties:
      proplist 
   methods:
      methlist 
};

-or-

[attributes]
dispinterface intfname {
   interface interfacename 
};
```

<dl> <dt>

<span id="attributes"></span><span id="ATTRIBUTES"></span>*attributes*
</dt> <dd>

The helpstring, helpcontext, hidden, uuid, and version attributes are accepted before dispinterface. Attributes (including the brackets) can be omitted, except for the uuidattribute, which is required.

</dd> <dt>

<span id="intfname"></span><span id="INTFNAME"></span>*intfname*
</dt> <dd>

The name by which the dispinterface is known in the type library. This name must be unique within the type library.

</dd> <dt>

<span id="interfacename"></span><span id="INTERFACENAME"></span>*interfacename*
</dt> <dd>

(Syntax 2) The name of the interface to declare as an [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface.

</dd> <dt>

<span id="proplist"></span><span id="PROPLIST"></span>*proplist*
</dt> <dd>

(Syntax 1) An optional list of properties supported by the object, declared in the form of variables. This is the short form for declaring the property functions in the methods list. See the comments section for details.

</dd> <dt>

<span id="methlist"></span><span id="METHLIST"></span>*methlist*
</dt> <dd>

(Syntax 1) A list comprising a function prototype for each method and property in the dispinterface. Any number of function definitions can appear in methlist. A function in methlisthas the following form:

attributes\] *returntypemethname*(*params*);

The following attributes are accepted on a method in a dispinterface: helpstring, helpcontext, string (for compatibility with the Interface Definition Language), bindable, defaultbind, displaybind, propget, propput, propputref, and vararg. If vararg is specified, the last parameter must be a safe array of VARIANT type.

The parameter list is a comma-delimited list, each element of which has the following form:

\[attributes\] *typeparamname*

The *type* can be any declared or built-in type, or a pointer to any type. Attributes on parameters are in, out, optional, and string.

If optional is specified, it must only be specified on the right-most parameters, and the types of those parameters must be VARIANT.

</dd> </dl>

## Remarks

Method functions are specified exactly as described in the module statement except that the entry attribute is not allowed.

Properties can be declared either in the properties or methods lists. Declaring properties in the properties list does not indicate the type of access the property supports (get, put, or putref). Specify the readonly attribute for properties that do not support put or putref. If the property functions are declared in the methods list, functions for one property will all have the same ID.

Using Syntax 1, the properties: and methods: tags are required. The id attribute is also required on each member. For example:

``` syntax
properties:
   [id(0)] int Value;   // Default property.
methods:
   [id(1)] void Show();
```

Unlike interface members, dispinterface members cannot use the retval attribute to return a value in addition to an HRESULT error code. The lcid attribute is also invalid for dispinterfaces because IDispatch::Invoke passes a locale ID (LCID). However, it is possible to declare an interface again that uses these attributes.

Using Syntax 2, interfaces that support IDispatch and are declared earlier in an Object Definition Language (ODL) script can be redeclared as IDispatch interfaces as follows:

``` syntax
dispinterface helloPro {
   interface hello;
};
```

This example declares all of the members of the Hello sample and all of the members that it inherits to support IDispatch. In this case, if Hello was declared earlier with lcid and retval members that returned HRESULTs, MIDL would remove each lcidparameter and HRESULT return type, and instead mark the return type as that of the base type of the retval parameter.

The properties and methods of a dispinterface are not part of the VTBL of the dispinterface. Consequently, [**CreateStdDispatch**](/windows/previous-versions/OleAuto/nf-oleauto-createstddispatch?branch=master) and [**DispInvoke**](/windows/previous-versions/OleAuto/nf-oleauto-dispinvoke?branch=master) cannot be used to implement [**IDispatch::Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master). The dispinterface is used when an application needs to expose existing non-VTBL functions through Automation. These applications can implement **IDispatch::Invoke** by examining the *dispidMember* parameter and directly calling the corresponding function.

## Example


```C++
[uuid(BFB73347-822A-1068-8849-00DD011087E8), version(1.0), helpstring("Useful help string."), helpcontext(2480)]
dispinterface MyDispatchObject {
   properties:
      [id(1)] int x;   // An integer property named x.
      [id(2)] BSTR y;   // A string property named y.
   methods:
      [id(3)] void show();      // No arguments, no result.
      [id(11)] int computeit(int inarg, double *outarg);
};

[uuid 00000000-0000-0000-0000-123456789012]
dispinterface MyObject
{
   properties:
   methods:
      [id(1), propget, bindable, defaultbind, displaybind] 
      long x();

      [id(1), propput, bindable, defaultbind, displaybind] 
      void x(long rhs);
}
```



 

 




