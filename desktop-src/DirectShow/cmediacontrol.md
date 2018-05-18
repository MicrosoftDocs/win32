---
Description: 'The CMediaControl class provides base class handling of the IDispatch methods of the dual-interface IMediaControl. It leaves as pure virtual the properties and methods of the IMediaControl interface.'
ms.assetid: '033a2de6-8046-408c-995f-ec2de6654c41'
title: CMediaControl class
---

# CMediaControl class

![cmediacontrol class hierarchy](images/cutil02.png)

The `CMediaControl` class provides base class handling of the [**IDispatch**](https://msdn.microsoft.com/library/windows/desktop/ms221608) methods of the dual-interface [**IMediaControl**](imediacontrol.md). It leaves as pure virtual the properties and methods of the **IMediaControl** interface.

Typically, the filter graph manager is the only object that implements the [**IMediaControl**](imediacontrol.md) interface. (filters implement the [**IMediaFilter**](imediafilter.md) interface, inherited by [**IBaseFilter**](ibasefilter.md), to receive control commands from the filter graph manager.) Therefore, this class library is of limited use to filter developers.

The [**CMediaControl::GetIDsOfNames**](cmediacontrol-getidsofnames.md), [**CMediaControl::GetTypeInfo**](cmediacontrol-gettypeinfo.md), [**CMediaControl::GetTypeInfoCount**](cmediacontrol-gettypeinfocount.md), and [**CMediaControl::Invoke**](cmediacontrol-invoke.md) member functions are standard implementations of the [**IDispatch**](https://msdn.microsoft.com/library/windows/desktop/ms221608) methods using the [**CBaseDispatch**](cbasedispatch.md) class (and a type library) to parse the commands and pass them to the pure virtual methods of the [**IMediaControl**](imediacontrol.md) interface.

The [**IMediaControl**](imediacontrol.md) methods, defined in control.odl, are left as pure virtual.



| Member Functions                                           | Description                                                                                                                                                                                                                             |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CMediaControl**](cmediacontrol-cmediacontrol.md)       | Constructs a **CMediaControl** object.                                                                                                                                                                                                  |
| IDispatch Methods                                          | Description                                                                                                                                                                                                                             |
| [**GetIDsOfNames**](cmediacontrol-getidsofnames.md)       | Maps a single member and an optional set of parameters to a corresponding set of integer dispatch identifiers (DISPIDs), which can be used during subsequent calls to the [**CMediaControl::Invoke**](cmediacontrol-invoke.md) method. |
| [**GetTypeInfo**](cmediacontrol-gettypeinfo.md)           | Retrieves a type-information object, which can retrieve the type information for an interface.                                                                                                                                          |
| [**GetTypeInfoCount**](cmediacontrol-gettypeinfocount.md) | Retrieves the number of type-information interfaces provided by an object.                                                                                                                                                              |
| [**Invoke**](cmediacontrol-invoke.md)                     | Provides access to properties and methods exposed by an object.                                                                                                                                                                         |



 

 

 



