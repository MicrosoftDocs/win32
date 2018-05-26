---
title: RequestStateChange method of the CIM\_EnabledLogicalElement class
description: Initiates a requests to change the state of a computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b240f7b0-1487-4cf6-9ecc-97c6444a720a
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RequestStateChange method
- RequestStateChange method, CIM_EnabledLogicalElement class
- CIM_EnabledLogicalElement class, RequestStateChange method
topic_type:
- apiref
api_name:
- CIM_EnabledLogicalElement.RequestStateChange
api_location:
- IpmiPrv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RequestStateChange method of the CIM\_EnabledLogicalElement class

Initiates a requests to change the state of a computer system.

This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

## Syntax


```mof
uint32 RequestStateChange(
  [in]  uint16              RequestedState,
  [out] CIM_ConcreteJob REF Job,
  [in]  datetime            TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

The new state to request.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

**Shut Down** (4)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (6)


</dt> <dd></dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

**Test** (7)


</dt> <dd></dd> <dt>

<span id="Defer"></span><span id="defer"></span><span id="DEFER"></span>

**Defer** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (10)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (11)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>12 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

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

**Completed with No Error**
</dt> <dd>

0

</dd> <dt>

**Not Supported**
</dt> <dd>

1

</dd> <dt>

**Unknown/Unspecified Error**
</dt> <dd>

2

Unknown or Unspecified Error

</dd> <dt>

**Can NOT complete within Timeout Period**
</dt> <dd>

3

Cannot complete within Timeout Period

</dd> <dt>

**Failed**
</dt> <dd>

4

</dd> <dt>

**Invalid Parameter**
</dt> <dd>

5

</dd> <dt>

**In Use**
</dt> <dd>

6

</dd> <dt>

**DMTF Reserved**
</dt> <dd>

7 4095

</dd> <dt>

**Method Parameters Checked - Job Started**
</dt> <dd>

4096

</dd> <dt>

**Invalid State Transition**
</dt> <dd>

4097

</dd> <dt>

**Use of Timeout Parameter Not Supported**
</dt> <dd>

4098

</dd> <dt>

**Busy**
</dt> <dd>

4099

</dd> <dt>

**Method Reserved**
</dt> <dd>

4100 32767

</dd> <dt>

**Vendor Specific**
</dt> <dd>

32768 65535

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

[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md)
</dt> </dl>

 

 





