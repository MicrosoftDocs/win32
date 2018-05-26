---
title: PullConformantInstances method of the MSFTSM\_RegisteredProfile class
description: Continues an enumeration session that is opened by the OpenConformantInstances method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05e1ded8-064f-44e6-bd2e-539a40376d05
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PullConformantInstances method iSCSI Software Target API
- PullConformantInstances method iSCSI Software Target API , MSFTSM_RegisteredProfile class
- MSFTSM_RegisteredProfile class iSCSI Software Target API , PullConformantInstances method
topic_type:
- apiref
api_name:
- MSFTSM_RegisteredProfile.PullConformantInstances
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PullConformantInstances method of the MSFTSM\_RegisteredProfile class

Continues an enumeration session that is opened by the [**OpenConformantInstances**](openconformantinstances-msftsm-registeredprofile.md) method.

This method is inherited from the [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) class.

## Syntax


```mof
uint32 PullConformantInstances(
  [in]      uint32  MaxObjectCount,
  [in, out] string  EnumerationContext,
  [out]     boolean EndOfSequence,
  [out]     uint16  InstanceType[],
  [out]     string  InstanceWithPathList[]
);
```



## Parameters

<dl> <dt>

*MaxObjectCount* \[in\]
</dt> <dd>

Specifies the maximum number of elements to be returned. If set to zero the operation timeout clock for the session is reset, but no elements are retrieved.

</dd> <dt>

*EnumerationContext* \[in, out\]
</dt> <dd>

On input, specifies the enumeration session context that identifies the session to query.

On return, indicates the enumeration session context.

Set to **NULL** if the session is closed. If not **NULL**, this value is used to identify the session on subsequent calls to the **PullConformantInstances** and [**CloseConformantInstances**](closeconformantinstances-msftsm-registeredprofile.md) methods.

</dd> <dt>

*EndOfSequence* \[out\]
</dt> <dd>

On return, indicates whether the enumeration session is exhausted.

If **True**, no more elements are available and the session is closed. If **false**, additional elements might be available, and the session remains open.

</dd> <dt>

*InstanceType* \[out\]
</dt> <dd>

On return, indicates the type of instance in the corresponding entry in the *InstanceWithPathList* array.

The possible values are.

<dt>

<span id="Central_Instance"></span><span id="central_instance"></span><span id="CENTRAL_INSTANCE"></span>

**Central Instance** (2)


</dt> <dd></dd> <dt>

<span id="Scoping_Instance"></span><span id="scoping_instance"></span><span id="SCOPING_INSTANCE"></span>

**Scoping Instance** (3)


</dt> <dd></dd> <dt>

<span id="Central_and_Scoping_Instance"></span><span id="central_and_scoping_instance"></span><span id="CENTRAL_AND_SCOPING_INSTANCE"></span>

**Central and Scoping Instance** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 = *value* </dd> </dl> </dd> <dt>

*InstanceWithPathList* \[out\]
</dt> <dd>

On return, contains an unordered set of the requested instances and their addresses. This array is correlated to the *InstanceType* array.

Returning an array with no entries does not indicate that the enumeration session has been exhausted. Only the *EndOfSequence* output parameter indicates whether the enumeration session has been exhausted.

</dd> </dl>

## Return value

Returns zero on success; otherwise returns an error.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\Interop<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md)
</dt> </dl>

 

 





