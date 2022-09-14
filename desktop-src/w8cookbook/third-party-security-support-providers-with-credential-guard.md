---
title: Credential Guard and third party apps
description: Credential Guard does not allow 3rd party SSPs to ask for password hashes from LSA.
ms.assetid: DA518005-C603-41CF-BBB9-2B46414653A5
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name:
api_type:
api_location:
---

# Third party Security Support Providers with Credential Guard

Credential Guard does not allow 3rd party SSPs to ask for password hashes from LSA. However, SSPs and APs still get notified of the password when a user logs on and/or changes their password. Any use of undocumented APIs within custom SSPs and APs are not supported.

As the depth and breadth of protections provided by Credential Guard are increased, subsequent releases of Windows 10 with Credential Guard running may impact scenarios that were working in the past. For example, Credential Guard may block the use of a particular type of credential or a particular component to prevent malware from taking advantage of vulnerabilities. Therefore, we recommend that scenarios required for operations in an organization are tested before upgrading a device that has Credential Guard running.

Please refer to [this article](/windows/security/identity-protection/credential-guard/credential-guard) for the full description and recommended mitigations.

 

 