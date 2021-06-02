---
description: Controller Port Object
ms.assetid: 5f94bcdc-93ab-4522-88bd-009a049b5dc9
title: Controller Port Object
ms.topic: article
ms.date: 05/31/2018
---

# Controller Port Object

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

A controller port object models a controller port in a subsystem. Host computers can write to and read from LUNs through controller ports. Controller ports are contained by controllers in a subsystem. In VDS 1.1 and VDS2.0, each of a subsystem's controller ports is set to either active or inactive in relation to each of the LUNs the subsystem surfaces. A single controller port, then, can be simultaneously set to active for one LUN and inactive for others. A controller port that is active for a given LUN carries responsibility for handling input to and output from the LUN.

Active controller ports serve as one of the endpoints of MPIO paths in Fibre Channel hardware providers, upon which load balancing policies can be imposed.

Use the [**IVdsControllerControllerPort::QueryControllerPorts**](/windows/desktop/api/Vds/nf-vds-ivdscontrollercontrollerport-querycontrollerports) method to determine the controller ports that are contained by a specific controller. Callers can get a pointer to a specific controller port by selecting the desired controller port object from the enumeration that is returned by the **QueryControllerPorts** method. With a controller object, a caller can set the controller port status and query for its associated LUNs.

Controller object properties include an object identifier, a name, a serial number, and the controller port status.

The following table lists related interfaces, enumerations, and structures.



| Type                                                                                              | Element                                                                                               |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object in VDS 1.1 and 2.0 Fibre Channel providers only | [**IVdsControllerPort**](/windows/desktop/api/Vds/nn-vds-ivdscontrollerport)                                                      |
| Associated enumerations                                                                           | [**VDS\_PORT\_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_port_status)                                                          |
| Associated structures                                                                             | [**VDS\_PORT\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_port_prop) and [**VDS\_PORT\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_port_notification) |



 

## Related topics

<dl> <dt>

[Hardware Provider Objects](hardware-provider-objects.md)
</dt> <dt>

[**IVdsControllerControllerPort::QueryControllerPorts**](/windows/desktop/api/Vds/nf-vds-ivdscontrollercontrollerport-querycontrollerports)
</dt> </dl>

 

 
