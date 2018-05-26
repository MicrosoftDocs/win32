---
title: GetSynchronizationSupported method of the CIM\_ReplicationServiceCapabilities class
description: For the supplied element, this method returns the supported synchronization operations in a series of parallel output arrays.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 113e85c0-d14c-4e94-a2b6-d87949f4ceca
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSynchronizationSupported method iSCSI Software Target API
- GetSynchronizationSupported method iSCSI Software Target API , CIM_ReplicationServiceCapabilities class
- CIM_ReplicationServiceCapabilities class iSCSI Software Target API , GetSynchronizationSupported method
topic_type:
- apiref
api_name:
- CIM_ReplicationServiceCapabilities.GetSynchronizationSupported
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSynchronizationSupported method of the CIM\_ReplicationServiceCapabilities class

For the supplied element, this method returns the supported synchronization operations in a series of parallel output arrays.

## Syntax


```mof
uint32 GetSynchronizationSupported(
  [in]  CIM_LogicalElement     REF LocalElement,
  [in]  CIM_LogicalElement     REF OtherElement,
  [in]  CIM_ServiceAccessPoint REF OtherElementAccessPoint,
  [in]  uint16                     MethodName,
  [out] uint16                     SyncTypes[],
  [out] uint16                     Modes[],
  [out] uint16                     LocalElementRole[]
);
```



## Parameters

<dl> <dt>

*LocalElement* \[in\]
</dt> <dd>

A reference to the supplied element.

</dd> <dt>

*OtherElement* \[in\]
</dt> <dd>

A reference to the other end of the synchronization association. OtherElement can be a local or a remote element. Method CreateSynchronizationAspect needs only one element to act on. Therefore there is no need to specify another element.

</dd> <dt>

*OtherElementAccessPoint* \[in\]
</dt> <dd>

A reference to the access point instance to allow the service to access the OtherElement. If NULL, it is assumed the service does not need any access information or the element is local.

</dd> <dt>

*MethodName* \[in\]
</dt> <dd>

A value representing the desired method name.

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


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*SyncTypes* \[out\]
</dt> <dd>

A array of supported SyncTypes for the copy operations using the supplied element.

<dt>

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


</dt> <dd>9 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*Modes* \[out\]
</dt> <dd>

An array of supported Modes for the copy operations using the supplied element.

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*LocalElementRole* \[out\]
</dt> <dd>

An array that specifies whether the local element can be the source or the target element of the copy operations. Possible values are:

SystemElement: the source element.

SyncedElement: the target element.

These designations correspond to the keys of the Synchronized association.

<dt>

<span id="SystemElement"></span><span id="systemelement"></span><span id="SYSTEMELEMENT"></span>

**SystemElement** (2)


</dt> <dd></dd> <dt>

<span id="SyncedElement"></span><span id="syncedelement"></span><span id="SYNCEDELEMENT"></span>

**SyncedElement** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> </dl>

## Return value

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

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 4294967295)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
</dt> </dl>

 

 





