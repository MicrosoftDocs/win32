---
title: MSFT\_VpnConnection class
description: The MSFT\_VpnConnection class provides a method to configure a virtual private network (VPN) connection profile.
audience: developer
ms.assetid: 8be81e82-55fd-4784-ba10-5431d76d40b8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_VpnConnection class
- MSFT_VpnConnection class, described
topic_type:
- apiref
api_name:
- MSFT_VpnConnection
- MSFT_VpnConnection.AllUserConnection
- MSFT_VpnConnection.Name
- MSFT_VpnConnection.Profile
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_VpnConnection class

The **MSFT\_VpnConnection** class provides a method to configure a virtual private network (VPN) connection profile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), InPartition("local-system", "local-user"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class MSFT_VpnConnection
{
  boolean AllUserConnection;
  string  Name;
  string  Profile;
};
```

## Members

The **MSFT\_VpnConnection** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_VpnConnection** class has these methods.



| Method                                | Description                                                                        |
|:--------------------------------------|:-----------------------------------------------------------------------------------|
| [**Set**](set-msft-vpnconnection.md) | Creates or modifies a virtual private network (VPN) connection profile.<br/> |



 

### Properties

The **MSFT\_VpnConnection** class has these properties.

<dl> <dt>

**AllUserConnection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

**True** if the VPN connection profile is for all users; **false** if it is for a single user.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the VPN connection profile.

</dd> <dt>

**Profile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serialized and encoded string form of the VPN connection profile.

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

[**VpnConnection**](vpnconnection.md)
</dt> </dl>

 

 





