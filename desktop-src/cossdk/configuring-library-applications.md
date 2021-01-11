---
description: Configuring Library Applications
ms.assetid: db375e0f-74ca-44df-918a-b0e48742a594
title: Configuring Library Applications
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Library Applications

Because COM+ library applications run in the client's process, the configurable elements for library applications are considerably different than for server applications. You cannot configure any aspect of the application that is determined by the hosting process.

At the application level, several settings are either limited or unavailable for library applications. These constraints are described in the following table:



| Attribute                                       | Description                                                                                                                                                                                                                                   |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Security level<br/>                       | You must choose component-level access checks. The library application cannot influence process-level access checks. See [Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md).<br/>             |
| Enabling or disabling authentication<br/> | You can indicate whether the library application will participate in authentication performed by the host process. See [Enabling Authentication for a Library Application](enabling-authentication-for-a-library-application.md).<br/> |
| Impersonation level<br/>                  | Unavailable. The setting of the host process is used. <br/>                                                                                                                                                                             |
| Security identity<br/>                    | Unavailable. The application runs under the identity of the host process.<br/>                                                                                                                                                          |
| Server process shutdown<br/>              | Unavailable.<br/>                                                                                                                                                                                                                       |
| Enable 3-GB support<br/>                  | Unavailable.<br/>                                                                                                                                                                                                                       |
| Launch in debugger<br/>                   | Unavailable.<br/>                                                                                                                                                                                                                       |
| Enable CRM<br/>                           | Unavailable.<br/>                                                                                                                                                                                                                       |
| Queuing<br/>                              | Unavailable.<br/>                                                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[COM+ Application Overview](com--application-overview.md)
</dt> </dl>

 

 




