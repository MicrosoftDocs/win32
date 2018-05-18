---
title: MSiSCSI\_RedirectPortalInfoClass structure
description: The MSiSCSI\_RedirectPortalInfoClass structure contains information about a collection of sessions for an adapter ID. It also contains the portal redirection information for each of the sessions.
ms.assetid: 'fcddf029-748b-4300-9f87-a103d961918a'
keywords: ["MSiSCSI_RedirectPortalInfoClass structure Storage Devices", "PMSiSCSI_RedirectPortalInfoClass structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSiSCSI_RedirectPortalInfoClass
api_location:
- iscsimgt.h
api_type:
- HeaderDef
---

# MSiSCSI\_RedirectPortalInfoClass structure

The MSiSCSI\_RedirectPortalInfoClass structure contains information about a collection of sessions for an adapter ID. It also contains the portal redirection information for each of the sessions.

## Syntax


```C++
typedef struct _MSiSCSI_RedirectPortalInfoClass {
  ULONGLONG                 UniqueAdapterId;
  ULONG                     SessionCount;
  ISCSI_RedirectSessionInfo RedirectSessionList[1];
} MSiSCSI_RedirectPortalInfoClass, *PMSiSCSI_RedirectPortalInfoClass;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID).

</dd> <dt>

**SessionCount**
</dt> <dd>

The number of sessions for which this structure contains information.

</dd> <dt>

**RedirectSessionList**
</dt> <dd>

An array of structures that contains as many ISCSI\_RedirectSessionInfo structures as specified in the connection count.

</dd> </dl>

## Remarks

You must implement this class if the adapter supports target portal hopping. Otherwise, it is optional.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_RedirectPortalInfoClass%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





