---
title: Implementation Issues for ADSI Providers
description: Implementation Issues for ADSI Providers
ms.assetid: 0be772aa-e7d8-4d34-b55a-162abfb0bfd4
ms.tgt_platform: multiple
keywords:
- Implementation Issues for ADSI Providers ADSI
- providers ADSI , implementing
ms.topic: article
ms.date: 05/31/2018
---

# Implementation Issues for ADSI Providers

To implement ADSI interfaces, first implement the COM interface [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject). By providing this interface as a minimal overhead layer, you supply client applications the control required to access directory objects directly from the directory rather than through the ADSI cache, which optimizes network performance. Using this interface will also supply your own implementation with the most flexibility.

Second, implement the fundamental ADSI interfaces, [**IADs**](/windows/desktop/api/Iads/nn-iads-iads), [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer), [**IADsCollection**](/windows/desktop/api/Iads/nn-iads-iadscollection), and the [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue), [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry), [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist) property cache interfaces. [**IADsGroup**](/windows/desktop/api/Iads/nn-iads-iadsgroup) and [**IADsMembers**](/windows/desktop/api/Iads/nn-iads-iadsmembers) are also interfaces in frequent demand by system administration software.

Third, implement the schema management interfaces if your directory service has an underlying schema: [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass), [**IADsProperty**](/windows/desktop/api/Iads/nn-iads-iadsproperty), [**IADsSyntax**](/windows/desktop/api/Iads/nn-iads-iadssyntax). If there is no underlying schema, use these interfaces to abstract the classes and properties used by the directory service. Schemas can be used to publish the features of your directory service to ADSI clients.

## Collections

ADSI provider components can follow one of three models for caching collections during enumeration. The choice of a caching model determines the behavior of ADSI when an object in a collection is deleted from the underlying directory service external to ADSI.

The caching models include:

-   Collections cached in advance. The collection of object instances is retrieved from the underlying directory service in its entirety when [**IADsCollection::get\_\_NewEnum**](/windows/desktop/api/Iads/nf-iads-iadscollection-get__newenum) is called to create a new enumerator object. If the source object for an Active Directory object instance in the retrieved collection is deleted from the underlying directory service, the client does not recognize the deletion until a [**IADs::GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo) or [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) attempts to access the collection.
-   Collections incrementally cached. The collection is retrieved from the underlying directory service one object at a time when [**IEnumVARIANT::Next**](/windows/win32/api/oaidl/nf-oaidl-ienumvariant-next) is called. [**IEnumVARIANT::Reset**](/windows/win32/api/oaidl/nf-oaidl-ienumvariant-reset) will return to the beginning of the collection in the cache and **IEnumVARIANT::Next** will return cached objects until the end of the cache is reached, at which point new objects will be added from the underlying store. When an Active Directory object instance is in the cache the client will not become aware of its deletion from the underlying directory service until an [**IADs::GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo) or [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) attempts to access the object.
-   Collections not cached. The collection is retrieved from the underlying directory service one object at a time when [**IEnumVARIANT::Next**](/windows/win32/api/oaidl/nf-oaidl-ienumvariant-next) is called. [**IEnumVARIANT::Reset**](/windows/win32/api/oaidl/nf-oaidl-ienumvariant-reset) will return to the beginning of the collection in the underlying store. **IEnumVARIANT::Next** and **IEnumVARIANT::Reset** operations cannot retrieve deleted objects, because the objects are retrieved on-demand from the underlying directory service. Only the current object is cached; if the current object is deleted, the client will not become aware of its deletion from the underlying directory service until a [**IADs::GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo) or [**IADs::SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) attempts to access the object.

Regardless of the caching model, be aware that ADSI enumeration returns Active Directory service interfaces to the caller. To avoid the overhead of obtaining a new interface pointer, ADSI applications should cache the returned interface pointers for objects that they intend to manipulate. For example, a Visual Basic application that enumerates a container and populates a list box with names can cache the interface pointers associated with the names for later use. This approach will provide greater performance than populating the list box during enumeration and obtaining a new interface pointer when the user makes a selection.

## About Dispatch IDs

[**IDispatch**](/previous-versions/windows/desktop/automat/implementing-the-idispatch-interface) is an Automation interface defined by COM for controllers that do not use COM interfaces directly. Accessing an object through **IDispatch** is called name-bound or late-bound access, because it occurs at run time ("late") and uses string names of properties and methods to resolve references ("name"). At run time, clients pass the string name of the property or method they wish to call into the [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames)() method. If the property or method exists on the object, the dispatch identifier (dispID) of the corresponding function is retrieved. The dispID is then used to execute the function through [**IDispatch::Invoke**](/windows/win32/api/oaidl/nf-oaidl-idispatch-invoke)(). Using **IDispatch**, properties and methods on the interfaces exposed by a single object appear as a flat list. Because name-bound access requires two function calls, it is less efficient than using a COM interface directly. Clients are encouraged to use the ADSI COM interfaces on the objects when performance is a consideration. Advanced Automation controllers such as Visual Basic 4.0 can call other COM interfaces as well as **IDispatch**, if the interfaces comply with the Automation constraints for data types and parameter passing.

ADSI providers generate dispIDs dynamically for each Active Directory object. The dispIDs retrieved through [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames) for a given object are the generated values, but not the values that are in the IDL for the object. [**IDispatch**](/previous-versions/windows/desktop/automat/implementing-the-idispatch-interface) users must call **GetIDsOfNames** to obtain valid dispIDs at run time.

## Type Information and Type Libraries

The ADSI SDK supplies a type library, Activeds.tlb, that documents all the standard interfaces supported by ADSI. A provider must supply a similar type library for all interfaces found in Activeds.tlb, plus any additional type data for the interfaces implemented within the provider component.

The following is an IDL code example.

``` syntax
[ object, uuid(IID_IADsXYZ), oleautomation, dual ]
interface IADsXYZ: IDispatch
{
// Read-only properties.
[propget]
HRESULT AReadOnlyProp ([out, retval]BSTR *pbstrAReadOnlyProp);
 
// Read/write properties.
[propget]
HRESULT AReadWriteProp ([out, retval]long *plAReadWriteProp);
[propput]
HRESULT AReadWriteProp ([in]long lAReadWriteProp);
 
// Methods.
HRESULT AMethod ([in]DATE dateInParameter,
[out, retval]BSTR *pbstrReturnValue);
};
```

## Thread Safety

The Component Object Model (COM) describes the following three threading models. COM applications indicate which model is in use when initializing the COM library using the [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) and [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) functions:

-   Single threading. The single threaded model assumes a single thread of execution in a process, further assuming that COM data structures in a process need no access serialization.
-   Apartment threading. A COM object is associated with the thread that created it. Calls to an object on another thread must be executed by the thread that created that object. To accomplish this, the source thread invokes a client proxy which arranges the method call and delivers it to a server stub function in the destination thread through the Win32 message queue associated with the destination thread.
-   Free threading. COM objects are assumed to be thread safe. Multiple threads are allowed access to any object in the process with no serialization imposed.

ADSI does not assume any particular threading model. Writers of provider components should assume the free threading model and guarantee the consistency of their internal data structures by protecting them from thread-unsafe, that is, uncoordinated, updates through the use of synchronization objects such as critical sections or semaphores.

## Object Locking

ADSI does not impose or define an object-locking scheme. Providers for namespaces that support access serialization using locking can expose the underlying locking scheme through provider-specific extensions to ADSI.

## Property Names Within a Schema

ADSI represents properties as property objects within the ADSI schema container. This requires that property names be unique within each schema container. The provider must ensure that there are no name collisions.

## Primary Interface

When a provider cannot identify which interface should be returned as the primary interface, **IID\_IADs** should be returned. This provides name-bound access to all properties of an object through [**IDispatch**](/previous-versions/windows/desktop/automat/implementing-the-idispatch-interface) and the [**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get), [**IADs::GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex), [**IADs::Put**](/windows/desktop/api/Iads/nf-iads-iads-put), and [**IADs::PutEx**](/windows/desktop/api/Iads/nf-iads-iads-putex) methods.

 

 