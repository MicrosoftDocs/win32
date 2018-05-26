---
Description: The CMediaControl class provides base class handling of the IDispatch methods of the dual-interface IMediaControl. It leaves as pure virtual the properties and methods of the IMediaControl interface.
ms.assetid: 033a2de6-8046-408c-995f-ec2de6654c41
title: CMediaControl class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaControl class

![cmediacontrol class hierarchy](images/cutil02.png)

The `CMediaControl` class provides base class handling of the [**IDispatch**](https://msdn.microsoft.com/library/windows/desktop/ms221608) methods of the dual-interface [**IMediaControl**](/windows/win32/Control/nn-control-imediacontrol?branch=master). It leaves as pure virtual the properties and methods of the **IMediaControl** interface.

Typically, the filter graph manager is the only object that implements the [**IMediaControl**](/windows/win32/Control/nn-control-imediacontrol?branch=master) interface. (filters implement the [**IMediaFilter**](/windows/win32/Strmif/nn-strmif-imediafilter?branch=master) interface, inherited by [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), to receive control commands from the filter graph manager.) Therefore, this class library is of limited use to filter developers.

The [**CMediaControl::GetIDsOfNames**](cmediacontrol-getidsofnames.md), [**CMediaControl::GetTypeInfo**](cmediacontrol-gettypeinfo.md), [**CMediaControl::GetTypeInfoCount**](cmediacontrol-gettypeinfocount.md), and [**CMediaControl::Invoke**](cmediacontrol-invoke.md) member functions are standard implementations of the [**IDispatch**](https://msdn.microsoft.com/library/windows/desktop/ms221608) methods using the [**CBaseDispatch**](cbasedispatch.md) class (and a type library) to parse the commands and pass them to the pure virtual methods of the [**IMediaControl**](/windows/win32/Control/nn-control-imediacontrol?branch=master) interface.

The [**IMediaControl**](/windows/win32/Control/nn-control-imediacontrol?branch=master) methods, defined in control.odl, are left as pure virtual.



| Member Functions                                           | Description                                                                                                                                                                                                                             |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CMediaControl**](cmediacontrol-cmediacontrol.md)       | Constructs a **CMediaControl** object.                                                                                                                                                                                                  |
| IDispatch Methods                                          | Description                                                                                                                                                                                                                             |
| [**GetIDsOfNames**](cmediacontrol-getidsofnames.md)       | Maps a single member and an optional set of parameters to a corresponding set of integer dispatch identifiers (DISPIDs), which can be used during subsequent calls to the [**CMediaControl::Invoke**](cmediacontrol-invoke.md) method. |
| [**GetTypeInfo**](cmediacontrol-gettypeinfo.md)           | Retrieves a type-information object, which can retrieve the type information for an interface.                                                                                                                                          |
| [**GetTypeInfoCount**](cmediacontrol-gettypeinfocount.md) | Retrieves the number of type-information interfaces provided by an object.                                                                                                                                                              |
| [**Invoke**](cmediacontrol-invoke.md)                     | Provides access to properties and methods exposed by an object.                                                                                                                                                                         |



 

 

 



