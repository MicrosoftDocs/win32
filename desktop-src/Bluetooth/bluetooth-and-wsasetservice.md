---
title: Bluetooth and WSASetService
description: Bluetooth uses the WSASetService function to register or remove a service instance within the Bluetooth namespace (NS\_BTH) from the registry.
ms.assetid: 71c5ed9c-fade-4d15-848e-eb810ad4cbb2
keywords:
- Bluetooth Bluetooth
- WSASetService Bluetooth
- Bluetooth and WSASetService Bluetooth
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and WSASetService

Bluetooth uses the [**WSASetService**](https://msdn.microsoft.com/library/windows/desktop/ms742211) function to register or remove a service instance within the Bluetooth namespace (NS\_BTH) from the registry. The handle returned by this operation may only be used to delete the service.

Bluetooth has two means of advertising services using the [**WSASetService**](https://msdn.microsoft.com/library/windows/desktop/ms742211) function:

-   The application can have the system advertise a simple Bluetooth SDP service record, constructed from standard members in the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure.
-   The application can have the system advertise their own Bluetooth SDP record by passing a [**BTH\_SET\_SERVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-_bth_set_service) structure in the **lpBlob** member of the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure. This is a more complex approach.

> [!Note]  
> SDP records advertised by [**WSASetService**](https://msdn.microsoft.com/library/windows/desktop/ms742211) do not persist after the process that published them has quit.

 

Use of [**WSASetService**](https://msdn.microsoft.com/library/windows/desktop/ms742211) with Bluetooth has the following requirements:

-   The *lpqsRegInfo* parameter is the address of the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure to be registered.
-   The *essOperation* parameter is an enumeration that contains one of the operations shown in the following table.



| Value                  | Description                                                                                |
|------------------------|--------------------------------------------------------------------------------------------|
| RNRSERVICE\_REGISTER   | Starts advertising the service to remote radios querying using the Bluetooth SDP protocol. |
| RNRSERVICE\_DEREGISTER | Not valid. Returns an error.                                                               |
| RNRSERVICE\_DELETE     | Stops advertising the service.                                                             |



 

> [!Note]  
> Service handles discovered during a [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) or [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641) call are incompatible with the RNRSERVICE\_DELETE operation.

 

-   The *dwControlFlags* parameter is reserved, and must be zero.

For more information and a list of Bluetooth socket options, see [Bluetooth and Socket Options](bluetooth-and-socket-options.md).

## Related topics

<dl> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> </dl>

 

 




