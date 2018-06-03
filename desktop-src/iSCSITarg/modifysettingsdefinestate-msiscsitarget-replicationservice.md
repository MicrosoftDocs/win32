---
title: ModifySettingsDefineState method of the MSISCSITARGET\_ReplicationService class
description: Modifies the CIM\_SettingsDefineState association between the storage objects and the synchronization aspect.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7eccd255-6e26-4984-a609-c38f4caa9fd6
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ModifySettingsDefineState method iSCSI Software Target API
- ModifySettingsDefineState method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , ModifySettingsDefineState method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.ModifySettingsDefineState
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ModifySettingsDefineState method of the MSISCSITARGET\_ReplicationService class

Modifies the [**CIM\_SettingsDefineState**](https://msdn.microsoft.com/library/cc136915) association between the storage objects and the synchronization aspect. The modification could range from introducing the target elements, which creates a new **CIM\_StorageSynchronized** association, to dissolving the [**CIM\_SettingsDefineState**](https://msdn.microsoft.com/library/cc136915) association.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 ModifySettingsDefineState(
  [in]            uint16                      Operation,
  [in]            CIM_SettingsDefineState Ref SettingsState,
  [in, out]       CIM_LogicalElement Ref      TargetElement,
  [in, out]       CIM_ReplicationGroup Ref    TargetGroup,
  [in, optional]  uint64                      TargetElementCount,
  [in, optional]  CIM_ServiceAccessPoint Ref  TargetAccessPoint,
  [out, optional] CIM_Synchronized Ref        Synchronization,
  [in, optional]  string                      ReplicationSettingData,
  [out]           CIM_ConcreteJob Ref         Job,
  [in, optional]  CIM_SettingData Ref         TargetSettingGoal,
  [in, optional]  CIM_ResourcePool Ref        TargetPool,
  [in, optional]  uint16                      WaitForCopyState
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

Specifies the type of modification to be made to the related associations. Required.

<dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>**Activate Consistency** (2)


</dt> <dd>

Activates consistency if it is not already active.

</dd> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>**Deactivate Consistency** (3)


</dt> <dd>

Deactivates consistency if it is active.

</dd> <dt>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>**Delete** (4)


</dt> <dd>

Removes the [**CIM\_SettingsDefineState**](https://msdn.microsoft.com/library/cc136915) association.

</dd> <dt>

<span id="Copy_To_Target"></span><span id="copy_to_target"></span><span id="COPY_TO_TARGET"></span>

<span id="Copy_To_Target"></span><span id="copy_to_target"></span><span id="COPY_TO_TARGET"></span>**Copy To Target** (5)


</dt> <dd>

Introduces the target elements and forms the necessary associations between the source and the target elements.

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

*SettingsState* \[in\]
</dt> <dd>

Specifies the association between the source element and a synchronization aspect. Required.

</dd> <dt>

*TargetElement* \[in, out\]
</dt> <dd>

On input, specifies a target element to use. Optional. If the *TargetElement* parameter is specified, the *TargetGroup* and *TargetCount* parameters must be **NULL**.

On output, contains a reference to the created target storage element. If a job is created, the target element might not be available immediately.

</dd> <dt>

*TargetGroup* \[in, out\]
</dt> <dd>

On input, specifies a target group to use. Optional. If the *TargetGroup* parameter is specified, the *TargetElement* and *TargetCount* parameters must be **NULL**.

On output, contains a reference to the created target group. If a job is created, the target group might not be available immediately.

</dd> <dt>

*TargetElementCount* \[in, optional\]
</dt> <dd>

Specifies how many target elements to create. Use this parameter to create multiple copies of a source element. If you specify the *TargetElementCount* parameter, the *TargetElement*and *TargetGroup* parameters must be **NULL**.

</dd> <dt>

*TargetAccessPoint* \[in, optional\]
</dt> <dd>

Specifies the target access point information. Can be **NULL**, if the service does not require access information to access the target element or target group.

</dd> <dt>

*Synchronization* \[out, optional\]
</dt> <dd>

On return, contains a reference to the created group association between the source and the target elements. If a job is created, this parameter can be **NULL** until the association is instantiated.

</dd> <dt>

*ReplicationSettingData* \[in, optional\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* input parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data. Optional.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

</dd> <dt>

*TargetSettingGoal* \[in, optional\]
</dt> <dd>

Specifies configuration-related and operational parameters for the target storage objects. If existing target elements are specified, this parameter must be set to **NULL**.

</dd> <dt>

*TargetPool* \[in, optional\]
</dt> <dd>

Specifies the resource pool to use for the underlying storage for the target element. If **NULL**, the allocation is implementation-specific. If a *TargetElement* is specified, this parameter must be **NULL**.

</dd> <dt>

*WaitForCopyState* \[in, optional\]
</dt> <dd>

Specifies the **CopyState** value that must be reached before this method returns. Only a subset of valid values applies.

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

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





