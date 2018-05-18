---
title: PS\_DhcpServerSetting class
description: Update DhcpServer settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0e6871bd-e736-42ee-ae4d-60c53ebab63e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerSetting class", "PS_DhcpServerSetting class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerSetting
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerSetting class

Update DhcpServer settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerSetting
{
};
```

## Members

The **PS\_DhcpServerSetting** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerSetting** class has these methods.



| Method                                  | Description                                                                     |
|:----------------------------------------|:--------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserversetting.md) | Gets the configuration parameters of the database of the DHCP server<br/> |
| [**Set**](set-ps-dhcpserversetting.md) | Sets a server level configuration parameter for the DHCP server<br/>      |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





