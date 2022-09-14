---
title: Binding Issues for Mixed Environments
description: Binding Issues for Mixed Environments
ms.assetid: d9f9a6bc-7733-4269-99c8-61a84b37d487
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,using,binding issues for mixed environments
ms.topic: article
ms.date: 05/31/2018
---

# Binding Issues for Mixed Environments

For environments in which the domain that contains Active Directory has a trust relationship with a Windows NT 4.0 domain, there may be a problem with using serverless binding to bind to Active Directory objects.

In some networking environments, trust relationships have been set up between domain controllers that contain Active Directory and Windows NT 4.0 servers for the purpose of allowing authentication between domains. In these mixed environments, if a user, who is a member of the Windows NT 4.0, domain attempts to use serverless binding to bind to an Active Directory object on a trusted domain, then the bind will fail and an error is returned. This is because a serverless bind uses the [**DsGetDcName**](/windows/desktop/api/dsgetdc/nf-dsgetdc-dsgetdcnamea) function to bind to the object in Active Directory, which is dependent upon the proper DNS.

In this scenario, the Windows NT user must provide the name of a specific domain to bind to. The following is an example.

``` syntax
LDAP://fabrikam.com/OU=Sales
```

 

 