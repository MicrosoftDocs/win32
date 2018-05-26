---
Description: The system uses the configuration information to determine how to start the service.
ms.assetid: 79aa4ad5-87ee-4f5d-9c8e-4e788f4c7182
title: Service Configuration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service Configuration

The system uses the configuration information to determine how to start the service. The configuration information also includes the service display name and its description. For example, for the DHCP service, you could use the display name "Dynamic Host Configuration Protocol Service" and the description "Provides internet addresses for computer on your network."

To modify the configuration information for a service object, a configuration program uses the [**ChangeServiceConfig**](/windows/win32/Winsvc/nf-winsvc-changeserviceconfiga?branch=master) or [**ChangeServiceConfig2**](/windows/win32/Winsvc/nf-winsvc-changeserviceconfig2a?branch=master) function. For an example, see [Changing a Service Configuration](changing-a-service-configuration.md).

To retrieve the configuration information for a service object, the configuration program uses the [**QueryServiceConfig**](/windows/win32/Winsvc/nf-winsvc-queryserviceconfiga?branch=master) or [**QueryServiceConfig2**](/windows/win32/Winsvc/nf-winsvc-queryserviceconfig2a?branch=master) function. For an example, see [Querying a Service's Configuration](querying-a-service-s-configuration.md).

The [**ChangeServiceConfig2**](/windows/win32/Winsvc/nf-winsvc-changeserviceconfig2a?branch=master) and [**QueryServiceConfig2**](/windows/win32/Winsvc/nf-winsvc-queryserviceconfig2a?branch=master) service configuration functions support the use of triggers to control service start.

To modify the security descriptor for either an SCManager object or a service object, a configuration program uses the [**SetServiceObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379589) function. To retrieve a copy of the security descriptor, the configuration program uses the [**QueryServiceObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379312) function.

## Related topics

<dl> <dt>

[Configuring a Service Using SC](configuring-a-service-using-sc.md)
</dt> </dl>

 

 



