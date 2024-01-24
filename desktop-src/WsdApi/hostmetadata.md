---
description: Defines the hosting metadata for the device to be implemented. This element is used for device implementations (hosts) only.
ms.assetid: ca7bc5ea-8ab2-4233-86d2-5b793021b8ee
title: hostMetadata element
ms.topic: reference
ms.date: 05/31/2018
---

# hostMetadata element

Defines the hosting metadata for the device to be implemented. This element is used for device implementations (hosts) only.

## Usage

``` syntax
<hostMetadata>
  child elements
</hostMetadata>
```

## Attributes

There are no attributes.

## Child elements



| Element                             | Description                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**host**](host.md)<br/>     | Defines the ServiceID and [**Types**](types.md) elements for the service host. If not provided explicitly, WSDAPI will not supply any default data in response to metadata requests.<br/> <br/>                                                                                                                                          |
| [**hosted**](hosted.md)<br/> | Defines the [**ServiceID**](serviceid.md) and [**Types**](types.md) elements for the services provided by this service host. Each service provided by this service host should have its own [**hosted**](hosted.md) element information to ensure that the service is published properly in responses to metadata requests.<br/> <br/> |



### Child element sequence

``` syntax
(
  host?, 
  hosted+
)
```

## Parent elements



| Element                                                         | Description                                                                   |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**relationshipMetadata**](relationshipmetadata.md)<br/> | Describes the host and hosted metadata for the device.<br/> <br/> |



## Remarks

The hosting metadata appears in this element in a form similar to the one specified in the device profile. **hostMetadata** is slightly different from the format described in the device profile in that the only reference property it supports is the service ID.

The [**relationshipMetadataDefinition**](relationshipmetadatadefinition.md) element is used subsequently to generate a C constant containing this information.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




