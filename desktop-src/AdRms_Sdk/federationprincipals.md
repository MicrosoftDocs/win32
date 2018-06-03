---
Description: Contains a list of principals associated with those identified by the ISSUEDPRINCIPALS element. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c87fcea8-9825-4565-9b1c-417c7da927dc
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: FEDERATIONPRINCIPALS
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FEDERATIONPRINCIPALS

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Contains a list of principals associated with those identified by the [**ISSUEDPRINCIPALS**](issuedprincipals.md) element. This element has the following definition.

``` syntax
<!ELEMENT FEDERATIONPRINCIPALS (PRINCIPAL*)>

<!ELEMENT PRINCIPAL (%aPrincipal;)>
<!ATTLIST PRINCIPAL
  type CDATA #IMPLIED

<!ENTITY % aPrincipal "OBJECT?, 
   AUTHENTICATOR*, 
   PASSWORD*,
   PUBLICKEY*,
   PRIVATEKEY*, 
   CERTIFICATE*,
   DIGEST*,
   VERIFICATIONDATA*, 
   ENABLINGBITS*, 
   PRINCIPAL*,
   SECURITYLEVEL*">
```

## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**BODY**](body.md)
</dt> <dt>

[XrML Elements](xrml-elements.md)
</dt> </dl>

 

 




