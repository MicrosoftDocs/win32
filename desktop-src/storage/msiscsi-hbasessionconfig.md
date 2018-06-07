---
title: MSiSCSI\_HBASessionConfig structure
description: The MSiSCSI\_HBASessionConfig structure contains the default logon characteristics that a particular instance of a storage miniport driver uses to create a logon session with a target device.
ms.assetid: a97f39b7-9356-45f1-b0a2-bd18eb4c7467
keywords:
- MSiSCSI_HBASessionConfig structure Storage Devices
- PMSiSCSI_HBASessionConfig structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_HBASessionConfig
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

# MSiSCSI\_HBASessionConfig structure

The MSiSCSI\_HBASessionConfig structure contains the default logon characteristics that a particular instance of a storage miniport driver uses to create a logon session with a target device.

## Syntax


```C++
typedef struct _MSiSCSI_HBASessionConfig {
  BOOLEAN InitialR2T;
  BOOLEAN ImmediateData;
  ULONG   MaxRecvDataSegmentLength;
  ULONG   MaxBurstLength;
  ULONG   FirstBurstLength;
  ULONG   MaxOutstandingR2T;
} MSiSCSI_HBASessionConfig, *PMSiSCSI_HBASessionConfig;
```



## Members

<dl> <dt>

**InitialR2T**
</dt> <dd>

A Boolean value that indicates if the HBA initiator requests permission from the target to transmit unsolicited SCSI data whenever it establishes a new session. If this member is **TRUE**, the HBA initiator requests permission from the target to transmit unsolicited SCSI data whenever it establishes a new session. By default, the initiator does not transmit SCSI data until the target solicits the data by sending a ready-to-transmit (R2T) request, with a buffer offset of 0 and a desired transfer length equal to the minimum of the first burst size and the expected data transfer.

If **InitialR2T** is **TRUE**, the initiator sends a protocol data unit (PDU) to the target with the the string "No" in the InitialR2T key of the PDU. The target must respond by sending a PDU to the initiator with the string "No" in the InitialR2T key of the PDU. Both initiator and target must agree before unsolicited data transmission is allowed. Therefore, even if you set **InitialR2T** to **TRUE**, it does not guarantee that the initiator will be able to send unsolicited SCSI data to the target.

If this member is **FALSE**, all sessions that the initiator creates follow the default behavior. For more information about the InitialR2T key, see the *IP Storage Working Group* specification.

</dd> <dt>

**ImmediateData**
</dt> <dd>

A Boolean value that indicates if the initiator requests permission from the target to transmit immediate data whenever it establishes a new session. If this member is **TRUE**, the initiator requests permission from the target to transmit immediate data whenever it establishes a new session. (*Immediate data* is data that the initiator piggybacks onto an iSCSI command PDU.)

The session's policy with regard to immediate data is determined by a negotiation between the initiator and the target. For more information about how the values in **ImmediateData** and **InitialR2T** affect the negotiation, see the *IP Storage Working Group* specification.

</dd> <dt>

**MaxRecvDataSegmentLength**
</dt> <dd>

The maximum length, in bytes, of a PDU data segment.

</dd> <dt>

**MaxBurstLength**
</dt> <dd>

The maximum length, in bytes, of the SCSI data payload in a sequence of input (Data-In) PDUs or solicited output (Data-Out) PDUs.

</dd> <dt>

**FirstBurstLength**
</dt> <dd>

The maximum amount, in bytes, of unsolicited data that an initiator can send to a target during the execution of a single SCSI command. This amount includes the immediate data, if any, and the sequence of unsolicited Data-Out PDUs, if any, that follow the command.

</dd> <dt>

**MaxOutstandingR2T**
</dt> <dd>

The maximum number of outstanding R2T requests for each task, excluding the first R2T that initiates the task. An R2T is considered *outstanding* until the last data PDU (with the F bit set to 1) is transferred, or until a sequence reception time-out occurs for that PDU data sequence.

</dd> </dl>

## Remarks

It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[MSiSCSI\_HBASessionConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563022)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_HBASessionConfig%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






