---
title: LOGINSESSIONTYPE enumeration
description: The LOGINSESSIONTYPE enumeration indicates the type of logon session.
ms.assetid: '838c2371-c1f3-4415-a624-fab1d8c15d0d'
keywords: ["LOGINSESSIONTYPE enumeration Storage Devices", "PLOGINSESSIONTYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- LOGINSESSIONTYPE
api_location:
- iscsiop.h
api_type:
- HeaderDef
---

# LOGINSESSIONTYPE enumeration

The LOGINSESSIONTYPE enumeration indicates the type of logon session.

## Syntax


```C++
typedef enum  { 
  ISCSI_LOGINTARGET_DISCOVERY      = 0,
  ISCSI_LOGINTARGET_INFORMATIONAL  = 1,
  ISCSI_LOGINTARGET_DATA           = 2
} LOGINSESSIONTYPE, *PLOGINSESSIONTYPE;
```



## Constants

<dl> <dt>

<span id="ISCSI_LOGINTARGET_DISCOVERY"></span><span id="iscsi_logintarget_discovery"></span>**ISCSI\_LOGINTARGET\_DISCOVERY**
</dt> <dd>

The logon session is for discovery only. Initiators use this type of session to discover targets with the **SendTargets** command. The initiator must already have access to at least one target IP address and one target port (target portal information).

</dd> <dt>

<span id="ISCSI_LOGINTARGET_INFORMATIONAL"></span><span id="iscsi_logintarget_informational"></span>**ISCSI\_LOGINTARGET\_INFORMATIONAL**
</dt> <dd>

The logon session is for informational purposes only. Initiators use this type of session to send SCSI commands that query for information. Management software can use informational sessions to query for information by calling the **SendScsiReportLuns** and **SendScsiReadCapacity** user-mode library routines.

This type of session does not support transmission of user data, and the Plug and Play (PnP) manager does not enumerate target logical units (LUNs) for the storage stack of the initiator node.

</dd> <dt>

<span id="ISCSI_LOGINTARGET_DATA"></span><span id="iscsi_logintarget_data"></span>**ISCSI\_LOGINTARGET\_DATA**
</dt> <dd>

The logon session is full-featured. It reports the target LUNs to the PnP manager on the (local) initiator node for enumeration. After enumerating these LUNs, the operating system can access them for data transfers, just as it would with local LUNs.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20LOGINSESSIONTYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






