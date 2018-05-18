---
title: ISCSI\_RedirectSessionInfo structure
description: This ISCSI\_RedirectSessionInfo structure contains information about an iSCSI session and its portal information resulted from iSCSI target redirection.
ms.assetid: 'e3980ac7-b539-4a8f-9869-14d418ebe1e7'
keywords: ["ISCSI_RedirectSessionInfo structure Storage Devices", "PISCSI_RedirectSessionInfo structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_RedirectSessionInfo
api_location:
- iscsimgt.h
api_type:
- HeaderDef
---

# ISCSI\_RedirectSessionInfo structure

This ISCSI\_RedirectSessionInfo structure contains information about an iSCSI session and its portal information resulted from iSCSI target redirection.

## Syntax


```C++
typedef struct _ISCSI_RedirectSessionInfo {
  ULONGLONG                UniqueSessionId;
  ULONG                    TargetPortalGroupTag;
  ULONG                    ConnectionCount;
  ISCSI_RedirectPortalInfo RedirectPortalList[1];
} ISCSI_RedirectSessionInfo, *PISCSI_RedirectSessionInfo;
```



## Members

<dl> <dt>

**UniqueSessionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the session. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in their UniqueSessionId parameter. Do not confuse this value with the values in the ISID and TSID members.

</dd> <dt>

**TargetPortalGroupTag**
</dt> <dd>

Target portal group tag for this session Id.

</dd> <dt>

**ConnectionCount**
</dt> <dd>

Number of connections for each session.

</dd> <dt>

**RedirectPortalList**
</dt> <dd>

This provides the redirection information, and it has as many entries as the number of connections for each session.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_RedirectSessionInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






