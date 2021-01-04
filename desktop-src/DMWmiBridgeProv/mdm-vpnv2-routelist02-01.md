---
title: MDM_VPNv2_RouteList02_01 class
description: The MDM\_VPNv2\_RouteList02\_01 class contains an optional list of routes to be added to the routing table for the VPN interface.
ms.assetid: 4271b0c4-9d29-4148-b956-ac9306316c9b
keywords:
- MDM_VPNv2_RouteList02_01 class
- MDM_VPNv2_RouteList02_01 class, described
topic_type:
- apiref
api_name:
- MDM_VPNv2_RouteList02_01
- MDM_VPNv2_RouteList02_01.InstanceID
- MDM_VPNv2_RouteList02_01.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_VPNv2\_RouteList02\_01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_VPNv2\_RouteList02\_01** class contains an optional list of routes to be added to the routing table for the VPN interface.

This is required for split tunneling case where the VPN server site has more subnets that the default subnet based on the IP assigned to the interface.

Every computer that runs TCP/IP makes routing decisions. These decisions are controlled by the IP routing table. Adding values under this node updates the routing table with routes for the VPN interface post connection. The values under this node represent the destination prefix of IP routes. A destination prefix consists of an IP address prefix and a prefix length.

Adding a route here allows the networking stack to identify the traffic that needs to go over the VPN interface for split tunnel VPN. Some VPN servers can configure this during connect negotiation and do not need this information in the VPN Profile. Please check with your VPN server administrator to determine whether you need this information in the VPN profile.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system", "local-user"), dynamic, provider("DMWmiBridgeProv")]
class MDM_VPNv2_RouteList02_01
{
  string InstanceID;
  string ParentID;
  string Address;
  sint32 PrefixSize;
};
```

## Members

The **MDM\_VPNv2\_RouteList02\_01** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_VPNv2\_RouteList02\_01** class has these properties.

<dl> <dt>

[Address](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-routelist-routerowid-address)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

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

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/VPNv2/*ProfileName*/RouteList"

</dd> <dt>

[PrefixSize](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-routelist-routerowid-prefixsize)
</dt> <dd> <dl> <dt>

Data type: **sint32**
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

 

