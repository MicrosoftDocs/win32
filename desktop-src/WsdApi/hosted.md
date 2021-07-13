---
description: Defines the ServiceID, Types,PnPXHardwareId, and PnPXCompatibleId elements for the services defined by the service host.
ms.assetid: f901a88f-7e01-4e7f-a0f2-59f2a01b03cd
title: hosted element
ms.topic: reference
ms.date: 05/31/2018
---

# hosted element

Defines the [**ServiceID**](serviceid.md), [**Types**](types.md),[**PnPXHardwareId**](pnpxhardwareid.md), and [**PnPXCompatibleId**](pnpxcompatibleid.md) elements for the services defined by the service host.

## Usage

``` syntax
<hosted>
  child elements
</hosted>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                      |
|---------------------------------------------------------|----------------------------------------------------------------------------------|
| [**PnPXCompatibleId**](pnpxcompatibleid.md)<br/> | Specifies the PnP-X Compatible Identifier of the service.<br/> <br/> |
| [**PnPXHardwareId**](pnpxhardwareid.md)<br/>     | Specifies the PnP-X Hardware Identifier of the service.<br/> <br/>   |
| [**ServiceID**](serviceid.md)<br/>               | Defines a service identifier for the service host.<br/> <br/>        |
| [**Types**](types.md)<br/>                       | Defines a list of XSD qualified names.<br/> <br/>                    |



### Child element sequence

``` syntax
(
  ServiceID, 
  Types, 
  PnPXHardwareId?, 
  PnPXCompatibleId?
)
```

## Parent elements



| Element                                         | Description                                                                   |
|-------------------------------------------------|-------------------------------------------------------------------------------|
| [**hostMetadata**](hostmetadata.md)<br/> | The hosting metadata for the device to be implemented.<br/> <br/> |



## Remarks

Each service provided by a service host should have its own **hosted** element information to ensure that the service is published properly in responses to metadata requests.

The [**PnPXHardwareId**](pnpxhardwareid.md) and [**PnPXCompatibleId**](pnpxcompatibleid.md) elements are optional, but when used, they must be used together. If one is present, the other must be present as well.

If a [**PnPXDeviceCategory**](pnpxdevicecategory.md) element is present, then at least one **hosted** element must contain both [**PnPXHardwareId**](pnpxhardwareid.md) and [**PnPXCompatibleId**](pnpxcompatibleid.md) elements. Similarly, if **PnPXHardwareId** and **PnPXCompatibleId** elements are present in a **hosted** element, at least one **PnPXDeviceCategory** element must be present inside the [**thisModelMetadata**](thismodelmetadata.md) element.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




