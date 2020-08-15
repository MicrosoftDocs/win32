---
title: Core Implementation
description: An ADSI provider supports the following features
ms.assetid: 39798237-a181-43b4-8441-ac711f923d4d
ms.tgt_platform: multiple
keywords:
- core implementation ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Core Implementation

An ADSI provider supports the following features:

-   ADsPath strings in both COM and URL format. By definition, you can retrieve an Active Directory object using an ADsPath. Providers support the syntax that their directory service requires using the **ParseDisplayName** implementation.
-   A top-level Namespace object that supports [**IParseDisplayName::ParseDisplayName**](/windows/win32/api/oleidl/nf-oleidl-iparsedisplayname-parsedisplayname) and [**IADsOpenDSObject**](/windows/desktop/api/Iads/nn-iads-iadsopendsobject). This object contains the root nodes for this namespace. Part of the **ParseDisplayName** implementation must include a parser that checks for syntax errors for its own namespace. This object must also support [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) and **IADsOpenDSObject**.
-   The [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface. This includes a simple property cache implementation through [**IADs::GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo) and [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo). Operations that get or set object properties occur in cached mode. Cache values are written to the underlying directory store during **IADs::SetInfo**. An ADSI method, however, is not cached, but executes immediately.
-   The [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist), [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry) and [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue) interfaces for directly accessing and enumerating the properties in the property cache. For directory services that do not expose a schema, this interface allows you to manipulate the properties of an object.
-   The [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) interface for non-Automation clients. This uses over-the-wire protocol for maximum performance and bypasses the property cache.
-   The [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer) interface. Every Active Directory object has a parent container that controls its lifetime. Be aware that for ADs container objects, [**IADs::GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo) affects only the container properties and not its contents. SetInfo on ADs container objects affects only the container properties and does not affect newly created objects or objects that already exist within the container.
-   The [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. This is the Automation interface for languages like Visual Basic Scripting Edition, that do not use compile-time binding. Related to this is the type library data that a provider must supply. For more information, see [Implementation Issues for ADSI Providers](implementation-issues-for-adsi-providers.md).
-   A schema class container object and the appropriate syntax, property, and schema class objects that support [**IADsSyntax**](/windows/desktop/api/Iads/nn-iads-iadssyntax), [**IADsProperty**](/windows/desktop/api/Iads/nn-iads-iadsproperty), and [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass) respectively. At a minimum, each root node must contain its own schema class container object.
-   The [**IADsMembers**](/windows/desktop/api/Iads/nn-iads-iadsmembers) interface, if any supported attributes are collections of ADSI objects, such as security groups.
-   The [**IADsCollection**](/windows/desktop/api/Iads/nn-iads-iadscollection) interface, if any supported attributes are collections of the same directory element type with [**IADsCollection::Add**](/windows/desktop/api/Iads/nf-iads-iadscollection-add) and [**IADsCollection::Remove**](/windows/desktop/api/Iads/nf-iads-iadscollection-remove) capability.
-   The **IEnumXXXX** enumeration supports all specific enumerator objects.
-   Routines to map syntax and convert native data to the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) data type.
-   Follow ADSI conventions for provider-supplied ADSI objects. Include help files and type libraries documenting the interface properties and methods.

As with any COM implementation, calls to [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) must return **E\_NOINTERFACE** for unimplemented interfaces, **E\_NOTIMPL** for unimplemented methods of interfaces that are otherwise implemented and return **E\_ADS\_PROPERTY\_NOT\_SUPPORTED** for unimplemented properties. For more information about dual interfaces and how they affect property implementation, see [Dual Interfaces](dual-interfaces.md).

 

 