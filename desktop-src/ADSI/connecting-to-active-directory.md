---
title: Connecting to Active Directory
description: There are several methods used to access Active Directory.
ms.assetid: ef5720ff-6c66-466c-967e-f9c72a7bc0fa
ms.tgt_platform: multiple
keywords:
- Connecting to Active Directory ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to Active Directory

There are several methods used to access Active Directory. It is recommended that you use the ADSI API to access Active Directory. ADSI implements the LDAP protocol to communicate with Active Directory. The following code examples show how to access Active Directory.


```VB
Set ns = GetObject("LDAP:")
```



This opens the LDAP provider and prepares it to retrieve data. No connection is established until data is requested. When data is requested, ADSI, with the help of the locator service, attempts to find the best domain controller (DC) for the connection and will establish a connection to the server. This process is known as serverless binding.

ADSI also enables you to specify the server name to use for the connection.


```VB
Set obj = GetObject("LDAP://mysrv01")
```



In another scenario, you may only know the domain name but not the specific server name. Again, ADSI enables you to specify the domain name. In Windows 2000, the domain name is represented as a DNS name. For example, if Joe Worden, the network administrator, chooses to connect using the domain name, he could use the following code example.


```VB
Set obj = GetObject("LDAP://fabrikam.com")
```



ADSI will connect to one of the domain controllers in the fabrikam.com domain.

## Related topics

<dl> <dt>

[Binding to Active Directory Objects](binding-to-active-directory-objects.md)
</dt> </dl>

 

 




