---
title: UFS\_PURGE\_STATUS enumeration
description: Specifies the current status of a purge operation.
ms.assetid: 9BC978A9-FA5E-4A1E-9775-1DC9C270F5DC
keywords:
- UFS_PURGE_STATUS enumeration Storage Devices
topic_type:
- apiref
api_name:
- UFS_PURGE_STATUS
api_location:
- Ufs.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UFS\_PURGE\_STATUS enumeration

Specifies the current status of a purge operation.

## Syntax


```C++
typedef enum _UFS_PURGE_STATUS { 
  UFS_PurgeStatusIdle           = 0,
  UFS_PurgeStatusInProgress     = 1,
  UFS_PurgeStatusInterrupted    = 2,
  UFS_PurgeStatusSuccess        = 3,
  UFS_PurgeStatusQueueNotEmpty  = 4,
  UFS_PurgeStatusFailure        = 5
} UFS_PURGE_STATUS;
```



## Constants

<dl> <dt>

<span id="UFS_PurgeStatusIdle"></span><span id="ufs_purgestatusidle"></span><span id="UFS_PURGESTATUSIDLE"></span>**UFS\_PurgeStatusIdle**
</dt> <dd>

The status of the purge operation has already been read but was not returned.

</dd> <dt>

<span id="UFS_PurgeStatusInProgress"></span><span id="ufs_purgestatusinprogress"></span><span id="UFS_PURGESTATUSINPROGRESS"></span>**UFS\_PurgeStatusInProgress**
</dt> <dd>

The purge operation is currently in progress.

</dd> <dt>

<span id="UFS_PurgeStatusInterrupted"></span><span id="ufs_purgestatusinterrupted"></span><span id="UFS_PURGESTATUSINTERRUPTED"></span>**UFS\_PurgeStatusInterrupted**
</dt> <dd>

The current purge operation was interrupted.

</dd> <dt>

<span id="UFS_PurgeStatusSuccess"></span><span id="ufs_purgestatussuccess"></span><span id="UFS_PURGESTATUSSUCCESS"></span>**UFS\_PurgeStatusSuccess**
</dt> <dd>

The current purge operation was successful.

</dd> <dt>

<span id="UFS_PurgeStatusQueueNotEmpty"></span><span id="ufs_purgestatusqueuenotempty"></span><span id="UFS_PURGESTATUSQUEUENOTEMPTY"></span>**UFS\_PurgeStatusQueueNotEmpty**
</dt> <dd>

The current purge operation failed due to the logical queue being not empty.

</dd> <dt>

<span id="UFS_PurgeStatusFailure"></span><span id="ufs_purgestatusfailure"></span><span id="UFS_PURGESTATUSFAILURE"></span>**UFS\_PurgeStatusFailure**
</dt> <dd>

The current purge operation failed.

</dd> </dl>

## Remarks

When the **UFS\_PURGE\_STATUS** is equal to the values 2, 3, 4, or 5, the **UFS\_PURGE\_STATUS** is automatically cleared to **UFS\_PurgeStatusIdle** the first time that it is read.

## Requirements



|                   |                                                                                  |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ufs.h</dt> </dl> |



## See also

<dl> <dt>

[**UFS\_ATTRIBUTES\_DESCRIPTOR**](ufs-attributes-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_PURGE_STATUS%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






