---
Description: Enables flow control on priority.
ms.assetid: 798843ca-3b2b-464b-a921-0d4ee073d02d
title: Enable method of the MSFT\_NetQosFlowControlSettingData class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enable method of the MSFT\_NetQosFlowControlSettingData class

Enables flow control on priority.

## Syntax


```mof
uint32 Enable(
  [out] MSFT_NetQosFlowControlSettingData Output
);
```



## Parameters

<dl> <dt>

*Output* \[out\]
</dt> <dd>

Receives a [**MSFT\_NetQosFlowControlSettingData**](msft-netqosflowcontrolsettingdata.md) object that represents the flow control settings after flow control is turned on.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>Dcbwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DcbWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetQosFlowControlSettingData**](msft-netqosflowcontrolsettingdata.md)
</dt> </dl>

 

 




