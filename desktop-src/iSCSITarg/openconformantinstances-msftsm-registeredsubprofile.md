---
title: OpenConformantInstances method of the MSFTSM\_RegisteredSubProfile class
description: Opens a session to enumerate class instances of this registered profile instance, and optionally to retrieve a set of the requested instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0435aa56-89a7-496b-b16e-9fda776a26d9
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- OpenConformantInstances method iSCSI Software Target API
- OpenConformantInstances method iSCSI Software Target API , MSFTSM_RegisteredSubProfile class
- MSFTSM_RegisteredSubProfile class iSCSI Software Target API , OpenConformantInstances method
topic_type:
- apiref
api_name:
- MSFTSM_RegisteredSubProfile.OpenConformantInstances
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OpenConformantInstances method of the MSFTSM\_RegisteredSubProfile class

Opens a session to enumerate class instances of this registered profile instance, and optionally to retrieve a set of the requested instances.

This method is inherited from the **CIM\_RegisteredSubProfile** class.

## Syntax


```mof
uint32 OpenConformantInstances(
  [in]  string  ResultClass,
  [in]  string  IncludedPropertyList[],
  [in]  uint32  OperationTimeout,
  [in]  boolean ContinueOnError,
  [in]  uint32  MaxObjectCount,
  [out] string  EnumerationContext,
  [out] boolean EndOfSequence,
  [out] uint16  InstanceType[],
  [out] string  InstanceWithPathList[]
);
```



## Parameters

<dl> <dt>

*ResultClass* \[in\]
</dt> <dd>

If not **NULL**, specifies a filter that is based on the class name. Only those central or scoping instances that are a kind of the specified class are returned.

</dd> <dt>

*IncludedPropertyList* \[in\]
</dt> <dd>

If not **NULL**, specifies a filter that is based on an unordered set of property names. Only the specified properties are returned. An empty list specifies to return no properties. The instance path is always returned.

</dd> <dt>

*OperationTimeout* \[in\]
</dt> <dd>

Specifies the minimum time, in seconds, the CIM server keeps the enumeration session open if the session is not explicitly closed by the **OpenConformantInstances** method or [**PullConformantInstances**](pullconformantinstances-msftsm-registeredsubprofile.md) method. If the operation timeout is exceeded, the enumeration session is closed, and any allocated session resources are released. A value of zero specifies no operation timeout. The meaning of a value of **NULL** is implementation-dependent.

The set of allowable values is implementation-specific. The implementation can require a timeout and limit the length of the timeout. If the specified value is not allowed, the method returns a failure code of **CIM\_ERR\_INVALID\_OPERATION\_TIMEOUT**.

</dd> <dt>

*ContinueOnError* \[in\]
</dt> <dd>

Set to **True** to request continuation on error. Continuation on error is the ability to resume an enumeration session successfully after the **OpenConformantInstances** or [**PullConformantInstances**](pullconformantinstances-msftsm-registeredsubprofile.md) method returns an error.

If set to **True**, and the implementation supports continuation on error, the enumeration session remains open after an error.

> [!Note]  
> For more information about continuation on error, see the DSP0223 standard on the [DMTF](http://dmtf.org/standards/wbem) website at http://dmtf.org/standards/wbem.

 

If set to **True**, and the implementation does not support continuation on error, this method returns a failure code of **CIM\_ERR\_CONTINUATION\_ON\_ERROR\_NOT\_SUPPORTED**, and the session is closed.

</dd> <dt>

*MaxObjectCount* \[in\]
</dt> <dd>

Specifies the maximum number of elements to be returned. If set to zero, no elements are retrieved.

</dd> <dt>

*EnumerationContext* \[out\]
</dt> <dd>

On return, indicates the enumeration session context. It is set to **NULL**, if the session is closed. If not set to **NULL**, this value is used to identify the session in calls to the [**PullConformantInstances**](pullconformantinstances-msftsm-registeredsubprofile.md) and [**CloseConformantInstances**](closeconformantinstances-msftsm-registeredsubprofile.md) methods.

</dd> <dt>

*EndOfSequence* \[out\]
</dt> <dd>

On return, indicates whether the enumeration session is exhausted.

If set to **True**, no more elements are available, and the session is closed. If set to **false**, additional elements might be available and the session remains open.

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

[**MSFTSM\_RegisteredSubProfile**](msftsm-registeredsubprofile.md)
</dt> </dl>

 

 





