---
title: Obtaining Service and User SDOs
description: To obtain SDOs for NPS (IAS) or a particular user, call the ISdoMachine GetServiceSDO or ISdoMachine GetUserSDO methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 23e23fb3-0102-4c36-b30f-18604131ee32
ms.prod: windows-server-dev
ms.technology: network-policy-and-access-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Service and User SDOs

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008.

 

To obtain SDOs for NPS (IAS) or a particular user, call the [**ISdoMachine::GetServiceSDO**](https://msdn.microsoft.com/library/bb960661) or [**ISdoMachine::GetUserSDO**](https://msdn.microsoft.com/library/bb960662) methods. These methods return pointers to [**IUnknown**](33f1d79a-33fc-4ce5-a372-e08bda378332) interfaces for these objects. For the user SDO, use the [**IUnknown::QueryInterface**](54d5ff80-18db-43f2-b636-f93ac053146d) method to obtain an [**ISdo**](https://msdn.microsoft.com/library/bb960639) interface for the object. For the service SDO, use **IUnknown::QueryInterface** to obtain an [**ISdo**](https://msdn.microsoft.com/library/bb960639) interface or [**ISdoServiceControl**](https://msdn.microsoft.com/library/bb960664) interface.

Before calling either [**ISdoMachine::GetServiceSDO**](https://msdn.microsoft.com/library/bb960661) or [**ISdoMachine::GetUserSDO**](https://msdn.microsoft.com/library/bb960662), call [**ISdoMachine::Attach**](https://msdn.microsoft.com/library/bb960656) to associate the machine object with the local computer.

See [Retrieving a Service SDO](https://msdn.microsoft.com/library/bb960709) and [Retrieving a User SDO](https://msdn.microsoft.com/library/bb960710) for sample code that demonstrates how to obtain these SDOs.

 

 




