---
title: ISCSI\_SessionStaticInfo structure
description: The ISCSI\_SessionStaticInfo structure provides information about the characteristics of an iSCSI session.
ms.assetid: c652268f-4a31-4ec1-a668-8700cb7f4e1b
keywords:
- ISCSI_SessionStaticInfo structure Storage Devices
- PISCSI_SessionStaticInfo structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_SessionStaticInfo
api_location:
- iscsimgt.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ISCSI\_SessionStaticInfo structure

The ISCSI\_SessionStaticInfo structure provides information about the characteristics of an iSCSI session.

## Syntax


```C++
typedef struct _ISCSI_SessionStaticInfo {
  ULONGLONG                  UniqueSessionId;
  WCHAR                      InitiatoriSCSIName[223 + 1];
  WCHAR                      TargetiSCSIName[223 + 1];
  USHORT                     TSID;
  UCHAR                      ISID[6];
  BOOLEAN                    InitialR2t;
  BOOLEAN                    ImmediateData;
  UCHAR                      Type;
  BOOLEAN                    DataSequenceInOrder;
  BOOLEAN                    DataPduInOrder;
  UCHAR                      ErrorRecoveryLevel;
  ULONG                      MaxOutstandingR2t;
  ULONG                      FirstBurstLength;
  ULONG                      MaxBurstLength;
  ULONG                      MaxConnections;
  USHORT                     ConnectionCount;
  ISCSI_ConnectionStaticInfo ConnectionsList[1];
} ISCSI_SessionStaticInfo, *PISCSI_SessionStaticInfo;
```



## Members

<dl> <dt>

**UniqueSessionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the session. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in their UniqueSessionId parameter. Do not confuse this value with the values in the **ISID** and **TSID** members.

</dd> <dt>

**InitiatoriSCSIName**
</dt> <dd>

A wide character string that specifies the initiator node name.

</dd> <dt>

**TargetiSCSIName**
</dt> <dd>

A wide character string that specifies the node name of the target.

</dd> <dt>

**TSID**
</dt> <dd>

An internal value that specifies the portion of the iSCSI session ID that the target provides. The iSCSI protocol uses TSID together with ISID to identify the session. Do not confuse TSID with the session ID that **UniqueSessionId** specifies.

</dd> <dt>

**ISID**
</dt> <dd>

An internal value that specifies the portion of the iSCSI session ID that the initiator provides.

</dd> <dt>

**InitialR2t**
</dt> <dd>

A Boolean value that indicates if the initiator must wait for a ready-to-send (R2T) request before sending data to the target. If this member is **TRUE**, the initiator must wait for a ready-to-send (R2T) request before sending data to the target. If this member is **FALSE**, the initiator can send unsolicited data within limits that the value of **FirstBurstLength** specifies.

</dd> <dt>

**ImmediateData**
</dt> <dd>

A Boolean value that indicates if the initiator and target have agreed to allow the transmission of immediate data in the session. (*Immediate data* is data that the initiator piggybacks onto an iSCSI command PDU.) If this member is **TRUE**, the initiator and target have agreed to allow the transmission of immediate data in this session.

</dd> <dt>

**Type**
</dt> <dd>

An [ISCSI\_SESSION\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561567) enumeration value that specifies the type of logon session.



| Type                             | Meaning                                                              |
|----------------------------------|----------------------------------------------------------------------|
| discoverySession<br/>      | Session is being used only for discovery.<br/>                 |
| informationtalSession<br/> | Session is being used for a limited set of SCSI commands.<br/> |
| dataSession<br/>           | Session is being used as a full feature session.<br/>          |
| bootSession<br/>           | Session is being used to boot from target.<br/>                |



 

</dd> <dt>

**DataSequenceInOrder**
</dt> <dd>

A Boolean value that indicates whether sequences of data PDUs must be transmitted by using continuously increasing offsets, except during error recovery. If this member is **TRUE**, sequences of data PDUs must be transmitted by using continuously increasing offsets, except during error recovery. If this member is **FALSE**, sequences of data PDUs can be transmitted in any order.

The value in **DataSequenceInOrder** indicates the ordering of the sequences themselves, not the ordering of the data PDUs within each sequence. The **DataPduInOrder** member indicates the ordering of the data PDUs within each sequence.

</dd> <dt>

**DataPduInOrder**
</dt> <dd>

A Boolean value that indicates whether the data PDUs within a sequence of data PDUs must be located at continuously increasing addresses. If this member is **TRUE**, the data PDUs within a sequence of data PDUs must be located at continuously increasing addresses, with no gaps or overlay between PDUs. If this member is **FALSE**, the data PDUs within each sequence can be in any order.

</dd> <dt>

**ErrorRecoveryLevel**
</dt> <dd>

The level of error recovery that the initiator and the target negotiated. Higher numbers represent more elaborate recovery schemes. Currently, this member must be 0 or ULONG\_VALUE\_UNKNOWN.

</dd> <dt>

**MaxOutstandingR2t**
</dt> <dd>

The maximum number of outstanding ready-to-transmit (R2T) requests that are allowed for each task within this session.

</dd> <dt>

**FirstBurstLength**
</dt> <dd>

The maximum amount of unsolicited data, in bytes, that you can send within this session.

</dd> <dt>

**MaxBurstLength**
</dt> <dd>

The maximum number of bytes that you can send within a single sequence of Data-In or Data-Out PDUs.

</dd> <dt>

**MaxConnections**
</dt> <dd>

The maximum number of connections that are allowed within this session.

</dd> <dt>

**ConnectionCount**
</dt> <dd>

The number of connections that currently belong to this session.

</dd> <dt>

**ConnectionsList**
</dt> <dd>

A variable length array of [**ISCSI\_ConnectionStaticInfo**](iscsi-connectionstaticinfo.md) structures that specifies the static configuration data for each connection that is associated with this session. **ConnectionCount** indicates the number of elements in the array.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[**ISCSI\_ConnectionStaticInfo**](iscsi-connectionstaticinfo.md)
</dt> <dt>

[**LOGINSESSIONTYPE**](loginsessiontype.md)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_SessionStaticInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






