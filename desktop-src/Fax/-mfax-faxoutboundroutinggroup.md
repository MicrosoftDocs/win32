---
Description: The FaxOutboundRoutingGroup configuration object is used by a fax client application to retrieve information about an individual fax outbound routing group.
ms.assetid: 894a58b7-3a5f-4723-abcb-764567e49e76
title: FaxOutboundRoutingGroup object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingGroup object

The **FaxOutboundRoutingGroup** configuration object is used by a fax client application to retrieve information about an individual fax outbound routing group. The object also includes a method to retrieve the ordered collection of device IDs ([**FaxDeviceIds**](-mfax-faxdeviceids.md) object) that participate in the routing group. The order of the devices in the collection determines the relative order in which available devices send outgoing transmissions.

## Members

The **FaxOutboundRoutingGroup** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxOutboundRoutingGroup** object has these properties.



| Property                                                                | Access type          | Description                                                                                                                                                                                                                                                                                                          |
|:------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DeviceIds**](-mfax-faxoutboundroutinggroup-deviceids.md)<br/> | Read-only<br/> | The [**DeviceIds**](-mfax-faxoutboundroutinggroup-deviceids.md) property retrieves the ordered collection of device IDs that participate in the outbound routing group. The order of the devices in the collection determines the relative order in which available devices send outgoing transmissions.<br/> |
| [**Name**](-mfax-faxoutboundroutinggroup-name-vb.md)<br/>        | Read-only<br/> | The [**Name**](-mfax-faxoutboundroutinggroup-name-vb.md) property is a null-terminated string that specifies the name of the outbound routing group.<br/>                                                                                                                                                     |
| [**Status**](-mfax-faxoutboundroutinggroup-status-vb.md)<br/>    | Read-only<br/> | The [**Status**](-mfax-faxoutboundroutinggroup-status-vb.md) property indicates the collective status of the fax devices in the outbound routing group.<br/>                                                                                                                                                  |



 

## Remarks

A **FaxOutboundRoutingGroup** object is accessed through a [**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md) object.

![faxoutboundroutinggroups and faxoutboundroutinggroup objects](images/faxoutboundroutinggroup.png)

To create a **FaxOutboundRoutingGroup** object in Microsoft Visual Basic, call the [**Item**](-mfax-faxoutboundroutinggroups-item.md) property of the [**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md) object.

To create a **FaxOutboundRoutingGroup** object in C++, call the [**Item**](-mfax-faxoutboundroutinggroups-item.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxOutboundRoutingGroup<br/>                                               |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md)
</dt> </dl>

 

 




