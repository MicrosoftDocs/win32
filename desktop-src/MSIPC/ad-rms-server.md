---
title: Server
description: This topic describes the purpose and functions of the RMS Server; for Azure and Windows Server.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 17B05780-B0EF-4805-8304-52DCDEB3AADB
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Server

This topic describes the purpose and functions of the RMS Server; for Azure and Windows Server.

**Azure RMS** - For information on using the Azure Rights Management service, see [Enable your service application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md).

> \[!Tip\]  
> We recommend developing and testing your application via Azure RMS.

 

**Windows Server** - For RMS on premise servers, beginning with Windows Server 2008, you can install and configure the RMS service by adding it as a role. To install the service on prior operating systems, download it from the Microsoft download center at [Microsoft Windows Rights Management Services with Service Pack 2](http://www.microsoft.com/download/en/details.aspx?id=4909).

Of the web services installed, the following are important for application development for RMS Server on Windows Server.



| Service                          | Description                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administration<br/>        | Hosts the Administration website that enables you to manage RMS. The service runs on root certification servers and on licensing servers. You can use the [Active Directory Rights Management Services Scripting API](https://msdn.microsoft.com/library/bb968797) to write administration scripts.<br/>                                                                               |
| Account Certification<br/> | Creates machine certificates that identify computers in the RMS certificate hierarchy and rights account certificates that associate users with specific computers. For more information, see [Activating a Computer](https://msdn.microsoft.com/library/cc530377) and [Activating a User](https://msdn.microsoft.com/library/cc530378).<br/> This service runs on the root certification server.<br/> |
| Licensing<br/>             | Issues an [*end-user license*](https://msdn.microsoft.com/library/aa362618#-rm-end-user-license-gly). The service runs on root certification servers and on licensing servers.<br/>                                                                                                                                                                                          |
| Publishing<br/>            | Creates an [*issuance license*](https://msdn.microsoft.com/library/aa362630#-rm-issuance-license-gly) which define the policies that can be enumerated in an end-user license. For more information, see [Creating an Issuance License](https://msdn.microsoft.com/library/aa362355).<br/> The service runs on root certification servers and on licensing servers.<br/>           |
| Pre-certification<br/>     | Enables a server to request a [*rights account certificate*](https://msdn.microsoft.com/library/aa362726#-rm-rights-account-certificate-gly) on behalf of a user. The service runs on root certification servers and on licensing servers.<br/>                                                                                                                    |
| Service Locator<br/>       | Provides the URL of the account certification, licensing, and publishing services to Active Directory so that they can be discovered by RMS clients. The service runs on root certification servers and on licensing servers.<br/>                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Overview](ad-rms-overview.md)
</dt> <dt>

[Microsoft Internet Information Services](http://www.iis.net/overview)
</dt> <dt>

[Enable your service application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md)
</dt> <dt>

[Microsoft Windows Rights Management Services with Service Pack 2](http://www.microsoft.com/download/en/details.aspx?id=4909)
</dt> <dt>

[Active Directory Rights Management Services Scripting API](https://msdn.microsoft.com/library/bb968797)
</dt> <dt>

[Activating a Computer](https://msdn.microsoft.com/library/cc530377)
</dt> <dt>

[Activating a User](https://msdn.microsoft.com/library/cc530378)
</dt> <dt>

[*end-user license*](https://msdn.microsoft.com/library/aa362618#-rm-end-user-license-gly)
</dt> <dt>

[Creating an Issuance License](https://msdn.microsoft.com/library/aa362355)
</dt> <dt>

[*issuance license*](https://msdn.microsoft.com/library/aa362630#-rm-issuance-license-gly)
</dt> <dt>

[*rights account certificate*](https://msdn.microsoft.com/library/aa362726#-rm-rights-account-certificate-gly)
</dt> </dl>

 

 





