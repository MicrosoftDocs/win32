---
Description: The installation of service classes, registration of service instances and basic query operations all map fairly directly from the API to the SPI.
ms.assetid: 2ae937f6-e0a6-4a02-9838-0a42575bae66
title: Name Resolution Mapping Between API and SPI Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Name Resolution Mapping Between API and SPI Functions

The installation of service classes, registration of service instances and basic query operations all map fairly directly from the API to the SPI. The [**WSAGetServiceClassNameByClassId**](/windows/win32/Winsock2/nf-winsock2-wsagetserviceclassnamebyclassida?branch=master) function does not have a corresponding function in the SPI, as this function is implemented in Ws2\_32.dll by making a call to [**NSPGetServiceClassInfo**](/windows/win32/Ws2spi/nc-ws2spi-lpnspgetserviceclassinfo?branch=master).

The helper functions [**WSAAddressToString**](/windows/win32/Winsock2/nf-winsock2-wsaaddresstostringa?branch=master) and [**WSAStringToAddress**](/windows/win32/Winsock2/nf-winsock2-wsastringtoaddressa?branch=master) are mapped to the corresponding functions in the transport API, as only a transport provider will necessarily know how to perform the translation on a [**sockaddr**](sockaddr-2.md) structure.

 

 



