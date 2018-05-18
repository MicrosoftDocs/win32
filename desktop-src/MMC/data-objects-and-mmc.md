---
title: Data Objects and MMC 2.0
description: Describes the process of data transfer within MMC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '11aa3e0f-28c3-4d06-97b2-ce644c2d2c14'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["data objects and MMC 2.0"]
---

# Data Objects and MMC 2.0

Data transfer within MMC is accomplished using the COM interface [**IDataObject**](_ole_idataobject), which snap-ins implement. The actual data is shared in [clipboard formats](clipboard-formats.md). The **IDataObject** interface includes methods that enable data to be transferred and notifications to be generated when data changes.

MMC uses the [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) and [**IDataObject::GetData**](_ole_idataobject_getdata) methods to get data from scope and result items. The [**IDataObject**](_ole_idataobject) interface and its methods are documented in the Platform Software Development Kit (SDK).

All data that is transferred resides in global memory, so the [**TYMED**](_ole_tymed) identifier of the [**STGMEDIUM**](_ole_stgmedium) structure passed to a data object in the [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) method is always an HGLOBAL.

MMC frequently requests snap-ins to provide data objects by calling their [**IComponentData::QueryDataObject**](icomponentdata-querydataobject.md) or [**IComponent::QueryDataObject**](icomponent-querydataobject.md) method. For this reason, snap-in developers should ensure that this is an efficient operation.

One technique for improving efficiency is to implement a pool of data objects that can be used more than once to fulfill common MMC data requests. These data objects exist for the lifetime of a snap-in instance. When MMC requests data that be provided by one of these data objects, the snap-in supplies that data object to MMC and increments its reference count. This technique is based on the fact that data objects are COM objects; MMC simply releases its interface to a data object after it is no longer required.

The following sequence diagram written in UML(Unified Modeling Language) illustrates the general method by which MMC requests a data object from a snap-in. In the diagram, MMC calls the data object's [**GetDataHere**](_ole_idataobject_getdatahere) method to request data in a specific clipboard format.

![mmc requesting a data object from a snap-in](images/data-objects.png)

In the scenario depicted in the diagram, MMC calls the [**QueryDataObject**](icomponentdata-querydataobject.md) method of CComponentData, which implements the MMC interface [**IComponentData**](icomponentdata.md). One of the arguments of **QueryDataObject** is the [cookie](cookies.md) value of the node for which MMC is requesting data. CComponentData creates a data object and passes the cookie to it. MMC then calls the [**GetDataHere**](_ole_idataobject_getdatahere) method of the data object and specifies the required clipboard format in which the data object should render the requested data. The data object in the diagram delegates the data rendering to a delegation base. This is the preferred implementation.

The data object then writes the requested data back into the stream created by using the *HGlobal* handle provided to it by MMC in [**GetDataHere**](_ole_idataobject_getdatahere). After using the data and at an appropriate time, MMC releases the interface pointer to the data object with a call to the object's [**Release**](_com_iunknown_release) method.

 

 




