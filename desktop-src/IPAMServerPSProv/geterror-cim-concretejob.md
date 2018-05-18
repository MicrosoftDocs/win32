---
Description: 'Retrieves error information for the operational status of a concrete job.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'cdb6ec25-37d1-4307-83d3-3a9ba91b4d24'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'GetError method of the CIM\_ConcreteJob class'
---

# GetError method of the CIM\_ConcreteJob class

Retrieves error information for the operational status of a concrete job.

## Syntax


```mof
uint32 GetError(
  [out] CIM_Error Error
);
```



## Parameters

<dl> <dt>

*Error* \[out\]
</dt> <dd>

When this method returns, this parameter contains either a [**CIM\_Error**](cim-error.md) object that contains the error information; or if there is no error, this method returns **null**. The **OperationalStatus** property of the [**CIM\_ConcreteJob**](cim-concretejob.md) object determines whether an error occurred.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
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

**Access Denied** (6)
</dt> <dt>

**DMTF Reserved** (7–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 




