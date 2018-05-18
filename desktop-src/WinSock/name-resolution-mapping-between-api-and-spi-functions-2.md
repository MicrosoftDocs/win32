---
Description: 'The installation of service classes, registration of service instances and basic query operations all map fairly directly from the API to the SPI.'
ms.assetid: '2ae937f6-e0a6-4a02-9838-0a42575bae66'
title: Name Resolution Mapping Between API and SPI Functions
---

# Name Resolution Mapping Between API and SPI Functions

The installation of service classes, registration of service instances and basic query operations all map fairly directly from the API to the SPI. The [**WSAGetServiceClassNameByClassId**](wsagetserviceclassnamebyclassid-2.md) function does not have a corresponding function in the SPI, as this function is implemented in Ws2\_32.dll by making a call to [**NSPGetServiceClassInfo**](nspgetserviceclassinfo-2.md).

The helper functions [**WSAAddressToString**](wsaaddresstostring-2.md) and [**WSAStringToAddress**](wsastringtoaddress-2.md) are mapped to the corresponding functions in the transport API, as only a transport provider will necessarily know how to perform the translation on a [**sockaddr**](sockaddr-2.md) structure.

 

 



