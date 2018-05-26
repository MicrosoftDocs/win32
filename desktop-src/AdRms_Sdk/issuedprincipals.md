---
Description: Contains a collection of principals to whom the Active Directory Rights Management Services (AD RMS) license or certificate has been issued. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 68532bf7-5cc7-46bc-84fd-93c2bae3c2a4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ISSUEDPRINCIPALS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ISSUEDPRINCIPALS

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Contains a collection of principals to whom the Active Directory Rights Management Services (AD RMS) license or certificate has been issued. This element has the following definition.

``` syntax
<!ELEMENT ISSUEDPRINCIPALS (PRINCIPAL*, ANYONE*, EVERYONE?)>

<!ELEMENT PRINCIPAL (%aPrincipal;)>
<!ATTLIST PRINCIPAL
  type CDATA #IMPLIED
  internal-id CDATA #IMPLIED>

<!ELEMENT ANYONE EMPTY>
<!ATTLIST ANYONE
  domain CDATA #IMPLIED>

<!ELEMENT EVERYONE (%aPrincipal;)>

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

## Remarks

Of the possible elements available in the **%aPrincipal** entity, Active Directory Rights Management Services (AD RMS) uses the [**OBJECT**](object.md), **PUBLICKEY**, and [**DIGEST**](digest.md) elements to describe each principal as shown in the following example from a machine certificate.

## Examples


```XML
<ISSUEDPRINCIPALS>
  <PRINCIPAL>
    <OBJECT type="Machine-Unique-Identifier">
      <ID type="MS-GUID">{c98e1602-1138-4f5e-aeb7-708845df7d47}</ID> 
      <NAME>Machine</NAME> 
    </OBJECT>
    <PUBLICKEY>
      <ALGORITHM>RSA</ALGORITHM> 
      <PARAMETER name="public-exponent">
        <VALUE encoding="integer32">65537</VALUE> 
      </PARAMETER>
     <PARAMETER name="modulus">
       <VALUE encoding="base64" size="1024">...</VALUE> 
     </PARAMETER>
   </PUBLICKEY>
   <DIGEST>
     <ALGORITHM>SHA1</ALGORITHM> 
     <PARAMETER name="codingtype">
       <VALUE encoding="string">surface-coding</VALUE> 
     </PARAMETER>
     <VALUE encoding="base64" size="160">...</VALUE> 
   </DIGEST>
   <SECURITYLEVEL name="Platform" value="2.6.0.6000"/> 
   <SECURITYLEVEL name="Manufacturer" value="mcoregen DLL"/> 
   <SECURITYLEVEL name="Repository" value="rep 6.0.5840.16389"/> 
 </PRINCIPAL>
</ISSUEDPRINCIPALS>
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

 

 




