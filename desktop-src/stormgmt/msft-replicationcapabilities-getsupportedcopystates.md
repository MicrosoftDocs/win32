---
title: GetSupportedCopyStates method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, the supported copy states.
ms.assetid: A9E00172-F462-46B7-9738-D87593CFC341
keywords:
- GetSupportedCopyStates method Windows Storage Management API
- GetSupportedCopyStates method Windows Storage Management API , MSFT_ReplicationCapabilities class
- MSFT_ReplicationCapabilities class Windows Storage Management API , GetSupportedCopyStates method
topic_type:
- apiref
api_name:
- MSFT_ReplicationCapabilities.GetSupportedCopyStates
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

# GetSupportedCopyStates method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, the supported copy states.

## Syntax


```mof
UInt32 GetSupportedCopyStates(
  [in]  UInt16 ReplicationType,
  [out] UInt16 SupportedCopyStates[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the replication type. This must be in the enumeration [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).SupportedReplicationTypes.

</dd> <dt>

*SupportedCopyStates* \[out\]
</dt> <dd>

The supported copy states. One of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span><dl> <dt>**Initialized**</dt> <dt>2</dt> </dl>                              | The link to enable replication is established, and the source and target have been associated. However, the copy operation has not started.<br/>                                  |
| <span id="Unsynchronized"></span><span id="unsynchronized"></span><span id="UNSYNCHRONIZED"></span><dl> <dt>**Unsynchronized**</dt> <dt>3</dt> </dl>                  | Not all of the source data has been copied to the target.<br/>                                                                                                                    |
| <span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span><dl> <dt>**Synchronized**</dt> <dt>4</dt> </dl>                          | All of the source data has been copied to the target.<br/>                                                                                                                        |
| <span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span><dl> <dt>**Broken**</dt> <dt>5</dt> </dl>                                                  | The relationship is nonfunctional due to errors in the source, the target, the path between the two, or space constraints.<br/>                                                   |
| <span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span><dl> <dt>**Fractured**</dt> <dt>6</dt> </dl>                                      | The target is split from the source.<br/>                                                                                                                                         |
| <span id="Split"></span><span id="split"></span><span id="SPLIT"></span><dl> <dt>**Split**</dt> <dt>7</dt> </dl>                                                      | The target was gracefully (or systematically) split from the source in a way that ensures consistency.<br/>                                                                       |
| <span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span><dl> <dt>**Inactive**</dt> <dt>8</dt> </dl>                                          | The copy operation has stopped. Writes to the source will not be sent to the target.<br/>                                                                                         |
| <span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span><dl> <dt>**Suspended**</dt> <dt>9</dt> </dl>                                      | Data flow between the source and target has stopped. Writes to the source are held until the association is resumed.<br/>                                                         |
| <span id="Failedover"></span><span id="failedover"></span><span id="FAILEDOVER"></span><dl> <dt>**Failedover**</dt> <dt>10</dt> </dl>                                 | Reads from and writes to the target have failed. The source is not reachable.<br/>                                                                                                |
| <span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span><dl> <dt>**Prepared**</dt> <dt>11</dt> </dl>                                         | Initialization is completed, and the copy operation has started. However, the data flow has not started.<br/>                                                                     |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>12</dt> </dl>                                             | The copy operation was aborted. Use the Resync Replica operation to restart the copy operation.<br/>                                                                              |
| <span id="Skewed"></span><span id="skewed"></span><span id="SKEWED"></span><dl> <dt>**Skewed**</dt> <dt>13</dt> </dl>                                                 | The target has been modified and is no longer synchronized with the source or the point-in-time view.<br/>                                                                        |
| <span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span><dl> <dt>**Mixed**</dt> <dt>14</dt> </dl>                                                     | Applies to the *CopyState* of *GroupSynchronized*. It indicates that the *StorageSynchronized* associations of the elements in the groups have different *CopyState* values.<br/> |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span><dl> <dt>**Not Applicable**</dt> <dt>15</dt> </dl>                 | The target does not have a replication state.<br/>                                                                                                                                |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl> | This value is reserved for system use.<br/>                                                                                                                                       |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>       | These values are reserved for vendors.<br/>                                                                                                                                       |



 

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

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (..)
</dt> <dt>

**Vendor Specific** (0x8000..)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
</dt> </dl>

 

 





