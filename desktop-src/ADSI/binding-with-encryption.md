---
title: Binding With Encryption
description: Sensitive data exchanged over a network should be encrypted.
ms.assetid: 51fe2131-5f7d-41b1-ad88-d965cbb4d630
ms.tgt_platform: multiple
keywords:
- ADSI ADSI , using, binding with encryption
- Binding With Encryption
ms.topic: article
ms.date: 05/31/2018
---

# Binding With Encryption

Sensitive data exchanged over a network should be encrypted. To allow this, ADSI supports two types of encryption, Kerberos and Secure Sockets Layer (SSL). Both types of encryption require the use of [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) or [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject) for binding.

**GetObject** and [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject) cannot be used for binding in this case because these functions cause the LDAP requests used by ADSI and the data returned from the directory server to transmit across the network as plaintext. For debugging purposes, it is helpful to turn encryption off so the Network Monitor can be used to view the LDAP requests and data between the client and the directory server.

## Kerberos-based Encryption

To use Kerberos-based encryption, specify the **ADS\_USE\_SEALING** flag when calling [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) or [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject). The **ADS\_USE\_SEALING** flag can also be used to verify data integrity, that is, to ensure the data received is the same as the data sent. If the **ADS\_USE\_SEALING** flag is specified, the **ADS\_USE\_SIGNING** flag is automatically specified as well. Both flags require Kerberos authentication, which works only under the following conditions:

-   The client computer must be logged on to the Windows domain, or to a domain trusted by a Windows domain.
-   [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) or [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject) must be called with null credentials; that is, alternate credentials cannot be specified.

## SSL-based Encryption

To use SSL-based encryption, specify the **ADS\_USE\_SSL** flag when calling [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) or [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject). If only the **ADS\_USE\_SSL** flag is specified, ADSI opens SSL port 636 and then performs a simple bind over that SSL channel. If both the **ADS\_SECURE\_AUTHENTICATION** and **ADS\_USE\_SSL** flags are specified, the binding behavior depends on the client that the call is made from. On unsupported versions of Windows, ADSI first opened an SSL channel and performs a simple bind using the specified user name and password or the current user context if both user name and password are null. On supported versions of Windows, ADSI performs a secure authentication rather than a simple bind.

To use SSL-based encryption while communicating with Active Directory, Active Directory must have enabled Public Key Infrastructure (PKI). PKI can be enabled by setting up an enterprise certification authority on one of the servers in Active Directory, including one of the Active Directory servers itself. Setting up an enterprise certification authority causes an Active Directory server to get a server certificate that can then be used to do SSL-based encryption.

 

 




