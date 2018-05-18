---
Description: 'Retrieves a list of relying parties that are available to Web Application Proxy.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '86adb6bc-9445-4076-94e2-570ef9aabdce'
ms.prod: 'windows-server-dev'
ms.technology:
- 'web-app-proxy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'CIM\_WebApplicationProxyAvailableADFSRelyingParty class'
---

# CIM\_WebApplicationProxyAvailableADFSRelyingParty class

Retrieves a list of relying parties that are available to Web Application Proxy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("AppProxyPSProvider"), AMENDMENT]
class CIM_WebApplicationProxyAvailableADFSRelyingParty
{
};
```

## Members

The **CIM\_WebApplicationProxyAvailableADFSRelyingParty** class has these types of members:

-   [Methods](#methods)

### Methods

The **CIM\_WebApplicationProxyAvailableADFSRelyingParty** class has these methods.



| Method                                                              | Description                                                                                                                                                                 |
|:--------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-cim-webapplicationproxyavailableadfsrelyingparty.md) | Retrieves a list of [**RelyingPartyMetadata**](relyingpartymetadata.md) objects that represent the relying parties that are available to Web Application Proxy.<br/> |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[Application Proxy WMI Provider Reference](application-proxy-wmi-provider-reference.md)
</dt> </dl>

 

 




