---
title: ISCSI\_LoginOptions structure
description: The ISCSI\_LoginOptions structure defines the characteristics of a logon session. The LoginToTarget\_IN routines use these defined characteristics while it logs into an iSCSI target.
ms.assetid: 2440999a-e10c-4a27-b076-a0b640c2ca7f
keywords:
- ISCSI_LoginOptions structure Storage Devices
- PISCSI_LoginOptions structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_LoginOptions
api_location:
- iscsidef.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ISCSI\_LoginOptions structure

The ISCSI\_LoginOptions structure defines the characteristics of a logon session. The LoginToTarget\_IN routines use these defined characteristics while it logs into an iSCSI target.

## Syntax


```C++
typedef struct _ISCSI_LoginOptions {
  ULONG InformationSpecified;
  ULONG HeaderDigest;
  ULONG DataDigest;
  ULONG MaximumConnections;
  ULONG DefaultTime2Wait;
  ULONG DefaultTime2Retain;
  ULONG LoginFlags;
  ULONG AuthType;
} ISCSI_LoginOptions, *PISCSI_LoginOptions;
```



## Members

<dl> <dt>

**InformationSpecified**
</dt> <dd>

A bitmap that indicates which members of the ISCSI\_LoginOptions structure contain valid data. The following table describes the possible values:



| Bit                                                        | Description                                                                                                                                                                       |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ISCSI\_LOGIN\_OPTIONS\_HEADER\_DIGEST<br/>           | The **HeaderDigest** member specifies the type of digest that is used to guarantee the integrity of header data. <br/>                                                      |
| ISCSI\_LOGIN\_OPTIONS\_DATA\_DIGEST<br/>             | The **DataDigest** member specifies the type of digest that is used to guarantee the integrity of header data.<br/>                                                         |
| ISCSI\_LOGIN\_OPTIONS\_MAXIMUM\_CONNECTIONS<br/>     | The **MaximumConnections** member specifies the maximum number of connections that are allowed in the iSCSI session. <br/>                                                  |
| ISCSI\_LOGIN\_OPTIONS\_DEFAULT\_TIME\_2\_WAIT<br/>   | The **DefaultTime2Wait** member specifies the minimum time to wait, in seconds, before the initiator attempts to reconnect or reassign a connection that was dropped. <br/> |
| ISCSI\_LOGIN\_OPTIONS\_DEFAULT\_TIME\_2\_RETAIN<br/> | The **DefaultTime2Retain** member specifies the maximum time that is allowed to reassign commands after the initial wait indicated in **DefaultTime2Wait**.<br/>            |
| ISCSI\_LOGIN\_OPTIONS\_AUTH\_TYPE<br/>               | The **AuthType** member specifies the type of authentication that establishes the logon session. <br/>                                                                      |
| ISCSI\_LOGIN\_OPTIONS\_USERNAME<br/>                 | The username to be used during logon. <br/>                                                                                                                                 |
| ISCSI\_LOGIN\_OPTIONS\_PASSWORD<br/>                 | The password to be used during logon. <br/>                                                                                                                                 |



 

</dd> <dt>

**HeaderDigest**
</dt> <dd>

A [**ISCSI\_DIGEST\_TYPES**](iscsi-digest-types.md) value that indicates the method that the initiator uses to verify the integrity of the header digest in a logon PDU.

</dd> <dt>

**DataDigest**
</dt> <dd>

A [**ISCSI\_DIGEST\_TYPES**](iscsi-digest-types.md) value that indicates the method that the initiator uses to verify the integrity of the data digest in a logon PDU.

</dd> <dt>

**MaximumConnections**
</dt> <dd>

A value between 1 and 65535 that specifies the maximum number of connections to target devices that can be associated with a single logon session. A value of 0 indicates that there is no limit to the number of connections.

</dd> <dt>

**DefaultTime2Wait**
</dt> <dd>

The minimum time to wait, in seconds, before the initiator attempts to reconnect or reassign a connection (or task) that has been dropped after an unexpected connection termination or reset. The initiator and target negotiate to determine this value.

</dd> <dt>

**DefaultTime2Retain**
</dt> <dd>

The maximum time, in seconds, to reassign a connection after the initial wait that is indicated in **DefaultTime2Wait** has elapsed. The initiator and target negotiate to determine this value.

</dd> <dt>

**LoginFlags**
</dt> <dd>

A bitwise OR of logon flags that define certain characteristics of the logon session. The following table indicates the values that you can assign to this member.



| Logon flag                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ISCSI\_LOGIN\_FLAG\_REQUIRE\_IPSEC<br/>            | The logon session must use the IPSec protocol.<br/>                                                                                                                                                                                                                                                                                                                  |
| ISCSI\_LOGIN\_FLAG\_MULTIPATH\_ENABLED<br/>        | Multipathing software is installed, so the iSCSI initiator service allows multiple sessions to the same target. <br/>                                                                                                                                                                                                                                                |
| ISCSI\_LOGIN\_FLAG\_RESERVED1<br/>                 | Microsoft internal use only. <br/>                                                                                                                                                                                                                                                                                                                                   |
| ISCSI\_LOGIN\_FLAG\_ALLOW\_PORTAL\_HOPPING<br/>    | If a target portal is not available for login, the initiator can "hop" through the list of target portals that it discovered and that can be used for login operations. That is, the initiator will continue to try the list of portals that are available until it finds one that can be used for login, so it can then log in to the available target portal.<br/> |
| ISCSI\_LOGIN\_FLAG\_USE\_RADIUS\_RESPONSE<br/>     | Use RADIUS to generate CHAP response. <br/>                                                                                                                                                                                                                                                                                                                          |
| ISCSI\_LOGIN\_FLAG\_USE\_RAIDUS\_VERIFICATION<br/> | Use RADIUS to verify CHAP response. <br/>                                                                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

**AuthType**
</dt> <dd>

A [**ISCSI\_AUTH\_TYPES**](iscsi-auth-types.md) value that indicates the authentication method that is used to establish a logon connection.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsidef.h (include Iscsidef.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_AUTH\_TYPES**](iscsi-auth-types.md)
</dt> <dt>

[**ISCSI\_DIGEST\_TYPES**](iscsi-digest-types.md)
</dt> <dt>

[ISCSI\_LoginOptions WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561543)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_LoginOptions%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






