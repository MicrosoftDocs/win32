---
title: Obtaining Service and User SDOs
description: To obtain SDOs for NPS (IAS) or a particular user, call the ISdoMachine GetServiceSDO or ISdoMachine GetUserSDO methods.
ms.assetid: 23e23fb3-0102-4c36-b30f-18604131ee32
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Service and User SDOs

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008.

 

To obtain SDOs for NPS (IAS) or a particular user, call the [**ISdoMachine::GetServiceSDO**](https://docs.microsoft.com/windows/desktop/api/sdoias/nf-sdoias-isdomachine-getservicesdo) or [**ISdoMachine::GetUserSDO**](https://docs.microsoft.com/windows/desktop/api/sdoias/nf-sdoias-isdomachine-getusersdo) methods. These methods return pointers to [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interfaces for these objects. For the user SDO, use the [**IUnknown::QueryInterface**](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx) method to obtain an [**ISdo**](https://docs.microsoft.com/windows/desktop/api/sdoias/nn-sdoias-isdo) interface for the object. For the service SDO, use **IUnknown::QueryInterface** to obtain an [**ISdo**](https://docs.microsoft.com/windows/desktop/api/sdoias/nn-sdoias-isdo) interface or [**ISdoServiceControl**](https://docs.microsoft.com/windows/desktop/api/sdoias/nn-sdoias-isdoservicecontrol) interface.

Before calling either [**ISdoMachine::GetServiceSDO**](https://docs.microsoft.com/windows/desktop/api/sdoias/nf-sdoias-isdomachine-getservicesdo) or [**ISdoMachine::GetUserSDO**](https://docs.microsoft.com/windows/desktop/api/sdoias/nf-sdoias-isdomachine-getusersdo), call [**ISdoMachine::Attach**](https://docs.microsoft.com/windows/desktop/api/sdoias/nf-sdoias-isdomachine-attach) to associate the machine object with the local computer.

See [Retrieving a Service SDO](https://docs.microsoft.com/windows/desktop/Nps/sdo-retrieving-a-service-sdo) and [Retrieving a User SDO](https://docs.microsoft.com/windows/desktop/Nps/sdo-retrieving-a-user-sdo) for sample code that demonstrates how to obtain these SDOs.

 

 




