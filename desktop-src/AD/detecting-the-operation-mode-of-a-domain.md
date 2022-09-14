---
title: Detecting the Operation Mode of a Domain
description: In Windows 2000, a domain can run in two operation modes mixed and native.
ms.assetid: c20dec14-50ad-4f63-bd5c-222c2f2c83e4
ms.tgt_platform: multiple
keywords:
- Detecting the Operation Mode of a Domain AD
ms.topic: article
ms.date: 05/31/2018
---

# Detecting the Operation Mode of a Domain

In Windows 2000, a domain can run in two operation modes: mixed and native. Mixed mode should be used to include domain controllers running Windows NT 4.0 in a Windows 2000 domain. Mixed mode does not support universal groups or nested groups. If all domain controllers in the domain are running Windows 2000, you can use native mode.

To programmatically detect the operation mode of a Windows 2000 domain, read the [**ntMixedDomain**](/windows/desktop/ADSchema/a-ntmixeddomain) property of the [**domainDNS**](/windows/desktop/ADSchema/c-domaindns) object for that domain. A value of zero (0) means that the domain is in native mode. A value of one (1) indicates that the domain is in mixed mode. You can also use the [**DsRoleGetPrimaryDomainInformation**](/windows/desktop/api/Dsrole/nf-dsrole-dsrolegetprimarydomaininformation) function to get the operation mode as well as other data about the domain and its state.

To bind to the [**domainDNS**](/windows/desktop/ADSchema/c-domaindns) object of the domain of the user account under which your application is running, use serverless binding and rootDSE to get the distinguished name for the domain and then use that distinguished name to bind to the **domainDNS** object that represents that domain. For more information about serverless binding and rootDSE, see [Serverless Binding and RootDSE](serverless-binding-and-rootdse.md).

For more information and a code example that shows how to programmatically detect the operation mode of a domain, see [Example Code for Determining the Operation Mode](example-code-for-determining-the-operation-mode.md).

 

 