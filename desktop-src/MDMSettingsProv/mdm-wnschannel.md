---
title: MDM\_WNSChannel class
description: Represents the Windows Notification Service (WNS) channel used for notifications to the MDM agent.
ms.assetid: 20a72a55-8d0a-4c99-b6d2-450ab318b439
keywords:
- MDM_WNSChannel class MDM Settings
- MDM_WNSChannel class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_WNSChannel
- MDM_WNSChannel.AppId
- MDM_WNSChannel.UserSID
- MDM_WNSChannel.Channel
- MDM_WNSChannel.ExpirationTime
- MDM_WNSChannel.ChannelStatus
- MDM_WNSChannel.LastError
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_WNSChannel class

Represents the Windows Notification Service (WNS) channel used for notifications to the MDM agent.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_WNSChannel
{
  string   AppId;
  string   UserSID;
  string   Channel;
  datetime ExpirationTime;
  uint32   ChannelStatus;
  uint32   LastError;
};
```

## Members

The **MDM\_WNSChannel** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_WNSChannel** class has these properties.

<dl> <dt>

**AppId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the MDM application.

</dd> <dt>

**Channel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the channel created for WNS notifications for the MDM user on this device.

</dd> <dt>

**ChannelStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The WNS channel creation status.

<dt>



 (0)


</dt> <dd></dd> <dt>



 (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**ExpirationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The expiration time for the WNS channel.

</dd> <dt>

**LastError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error code reported if WNS channel creation fails.

</dd> <dt>

**UserSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The security identifier (SID) of the enrolled user.

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

 

 





