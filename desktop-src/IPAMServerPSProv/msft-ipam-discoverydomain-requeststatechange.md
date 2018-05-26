---
Description: Requests the specified state change to a domain in IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 982BE84B-2DD5-4B37-A67C-B6DDDB9B6B01
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RequestStateChange method of the MSFT\_IPAM\_DiscoveryDomain class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RequestStateChange method of the MSFT\_IPAM\_DiscoveryDomain class

Requests the specified state change to a domain in IPAM.

This method is inherited from **CIM\_System**.

## Syntax


```mof
uint32 RequestStateChange(
  [in]  uint16              RequestedState,
  [out] CIM_ConcreteJob Ref Job,
  [in]  datetime            TimeoutPeriod
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

The timeout period required by the client when waiting for a state transition. A "0" or **null** value indicates that the client does not have a timeout requirement for this state transition.

</dd> </dl>

## Return value

A return code that indicates whether the operation completed successfully.

The possible return codes are:

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



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_DiscoveryDomain**](msft-ipam-discoverydomain.md)
</dt> </dl>

 

 




