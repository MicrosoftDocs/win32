---
title: EapConfiguration class
description: The EapConfiguration class represents an Extensible Authentication Protocol (EAP) configuration object.
audience: developer
ms.assetid: 0d34f4db-2199-4f03-86f0-6c3367cb61d6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EapConfiguration class
- EapConfiguration class, described
topic_type:
- apiref
api_name:
- EapConfiguration
- EapConfiguration.EapConfigXmlStream
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EapConfiguration class

The **EapConfiguration** class represents an Extensible Authentication Protocol (EAP) configuration object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class EapConfiguration
{
  string EapConfigXmlStream;
};
```

## Members

The **EapConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **EapConfiguration** class has these properties.

<dl> <dt>

**EapConfigXmlStream**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An XML stream that contains the detailed EAP configuration for the virtual private network (VPN) profile.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_EapConfiguration**](ps-eapconfiguration.md)
</dt> </dl>

 

 





