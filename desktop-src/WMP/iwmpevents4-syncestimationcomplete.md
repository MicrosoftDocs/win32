---
title: IWMPEvents4 SyncEstimationComplete method
description: The SyncEstimationComplete event occurs when a size estimation, previously initiated by IWMPSyncDevice3 estimateSyncSize, is complete.
ms.assetid: 2fb45a13-d82b-48b6-b9bb-46409f33a33f
keywords:
- SyncEstimationComplete method Windows Media Player
- SyncEstimationComplete method Windows Media Player , IWMPEvents4 interface
- IWMPEvents4 interface Windows Media Player , SyncEstimationComplete method
topic_type:
- apiref
api_name:
- IWMPEvents4.SyncEstimationComplete
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMPEvents4::SyncEstimationComplete method

The **SyncEstimationComplete** event occurs when a size estimation, previously initiated by [**IWMPSyncDevice3::estimateSyncSize**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice3-estimatesyncsize), is complete.

## Syntax


```C++
void SyncEstimationComplete(
  [in] IWMPSyncDevice *pDevice,
  [in] long           hrResult,
  [in] long           lEstimatedUsedSpace,
  [in] long           lEstimatedSize
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Pointer to the [**IWMPSyncDevice**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice) interface that represents the device for which the size estimation was initiated.

</dd> <dt>

*hrResult* \[in\]
</dt> <dd>

A value that indicates the success or failure of the estimation.



| Value                                                                                                                                       | Meaning                                |
|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="S_OK"></span><span id="s_ok"></span><dl> <dt>**S\_OK**</dt> </dl>          | The estimation succeeded.<br/>   |
| <span id="E_ABORT"></span><span id="e_abort"></span><dl> <dt>**E\_ABORT**</dt> </dl> | The estimation was aborted.<br/> |



 

</dd> <dt>

*lEstimatedUsedSpace* \[in\]
</dt> <dd>

The estimated space (in bytes) that would be used on the device.

</dd> <dt>

*lEstimatedSize* \[in\]
</dt> <dd>

The estimated size (in bytes) of the data to be synchronized.

</dd> </dl>

## Return value

This method does not return a value.

## See also

<dl> <dt>

[**IWMPEvents4 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents4)
</dt> <dt>

[**IWMPSyncDevice3::estimateSyncSize**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice3-estimatesyncsize)
</dt> </dl>

 

 





