---
title: GetSynchronizationSupported method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves the supported synchronization operations for the specified element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e0393f06-a176-4d61-af2f-30e0c78638e7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSynchronizationSupported method iSCSI Software Target API", "GetSynchronizationSupported method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class", "MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetSynchronizationSupported method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetSynchronizationSupported
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetSynchronizationSupported method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves the supported synchronization operations for the specified element.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetSynchronizationSupported(
  [in]           CIM_LogicalElement Ref     LocalElement,
  [in, optional] CIM_LogicalElement Ref     OtherElement,
  [in]           CIM_ServiceAccessPoint Ref OtherElementAccessPoint,
  [in]           uint16                     MethodName,
  [out]          uint16                     SyncTypes[],
  [out]          uint16                     Modes[],
  [out]          uint16                     LocalElementRole[]
);
```



## Parameters

<dl> <dt>

*LocalElement* \[in\]
</dt> <dd>

Specifies the local element in the synchronization association.

</dd> <dt>

*OtherElement* \[in, optional\]
</dt> <dd>

Specifies the other end of the synchronization association. This element can be local or remote.

</dd> <dt>

*OtherElementAccessPoint* \[in\]
</dt> <dd>

Specifies the service access point (SAP) instance that is used to enable access to the element referenced in the *OtherElement* parameter. Can be **NULL** if a service access point is not required to access the element.

</dd> <dt>

*MethodName* \[in\]
</dt> <dd>

Specifies the requested method name.

The possible values are.

<dt>

<span id="CreateElementReplica"></span><span id="createelementreplica"></span><span id="CREATEELEMENTREPLICA"></span>

**CreateElementReplica** (2)


</dt> <dd></dd> <dt>

<span id="CreateGroupReplica"></span><span id="creategroupreplica"></span><span id="CREATEGROUPREPLICA"></span>

**CreateGroupReplica** (3)


</dt> <dd></dd> <dt>

<span id="CreateSynchronizationAspect"></span><span id="createsynchronizationaspect"></span><span id="CREATESYNCHRONIZATIONASPECT"></span>

**CreateSynchronizationAspect** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*SyncTypes* \[out\]
</dt> <dd>

On return, contains the supported sync types that are available for the supplied element.

The possible values are.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd> *value* = 5</dd> <dt>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>

**Mirror** (6)


</dt> <dd></dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

**Snapshot** (7)


</dt> <dd></dd> <dt>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>

**Clone** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*Modes* \[out\]
</dt> <dd>

On return, contains the supported modes that are available for the supplied element.

The possible values are.

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*LocalElementRole* \[out\]
</dt> <dd>

On return, indicates whether the local element can be the source or the target element of the copy operations. These values correspond to the key properties of a [**MSISCSITARGET\_StorageSynchronized**](msiscsitarget-storagesynchronized.md) association.

The possible values are.

<dt>

<span id="SystemElement"></span><span id="systemelement"></span><span id="SYSTEMELEMENT"></span>

**SystemElement** (2)


</dt> <dd></dd> <dt>

<span id="SyncedElement"></span><span id="syncedelement"></span><span id="SYNCEDELEMENT"></span>

**SyncedElement** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Success** (0)
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

**DMTF Reserved** (7–0x7FFF)
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

[**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





