---
title: RequestStateChange method of the MSFT\_StorageJob class
description: Requests that the state of the job be changed to the value specified in the RequestedState parameter.
ms.assetid: 5259BE29-2B3C-4FED-9D99-14264751D898
keywords:
- RequestStateChange method Windows Storage Management API
- RequestStateChange method Windows Storage Management API , MSFT_StorageJob class
- MSFT_StorageJob class Windows Storage Management API , RequestStateChange method
topic_type:
- apiref
api_name:
- MSFT_StorageJob.RequestStateChange
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

# RequestStateChange method of the MSFT\_StorageJob class

Requests that the state of the job be changed to the value specified in the *RequestedState* parameter.

## Syntax


```mof
UInt32 RequestStateChange(
  [in]  UInt16 RequestedState,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

The new state.



| Value                                                                                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Start"></span><span id="start"></span><span id="START"></span><dl> <dt>**Start**</dt> <dt>2</dt> </dl>                                                    | This value changes the value of the **JobState** property to **Running**.<br/>                                                                                                                                                                                                                                |
| <span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span><dl> <dt>**Suspend**</dt> <dt>3</dt> </dl>                                            | This value stops the job temporarily. The intention is to subsequently restart the job with a second call to **RequestStateChange** with the *RequestedState* parameter set to **Start**. It might be possible for the job to enter the **Service** state while it is suspended. (This is job-specific.)<br/> |
| <span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span><dl> <dt>**Terminate**</dt> <dt>4</dt> </dl>                                    | This value stops the job cleanly, saving data, preserving the state, and shutting down all underlying processes in an orderly manner.<br/>                                                                                                                                                                    |
| <span id="Kill"></span><span id="kill"></span><span id="KILL"></span><dl> <dt>**Kill**</dt> <dt>5</dt> </dl>                                                        | This value terminates the job immediately with no requirement to save data or preserve the state.<br/>                                                                                                                                                                                                        |
| <span id="Service"></span><span id="service"></span><span id="SERVICE"></span><dl> <dt>**Service**</dt> <dt>6</dt> </dl>                                            | This value puts the job into a vendor-specific service state. It might be possible to restart the job.<br/>                                                                                                                                                                                                   |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>7..32767</dt> </dl>             | Values between 7 and 32767 (inclusive) are reserved for DMTF.<br/>                                                                                                                                                                                                                                            |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768..65535</dt> </dl> | Values between 32768 and 65535 (inclusive) are reserved for vendors.<br/>                                                                                                                                                                                                                                     |



 

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

**Size Not Supported** (4097)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> </dl>

## Remarks

If you call this method multiple times, earlier requests could be overwritten or lost.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageJob**](msft-storagejob.md)
</dt> </dl>

 

 





