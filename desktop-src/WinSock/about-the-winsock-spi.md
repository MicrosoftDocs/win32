---
description: Winsock provides a Service Provider Interface for creating Winsock services, commonly referred to as the Winsock SPI.
ms.assetid: e3d21dd8-2b58-4108-857d-a075b8be68b0
title: About the Winsock SPI
ms.topic: article
ms.date: 05/31/2018
---

# About the Winsock SPI

Winsock provides a Service Provider Interface for creating Winsock services, commonly referred to as the Winsock SPI. Two types of service providers exist: transport providers and namespace providers. Examples of transport providers include protocol stacks such as TCP/IP or IPX/SPX, while an example of a namespace provider would be an interface to the Internet's Domain Naming System (DNS). Separate sections of the service provider interface specification apply to each type of service provider.

[Transport](transport-service-providers-2.md) and [namespace](name-space-service-providers-2.md) service providers must be registered with the Ws2\_32.dll at the time they are installed. This registration need only be done once for each provider as the necessary information is retained in persistent storage.

 

 



