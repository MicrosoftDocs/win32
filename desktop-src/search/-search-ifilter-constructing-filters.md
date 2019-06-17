---
Description: It is important that you understand the required DLL structure of a filter handler (an implementation of the IFilter interface).
ms.assetid: a2b5a813-573a-44d3-8780-99603e3246c1
title: Implementing Filter Handlers in Windows Search
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Filter Handlers in Windows Search

It is important that you understand the required DLL structure of a filter handler (an implementation of the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface).

This topic is organized as follows:

- [Implementing and Exporting the DLL Entry Points](#implementing-and-exporting-the-dll-entry-points)
- [Implementing the IFilter Class and Class Factory](#implementing-the-ifilter-class-and-class-factory)
- [Inheriting the COM Interfaces](#inheriting-the-com-interfaces)
- [Implementing the COM Interface Methods](#implementing-the-com-interface-methods)
  - [COM Methods that are not Implemented](#com-methods-that-are-not-implemented)
- [Additional Resources](#additional-resources)
- [Related topics](#related-topics)

## Implementing and Exporting the DLL Entry Points

Each [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) DLL (denoted by Ifilter.dll in this section) must implement and export the following entry points. These entry points are typically exported using a module-definition (.def) file for the **IFilter** interface or by using the **\_\_declspec(dllexport)** keyword. The DLL file can be registered to be in any folder, but it usually resides in the %SystemRoot%\\system32 folder.

DLL entry points are listed and described in the following table.

| DLL name                                                                                     | DLL description                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DllRegisterServer](https://msdn.microsoft.com/en-us/library/ms682162(VS.85).aspx)            | The [DllRegisterServer](https://msdn.microsoft.com/en-us/library/ms682162(VS.85).aspx) entry point registers the DLL as a filter in the registry. You register the DLL by running the regsvr32.exe program with the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface DLL file name as an argument: `regsvr32.exe %SystemRoot%\system32\Ifilter.dll`                                              |
| [DllUnregisterServer Function](https://msdn.microsoft.com/en-us/library/ms691457(VS.85).aspx) | The [DllUnregisterServer Function](https://msdn.microsoft.com/en-us/library/ms691457(VS.85).aspx) entry point removes the DLL as a persistent handler in the registry. You unregister the DLL by running the regsvr32.exe program with the `/u` flag: `regsvr32.exe /u %SystemRoot%\system32\Ifilter.dll`                                                                                    |
| [DllGetClassObject Function](https://msdn.microsoft.com/en-us/library/ms680760(VS.85).aspx)   | The content indexing client calls the [DllGetClassObject Function](https://msdn.microsoft.com/en-us/library/ms680760(VS.85).aspx) entry point, through Component Object Model (COM), to create a class factory object for the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface and to get a pointer to the class factory interface of that object.                                               |
| [DllCanUnloadNow Function](https://msdn.microsoft.com/en-us/library/ms690368(VS.85).aspx)     | The content-indexing client calls the [DllCanUnloadNow Function](https://msdn.microsoft.com/en-us/library/ms690368(VS.85).aspx) entry point, through COM, to determine whether it is possible to unload the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx)  DLL. The **IFilter** interface is unloaded after it is unused for an interval of time, as specified by the FilterIdleTimeOut registry value. |

## Implementing the IFilter Class and Class Factory

At least two classes, such as CFilter and CFilterCF, are typically implemented by each [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) DLL. The CFilter class produces the **IFilter** interface object that implements the content-filtering functionality. Its member functions implement the interface methods of the **IFilter** interface. Each **IFilter** class requires a unique class identifier (CLSID), which the **IFilter** interface implementer generates.

The CFilterCF class produces the class-factory object for the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface. The class factory is called, through its [IClassFactory Interface](https://msdn.microsoft.com/en-us/library/ms694364(VS.85).aspx) interface, by the [DllGetClassObject Function](https://msdn.microsoft.com/en-us/library/ms680760(VS.85).aspx) entry point of the DLL. The CFilterCF class creates the CFilter object and returns a pointer to [IUnknown](https://msdn.microsoft.com/en-us/library/ms680509(VS.85).aspx). In more complex cases, an **IFilter** can implement a class hierarchy in place of the single CFilter class.

## Inheriting the COM Interfaces

Windows Search 3.0 and later require that you use [IPersistStream](https://msdn.microsoft.com/en-us/library/ms690091(VS.85).aspx) for the following reasons:

- To ensure performance and future compatibility.
- To help increase security. IFilters implemented with [IPersistStream](https://msdn.microsoft.com/en-us/library/ms690091(VS.85).aspx) are more secure because the context in which the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface runs does not need the rights to open files on the disk or over the network.
- While Windows Search uses only [IPersistStream](https://msdn.microsoft.com/en-us/library/ms690091(VS.85).aspx), the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface class can also inherit the [IPersistFile Interface](https://msdn.microsoft.com/en-us/library/ms687223(VS.85).aspx) and/or [IPersistStorage Interface](https://msdn.microsoft.com/en-us/library/ms679731(VS.85).aspx) interface implementations for backward compatibility.

These interfaces are declared in files included from the mssdk\\include directory and have pre-defined interface identifiers (IIDs). The content-indexing client queries the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface through [IUnknown](https://msdn.microsoft.com/en-us/library/ms680509(VS.85).aspx) to determine which of these interfaces to use when filtering content.

## Implementing the COM Interface Methods

The [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface implements the [IUnknown](https://msdn.microsoft.com/en-us/library/ms680509(VS.85).aspx) methods for both the **IFilter** interface class and the **IFilter** interface-class factory. The following table lists, in vtable order, the **IFilter** interface-specific interfaces and methods that the **IFilter** interface should implement. The **IFilter** interface must implement at least [IPersistStream](https://msdn.microsoft.com/en-us/library/ms690091(VS.85).aspx), but can implement additional IPersist-derived interfaces.

| COM interface                                                                             | Method                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IClassFactory Interface](https://msdn.microsoft.com/en-us/library/ms694364(VS.85).aspx)   | CreateInstance, LockServer                                                                                                                                                                                                                                                     |
| [IClassFactory2 Interface](https://msdn.microsoft.com/en-us/library/ms692720(VS.85).aspx)  | GetLicInfo, RequestLicKey, CreateInstanceLic                                                                                                                                                                                                                                   |
| [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx)                                                        | [**IFilter::Init**](https://msdn.microsoft.com/library/Bb266452(v=VS.85).aspx), [**IFilter::GetChunk**](https://msdn.microsoft.com/library/Bb266448(v=VS.85).aspx), [**IFilter::GetText**](https://msdn.microsoft.com/library/Bb266449(v=VS.85).aspx), [**IFilter::GetValue**](https://msdn.microsoft.com/library/Bb266450(v=VS.85).aspx), [**IFilter::BindRegion**](https://msdn.microsoft.com/library/Bb266447(v=VS.85).aspx) |
| [IPersist Interface](https://docs.microsoft.com/windows/desktop/api/objidl/nn-objidl-ipersist)               | GetClassID                                                                                                                                                                                                                                                                     |
| [IPersistFile Interface](https://msdn.microsoft.com/en-us/library/ms687223(VS.85).aspx)    | IsDirty, Load, Save, SaveCompleted, GetCurFile                                                                                                                                                                                                                                 |
| [IPersistStorage Interface](https://msdn.microsoft.com/en-us/library/ms679731(VS.85).aspx) | IsDirty, Load, Save, GetSizeMax                                                                                                                                                                                                                                                |
| [IPersistStream](https://msdn.microsoft.com/en-us/library/ms690091(VS.85).aspx)            | IsDirty, Load, Save, GetSizeMax                                                                                                                                                                                                                                                |

The reference page for each method specifies the parameters and functional behavior for that method. Each reference page also gives the result codes to implement for that method. The reference pages for the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) methods give the interface-specific [Codes in FACILITY\_ITF](https://msdn.microsoft.com/en-us/library/ms679751(VS.85).aspx) result codes to be implemented, and the content-indexing client can also handle any of the generic result codes, such as FACILITY\_NULL and FACILITY\_WIN32. For more information, see [Structure of COM Error Codes](https://msdn.microsoft.com/en-us/library/ms690088(VS.85).aspx).

### COM Methods that are not Implemented

The [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface must implement at least [IPersistStream](https://msdn.microsoft.com/en-us/library/ms690091(VS.85).aspx), but does not need to implement additional IPersist-derived interfaces.

Windows Search does not need to implement the COM methods listed in the following table.

| Method that is not required                               | Description                       |
|-----------------------------------------------------------|-----------------------------------|
| IPersistStream::IsDirty                                   | Filters should return E\_NOTIMPL. |
| IPersistStream::Save                                      | Filters should return E\_NOTIMPL. |
| IPersistStream::GetSizeMax                                | Filters should return E\_NOTIMPL. |
| [**IFilter::BindRegion**](https://msdn.microsoft.com/library/Bb266447(v=VS.85).aspx) | Filters should return E\_NOTIMPL. |

## Additional Resources

- The [IFilterSample](-search-sample-ifiltersample.md) code sample, available on [GitHub](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/IFilterSample), demonstrates how to create an IFilter base class for implementing the [**IFilter**](https://msdn.microsoft.com/library/Bb266451(v=VS.85).aspx) interface.
- For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
- For an overview of file types, see [File Types](https://msdn.microsoft.com/en-us/library/cc144148(VS.85).aspx).
- To query file association attributes for a file type, see [PerceivedTypes, SystemFileAssociations, and Application Registration](https://msdn.microsoft.com/en-us/library/cc144150(VS.85).aspx).

## Related topics

[Developing Filter Handlers](-search-ifilter-conceptual.md)

[Understanding Filter Handlers in Windows Search](-search-ifilter-about.md)

[Best Practices for Creating Filter Handlers in Windows Search](-search-3x-wds-extidx-filters.md)

[Returning Properties from a Filter Handler](-search-ifilter-property-filtering.md)

[Filter Handlers that Ship with Windows](-search-ifilter-implementations.md)

[Registering Filter Handlers](-search-ifilter-registering-filters.md)

[Testing Filter Handlers](-search-ifilter-testing-filters.md)
