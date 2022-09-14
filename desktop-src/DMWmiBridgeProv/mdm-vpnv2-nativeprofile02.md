---
title: MDM_VPNv2_NativeProfile02 class
description: The MDM\_VPNv2\_NativeProfile2 class defines profile information when using a Windows Inbox VPN Protocol (IKEv2, PPTP, L2TP).
ms.assetid: 50c4adc6-baef-437c-8223-9aeaaec813af
keywords:
- MDM_VPNv2_NativeProfile02 class
- MDM_VPNv2_NativeProfile02 class, described
topic_type:
- apiref
api_name:
- MDM_VPNv2_NativeProfile02
- MDM_VPNv2_NativeProfile02.InstanceID
- MDM_VPNv2_NativeProfile02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_VPNv2\_NativeProfile02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_VPNv2\_NativeProfile2** class defines profile information when using a Windows Inbox VPN Protocol (IKEv2, PPTP, L2TP).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[InPartition("local-system", "local-user"), dynamic, provider("DMWmiBridgeProv")]
class MDM_VPNv2_NativeProfile02
{
  string InstanceID;
  string ParentID;
  string Servers;
  string RoutingPolicyType;
  string NativeProtocolType;
  string L2tpPsk;
};
```

## Members

The **MDM\_VPNv2\_NativeProfile02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_VPNv2\_NativeProfile02** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node.

</dd> <dt>

[L2tpPsk](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-nativeprofile-l2tppsk)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[NativeProtocolType](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-nativeprofile-nativeprotocoltype)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/VPNv2/*ProfileName*"

</dd> <dt>

[RoutingPolicyType](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-trafficfilterlist-trafficfilterid-routingpolicytype)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Servers](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-nativeprofile-servers)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

