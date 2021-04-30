---
description: A URI that represents the service identifier.
ms.assetid: ef676f02-56a7-4b3a-9ca3-e7fa3c494ec7
title: ServiceID element
ms.topic: reference
ms.date: 05/31/2018
---

# ServiceID element

A URI that represents the service identifier.

## Usage

``` syntax
<ServiceID/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                             | Description                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**host**](host.md)<br/>     | Defines the **ServiceID** and [**Types**](types.md) elements for the service host. If not provided explicitly, WSDAPI will not supply any default data in response to metadata requests.<br/> <br/>                                                                                                                     |
| [**hosted**](hosted.md)<br/> | Defines the **ServiceID** and [**Types**](types.md) elements for the services provided by this service host. Each service provided by this service host should have its own [**hosted**](hosted.md) element information to ensure that the service is published properly in responses to metadata requests.<br/> <br/> |



## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




