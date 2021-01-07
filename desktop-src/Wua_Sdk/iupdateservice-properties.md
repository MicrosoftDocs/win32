---
description: The IUpdateService interface defines the following properties.
ms.assetid: 33bc28e8-0b83-4d58-a03e-ccf2a97887e6
title: IUpdateService Properties
ms.topic: article
ms.date: 05/31/2018
---

# IUpdateService Properties

The [**IUpdateService**](/windows/desktop/api/Wuapi/nn-wuapi-iupdateservice) interface defines the following properties.



| Property                                                              | Description                                                                                     |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**CanRegisterWithAU**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_canregisterwithau)         | Gets a Boolean value that indicates whether the service can register with Automatic Updates.    |
| [**ContentValidationCert**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_contentvalidationcert) | Gets an SHA-1 hash of the certificate that is used to sign the contents of the service.         |
| [**ExpirationDate**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_expirationdate)               | Gets the date on which the authorization cabinet file expires.                                  |
| [**IsManaged**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_ismanaged)                         | Gets a Boolean value that indicates whether a service is a managed service.                     |
| [**IsRegisteredWithAU**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_isregisteredwithau)       | Gets a Boolean value that indicates whether a service is registered with Automatic Updates.     |
| [**IsScanPackageService**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_isscanpackageservice)   | Gets a Boolean value that indicates whether a service is based on a scan package.               |
| [**IssueDate**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_issuedate)                         | Gets the date on which the authorization cabinet file was issued.                               |
| [**Name**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_name)                                   | Gets the name of the service.                                                                   |
| [**OffersWindowsUpdates**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_offerswindowsupdates)   | Gets a Boolean value indicates whether the current service offers updates from Windows Updates. |
| [**RedirectUrls**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_redirecturls)                   | Gets the URL for the redirector cabinet file.                                                   |
| [**ServiceID**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_serviceid)                         | Gets the identifier for a service.                                                              |
| [**ServiceUrl**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_serviceurl)                       | Gets the URL for the service.                                                                   |
| [**SetupPrefix**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservice-get_setupprefix)                     | Gets the prefix for the setup files.                                                            |



 

 

 



