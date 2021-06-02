---
description: Defines the ServiceID and Types elements for the service host.
ms.assetid: 95066c04-5bdc-4c97-98b8-1da9928d9395
title: host element
ms.topic: reference
ms.date: 05/31/2018
---

# host element

Defines the [**ServiceID**](serviceid.md) and [**Types**](types.md) elements for the service host.

## Usage

``` syntax
<host>
  child elements
</host>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| [**ServiceID**](serviceid.md)<br/> | Defines the service identifier for the service host.<br/> <br/> |
| [**Types**](types.md)<br/>         | Defines a list of XSD qualified names.<br/> <br/>               |



### Child element sequence

``` syntax
(
  ServiceID, 
  Types
)
```

## Parent elements



| Element                                         | Description                                                                   |
|-------------------------------------------------|-------------------------------------------------------------------------------|
| [**hostMetadata**](hostmetadata.md)<br/> | The hosting metadata for the device to be implemented.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




