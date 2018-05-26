---
title: Creating an External Referral
description: If an external crossRef object is created and a domain controller uses it to generate a referral, the crossRef object provides two important data elements in the following properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9805390c-9e8d-4afd-bffc-43abf6055413
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- external referrals Active Directory
- Active Directory examples Active Directory , creating an external referral
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating an External Referral

If an external [**crossRef**](https://msdn.microsoft.com/library/ms681007) object is created and a domain controller uses it to generate a referral, the **crossRef** object provides two important data elements in the following properties. For more information about situations where this can occur, see the previous section.



| Property                           | Description                                                                                                                                                         |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**dnsRoot**](https://msdn.microsoft.com/library/ms675528) | Specifies the server or domain that can serve data from the naming context specified in [**nCName**](https://msdn.microsoft.com/library/ms678699).                                           |
| [**nCName**](https://msdn.microsoft.com/library/ms678699)   | Specifies the distinguished name for the domain, schema, or configuration container rooted at the server or domain specified by [**dnsRoot**](https://msdn.microsoft.com/library/ms675528). |



 

For example, if the server with DNS address of serv1.northwest.Fabrikam.com serves the naming context rooted at CN=MyContainer,OU=MyDOM,O=Fabrikam, set the [**dnsRoot**](https://msdn.microsoft.com/library/ms675528) to that server's DNS address and the [**nCName**](https://msdn.microsoft.com/library/ms678699) to the distinguished name of the domain, schema, or configuration container.

For more information and a code example that shows how to create an external referral, see [Example Code for Creating an External crossRef Object](example-code-for-creating-an-external-crossref-object.md).

 

 




