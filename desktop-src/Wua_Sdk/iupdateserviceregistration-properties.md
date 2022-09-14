---
description: The IUpdateServiceRegistration interface defines the following properties.
ms.assetid: 2bcde8b4-7bff-4887-8080-89da817afb5f
title: IUpdateServiceRegistration Properties
ms.topic: article
ms.date: 05/31/2018
---

# IUpdateServiceRegistration Properties

The **IUpdateServiceRegistration** interface defines the following properties.



| Property                                                                                      | Description                                                                                                                                          |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IsPendingRegistrationWithAU**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateserviceregistration-get_ispendingregistrationwithau) | Gets a Boolean value that indicates whether the service will also be registered with Automatic Updates, when added.                                  |
| [**RegistrationState**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateserviceregistration-get_registrationstate)                     | Gets an [**UpdateServiceRegistrationState**](/windows/win32/api/wuapi/ne-wuapi-updateserviceregistrationstate) value that indicates the current state of the service registration. |
| [**Service**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateserviceregistration-get_service)                                         | Gets a pointer to an [**IUpdateService2**](/windows/desktop/api/Wuapi/nn-wuapi-iupdateservice2) interface. This property is the default property.                                    |



 

 

 



