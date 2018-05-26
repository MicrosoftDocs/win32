---
Description: The link level flow control settings for an IEEE 802.1p priority.
ms.assetid: 331b7b4f-fbd9-4dcb-aa25-eff5a279948e
title: MSFT\_NetQosFlowControlSettingData class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_NetQosFlowControlSettingData class

The link level flow control settings for an IEEE 802.1p priority.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("DcbQosCim")]
class MSFT_NetQosFlowControlSettingData : MSFT_NetSettingData
{
  string  Name;
  uint8   Priority;
  boolean Enabled;
};
```

## Members

The **MSFT\_NetQosFlowControlSettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetQosFlowControlSettingData** class has these methods.



| Method                                                       | Description                                   |
|:-------------------------------------------------------------|:----------------------------------------------|
| [**Disable**](disable-msft-netqosflowcontrolsettingdata.md) | Disables flow control on priority.<br/> |
| [**Enable**](enable-msft-netqosflowcontrolsettingdata.md)   | Enables flow control on priority.<br/>  |



 

### Properties

The **MSFT\_NetQosFlowControlSettingData** class has these properties.

<dl> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Flow control enabled for priority.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the flow control class.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxValue** (7)
</dt> </dl>

Priority value.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>Dcbwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DcbWmi.dll</dt> </dl> |



 

 




