---
title: Core Implementation
description: An ADSI provider supports the following features
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '39798237-a181-43b4-8441-ac711f923d4d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["core implementation ADSI"]
---

# Core Implementation

An ADSI provider supports the following features:

-   ADsPath strings in both COM and URL format. By definition, you can retrieve an Active Directory object using an ADsPath. Providers support the syntax that their directory service requires using the **ParseDisplayName** implementation.
-   A top-level Namespace object that supports [**IParseDisplayName::ParseDisplayName**](_com_iparsedisplayname_parsedisplayname) and [**IADsOpenDSObject**](iadsopendsobject.md). This object contains the root nodes for this namespace. Part of the **ParseDisplayName** implementation must include a parser that checks for syntax errors for its own namespace. This object must also support [**IADs**](iads.md) and **IADsOpenDSObject**.
-   The [**IADs**](iads.md) interface. This includes a simple property cache implementation through [**IADs::GetInfo**](iads-getinfo.md) and [**IADs::SetInfo**](iads-setinfo.md). Operations that get or set object properties occur in cached mode. Cache values are written to the underlying directory store during **IADs::SetInfo**. An ADSI method, however, is not cached, but executes immediately.
-   The [**IADsPropertyList**](iadspropertylist.md), [**IADsPropertyEntry**](iadspropertyentry.md) and [**IADsPropertyValue**](iadspropertyvalue.md) interfaces for directly accessing and enumerating the properties in the property cache. For directory services that do not expose a schema, this interface allows you to manipulate the properties of an object.
-   The [**IDirectoryObject**](idirectoryobject.md) interface for non-Automation clients. This uses over-the-wire protocol for maximum performance and bypasses the property cache.
-   The [**IADsContainer**](iadscontainer.md) interface. Every Active Directory object has a parent container that controls its lifetime. Be aware that for ADs container objects, [**IADs::GetInfo**](iads-getinfo.md) affects only the container properties and not its contents. SetInfo on ADs container objects affects only the container properties and does not affect newly created objects or objects that already exist within the container.
-   The [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. This is the Automation interface for languages like Visual Basic Scripting Edition, that do not use compile-time binding. Related to this is the type library data that a provider must supply. For more information, see [Implementation Issues for ADSI Providers](implementation-issues-for-adsi-providers.md).
-   A schema class container object and the appropriate syntax, property, and schema class objects that support [**IADsSyntax**](iadssyntax.md), [**IADsProperty**](iadsproperty.md), and [**IADsClass**](iadsclass.md) respectively. At a minimum, each root node must contain its own schema class container object.
-   The [**IADsMembers**](iadsmembers.md) interface, if any supported attributes are collections of ADSI objects, such as security groups.
-   The [**IADsCollection**](iadscollection.md) interface, if any supported attributes are collections of the same directory element type with [**IADsCollection::Add**](iadscollection-add.md) and [**IADsCollection::Remove**](iadscollection-remove.md) capability.
-   The **IEnumXXXX** enumeration supports all specific enumerator objects.
-   Routines to map syntax and convert native data to the [**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118) data type.
-   Follow ADSI conventions for provider-supplied ADSI objects. Include help files and type libraries documenting the interface properties and methods.

As with any COM implementation, calls to [**QueryInterface**](_com_iunknown_queryinterface) must return **E\_NOINTERFACE** for unimplemented interfaces, **E\_NOTIMPL** for unimplemented methods of interfaces that are otherwise implemented and return **E\_ADS\_PROPERTY\_NOT\_SUPPORTED** for unimplemented properties. For more information about dual interfaces and how they affect property implementation, see [Dual Interfaces](dual-interfaces.md).

 

 




