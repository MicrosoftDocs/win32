---
title: MSFT\_SmbWitnessClient class
description: Represents an SMB witness client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'F2A78DC1-B1C3-47C3-9AE5-0F16C2CE11EF'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SmbWitnessClient class SMB", "MSFT_SmbWitnessClient class SMB , described"]
topic_type:
- apiref
api_name:
- MSFT_SmbWitnessClient
- MSFT_SmbWitnessClient.ClientName
- MSFT_SmbWitnessClient.WitnessNodeName
- MSFT_SmbWitnessClient.FileServerNodeName
- MSFT_SmbWitnessClient.NetworkName
- MSFT_SmbWitnessClient.ShareName
- MSFT_SmbWitnessClient.IpAddress
- MSFT_SmbWitnessClient.State
- MSFT_SmbWitnessClient.Flags
- MSFT_SmbWitnessClient.ResourcesMonitored
- MSFT_SmbWitnessClient.NotificationsSent
- MSFT_SmbWitnessClient.NotificationsCancelled
- MSFT_SmbWitnessClient.QueuedNotifications
api_location:
- WitnessWmiv2Provider.dll
api_type:
- DllExport
---

# MSFT\_SmbWitnessClient class

Represents an SMB witness client.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_SmbWitnessClient
{
  string ClientName;
  string WitnessNodeName;
  string FileServerNodeName;
  string NetworkName;
  string ShareName;
  string IpAddress;
  string State;
  uint32 Flags;
  uint32 ResourcesMonitored;
  uint32 NotificationsSent;
  uint32 NotificationsCancelled;
  uint32 QueuedNotifications;
};
```

## Members

The **MSFT\_SmbWitnessClient** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbWitnessClient** class has these methods.



| Method                                                  | Description                                                                                                                 |
|:--------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**MoveClient**](msft-smbwitnessclient--moveclient.md) | Moves an SMB witness client that is connected to a scale-out cluster node to a different scale-out cluster node.<br/> |



 

### Properties

The **MSFT\_SmbWitnessClient** class has these properties.

<dl> <dt>

**ClientName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The fully qualified domain name of the SMB witness client.

</dd> <dt>

**FileServerNodeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file server node name.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**BitMap**](https://msdn.microsoft.com/library/aa384827) ("1","2","3"), [**BitValues**](https://msdn.microsoft.com/library/aa384827) ("NetworkName","ShareName","Multichannel")
</dt> </dl>

The flags for the client.

**Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2012 R2 and Windows 8.1.

</dd> <dt>

**IpAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address for which the client needs to receive notifications.

</dd> <dt>

**NetworkName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The network name.

</dd> <dt>

**NotificationsCancelled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of notifications that have been canceled.

</dd> <dt>

**NotificationsSent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of notifications that have been sent to the client.

</dd> <dt>

**QueuedNotifications**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of notifications that are currently queued for the client.

</dd> <dt>

**ResourcesMonitored**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of resources that are currently being monitored for the client.

</dd> <dt>

**ShareName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The share name.

**Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2012 R2 and Windows 8.1.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of this witness registration.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**"Unknown"** (0)


</dt> <dd></dd> <dt>

<span id="Connected"></span><span id="connected"></span><span id="CONNECTED"></span>

**"Connected"** (1)


</dt> <dd></dd> <dt>

<span id="Registered"></span><span id="registered"></span><span id="REGISTERED"></span>

**"Registered"** (2)


</dt> <dd></dd> <dt>

<span id="Requested_notification"></span><span id="requested_notification"></span><span id="REQUESTED_NOTIFICATION"></span>

**"Requested notification"** (3)


</dt> <dd></dd> <dt>

<span id="Cancelled"></span><span id="cancelled"></span><span id="CANCELLED"></span>

**"Cancelled"** (4)


</dt> <dd></dd> <dt>

<span id="Disconnected"></span><span id="disconnected"></span><span id="DISCONNECTED"></span>

**"Disconnected"** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**WitnessNodeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The witness node name.

</dd> </dl>

## Remarks

SMB witness is a feature that does the following:

-   Accelerates recovery from an unplanned failure by alerting SMB clients that have registered for notification when a failure has occurred, rather than forcing the client to wait for a timeout.
-   Enables the system administrator to redirect a client from one cluster node to another in a SMB Scale-Out file server cluster to a different scale-out cluster node for load balancing or other administrative purposes.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\SmbWitness<br/>                                                        |
| MOF<br/>                      | <dl> <dt>SmbWitnessWmiv2Provider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WitnessWmiv2Provider.dll</dt> </dl>    |



## See also

<dl> <dt>

[SMB Management API](smb-management-api-portal.md)
</dt> </dl>

 

 





