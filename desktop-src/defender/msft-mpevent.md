---
title: MSFT\_MpEvent class
description: Windows Defender Event Indication Class.
ms.assetid: a565e4e7-b7b7-45ce-90b4-f69f3ef9bc58
keywords:
- MSFT_MpEvent class
- MSFT_MpEvent class, described
topic_type:
- apiref
api_name:
- MSFT_MpEvent
- MSFT_MpEvent.CategoryDiscriminant
- MSFT_MpEvent.ScanNotificationsValue
- MSFT_MpEvent.ThreatNotificationsValue
- MSFT_MpEvent.SignatureNotificationsValue
- MSFT_MpEvent.ComputerNotificationsValue
- MSFT_MpEvent.NotificationTime
- MSFT_MpEvent.AdditionalData
api_location:
- ProtectionManagement.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_MpEvent class

Windows Defender Event Indication Class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_MpEvent
{
  uint32   CategoryDiscriminant;
  uint32   ScanNotificationsValue;
  uint32   ThreatNotificationsValue;
  uint32   SignatureNotificationsValue;
  uint32   ComputerNotificationsValue;
  DateTime NotificationTime;
  uint32   AdditionalData;
};
```

## Members

The **MSFT\_MpEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MpEvent** class has these properties.

<dl> <dt>

**AdditionalData**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional Data. At the moment, the only use is when the CategoryDiscriminant is equal to ThreatStateNotificationsthen this value will contains the ThreatID

</dd> <dt>

**CategoryDiscriminant**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Category of Notification.

</dd> <dt>

**ComputerNotificationsValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Detailed Computer Notifications.

</dd> <dt>

**NotificationTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the WMI Event was generated

</dd> <dt>

**ScanNotificationsValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Detailed Scan Notifications.

</dd> <dt>

**SignatureNotificationsValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Detailed Signature Notifications.

</dd> <dt>

**ThreatNotificationsValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Detailed Threat Notifications.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Defender<br/>                                                       |
| MOF<br/>                      | <dl> <dt>ProtectionManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ProtectionManagement.dll</dt> </dl> |



 

 





