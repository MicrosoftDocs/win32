---
Description: 'The MSIscsiInitiator\_SessionClass structure describes the characteristics of a session and provides methods that allow the creation and management of connections within the session established by the Initiator.'
ms.assetid: '6f116e76-7c62-46ba-bb8f-ea23e1d8fa87'
title: 'MSIscsiInitiator\_SessionClass class'
---

# MSIscsiInitiator\_SessionClass class

The **MSIscsiInitiator\_SessionClass** structure describes the characteristics of a session and provides methods that allow the creation and management of connections within the session established by the Initiator.

## Syntax

``` syntax
class MSIscsiInitiator_SessionClass
{
  string                                 SessionId;
  string                                 InitiatorName;
  string                                 TargetNodeName;
  string                                 TargetName;
  uint8                                  ISID[];
  uint8                                  TSID[];
  MSIscsiInitiator_ConnectionInformation ConnectionInformation[];
  MSIscsiInitiator_DeviceOnSession       Devices[];
};
```

## Members

The **MSIscsiInitiator\_SessionClass** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSIscsiInitiator\_SessionClass** class has these methods.



| Method                                                                             | Description                                        |
|:-----------------------------------------------------------------------------------|:---------------------------------------------------|
| [**AddConnection**](addconnection-msiscsiinitiator-sessionclass.md)               | Add a connection to the session.<br/>        |
| [**Logout**](logout-msiscsiinitiator-sessionclass.md)                             | Log an iSCSI Target out of the session.<br/> |
| [**RemoveConnection**](removeconnection-msiscsiinitiator-sessionclass.md)         | Remove a connection from the session.<br/>   |
| [**SendScsiInquiry**](sendscsiinquiry-msiscsiinitiator-sessionclass.md)           | Send the SCSI Inquiry command.<br/>          |
| [**SendScsiReadCapacity**](sendscsireadcapacity-msiscsiinitiator-sessionclass.md) | Send the SCSI Read Capacity command.<br/>    |
| [**SendScsiReportLuns**](sendscsireportluns-msiscsiinitiator-sessionclass.md)     | Send the SCSI Report LUNs command.<br/>      |



 

### Properties

The **MSIscsiInitiator\_SessionClass** class has these properties.

<dl> <dt>

**ConnectionInformation**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_ConnectionInformation** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An [**MSIscsiInitiator\_ConnectionInformation**](msiscsiinitiator-connectioninformation.md) structure containing data that indicates the number of connections associated with the session.

</dd> <dt>

**Devices**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_DeviceOnSession** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An [**MSIscsiInitiator\_DeviceOnSession**](msiscsiinitiator-deviceonsession.md) structure containing information about the devices exposed by the session.

</dd> <dt>

**InitiatorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Initiator name.

</dd> <dt>

**ISID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Initiator-side identifier (ISID) used in the iSCSI protocol.

</dd> <dt>

**SessionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The Unique Identifier associated with the session.

</dd> <dt>

**TargetName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the target.

</dd> <dt>

**TargetNodeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the target node.

</dd> <dt>

**TSID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Target-side identifier (TSID) used in the iSCSI protocol.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




