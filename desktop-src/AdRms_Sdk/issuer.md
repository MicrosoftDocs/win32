---
Description: Specifies the principal who issued the XrML document. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1e0b86ce-9655-42a1-ac63-886ec560860f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ISSUER
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISSUER

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Specifies the principal who issued the XrML document. This element has the following definition.

``` syntax
<!ELEMENT ISSUER (%aPrincipal;)>
<!ATTLIST ISSUER
 type CDATA #IMPLIED
 internal-id CDATA #IMPLIED

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

Of the possible elements available in the **%aPrincipal** entity, Active Directory Rights Management Services (AD RMS) uses the [**OBJECT**](object.md) and **PUBLICKEY** elements.

## Examples

The following example shows an issuer for a machine certificate.


```XML
<ISSUER>
  <OBJECT type="MS-DRM-Desktop-Security-Processor">
    <ID type="MS-GUID">{d250be5b-50f1-48e6-81a5-6003ccf9cb44}</ID> 
    <NAME>Microsoft DRM Activation Certificate</NAME> 
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
</ISSUER>
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

 

 




