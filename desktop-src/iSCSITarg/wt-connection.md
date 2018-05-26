---
title: WT\_Connection class
description: Represents a connection from the initiator to the target.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 029a4689-c195-4243-bdc4-524375847bdd
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_Connection class iSCSI Software Target API
- WT_Connection class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_Connection
- WT_Connection.CID
- WT_Connection.TSIH
- WT_Connection.InitiatorIPAddress
- WT_Connection.InitiatorPort
- WT_Connection.TargetIPAddress
- WT_Connection.TargetPort
- WT_Connection.HeaderDigestEnabled
- WT_Connection.DataDigestEnabled
- WT_Connection.MaxReceiveDataSegmentLength
- WT_Connection.MaxTransmitDataSegmentLength
- WT_Connection.HeaderDigestMethod
- WT_Connection.DataDigestMethod
- WT_Connection.ReceivingMarkers
- WT_Connection.SendingMarkers
- WT_Connection.ActiveVersion
- WT_Connection.AuthenticationMethodUsed
- WT_Connection.IsMutualAuthentication
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_Connection class

Represents a connection from the initiator to the target.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_Connection
{
  uint16  CID;
  uint16  TSIH;
  string  InitiatorIPAddress;
  uint32  InitiatorPort;
  string  TargetIPAddress;
  uint32  TargetPort;
  boolean HeaderDigestEnabled;
  boolean DataDigestEnabled;
  uint32  MaxReceiveDataSegmentLength;
  uint32  MaxTransmitDataSegmentLength;
  uint16  HeaderDigestMethod;
  uint16  DataDigestMethod;
  boolean ReceivingMarkers;
  boolean SendingMarkers;
  uint8   ActiveVersion;
  uint16  AuthenticationMethodUsed;
  boolean IsMutualAuthentication;
};
```

## Members

The **WT\_Connection** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_Connection** class has these properties.

<dl> <dt>

**ActiveVersion**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Active version number of the iSCSI specification negotiated on this connection.

This is the iSCSI protocol version defined by RFC3720.

</dd> <dt>

**AuthenticationMethodUsed**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (None, SRP, CHAP, Kerberos), **ValueMap** (2, 3, 4, 5)
</dt> </dl>

Primary authentication method used on this connection.

The iSCSI Target only supports CHAP.

</dd> <dt>

**CID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The unique connection identifier. This identifier is only unique within the session context.

</dd> <dt>

**DataDigestEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flag indicating whether data digest is enabled on this connection.

</dd> <dt>

**DataDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Other, None, CRC32C), **ValueMap** (1, 2, 3)
</dt> </dl>

Primary data digest method.

</dd> <dt>

**HeaderDigestEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flag indicating whether header digest is enabled on this connection.

</dd> <dt>

**HeaderDigestMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** (Other, None, CRC32C), **ValueMap** (1, 2, 3)
</dt> </dl>

Primary header digest method.

</dd> <dt>

**InitiatorIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address (either IPv4 or IPv6) of the initiator that connects to the target.

</dd> <dt>

**InitiatorPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The TCP port of the initiator that connects to the target.

</dd> <dt>

**IsMutualAuthentication**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flag indicating whether mutual authentication is used on this connection.

</dd> <dt>

**MaxReceiveDataSegmentLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum receive data segment length that is supported.

</dd> <dt>

**MaxTransmitDataSegmentLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum transmit data segment length that is supported.

</dd> <dt>

**ReceivingMarkers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flag indicating whether receiving markers are in use.

</dd> <dt>

**SendingMarkers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flag indicating whether sending markers are in use.

</dd> <dt>

**TargetIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address (either IPv4 or IPv6) of the target that the initiator is connected to.

</dd> <dt>

**TargetPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The TCP port of the target that the initiator connects to.

</dd> <dt>

**TSIH**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The identifier of the session that this connection belongs to.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





