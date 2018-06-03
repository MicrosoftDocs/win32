---
title: MDM\_SecurityStatusUser class
description: Represents security health metrics on the device that are specific to the user.
ms.assetid: 8b130592-9eff-4bc5-a05c-ea22150afd23
keywords:
- MDM_SecurityStatusUser class MDM Settings
- MDM_SecurityStatusUser class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_SecurityStatusUser
- MDM_SecurityStatusUser.key
- MDM_SecurityStatusUser.HasConnectedAccount
- MDM_SecurityStatusUser.ConnectedAccountPolicy
- MDM_SecurityStatusUser.PasswordStatus
- MDM_SecurityStatusUser.EncryptionStatus
- MDM_SecurityStatusUser.DeviceEncryptionPolicy
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MDM\_SecurityStatusUser class

Represents security health metrics on the device that are specific to the user.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_SecurityStatusUser
{
  uint32  key;
  boolean HasConnectedAccount;
  uint32  ConnectedAccountPolicy;
  uint32  PasswordStatus;
  uint32  EncryptionStatus;
  uint32  DeviceEncryptionPolicy;
};
```

## Members

The **MDM\_SecurityStatusUser** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_SecurityStatusUser** class has these properties.

<dl> <dt>

**ConnectedAccountPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets whether to require the policy for the connected account.

The following list shows the possible values.

<dt>

<span id="Don_t_require"></span><span id="don_t_require"></span><span id="DON_T_REQUIRE"></span>

**Don't require** (0)


</dt> <dd></dd> <dt>

<span id="Require"></span><span id="require"></span><span id="REQUIRE"></span>

**Require** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**DeviceEncryptionPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets whether to require the encryption policy for the device.

The following list shows the possible values.

<dt>

<span id="Don_t_require"></span><span id="don_t_require"></span><span id="DON_T_REQUIRE"></span>

**Don't require** (0)


</dt> <dd></dd> <dt>

<span id="Require"></span><span id="require"></span><span id="REQUIRE"></span>

**Require** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**EncryptionStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the status of the device encryption as reported by the result of the [**EasClientSecurityPolicy.CheckCompliance**](https://msdn.microsoft.com/library/windows/apps/hh701410) method.

</dd> <dt>

**HasConnectedAccount**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets whether the connected account is present.

</dd> <dt>

**key**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the instance of the **MDM\_SecurityStatusUser** class.

</dd> <dt>

**PasswordStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the status of the password for the account.

The following list shows the possible values.

<dt>

<span id="Not_compliant"></span><span id="not_compliant"></span><span id="NOT_COMPLIANT"></span>

**Not compliant** (0)


</dt> <dd></dd> <dt>

<span id="No_policy"></span><span id="no_policy"></span><span id="NO_POLICY"></span>

**No policy** (1)


</dt> <dd></dd> <dt>

<span id="Compliant"></span><span id="compliant"></span><span id="COMPLIANT"></span>

**Compliant** (2)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_SecurityStatus**](https://msdn.microsoft.com/library/dn610394)
</dt> </dl>

 

 





