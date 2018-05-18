---
title: MDM\_DeviceRegistrationInfo class
description: This class provides device registration details.
ms.assetid: '75cc6ba1-e166-410e-85ad-dbf9f6f74f08'
keywords: ["MDM_DeviceRegistrationInfo class MDM Settings", "MDM_DeviceRegistrationInfo class MDM Settings , described"]
topic_type:
- apiref
api_name:
- MDM_DeviceRegistrationInfo
- MDM_DeviceRegistrationInfo.DeviceId
- MDM_DeviceRegistrationInfo.UPN
- MDM_DeviceRegistrationInfo.CertificateThumbprint
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
---

# MDM\_DeviceRegistrationInfo class

This class provides device registration details.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_DeviceRegistrationInfo
{
  string DeviceId;
  string UPN;
  string CertificateThumbprint;
};
```

## Members

The **MDM\_DeviceRegistrationInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_DeviceRegistrationInfo** class has these properties.

<dl> <dt>

**CertificateThumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The thumb print of the Active Directory certificate for device registration.

</dd> <dt>

**DeviceId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The identity of the device in the Active Directory device registration record.

</dd> <dt>

**UPN**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user principle name (UPN) of the registered user.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





