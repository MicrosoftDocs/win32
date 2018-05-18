---
Description: 'Disables flow control on priority.'
ms.assetid: '331b7b4f-fbd9-4dcb-aa25-eff5a279948e'
title: 'Disable method of the MSFT\_NetQosFlowControlSettingData class'
---

# Disable method of the MSFT\_NetQosFlowControlSettingData class

Disables flow control on priority.

## Syntax


```mof
uint32 Disable(
  [out] MSFT_NetQosFlowControlSettingData Output
);
```



## Parameters

<dl> <dt>

*Output* \[out\]
</dt> <dd>

Receives a [**MSFT\_NetQosFlowControlSettingData**](msft-netqosflowcontrolsettingdata.md) object that represents the flow control settings after flow control is turned off.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>Dcbwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DcbWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetQosFlowControlSettingData**](msft-netqosflowcontrolsettingdata.md)
</dt> </dl>

 

 




