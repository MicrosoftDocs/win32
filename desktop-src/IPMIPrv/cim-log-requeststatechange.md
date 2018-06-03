---
title: RequestStateChange method of the CIM\_Log class
description: Initiates a requests to change the state of a computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e1c00c5e-7eed-4363-80a2-e974923a783c
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RequestStateChange method
- RequestStateChange method, CIM_Log class
- CIM_Log class, RequestStateChange method
topic_type:
- apiref
api_name:
- CIM_Log.RequestStateChange
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequestStateChange method of the CIM\_Log class

Initiates a requests to change the state of a computer system.

This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

## Syntax


```mof
uint32 RequestStateChange(
  [in]  uint16          RequestedState,
  [out] CIM_ConcreteJob Job,
  [in]  datetime        TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

The new state to request.

<dt>

2
</dt> <dd>

Enabled

</dd> <dt>

3
</dt> <dd>

Disabled

</dd> <dt>

4
</dt> <dd>

Shut Down

</dd> <dt>

6
</dt> <dd>

Offline

</dd> <dt>

7
</dt> <dd>

Test

</dd> <dt>

8
</dt> <dd>

Defer

</dd> <dt>

9
</dt> <dd>

Quiesce

</dd> <dt>

10
</dt> <dd>

Reboot

</dd> <dt>

11
</dt> <dd>

Reset

</dd> <dt>

12 32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768 65535
</dt> <dd>

Vendor Reserved

</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

A concrete job that tracks the state transition initiated by this operation.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

The timeout period that specifies the maximum amount of time to use to transition to the new state.

</dd> </dl>

## Return value

A return code that indicates whether the operation completed successfully.

<dl> <dt>


</dt> <dd>

0

Completed with No Error

</dd> <dt>


</dt> <dd>

1

Not Supported

</dd> <dt>


</dt> <dd>

2

Unknown or Unspecified Error

</dd> <dt>


</dt> <dd>

3

Cannot complete within Timeout Period

</dd> <dt>


</dt> <dd>

4

Failed

</dd> <dt>


</dt> <dd>

5

Invalid Parameter

</dd> <dt>


</dt> <dd>

6

In Use

</dd> <dt>


</dt> <dd>

7 4095

DMTF Reserved

</dd> <dt>


</dt> <dd>

4096

Method Parameters Checked - Job Started

</dd> <dt>


</dt> <dd>

4097

Invalid State Transition

</dd> <dt>


</dt> <dd>

4098

Use of Timeout Parameter Not Supported

</dd> <dt>


</dt> <dd>

4099

Busy

</dd> <dt>


</dt> <dd>

4100 32767

Method Reserved

</dd> <dt>


</dt> <dd>

32768 65535

Vendor Specific

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Log**](cim-log.md)
</dt> </dl>

 

 





