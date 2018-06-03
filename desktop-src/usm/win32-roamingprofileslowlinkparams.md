---
title: Win32\_RoamingProfileSlowLinkParams class
description: Represents the slow-link parameters for roaming profiles.
ms.assetid: 3c170e41-218e-44f7-80c4-6c5494575671
keywords:
- Win32_RoamingProfileSlowLinkParams class User State Manageability API
- Win32_RoamingProfileSlowLinkParams class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_RoamingProfileSlowLinkParams
- Win32_RoamingProfileSlowLinkParams.TimeOut
- Win32_RoamingProfileSlowLinkParams.ConnectionTransferRate
api_location:
- Root\CIMv2
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_RoamingProfileSlowLinkParams class

Represents the slow-link parameters for roaming profiles.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_RoamingProfileSlowLinkParams
{
  uint16 TimeOut;
  uint32 ConnectionTransferRate;
};
```

## Members

The **Win32\_RoamingProfileSlowLinkParams** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RoamingProfileSlowLinkParams** class has these properties.

<dl> <dt>

**ConnectionTransferRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The connection speed, in kilobytes per second (kbps). This threshold is used to determine if the connection is a slow link. If the server's transfer rate in kbps is less than this threshold, the connection is considered to be slow.

This property applies to IP networks.

</dd> <dt>

**TimeOut**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (20000)
</dt> </dl>

The slow-network connection timeout, in milliseconds. This threshold is used to determine if the connection is a slow link. If the delay in milliseconds is greater than this threshold, the connection is considered to be slow.

This property applies to non-IP networks.

</dd> </dl>

## Requirements



|                                     |                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                               |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                             |
| MOF<br/>                      | <dl> <dt>UserProfileConfigurationWmiProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_RoamingProfileMachineConfiguration**](win32-roamingprofilemachineconfiguration.md)
</dt> </dl>

 

 





