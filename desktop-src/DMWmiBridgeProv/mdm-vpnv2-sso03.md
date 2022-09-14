---
title: MDM_VPNv2_Sso03 class
description: The MDM\_VPNv2\_Sso03 class can be used to select a certificate different from the VPN Authentication certificate for the Kerberos Authentication in the case of Device Compliance.
ms.assetid: 179b6b69-1319-4310-aebc-f61550af6c77
keywords:
- MDM_VPNv2_Sso03 class
- MDM_VPNv2_Sso03 class, described
topic_type:
- apiref
api_name:
- MDM_VPNv2_Sso03
- MDM_VPNv2_Sso03.InstanceID
- MDM_VPNv2_Sso03.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_VPNv2\_Sso03 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_VPNv2\_Sso03** class can be used to select a certificate different from the VPN Authentication certificate for the Kerberos Authentication in the case of Device Compliance.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system", "local-user"), dynamic, provider("DMWmiBridgeProv")]
class MDM_VPNv2_Sso03
{
  string  InstanceID;
  string  ParentID;
  boolean Enabled;
  string  IssuerHash;
  string  Eku;
};
```

## Members

The **MDM\_VPNv2\_Sso03** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_VPNv2\_Sso03** class has these properties.

<dl> <dt>

[Eku](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-nativeprofile-authentication-certificate-eku)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Enabled](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-devicecompliance-sso-enabled)
</dt> <dd> <dl> <dt>

Data type: **boolean**
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

[IssuerHash](/windows/client-management/mdm/vpnv2-csp#vpnv2-profilename-devicecompliance-sso-issuerhash)
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

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/VPNv2/*ProfileName*/DeviceCompliance"

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

 

