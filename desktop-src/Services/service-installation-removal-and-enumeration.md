---
Description: 'A configuration program uses the CreateService function to install a new service in the SCM database.'
ms.assetid: '554b9983-4e49-4b11-b420-a4754123d854'
title: 'Service Installation, Removal, and Enumeration'
---

# Service Installation, Removal, and Enumeration

A configuration program uses the [**CreateService**](createservice.md) function to install a new service in the SCM database. This function specifies the name of the service and provides configuration information that is stored in the database. For a description of the information stored in the database for each service, see [Database of Installed Services](database-of-installed-services.md). For sample code, see [Installing a Service](installing-a-service.md).

A configuration program uses the [**DeleteService**](deleteservice.md) function to remove an installed service from the database. For more information, see [Deleting a Service](deleting-a-service.md).

To obtain the service name, call the [**GetServiceKeyName**](getservicekeyname.md) function. The service display name, used in the Services control panel applet, can be obtained by calling the [**GetServiceDisplayName**](getservicedisplayname.md) function.

A service configuration program can use the [**EnumServicesStatusEx**](enumservicesstatusex.md) function to enumerate all services and their statuses. It can also use the [**EnumDependentServices**](enumdependentservices.md) function to enumerate which services are dependent on a specified service object.

 

 



