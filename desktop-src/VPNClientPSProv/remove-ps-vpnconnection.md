---
title: Remove method of the PS\_VpnConnection class
description: Removes virtual private network (VPN) connection profiles from the Connection Manager phone book.
audience: developer
ms.assetid: b764ebf2-7228-4cae-a995-451e9d191f20
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_VpnConnection class
- PS_VpnConnection class, Remove method
topic_type:
- apiref
api_name:
- PS_VpnConnection.Remove
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_VpnConnection class

Removes virtual private network (VPN) connection profiles from the Connection Manager phone book.

## Syntax


```mof
static uint32 Remove(
  [in]  string          Name[],
  [in]  boolean         Force,
  [in]  boolean         PassThru,
  [in]  boolean         AllUserConnection,
  [out] VpnCommonConfig cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The names of the VPN connection profiles to remove.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the removal of the VPN connection profile from the phone book; otherwise, **false**.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the [**VpnConnection**](vpnconnection.md) object that contains the VPN configuration settings; otherwise, **false**.

</dd> <dt>

*AllUserConnection* \[in\]
</dt> <dd>

**True** if the VPN connection profile is for all users; **false** if it is for a single user.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnection**](vpnconnection.md) object.

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

[**PS\_VpnConnection**](ps-vpnconnection.md)
</dt> </dl>

 

 





