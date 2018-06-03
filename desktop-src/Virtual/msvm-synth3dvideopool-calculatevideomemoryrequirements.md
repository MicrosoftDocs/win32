---
title: CalculateVideoMemoryRequirements method of the Msvm\_Synth3dVideoPool class
description: Calculates the amount of video memory required for a RemoteFX virtual machine.
ms.assetid: FF664228-989F-4820-BD70-117C092BB26C
keywords:
- CalculateVideoMemoryRequirements method Hyper-V
- CalculateVideoMemoryRequirements method Hyper-V , Msvm_Synth3dVideoPool class
- Msvm_Synth3dVideoPool class Hyper-V , CalculateVideoMemoryRequirements method
topic_type:
- apiref
api_name:
- Msvm_Synth3dVideoPool.CalculateVideoMemoryRequirements
api_location:
- Root\Virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CalculateVideoMemoryRequirements method of the Msvm\_Synth3dVideoPool class

Calculates the amount of video memory required for a RemoteFX virtual machine.

## Syntax


```mof
uint32 CalculateVideoMemoryRequirements(
  [in]  uint32 monitorResolution,
  [in]  uint32 numberOfMonitors,
  [out] uint64 requiredVideoMemory
);
```



## Parameters

<dl> <dt>

*monitorResolution* \[in\]
</dt> <dd>

The maximum monitor resolution for the virtual machine. This must be one of the following values.



| Value                                                                        | Meaning                                           |
|------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The maximum resolution is 1024   768.<br/>  |
| <dl> <dt>1</dt> </dl> | The maximum resolution is 1280   1024.<br/> |
| <dl> <dt>2</dt> </dl> | The maximum resolution is 1600   1200.<br/> |
| <dl> <dt>3</dt> </dl> | The maximum resolution is 1920   1200.<br/> |



 

</dd> <dt>

*numberOfMonitors* \[in\]
</dt> <dd>

The maximum number of monitors for the virtual machine. The minimum number of monitors is one and the maximum is dependent upon the maximum screen resolution. The following table defines the maximum number of monitors allowed for different resolutions.



| Resolution             | Maximum monitors |
|------------------------|------------------|
| 1024   768<br/>  | 4<br/>     |
| 1280   1024<br/> | 4<br/>     |
| 1600   1200<br/> | 3<br/>     |
| 1920   1200<br/> | 2<br/>     |



 

</dd> <dt>

*requiredVideoMemory* \[out\]
</dt> <dd>

Receives the required amount of video memory, in bytes.

</dd> </dl>

## Return value

Returns a status code, which can be one of the following values.



| Return code/value                                                                                                                                                                | Description                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl>                    | Successful.<br/>                                |
| <dl> <dt>**Method Parameters Checked - Job Started**</dt> <dt>4096</dt> </dl> | Job started.<br/>                               |
| <dl> <dt>**Failed**</dt> <dt>32768</dt> </dl>                                 | Failed.<br/>                                    |
| <dl> <dt>**Access Denied**</dt> <dt>32769</dt> </dl>                          | Access denied.<br/>                             |
| <dl> <dt>**Not Supported**</dt> <dt>32770</dt> </dl>                          | Not supported.<br/>                             |
| <dl> <dt>**Status is unknown**</dt> <dt>32771</dt> </dl>                      | Status is unknown.<br/>                         |
| <dl> <dt>**Timeout**</dt> <dt>32772</dt> </dl>                                | Timeout.<br/>                                   |
| <dl> <dt>**Invalid parameter**</dt> <dt>32773</dt> </dl>                      | A parameter is not valid.<br/>                  |
| <dl> <dt>**System is in used**</dt> <dt>32774</dt> </dl>                      | System is in use.<br/>                          |
| <dl> <dt>**Invalid state for this operation**</dt> <dt>32775</dt> </dl>       | The state is not valid for this operation.<br/> |
| <dl> <dt>**Incorrect data type**</dt> <dt>32776</dt> </dl>                    | Incorrect data type.<br/>                       |
| <dl> <dt>**System is not available**</dt> <dt>32777</dt> </dl>                | System is not available.<br/>                   |
| <dl> <dt>**Out of memory**</dt> <dt>32778</dt> </dl>                          | Out of memory.<br/>                             |



 

## Remarks

This method is typically called on the host system to determine if the host has enough available video memory to host a RemoteFX virtual machine. To do this, you compare the amount of video memory calculated by this method with the [**Msvm\_PhysicalGPUInfo.AvailableVideoMemory**](msvm-physicalgpuinfo.md) property to determine if the host machine has enough available video memory. You can use this information to determine if a virtual machine can be moved to the host system.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 with SP1<br/>                                                           |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_PhysicalGPUInfo**](msvm-physicalgpuinfo.md)
</dt> <dt>

[**Msvm\_Synth3dVideoPool**](msvm-synth3dvideopool.md)
</dt> </dl>

 

 





