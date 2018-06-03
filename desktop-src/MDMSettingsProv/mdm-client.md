---
title: MDM\_Client class
description: Identifies and describes a user-device pair. It also provides methods unenrolling the device from management and for resetting the user's password.
ms.assetid: 0a3eb6be-c1c0-4205-b4b6-da82d1027817
keywords:
- MDM_Client class MDM Settings
- MDM_Client class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_Client
- MDM_Client.DeviceClientID
- MDM_Client.DomainSID
- MDM_Client.PlatformID
- MDM_Client.DeviceName
- MDM_Client.ProcessorDescription
- MDM_Client.UserSid
- MDM_Client.Version
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

# MDM\_Client class

Identifies and describes a user-device pair. It also provides methods unenrolling the device from management and for resetting the user's password.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_Client
{
  string DeviceClientID;
  string DomainSID;
  string PlatformID;
  string DeviceName;
  string ProcessorDescription;
  string UserSid;
  string Version;
};
```

## Members

The **MDM\_Client** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_Client** class has these methods.



| Method                                                                    | Description                                                                                                                                                                                  |
|:--------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LockWorkstation**](https://msdn.microsoft.com/library/dn610381)         | Locks the device.<br/> **Windows 10:** This method is currently not supported in Windows 10.<br/> **Windows 8:** This method is supported beginning with Windows 8.1.<br/> |
| [**ResetUserPassword**](https://msdn.microsoft.com/library/dn610403)     | Resets the user's password.<br/> **Windows 8:** This method is supported beginning with Windows 8.1 Update.<br/>                                                                 |
| [**SendUnenrollRequest**](https://msdn.microsoft.com/library/dn610404) | Unenrolls the device.<br/>                                                                                                                                                             |



 

### Properties

The **MDM\_Client** class has these properties.

<dl> <dt>

**DeviceClientID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the **MDM\_Client** class instance. This is a device ID.

</dd> <dt>

**DeviceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fully qualified domain name (FQDN) of the device.

</dd> <dt>

**DomainSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local workstation security identifier (SID).

</dd> <dt>

**PlatformID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The textual name of the local operating system.

</dd> <dt>

**ProcessorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The textual description of the main processor on the device.

</dd> <dt>

**UserSid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The security identifier (SID) of the local user account that is associated with the device.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local operating system version in the following format: *major*.*minor*.*revision*

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





