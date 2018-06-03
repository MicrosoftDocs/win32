---
Description: Retrieves a list of RelyingPartyMetadata objects that represent the relying parties that are available to Web Application Proxy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f5b7789e-cedf-4eb3-a794-ef556ead9099
ms.prod: windows-server-dev
ms.technology:
- web-app-proxy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Get method of the CIM\_WebApplicationProxyAvailableADFSRelyingParty class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the CIM\_WebApplicationProxyAvailableADFSRelyingParty class

Retrieves a list of [**RelyingPartyMetadata**](relyingpartymetadata.md) objects that represent the relying parties that are available to Web Application Proxy.

## Syntax


```mof
uint32 Get(
  [out] RelyingPartyMetadata cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, it contains an array of the [**RelyingPartyMetadata**](relyingpartymetadata.md) objects.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_WebApplicationProxyAvailableADFSRelyingParty**](cim-webapplicationproxyavailableadfsrelyingparty.md)
</dt> </dl>

 

 




