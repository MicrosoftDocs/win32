---
title: Discover method of the MSFT\_StorageProvider class
description: Discovers the objects that are owned by the storage provider.
ms.assetid: afafd4d5-c0c1-4461-814d-bf00de403b3f
keywords:
- Discover method Windows Storage Management API
- Discover method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , Discover method
topic_type:
- apiref
api_name:
- MSFT_StorageProvider.Discover
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Discover method of the MSFT\_StorageProvider class

Discovers the objects that are owned by the storage provider.

This method is used when a user needs to explicitly discover or re-enumerate objects owned by the storage provider. A call to this method will result in full or partial cache invalidation and over-the-wire calls to the storage subsystem to discover new or updated objects. Because this is an expensive task, this method should be used sparingly.

The scope of the discovery operation is controlled by the *DiscoveryLevel* and *RootObject* parameters. *DiscoveryLevel* controls the depth of the object discovery. *RootObject* defines the starting point from which discovery will happen.

## Syntax


```mof
UInt32 Discover(
  [in]  UInt16                 DiscoveryLevel,
  [in]  MSFT_StorageObject REF RootObject,
  [in]  Boolean                RunAsJob,
  [out] MSFT_StorageJob    REF CreatedStorageJob,
  [out] String                 ExtendedStatus
);
```



## Parameters

<dl> <dt>

*DiscoveryLevel* \[in\]
</dt> <dd>

The level (or depth) of discovery that should be performed. This parameter can only be specified if the root object is a storage provider, storage subsystem, or **NULL**. When specified, the storage provider will discover objects starting from **Level 0** and continuing until the specified level is reached. Associations between objects (within the discovered levels) will also be discovered.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="Level_0"></span><span id="level_0"></span><span id="LEVEL_0"></span><dl> <dt><strong>Level 0</strong></dt> <dt>0</dt> </dl></td>
<td>The storage provider, storage subsystem, and fileserver objects will be discovered.<br/>
<blockquote>
[!Note]<br />
<strong>Starting in Windows 10:</strong> Discovery of fileserver objects has been added.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><span id="Level_1"></span><span id="level_1"></span><span id="LEVEL_1"></span><dl> <dt><strong>Level 1</strong></dt> <dt>1</dt> </dl></td>
<td>Storage pools, file shares, resiliency settings, target ports, target portals, and initiator identifiers will be discovered.<br/>
<blockquote>
[!Note]<br />
<strong>Starting in Windows 10:</strong> Discovery of file shares has been added.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><span id="Level_2"></span><span id="level_2"></span><span id="LEVEL_2"></span><dl> <dt><strong>Level 2</strong></dt> <dt>2</dt> </dl></td>
<td>Virtual disks, volumes, partitions, disks, and masking sets will be discovered.<br/>
<blockquote>
[!Note]<br />
<strong>Starting in Windows 10:</strong> Discovery of volumes, partitions, and disks has been added.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><span id="Level_3"></span><span id="level_3"></span><span id="LEVEL_3"></span><dl> <dt><strong>Level 3</strong></dt> <dt>3</dt> </dl></td>
<td>Physical disks will be discovered.<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

*RootObject* \[in\]
</dt> <dd>

If this parameter is set, discovery will begin from this object. When *DiscoveryLevel* is **NULL**, well-defined actions will be taken depending on the type of object specified by *RootObject*:

-   Storage subsystem: All associated objects will be discovered.
-   Storage pool: The pool, along with any associated resiliency settings, virtual disks, and physical disks will be discovered.
-   Masking set: The masking set, along with any associated target ports, initiator identifiers, and virtual disks will be discovered.
-   For all other objects, only that object will be discovered or refreshed.

</dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**The storage provider does not support a required profile.** (46002)
</dt> <dt>

**The storage provider does not support a required association.** (46003)
</dt> <dt>

**Discover failed for the root object.** (46009 )
</dt> <dt>

**Discover failed on one or more subsystems.** (46010)
</dt> </dl>

## Remarks

Storage providers should complete **Level 0** discovery at start-up. The [**MSFT\_StorageProvider**](msft-storageprovider.md) and [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) objects should be loaded into cache.

For better performance, storage subsystems that have the **iSCSITargetCreationScheme** property set to **Auto** should do their discovery of target ports along with the virtual disks in **Level 2**. Note that target portals should still be discovered in **Level 1**.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageProvider**](msft-storageprovider.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





