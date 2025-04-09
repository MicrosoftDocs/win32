---
description: Initiates a requests to change the state of a DNS server interface. This method is inherited from CIM\_EnabledLogicalElement.
ms.assetid: 59583CA2-2093-4D1B-8B03-AC2BC4A02A3C
title: RequestStateChange method of the MSFT\_DNSClientServerAddress class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_DNSClientServerAddress.RequestStateChange
api_type: 
- COM
api_location: 
- DnsClientCim.dll
ROBOTS: INDEX,FOLLOW
---

# RequestStateChange method of the MSFT\_DNSClientServerAddress class

Initiates a requests to change the state of a DNS server interface.

This method is inherited from **CIM\_EnabledLogicalElement**.

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



| Value                                                                                  | Meaning                    |
|----------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>2</dt> </dl>           | Enabled<br/>         |
| <dl> <dt>3</dt> </dl>           | Disabled<br/>        |
| <dl> <dt>4</dt> </dl>           | Shut Down<br/>       |
| <dl> <dt>6</dt> </dl>           | Offline<br/>         |
| <dl> <dt>7</dt> </dl>           | Test<br/>            |
| <dl> <dt>8</dt> </dl>           | Defer<br/>           |
| <dl> <dt>9</dt> </dl>           | Quiesce<br/>         |
| <dl> <dt>10</dt> </dl>          | Reboot<br/>          |
| <dl> <dt>11</dt> </dl>          | Reset<br/>           |
| <dl> <dt>12 32767</dt> </dl>    | DMTF Reserved<br/>   |
| <dl> <dt>32768 65535</dt> </dl> | Vendor Reserved<br/> |



 

</dd> <dt>

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



| Return value                                                                           | Description                                        |
|----------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>0</dt> </dl>           | Completed with No Error<br/>                 |
| <dl> <dt>1</dt> </dl>           | Not Supported<br/>                           |
| <dl> <dt>2</dt> </dl>           | Unknown or Unspecified Error<br/>            |
| <dl> <dt>3</dt> </dl>           | Cannot complete within Timeout Period<br/>   |
| <dl> <dt>4</dt> </dl>           | Failed<br/>                                  |
| <dl> <dt>5</dt> </dl>           | Invalid Parameter<br/>                       |
| <dl> <dt>6</dt> </dl>           | In Use<br/>                                  |
| <dl> <dt>7 4095</dt> </dl>      | DMTF Reserved<br/>                           |
| <dl> <dt>4096</dt> </dl>        | Method Parameters Checked - Job Started<br/> |
| <dl> <dt>4097</dt> </dl>        | Invalid State Transition<br/>                |
| <dl> <dt>4098</dt> </dl>        | Use of Timeout Parameter Not Supported<br/>  |
| <dl> <dt>4099</dt> </dl>        | Busy<br/>                                    |
| <dl> <dt>4100 32767</dt> </dl>  | Method Reserved<br/>                         |
| <dl> <dt>32768 65535</dt> </dl> | Vendor Specific<br/>                         |



 

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                        |
| Namespace<br/>                | Root\\StandardCimV2<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DnsClientCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DNSClientServerAddress**](msft-dnsclientserveraddress.md)
</dt> </dl>

 

 




