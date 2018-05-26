---
title: Type Descriptions
description: The information associated with an object described by ITypeInfo can include a set of functions, a set of data members, and various type attributes.
ms.assetid: f3372c15-51f2-43c5-986a-8ab51911b51c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Type Descriptions

The information associated with an object described by [**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master) can include a set of functions, a set of data members, and various type attributes. It is essentially the same as the information described by a C++ class declaration, which can be used to define both interfaces and structures, as well as any combination of functions and data members. In addition to interfaces and structure definitions, the [**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master) interface is used to describe other types, including enumerations and aliases. Because the interface to a C file or library is simply a set of functions and variable declarations, **ITypeInfo** can also be used to describe them.

Type information comprises individual type descriptions. Each type description must have one of the following forms.



| Category                       | ODL keyword                        | Description                                                                                                                                    |
|--------------------------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| alias                          | [typedef](typedef.md)             | An alias for another type.                                                                                                                     |
| enumeration                    | [enum](enum.md)                   | An enumeration.                                                                                                                                |
| structure                      | [struct](struct.md)               | A structure.                                                                                                                                   |
| union                          | [union](union.md)                 | A single data item that can have one of a specified group of types.                                                                            |
| module                         | [module](module.md)               | Data and functions not accessed through virtual function table (VTBL) entries.                                                                 |
| [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) | [dispinterface](dispinterface.md) | [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) properties and methods accessed through [**IDispatch::Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master).                          |
| OLE interface                  | [interface](interface.md)         | OLE member functions accessed through VTBL entries.                                                                                            |
| dual interface                 | [dual](dual.md)                   | Supports either VTBL or [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master).                                                                                        |
| component object class         | [coclass](coclass.md)             | A component object class. Specifies an implementation of one or more OLE interfaces and one or more [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interfaces. |



 

> [!Note]  
> All bit flags that are not used specifically should be set to zero for future compatibility.

 

## Alias

An alias has TypeKind = TKIND\_ALIAS. An alias is an empty set of functions, an empty set of data members, and a type description (located in the TYPEATTR), which gives the actual type definition (typedef) of the alias.

## Enumeration (Statement)

An enumeration (enum) has TypeKind = TKIND\_ENUM. An enumeration is an empty set of functions and a set of constant data members.

## Structure (Statement)

A structure (struct) description has TypeKind = TKIND\_RECORD. A structure is an empty set of functions and a set of per-instance data members.

## Union (Statement)

A union description has TypeKind = TKIND\_UNION. A union is an empty set of functions and a set of per-instance data members, each of which has an instance offset of zero.

## Module (Statement)

A module has TypeKind = TKIND\_MODULE. A module is a set of static functions and a set of static data members.

## OLE-Compatible Interface

An interface definition has TypeKind = TKIND\_INTERFACE. An interface is a set of pure virtual functions and an empty set of data members. If a type description contains any virtual functions, then the pointer to the VTBL is the first 4 bytes of the instance.

The type information fully describes the member functions in the VTBL, including parameter names and types and function return types. It may inherit from no more than one other interface.

With interfaces and dispinterfaces, all members should have different names, except the accessor functions of properties. For property functions having the same name, the documentation string and Help context should be set for only one of the functions (because they define the same property conceptually).

## IDispatch Interface

These include objects (TypeKind = TKIND\_DISPATCH) that support the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface with a specification of the dispatch data members (such as properties) and methods supported through the object's [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo-invoke?branch=master) implementation. All members of the dispinterface should have different IDs, except for the accessor functions of properties.

## Dual Interface

Dual interfaces ([dual](dual.md)) have two different type descriptions for the same interface. The TKIND\_INTERFACE type description describes the interface as a standard OLE Component Object Model (COM) interface. The TKIND\_DISPATCH type description describes the interface as a standard dispatch interface. The lcid and retval parameters, and the HRESULT return types are removed, and the return type of the member is specified to be the same type as the retval parameter.

By default, the TYPEKIND enumeration for a dual interface is TKIND\_INTERFACE. Tools that bind to interfaces should check the type flags for TYPEFLAG\_FDUAL. If this flag is set, the TKIND\_DISPATCH type description is available through a call to [**ITypeInfo::GetRefTypeOfImplType**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo-getreftypeofimpltype?branch=master) with an index of –1, followed by a call to [**ITypeInfo::GetRefTypeInfo**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo-getreftypeinfo?branch=master).

## Component Object Classes

These coclass objects (TypeKind = TKIND\_COCLASS) support a set of implemented interfaces, which can be of either TKIND\_INTERFACE or TKIND\_DISPATCH.

## Related topics

<dl> <dt>

[**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master)
</dt> </dl>

 

 




