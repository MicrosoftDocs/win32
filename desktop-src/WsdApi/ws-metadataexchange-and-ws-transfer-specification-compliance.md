---
description: Before August 2006, WS-MetadataExchange defined its own Get metadata exchange method, which was used by Devices Profile for Web Services (DPWS).
ms.assetid: 2441beac-ee40-405a-8e98-8b8d65477911
title: WS-MetadataExchange and WS-Transfer Specification Compliance
ms.topic: article
ms.date: 05/31/2018
---

# WS-MetadataExchange and WS-Transfer Specification Compliance

Before August 2006, [WS-MetadataExchange](https://schemas.xmlsoap.org/ws/2004/09/mex/) defined its own [Get](get--metadata-exchange--http-request-and-message.md) metadata exchange method, which was used by [Devices Profile for Web Services](https://specs.xmlsoap.org/ws/2006/02/devprof/) (DPWS). The WS-MetadataExchange specification version 1.1 replaced this method with the Get method defined in the WS-Transfer specification.

In the current model, WS-Transfer provides the [Get](get--metadata-exchange--http-request-and-message.md) method and makes no reference to the type of the body. WS-MetadataExchange describes the format of the body and a mechanism for packaging multiple pieces of metadata in a single response, and DPWS describes specific pieces of metadata that a service should include in a metadata response.

WSDAPI does not fully support the WS-Transfer specification. Because only the [Get](get--metadata-exchange--http-request-and-message.md) method is required for devices, no other portions of WS-Transfer have been implemented. Also, WSDAPI does not implement the optional GetMetadata method described in WS-MetadataExchange.

 

 



