---
description: Windows Portable Devices supports the following event properties.
ms.assetid: 672b75ac-cd47-4212-a505-c220ecdf98e3
title: Event Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Event
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Event Properties

Windows Portable Devices supports the following event properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>VarType</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>WPD_EVENT_OPTION_IS_AUTOPLAY_EVENT</strong></td>
<td><strong>VT_BOOL</strong></td>
<td>Reserved for future use.</td>
</tr>
<tr class="even">
<td><strong>WPD_EVENT_OPTION_IS_BROADCAST_EVENT</strong></td>
<td><strong>VT_BOOL</strong></td>
<td>A Boolean value that specifies whether the event is broadcast to all clients.Clients can receive this event by registering their callback with <strong>IPortableDevice::Advise</strong>.<br/></td>
</tr>
<tr class="odd">
<td><strong>WPD_EVENT_PARAMETER_CHILD_HIERARCHY_CHANGED</strong></td>
<td><strong>VT_BOOL</strong></td>
<td>A Boolean value that specifies whether the child hierarchy for the object has changed.This parameter is used to notify the caller that some children for the specified object have been added or removed. Typically the hierarchy change is initiated on the device side. Clients may have to re-enumerate this folder's children to keep their views up to date.<br/></td>
</tr>
<tr class="even">
<td><strong>WPD_EVENT_PARAMETER_EVENT_ID</strong></td>
<td><strong>VT_CLSID</strong></td>
<td>A value that identifies an event.</td>
</tr>
<tr class="odd">
<td><strong>WPD_EVENT_PARAMETER_OBJECT_CREATION_COOKIE</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>The cookie handed back to a client when it requests an object creation by calling the <a href="/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecontent-createobjectwithpropertiesanddata"><strong>IPortableDeviceContent::CreateObjectWithPropertiesAndData</strong></a> method.This parameter is added as a convenience to help the caller tie an object-added event to the request it sent to create the object. The driver hands this cookie back as the <strong>WPD_PROPERTY_OBJECT_MANAGEMENT_CONTEXT</strong> return value when processing the <strong>WPD_COMMAND_OBJECT_MANAGEMENT_CREATE_OBJECT_WITH_PROPERTIES_AND_DATA</strong> command.<br/></td>
</tr>
<tr class="even">
<td><strong>WPD_EVENT_PARAMETER_OBJECT_PARENT_PERSISTENT_UNIQUE_ID</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>A value that uniquely identifies the parent object. This property is similar to <strong>WPD_OBJECT_PARENT_ID</strong>, but this ID does not change between sessions.</td>
</tr>
<tr class="odd">
<td><strong>WPD_EVENT_PARAMETER_OPERATION_PROGRESS</strong></td>
<td><strong>VT_UI4</strong></td>
<td>A value that specifies the progress of a currently executing operation. The value of this property can range from 0 to 100, with 100 indicating that the operation is complete.</td>
</tr>
<tr class="even">
<td><strong>WPD_EVENT_PARAMETER_OPERATION_STATE</strong></td>
<td><strong>VT_UI4</strong></td>
<td>A value that indicates the current state of the operation, for example, started, running, stopped, and so on.This parameter's possible values are from the <strong>WPD_OPERATION_STATES</strong> enumeration defined in PortableDevice.h. Possible values are:<br/> <dl> <strong>WPD_OPERATION_STATE_UNSPECIFIED</strong><br />
<strong>WPD_OPERATION_STATE_STARTED</strong><br />
<strong>WPD_OPERATION_STATE_RUNNING</strong><br />
<strong>WPD_OPERATION_STATE_PAUSED</strong><br />
<strong>WPD_OPERATION_STATE_CANCELLED</strong><br />
<strong>WPD_OPERATION_STATE_FINISHED</strong><br />
<strong>WPD_OPERATION_STATE_ABORTED</strong><br />
</dl></td>
</tr>
<tr class="odd">
<td><strong>WPD_EVENT_PARAMETER_PNP_DEVICE_ID</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>A value that specifies the device that originated the event.This is the device or service identifier given by the Plug-and-Play (PnP) system, and is the same string used in the <strong>IPortableDevice::Open</strong>or <a href="/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservice-open"><strong>IPortableDeviceService::Open</strong></a> methods.<br/></td>
</tr>
<tr class="even">
<td><strong>WPD_EVENT_PARAMETER_SERVICE_METHOD_CONTEXT</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>A string that is used by a WPD driver to identify the operation of a device-service method. Applications should not use this parameter directly.</td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




