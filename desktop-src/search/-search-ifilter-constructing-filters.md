---
description: It is important that you understand the required DLL structure of a filter handler (an implementation of the IFilter interface).
ms.assetid: a2b5a813-573a-44d3-8780-99603e3246c1
title: Implementing Filter Handlers in Windows Search
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Filter Handlers in Windows Search

It is important that you understand the required DLL structure of a filter handler (an implementation of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface).

This topic is organized as follows:

- [Implementing and Exporting the DLL Entry Points](#implementing-and-exporting-the-dll-entry-points)
- [Implementing the IFilter Class and Class Factory](#implementing-the-ifilter-class-and-class-factory)
- [Inheriting the COM Interfaces](#inheriting-the-com-interfaces)
- [Implementing the COM Interface Methods](#implementing-the-com-interface-methods)
  - [COM Methods that are not Implemented](#com-methods-that-are-not-implemented)
- [Additional Resources](#additional-resources)
- [Related topics](#related-topics)

## Implementing and Exporting the DLL Entry Points

Each [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) DLL (denoted by Ifilter.dll in this section) must implement and export the following entry points. These entry points are typically exported using a module-definition (.def) file for the **IFilter** interface or by using the **\_\_declspec(dllexport)** keyword. The DLL file can be registered to be in any folder, but it usually resides in the %SystemRoot%\\system32 folder.

DLL entry points are listed and described in the following table.

| DLL name                                                                                     | DLL description                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DllRegisterServer](/windows/win32/api/olectl/nf-olectl-dllregisterserver)            | The [DllRegisterServer](/windows/win32/api/olectl/nf-olectl-dllregisterserver) entry point registers the DLL as a filter in the registry. You register the DLL by running the regsvr32.exe program with the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface DLL file name as an argument: `regsvr32.exe %SystemRoot%\system32\Ifilter.dll`                                              |
| [DllUnregisterServer Function](/windows/win32/api/olectl/nf-olectl-dllunregisterserver) | The [DllUnregisterServer Function](/windows/win32/api/olectl/nf-olectl-dllunregisterserver) entry point removes the DLL as a persistent handler in the registry. You unregister the DLL by running the regsvr32.exe program with the `/u` flag: `regsvr32.exe /u %SystemRoot%\system32\Ifilter.dll`                                                                                    |
| [DllGetClassObject Function](/windows/win32/api/combaseapi/nf-combaseapi-dllgetclassobject)   | The content indexing client calls the [DllGetClassObject Function](/windows/win32/api/combaseapi/nf-combaseapi-dllgetclassobject) entry point, through Component Object Model (COM), to create a class factory object for the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface and to get a pointer to the class factory interface of that object.                                               |
| [DllCanUnloadNow Function](/windows/win32/api/combaseapi/nf-combaseapi-dllcanunloadnow)     | The content-indexing client calls the [DllCanUnloadNow Function](/windows/win32/api/combaseapi/nf-combaseapi-dllcanunloadnow) entry point, through COM, to determine whether it is possible to unload the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter)  DLL. The **IFilter** interface is unloaded after it is unused for an interval of time, as specified by the FilterIdleTimeOut registry value. |

## Implementing the IFilter Class and Class Factory

At least two classes, such as CFilter and CFilterCF, are typically implemented by each [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) DLL. The CFilter class produces the **IFilter** interface object that implements the content-filtering functionality. Its member functions implement the interface methods of the **IFilter** interface. Each **IFilter** class requires a unique class identifier (CLSID), which the **IFilter** interface implementer generates.

The CFilterCF class produces the class-factory object for the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface. The class factory is called, through its [IClassFactory Interface](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) interface, by the [DllGetClassObject Function](/windows/win32/api/combaseapi/nf-combaseapi-dllgetclassobject) entry point of the DLL. The CFilterCF class creates the CFilter object and returns a pointer to [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown). In more complex cases, an **IFilter** can implement a class hierarchy in place of the single CFilter class.

## Inheriting the COM Interfaces

Windows Search 3.0 and later require that you use [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream) for the following reasons:

- To ensure performance and future compatibility.
- To help increase security. IFilters implemented with [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream) are more secure because the context in which the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface runs does not need the rights to open files on the disk or over the network.
- While Windows Search uses only [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream), the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface class can also inherit the [IPersistFile Interface](/windows/win32/api/objidl/nn-objidl-ipersistfile) and/or [IPersistStorage Interface](/windows/win32/api/objidl/nn-objidl-ipersiststorage) interface implementations for backward compatibility.

These interfaces are declared in files included from the mssdk\\include directory and have pre-defined interface identifiers (IIDs). The content-indexing client queries the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface through [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) to determine which of these interfaces to use when filtering content.

## Implementing the COM Interface Methods

The [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface implements the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) methods for both the **IFilter** interface class and the **IFilter** interface-class factory. The following table lists, in vtable order, the **IFilter** interface-specific interfaces and methods that the **IFilter** interface should implement. The **IFilter** interface must implement at least [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream), but can implement additional IPersist-derived interfaces.

| COM interface                                                                             | Method                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IClassFactory Interface](/windows/win32/api/unknwn/nn-unknwn-iclassfactory)   | CreateInstance, LockServer                                                                                                                                                                                                                                                     |
| [IClassFactory2 Interface](/windows/win32/api/ocidl/nn-ocidl-iclassfactory2)  | GetLicInfo, RequestLicKey, CreateInstanceLic                                                                                                                                                                                                                                   |
| [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter)                                                        | [**IFilter::Init**](/windows/win32/api/filter/nf-filter-ifilter-init), [**IFilter::GetChunk**](/windows/win32/api/filter/nf-filter-ifilter-getchunk), [**IFilter::GetText**](/windows/win32/api/filter/nf-filter-ifilter-gettext), [**IFilter::GetValue**](/windows/win32/api/filter/nf-filter-ifilter-getvalue), [**IFilter::BindRegion**](/windows/win32/api/filter/nf-filter-ifilter-bindregion) |
| [IPersist Interface](/windows/desktop/api/objidl/nn-objidl-ipersist)               | GetClassID                                                                                                                                                                                                                                                                     |
| [IPersistFile Interface](/windows/win32/api/objidl/nn-objidl-ipersistfile)    | IsDirty, Load, Save, SaveCompleted, GetCurFile                                                                                                                                                                                                                                 |
| [IPersistStorage Interface](/windows/win32/api/objidl/nn-objidl-ipersiststorage) | IsDirty, Load, Save, GetSizeMax                                                                                                                                                                                                                                                |
| [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream)            | IsDirty, Load, Save, GetSizeMax                                                                                                                                                                                                                                                |

The reference page for each method specifies the parameters and functional behavior for that method. Each reference page also gives the result codes to implement for that method. The reference pages for the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) methods give the interface-specific [Codes in FACILITY\_ITF](../com/codes-in-facility-itf.md) result codes to be implemented, and the content-indexing client can also handle any of the generic result codes, such as FACILITY\_NULL and FACILITY\_WIN32. For more information, see [Structure of COM Error Codes](../com/structure-of-com-error-codes.md).

### COM Methods that are not Implemented

The [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface must implement at least [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream), but does not need to implement additional IPersist-derived interfaces.

Windows Search does not need to implement the COM methods listed in the following table.

| Method that is not required                               | Description                       |
|-----------------------------------------------------------|-----------------------------------|
| IPersistStream::IsDirty                                   | Filters should return E\_NOTIMPL. |
| IPersistStream::Save                                      | Filters should return E\_NOTIMPL. |
| IPersistStream::GetSizeMax                                | Filters should return E\_NOTIMPL. |
| [**IFilter::BindRegion**](/windows/win32/api/filter/nf-filter-ifilter-bindregion) | Filters should return E\_NOTIMPL. |

## Additional Resources

- The [IFilterSample](-search-sample-ifiltersample.md) code sample, available on [GitHub](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/IFilterSample), demonstrates how to create an IFilter base class for implementing the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface.
- For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
- For an overview of file types, see [File Types](../shell/fa-file-types.md).
- To query file association attributes for a file type, see [PerceivedTypes, SystemFileAssociations, and Application Registration](/previous-versions/windows/desktop/legacy/cc144150(v=vs.85)).

## Related topics

[Developing Filter Handlers](-search-ifilter-conceptual.md)

[Understanding Filter Handlers in Windows Search](-search-ifilter-about.md)

[Best Practices for Creating Filter Handlers in Windows Search](-search-3x-wds-extidx-filters.md)

[Returning Properties from a Filter Handler](-search-ifilter-property-filtering.md)

[Filter Handlers that Ship with Windows](-search-ifilter-implementations.md)

[Registering Filter Handlers](-search-ifilter-registering-filters.md)

[Testing Filter Handlers](-search-ifilter-testing-filters.md)
