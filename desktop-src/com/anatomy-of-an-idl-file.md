---
title: Anatomy of an IDL File
description: These example IDL files demonstrate the fundamental constructs of interface definition.
ms.assetid: 9c276b8a-5342-4c09-91a7-c9a9f0f83c73
ms.topic: article
ms.date: 05/31/2018
---

# Anatomy of an IDL File

These example IDL files demonstrate the fundamental constructs of interface definition. Memory allocation, custom marshaling, and asynchronous messaging are just a few of the features you can implement in a custom COM interface. MIDL attributes are used to define COM interfaces. For more information about implementing interfaces and type libraries, including a summary of MIDL attributes, see [Interface Definitions and Type Libraries](/windows/desktop/Midl/interface-definitions-and-type-libraries) in the MIDL Programmer's Guide and Reference. For a complete reference of all MIDL attributes, keywords, and directives, see the [MIDL Language Reference](/windows/desktop/Midl/midl-language-reference).

## Example.idl

The following example IDL file defines two COM interfaces. From this IDL file, Midl.exe will generate proxy/stub and marshaling code and header files. A line-by-line dissection follows the example.

``` syntax
//
// Example.idl 
//
import "mydefs.h","unknwn.idl"; 
[
object,
uuid(a03d1420-b1ec-11d0-8c3a-00c04fc31d2f),
] interface IFace1 : IUnknown
{
HRESULT MethodA([in] short Bread, [out] BKFST * pBToast);
HRESULT MethodB([in, out] BKFST * pBPoptart);
};
 
[
object,
uuid(a03d1421-b1ec-11d0-8c3a-00c04fc31d2f),
pointer_default(unique)
] interface IFace2 : IUnknown
{
HRESULT MethodC([in] long Max,
                [in, max_is(Max)] BkfstStuff[ ],
                [out] long * pSize,
                [out, size_is( , *pSize)] BKFST ** ppBKFST);
}; 
 
```

The IDL [**import**](/windows/desktop/Midl/import) statement is used here to bring in a header file, Mydefs.h, which contains user-defined types, and Unknwn.idl, which contains the definition of [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown), from which IFace1 and IFace2 derive.

The [**object**](/windows/desktop/Midl/object) attribute identifies the interface as an object interface and tells the MIDL compiler to generate proxy/stub code instead of RPC client and server stubs. Object interface methods must have a return type of [**HRESULT**](/openspecs/windows_protocols/ms-erref/0642cb2f-2075-4469-918c-4441e69c548a), to allow the underlying RPC mechanism to report errors for calls that fail to complete due to network problems.

The [**uuid**](/windows/desktop/Midl/uuid) attribute specifies the interface identifier (IID). Each interface, class, and type library must be identified with its own unique identifier. Use the utility Uuidgen.exe to generate a set of unique IDs for your interfaces and other components.

The [**interface**](/windows/desktop/Midl/interface) keyword defines the interface name. All object interfaces must derive, directly or indirectly, from [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown).

The [**in**](/windows/desktop/Midl/in) directional parameter specifies a parameter that is set only by the caller. The [**out**](/windows/desktop/Midl/out-idl) parameter specifies data that is passed back to the caller. Using both directional attributes on one parameter specifies that the parameter is used both to send data to the method and to pass data back to the caller.

The [**pointer\_default**](/windows/desktop/Midl/pointer-default) attribute specifies the default pointer type ([**unique**](/windows/desktop/Midl/unique), [**ref**](/windows/desktop/Midl/ref), or [**ptr**](/windows/desktop/Midl/ptr)) for all pointers except for those included in parameter lists. If no default type is specified, MIDL assumes that single pointers are **unique**. However, when you have multiple levels of pointers, you must explicitly specify a default pointer type, even if you want the default type to be **unique**.

In the preceding example, the array BkfstStuff\[ \] is a *conformant array*, the size of which is determined at run time. The [**max\_is**](/windows/desktop/Midl/max-is) attribute specifies the variable that contains the maximum value for the array index.

The [**size\_is**](/windows/desktop/Midl/size-is) attribute is also used to specify the size of an array or, as in the preceding example, multiple levels of pointers. In the example, the call can be made without knowing in advance how much data will be returned.

## Example2.idl

The following IDL example (which reuses the interfaces described in the previous IDL example) shows the various ways to generate type library information for interfaces.

``` syntax
//
// Example2.idl
//

import "example.idl","oaidl.idl"; 

[
uuid(a03d1422-b1ec-11d0-8c3a-00c04fc31d2f),
helpstring("IFace3 interface"),
pointer_default(unique);
dual,
oleautomation
] 
interface IFace3 : IDispatch
{
   HRESULT MethodD([in] BSTR OrderIn,
                   [out, retval] * pTakeOut);
}; //end IFace3 def

[
uuid(a03d1423-b1ec-11d0-8c3a-00c04fc31d2f),
version(1.0),
helpstring("Example Type Library"),
] library ExampleLib
{
  importlib("stdole32.tlb");
  interface IFace3;
  [
  uuid(a03d1424-b1ec-11d0-8c3a-00c04fc31d2f),
  helpstring("Breakfast Component Class")
  ] coclass BkfstComponent
    {
    [default]interface IFace1;
    interfaceIFace2
    }; //end coclass def

[
uuid(a03d1424-b1ec-11d0-8c3a-00c04fc31d2f),
helpstring("IFace4 interface"),
pointer_default(unique);
dual,
oleautomation
] 
interface IFace4 : IDispatch
{
[propput] HRESULT MethodD([in] BSTR OrderIn);
[propget] HRESULT MethodE([out, retval] * pTakeOut);
}; //end IFace4 def
 
}; //end library def
 
```

The [**helpstring**](/windows/desktop/Midl/helpstring) attribute is optional; you use it to briefly describe the object or to provide a status line. These help strings are readable with an object browser such as the one provided with Microsoft Visual Basic.

The [**dual**](/windows/desktop/Midl/dual) attribute on IFace3 creates an interface that is both a dispatch interface and a COM interface. Because it is derived from **IDispatch**, a dual interface supports Automation, which is what the [**oleautomation**](/windows/desktop/Midl/oleautomation) attribute specifies. IFace3 imports Oaidl.idl to get the definition of **IDispatch**.

The [**library**](/windows/desktop/Midl/library) statement defines the ExampleLib type library, which has its own [**uuid**](/windows/desktop/Midl/uuid), [**helpstring**](/windows/desktop/Midl/helpstring), and [**version**](/windows/desktop/Midl/version) attributes.

Within the type library definition, the [**importlib**](/windows/desktop/Midl/importlib) directive brings in a compiled type library. All type library definitions should bring in the base type library defined in Stdole32.tlb.

This type library definition demonstrates three different ways to include interfaces in the type library. IFace3 is included merely by referencing it within the library statement.

The [**coclass**](/windows/desktop/Midl/coclass) statement defines an entirely new component class, BkfstComponent, that includes two previously defined interfaces, IFace1 and IFace2. The default attribute designates IFace1 as the default interface.

IFace4 is described within the library statement. The [**propput**](/windows/desktop/Midl/propput) attribute on MethodD indicates that the method performs a set action on a property of the same name. The [**propget**](/windows/desktop/Midl/propget) attribute indicates that the method retrieves information from a property of the same name as the method. The [**retval**](/windows/desktop/Midl/retval) attribute in MethodD designates an output parameter that contains the return value of the function.

 

 
