---
Description: Specifies the principal from which the Active Directory Rights Management Services (AD RMS) license or certificate is distributed or can be obtained. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9df7c78b-3d9c-4971-a380-b69776a25cf5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DISTRIBUTIONPOINT
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DISTRIBUTIONPOINT

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Specifies the principal from which the Active Directory Rights Management Services (AD RMS) license or certificate is distributed or can be obtained. This element has the following definition.

``` syntax
<!ELEMENT DISTRIBUTIONPOINT (%aPrincipal;)>
<!ATTLIST DISTRIBUTIONPOINT
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

The distribution point is identified by the **ID**, **NAME**, and **ADDRESS** elements of an encapsulated [**OBJECT**](object.md) element as shown in the following example.

## Examples


```XML
<DISTRIBUTIONPOINT>
  <OBJECT type="Activation">
    <ID type="MS-GUID">{99F48562-703E-4E7D-9175-DD69C66921B7}</ID> 
    <NAME>Microsoft Activation</NAME> 
    <ADDRESS type="URL">file:///rmactivate.exe</ADDRESS> 
  </OBJECT>
</DISTRIBUTIONPOINT>
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

 

 




