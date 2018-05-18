---
title: FindNLSCertificate method of the PS\_RemoteAccessLocal class
description: This method retrieves a Certificate for NLS from the local machine whose subject name does not match the ConnectTo addresses, but resolves to at least one IP from each site.
audience: developer
ms.assetid: 'd9fdb2fd-9613-4354-9d66-307c3a7b1c2e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["FindNLSCertificate method", "FindNLSCertificate method, PS_RemoteAccessLocal class", "PS_RemoteAccessLocal class, FindNLSCertificate method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.FindNLSCertificate
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# FindNLSCertificate method of the PS\_RemoteAccessLocal class

This method retrieves a Certificate for NLS from the local machine whose subject name does not match the ConnectTo addresses, but resolves to at least one IP from each site.

## Syntax


```mof
uint32 FindNLSCertificate(
  [in]  DASiteAddresses      SiteAddresses[],
  [in]  string               ConnectToAddress[],
  [in]  string               MachineNamesForAllSites[],
  [in]  boolean              IncludeSelfSigned,
  [out] string               ResolvedAddress[],
  [out] DACertificateContext EncodedCertificate
);
```



## Parameters

<dl> <dt>

*SiteAddresses* \[in\]
</dt> <dd>

An array of [**DASiteAddresses**](dasiteaddresses.md) Site addresses. Each DASiteAddresses object is a list of addresses for a specific Site.

</dd> <dt>

*ConnectToAddress* \[in\]
</dt> <dd>

The addresses to which the DirectAccess client connects to.

</dd> <dt>

*MachineNamesForAllSites* \[in\]
</dt> <dd>

List of all the machine names for all the sites

</dd> <dt>

*IncludeSelfSigned* \[in\]
</dt> <dd>

This boolean indicates that self signed certificates should also be included while searching.

</dd> <dt>

*ResolvedAddress* \[out\]
</dt> <dd>

List of IP Addresses that resolve to the certificate subject name.

</dd> <dt>

*EncodedCertificate* \[out\]
</dt> <dd>

An embedded [**DACertificateContext**](dacertificatecontext.md) object containing the encoded certificate.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





