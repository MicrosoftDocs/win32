---
title: PS\_VpnS2SInterface class
description: Represents a site-to-site VPN interface.
audience: developer
ms.assetid: 3d75f881-b98e-4ab3-9f8a-2b14871d0b68
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnS2SInterface class
- PS_VpnS2SInterface class, described
topic_type:
- apiref
api_name:
- PS_VpnS2SInterface
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_VpnS2SInterface class

Represents a site-to-site VPN interface.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_VpnS2SInterface
{
};
```

## Members

The **PS\_VpnS2SInterface** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnS2SInterface** class has these methods.



| Method                                                                | Description                                                                                                                                                  |
|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddByCustomPolicy**](addbycustompolicy-ps-vpns2sinterface.md)     | This cmdlet is used to create a S2S interface with the specified parameters.<br/>                                                                      |
| [**AddByEncryptionType**](addbyencryptiontype-ps-vpns2sinterface.md) | This cmdlet is used to create a S2S interface with the specified parameters.<br/>                                                                      |
| [**AddGreInterface**](ps-vpns2sinterface-addgreinterface.md)         | Creates an S2S interface.<br/> **Windows Server 2012 R2 and Windows Server 2012:** This method is not supported before Windows Server 2016.<br/> |
| [**Connect**](connect-ps-vpns2sinterface.md)                         | This cmdlet is used to connect a S2S interface that is currently not connected.<br/>                                                                   |
| [**Disconnect**](disconnect-ps-vpns2sinterface.md)                   | This cmdlet is used to disconnect a S2S interface that is currently connected.<br/>                                                                    |
| [**Get**](get-ps-vpns2sinterface.md)                                 | This cmdlet is used to retrieve details of a S2S interface.<br/>                                                                                       |
| [**Remove**](remove-ps-vpns2sinterface.md)                           | This cmdlet is used to remove a S2S interface.<br/>                                                                                                    |
| [**SetByCustomPolicy**](setbycustompolicy-ps-vpns2sinterface.md)     | This cmdlet is used to modify parameters a S2S interface. If the interface is already connected, the changes take effect after disconnection.<br/>     |
| [**SetByEncryptionType**](setbyencryptiontype-ps-vpns2sinterface.md) | This cmdlet is used to modify parameters a S2S interface. If the interface is already connected, the changes take effect after disconnection.<br/>     |
| [**SetGreInterface**](ps-vpns2sinterface-setgreinterface.md)         | Modifies a GRE interface.<br/> **Windows Server 2012 R2 and Windows Server 2012:** This method is not supported before Windows Server 2016.<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





