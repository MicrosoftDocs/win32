---
title: PS\_RemoteAccess class
description: Represents installation of both DirectAccess and VPN and configuration common to both.
audience: developer
ms.assetid: '65c3fc93-1a39-418b-adbf-9232f56a51cb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_RemoteAccess class", "PS_RemoteAccess class, described"]
topic_type:
- apiref
api_name:
- PS_RemoteAccess
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_RemoteAccess class

Represents installation of both DirectAccess and VPN and configuration common to both.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccess
{
};
```

## Members

The **PS\_RemoteAccess** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccess** class has these methods.



| Method                                                                                 | Description                                                                                                                                                                                                                                                                                                            |
|:---------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-remoteaccess.md)                                                     | This cmdlet displays the configuration of DirectAccess and VPN.<br/>                                                                                                                                                                                                                                             |
| [**InstallByDAPrerequisiteChecks**](installbydaprerequisitechecks-ps-remoteaccess.md) | This cmdlet does the following 1. Performs pre-requisite checks for DirectAccess to ensure that it can be installed2. Installs DirectAccess for remote access (includes management of remote clients) or for management of remote clients only3. Installs VPN (both Remote Access VPN and site-to-site VPN)<br/> |
| [**InstallByDirectAccess**](installbydirectaccess-ps-remoteaccess.md)                 | This cmdlet does the following 1. Performs pre-requisite checks for DirectAccess to ensure that it can be installed2. Installs DirectAccess for remote access (includes management of remote clients) or for management of remote clients only3. Installs VPN (both Remote Access VPN and site-to-site VPN)<br/> |
| [**InstallByMultiTenant**](installbymultitenant-ps-remoteaccess.md)                   | Installs DirectAccess and multi-tenant site-to-site (S2S) VPN.<br/>                                                                                                                                                                                                                                              |
| [**InstallByVpn**](installbyvpn-ps-remoteaccess.md)                                   | This cmdlet does the following 1. Performs pre-requisite checks for DirectAccess to ensure that it can be installed2. Installs DirectAccess for remote access (includes management of remote clients) or for management of remote clients only3. Installs VPN (both Remote Access VPN and site-to-site VPN)<br/> |
| [**Set**](set-ps-remoteaccess.md)                                                     | This cmdlet modifies configuration that is common to both DirectAccess and VPN viz. the following1. SSL certificate2. Internal interface 3. Internet interface<br/>                                                                                                                                              |
| [**Uninstall**](uninstall-ps-remoteaccess.md)                                         | This cmdlet uninstalls DirectAccess and VPN (both remote access VPN and site-to-site VPN)<br/>                                                                                                                                                                                                                   |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





