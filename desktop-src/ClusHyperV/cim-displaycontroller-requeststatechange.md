---
title: RequestStateChange method of the CIM\_DisplayController class
description: Requests the specified change to the state of the element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec7ae5de-182e-41b8-8c30-1023e0ee9cab
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RequestStateChange method
- RequestStateChange method, CIM_DisplayController class
- CIM_DisplayController class, RequestStateChange method
topic_type:
- apiref
api_name:
- CIM_DisplayController.RequestStateChange
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RequestStateChange method of the CIM\_DisplayController class

Requests the specified change to the state of the element.

## Syntax


```mof
uint32 RequestStateChange(
  [in]      uint16              RequestedState,
  [in, out] CIM_ConcreteJob REF Job,
  [in]      datetime            TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

The requested state for the element.

The possible values are:

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

32768..65535
</dt> <dd>

Vendor Reserved

</dd> </dl> </dd> <dt>

*Job* \[in, out\]
</dt> <dd>

A reference to the job created to track the state transition initiated by the method invocation.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

The client specified timeout interval for the length of the state transition. A 0 or a null value indicates that the client has no time requirements for the transition. If this property does not contain 0 or null and the implementation does not support this parameter, this method returns 4098 (Use Of Timeout Parameter Not Supported).

</dd> </dl>

## Return value

The is method returns one of the following values:

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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_DisplayController**](cim-displaycontroller.md)
</dt> </dl>

 

 





