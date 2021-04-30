---
description: The installation of service classes, registration of service instances and basic query operations all map fairly directly from the API to the SPI.
ms.assetid: 2ae937f6-e0a6-4a02-9838-0a42575bae66
title: Name Resolution Mapping Between API and SPI Functions
ms.topic: article
ms.date: 05/31/2018
---

# Name Resolution Mapping Between API and SPI Functions

The installation of service classes, registration of service instances and basic query operations all map fairly directly from the API to the SPI. The [**WSAGetServiceClassNameByClassId**](/windows/desktop/api/Winsock2/nf-winsock2-wsagetserviceclassnamebyclassida) function does not have a corresponding function in the SPI, as this function is implemented in Ws2\_32.dll by making a call to [**NSPGetServiceClassInfo**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpnspgetserviceclassinfo).

The helper functions [**WSAAddressToString**](/windows/desktop/api/Winsock2/nf-winsock2-wsaaddresstostringa) and [**WSAStringToAddress**](/windows/desktop/api/Winsock2/nf-winsock2-wsastringtoaddressa) are mapped to the corresponding functions in the transport API, as only a transport provider will necessarily know how to perform the translation on a [**sockaddr**](sockaddr-2.md) structure.

 

 



