---
title: MDM_EnterpriseAPN_01 class
description: The MDM\_EnterpriseAPN\_01 class is used by the enterprise to provision an APN for the Internet.
ms.assetid: c5fc0a86-98b7-4d0c-aae5-be836e48eee7
keywords:
- MDM_EnterpriseAPN_01 class
- MDM_EnterpriseAPN_01 class, described
topic_type:
- apiref
api_name:
- MDM_EnterpriseAPN_01
- MDM_EnterpriseAPN_01.InstanceID
- MDM_EnterpriseAPN_01.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_EnterpriseAPN\_01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_EnterpriseAPN\_01** class is used by the enterprise to provision an APN for the Internet.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_EnterpriseAPN_01
{
  string  InstanceID;
  string  ParentID;
  string  APNName;
  string  IPType;
  boolean IsAttachAPN;
  string  ClassId;
  string  AuthType;
  string  UserName;
  string  Password;
  string  IccId;
  boolean AlwaysOn;
  boolean Enabled;
  string  Roaming;
};
```

## Members

The **MDM\_EnterpriseAPN\_01** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_EnterpriseAPN\_01** class has these properties.

<dl> <dt>

[AlwaysOn](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-alwayson)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[APNName](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-apnname)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AuthType](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-authtype)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ClassId](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-classid)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Enabled](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-enabled)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[IccId](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-iccid)
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

Name of the connection as seen by Windows Connection Manager.

</dd> <dt>

[IPType](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-iptype)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[IsAttachAPN](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-isattachapn)
</dt> <dd> <dl> <dt>

Data type: **boolean**
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

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/EnterpriseAPN"

</dd> <dt>

[Password](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-password)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Roaming](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-roaming)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[UserName](/windows/client-management/mdm/enterpriseapn-csp#enterpriseapn-connectionname-username)
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

 

