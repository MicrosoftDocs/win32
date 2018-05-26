---
Description: This MSIscsiIIinitiator\_ConnectionInformation MOF class describes the characteristics of an iSCSI connection.
ms.assetid: 9f50ed92-816e-4f0e-a01f-ba46604aae57
title: MSIscsiInitiator\_ConnectionInformation class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSIscsiInitiator\_ConnectionInformation class

This **MSIscsiIIinitiator\_ConnectionInformation** MOF class describes the characteristics of an iSCSI connection.

## Syntax

``` syntax
class MSIscsiInitiator_ConnectionInformation
{
  string ConnectionID;
  string InitiatorAddress;
  string TargetAddress;
  uint16 InitiatorPort;
  uint16 TargetPort;
  uint8  CID[];
};
```

## Members

The **MSIscsiInitiator\_ConnectionInformation** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_ConnectionInformation** class has these properties.

<dl> <dt>

**CID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The iSCSI connection ID (CID) for this connection instance. The iSCSI protocol uses this value to identify the connection.

</dd> <dt>

**ConnectionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique ID associated with the connection. This value is returned by the [**MSIscsiInitiator\_SessionClass::AddConnection**](addconnection-msiscsiinitiator-sessionclass.md) method with the *UniqueConnectionID* parameter.

</dd> <dt>

**InitiatorAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the local network card that the initiator uses to connect to the network.

</dd> <dt>

**InitiatorPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port on the initiator that establishes the connection.

</dd> <dt>

**TargetAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the remote network card that this connection instance uses.

</dd> <dt>

**TargetPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The remote port number that the initiator uses to make a connection with the target.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSIscsiInitiator\_SessionClass::AddConnection**](addconnection-msiscsiinitiator-sessionclass.md)
</dt> </dl>

 

 




