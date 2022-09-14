---
description: ModifyServiceSettings method of the Msvm_MetricService class - Modifies the setting data for the service.
ms.assetid: E6133DA7-A137-42FA-A523-5B93E9C6DB79
title: ModifyServiceSettings method of the Msvm_MetricService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MetricService.ModifyServiceSettings
api_type: 
- COM
api_location: 
- vmms.exe
---

# ModifyServiceSettings method of the Msvm\_MetricService class

Modifies the setting data for the service.

## Syntax


```mof
uint32 ModifyServiceSettings(
  [in]  string              SettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SettingData* \[in\]
</dt> <dd>

Contains an embedded instance of the [**Msvm\_MetricServiceSettingData**](msvm-metricservicesettingdata.md) class that contains the modified setting data for the service.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

</dd> </dl>

## Return value

This method returns one of the following values.



| Return code/value                                                                                                                                                                | Description                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl>                    | Success.<br/>                                |
| <dl> <dt>**Method Parameters Checked - Job Started**</dt> <dt>4096</dt> </dl> | Method parameters checked, job started.<br/> |
| <dl> <dt>**Failed**</dt> <dt>32768</dt> </dl>                                 | Failed.<br/>                                 |
| <dl> <dt>**Access Denied**</dt> <dt>32769</dt> </dl>                          | Access denied.<br/>                          |
| <dl> <dt>**Not Supported**</dt> <dt>32770</dt> </dl>                          | Not supported.<br/>                          |
| <dl> <dt>**Status is unknown**</dt> <dt>32771</dt> </dl>                      | Status is unknown.<br/>                      |
| <dl> <dt>**Timeout**</dt> <dt>32772</dt> </dl>                                | Time-out.<br/>                               |
| <dl> <dt>**Invalid parameter**</dt> <dt>32773</dt> </dl>                      | Invalid parameter.<br/>                      |
| <dl> <dt>**System is in use**</dt> <dt>32774</dt> </dl>                       | System is in use.<br/>                       |
| <dl> <dt>**Invalid state for this operation**</dt> <dt>32775</dt> </dl>       | Invalid state for this operation.<br/>       |
| <dl> <dt>**Incorrect data type**</dt> <dt>32776</dt> </dl>                    | Incorrect data type.<br/>                    |
| <dl> <dt>**System is not available**</dt> <dt>32777</dt> </dl>                | System is not available.<br/>                |
| <dl> <dt>**Out of memory**</dt> <dt>32778</dt> </dl>                          | Out of memory.<br/>                          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_MetricService**](msvm-metricservice.md)
</dt> </dl>

 

