---
title: ModifyListSettingsDefineState method of the MSISCSITARGET\_ReplicationService class
description: Modifies or starts a job to modify a list of CIM\_SettingsDefineState associations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6b4218e1-4524-4a6a-9ec1-145136af080e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifyListSettingsDefineState method iSCSI Software Target API", "ModifyListSettingsDefineState method iSCSI Software Target API , MSISCSITARGET_ReplicationService class", "MSISCSITARGET_ReplicationService class iSCSI Software Target API , ModifyListSettingsDefineState method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.ModifyListSettingsDefineState
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# ModifyListSettingsDefineState method of the MSISCSITARGET\_ReplicationService class

Modifies or starts a job to modify a list of **CIM\_SettingsDefineState** associations.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 ModifyListSettingsDefineState(
  [in]                uint16                      Operation,
  [in]                CIM_SettingsDefineState Ref SettingsStates[],
  [in, out, optional] CIM_LogicalElement Ref      TargetElements[],
  [in, out, optional] CIM_ReplicationGroup Ref    TargetGroups[],
  [in]                uint64                      TargetElementCount,
  [in, optional]      CIM_ServiceAccessPoint Ref  TargetAccessPoint,
  [out]               CIM_Synchronized Ref        Synchronizations[],
  [in, optional]      string                      ReplicationSettingData,
  [out]               CIM_ConcreteJob Ref         Job,
  [in]                CIM_SettingData Ref         TargetSettingGoal,
  [in]                CIM_ResourcePool Ref        TargetPool,
  [in]                uint16                      WaitForCopyState
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

Specifies the type of modification to be made to the related associations. Required.

The possible values are.

<dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>**Activate Consistency** (2)


</dt> <dd>

Activate consistency if not already active.

</dd> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>**Deactivate Consistency** (3)


</dt> <dd>

Deactivate consistency if it is active.

</dd> <dt>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>**Delete** (4)


</dt> <dd>

Remove the **CIM\_SettingsDefineState** association.

</dd> <dt>

<span id="Copy_To_Target"></span><span id="copy_to_target"></span><span id="COPY_TO_TARGET"></span>

<span id="Copy_To_Target"></span><span id="copy_to_target"></span><span id="COPY_TO_TARGET"></span>**Copy To Target** (5)


</dt> <dd>

Introduce the target elements and form the necessary associations between the source and the target elements.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

*SettingsStates* \[in\]
</dt> <dd>

Specifies an array of references to the associations between the source elements and instances of the synchronization aspect.

</dd> <dt>

*TargetElements* \[in, out, optional\]
</dt> <dd>

On input, optionally specifies a list of target elements to use. On return, contains references to the created target storage elements. If a job is created, the target elements might not be available immediately.

If you specify the *TargetElements* parameter, the *TargetGroups* and *TargetElementCount* parameters must be **NULL**.

</dd> <dt>

*TargetGroups* \[in, out, optional\]
</dt> <dd>

On input, optionally specifies a list of target groups to use. On return, contains references to the created target groups. If a job is created, the target groups might not be available immediately.

If you specify the *TargetGroups* parameter, the *TargetElements* and *TargetElementCount* parameters must be **NULL**.

</dd> <dt>

*TargetElementCount* \[in\]
</dt> <dd>

Specifies how many target elements to create. Use this parameter to create multiple copies of a source element.

If you specify the *TargetElementCount* parameter, the *TargetGroups* and *TargetElements* parameters must be **NULL**.

</dd> <dt>

*TargetAccessPoint* \[in, optional\]
</dt> <dd>

Specifies the target access point information. Can be **NULL**, if the service does not require access information to access the target element or group.

</dd> <dt>

*Synchronizations* \[out\]
</dt> <dd>

On return, contains an array of references to the created replication associations.

</dd> <dt>

*ReplicationSettingData* \[in, optional\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* input parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data. Optional.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

</dd> <dt>

*TargetSettingGoal* \[in\]
</dt> <dd>

Specifies configuration-related and operational parameters for the replica storage objects. If existing target elements are specified, this parameter must be **NULL**.

</dd> <dt>

*TargetPool* \[in\]
</dt> <dd>

Specifies the underlying storage for the new target elements. If **NULL**, the allocation is implementation-specific. If existing target elements are supplied, this parameter must be **NULL**.

</dd> <dt>

*WaitForCopyState* \[in\]
</dt> <dd>

Specifies the **CopyState** values that must be reached before this method returns. Only a subset of valid values applies.

For example.

-   **Initialized**: Associations have been established, but there is no data flow.
-   **Inactive**: Initialization is complete, but the data flow remains idle until it is activated.
-   **Synchronized**: Replicas are an exact copy of the source.
-   **UnSynchronized**: Copy operation is in progress.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





