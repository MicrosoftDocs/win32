---
description: 'VDS provides two helper objects: the enumeration object and the async object. This topic describes each of these objects and provides links to examples of how callers work with each.'
ms.assetid: 0f809c71-a3bd-4c62-8086-9651ea1a3400
title: Helper Objects
ms.topic: article
ms.date: 05/31/2018
---

# Helper Objects

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

VDS provides two helper objects: the enumeration object and the async object. This topic describes each of these objects and provides links to examples of how callers work with each.

## Enumeration Object

An enumeration object enumerates through a set of VDS objects of a given type. Objects can be providers, subsystems, controllers, LUNs, LUN plexes, drives, disk packs, disks, volumes, or volume plexes. Callers can get a pointer to a specific object by selecting the desired object from the enumeration that is returned by the appropriate method. For a code example, see [Working with Enumeration Objects](working-with-enumeration-objects.md).

The following table lists related interfaces, enumerations, and structures. 

| Type                                              | Element                                  |
|---------------------------------------------------|------------------------------------------|
| Interfaces that are always exposed by this object | [**IEnumVdsObject**](/windows/desktop/api/Vds/nn-vds-ienumvdsobject) |
| Associated enumerations                           | None.                                    |
| Associated structures                             | None.                                    |



 

## Async Object

An async object manages asynchronous operations. Methods that initiate asynchronous operations return a pointer to an [**IVdsAsync**](/windows/desktop/api/Vds/nn-vds-ivdsasync) interface, which allows the caller to cancel, wait for, and query the status of the asynchronous operation.

Long-running VDS operations tend to be implemented asynchronously. The basic and dynamic software provider programs implement asynchronous methods consistently for volume, partition, and disk operations. Hardware providers optionally implement async-related methods asynchronously. Regardless of how the provider implements the method, the operation must return a pointer to an [**IVdsAsync**](/windows/desktop/api/Vds/nn-vds-ivdsasync) interface to the caller. For a code example, see [Managing Asynchronous Operations](managing-asynchronous-operations.md).

Asynchronous operations include:

-   Creating a LUN, volume, or partition.
-   Formatting a volume or partition.
-   Adding or removing a LUN or volume plex.
-   Breaking a volume plex.
-   Extending or shrinking a LUN or volume.
-   Recovering a LUN or volume.
-   Cleaning a disk.
-   Replacing a disk.

The following table lists related interfaces, enumerations, and structures. 

| Type                                              | Element                        |
|---------------------------------------------------|--------------------------------|
| Interfaces that are always exposed by this object | [**IVdsAsync**](/windows/desktop/api/Vds/nn-vds-ivdsasync) |
| Associated enumerations                           | None.                          |
| Associated structures                             | None.                          |



 

## Related topics

<dl> <dt>

[VDS Object Model](vds-object-model.md)
</dt> <dt>

[**IVdsAsync**](/windows/desktop/api/Vds/nn-vds-ivdsasync)
</dt> <dt>

[Working with Enumeration Objects](working-with-enumeration-objects.md)
</dt> <dt>

[Managing Asynchronous Operations](managing-asynchronous-operations.md)
</dt> </dl>

 

 
