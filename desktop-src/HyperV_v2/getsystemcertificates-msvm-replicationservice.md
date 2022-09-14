---
description: Retrieves the system certificates on a host system.
ms.assetid: d470a57d-85b9-4d31-bb2c-9b6f21e2860d
title: GetSystemCertificates method of the Msvm_ReplicationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ReplicationService.GetSystemCertificates
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetSystemCertificates method of the Msvm\_ReplicationService class

Retrieves the system certificates on a host system.

## Syntax


```mof
uint32 GetSystemCertificates(
  [out] string EncodedCertificates[]
);
```



## Parameters

<dl> <dt>

*EncodedCertificates* \[out\]
</dt> <dd>

If successful, receives the certificates available from the Personal store for the local machine. Each entry is a base 64 encoded certificate string. This string can be converted to a byte array by constructing an X509Certificate2 object.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in used** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> <dt>

**File not found** (32779)
</dt> </dl>

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

[**Msvm\_ReplicationService**](msvm-replicationservice.md)
</dt> </dl>

 

 




