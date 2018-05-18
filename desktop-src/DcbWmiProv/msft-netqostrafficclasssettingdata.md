---
Description: 'The settings for a QoS traffic class.'
ms.assetid: '71b8ce92-8d57-4d48-a702-f180a403cb7c'
title: 'MSFT\_NetQosTrafficClassSettingData class'
---

# MSFT\_NetQosTrafficClassSettingData class

The settings for a QoS traffic class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("DcbQosCim")]
class MSFT_NetQosTrafficClassSettingData : MSFT_NetSettingData
{
  string Name;
  uint8  Algorithm;
  uint8  BandwidthPercentage;
  uint8  Priority[];
};
```

## Members

The **MSFT\_NetQosTrafficClassSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetQosTrafficClassSettingData** class has these properties.

<dl> <dt>

**Algorithm**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The assigned Transmission Selection Algorithm.

<dl> <dt>

<span id="Strict"></span><span id="strict"></span><span id="STRICT"></span>**Strict** (0)
</dt> <dt>

<span id="ETS"></span><span id="ets"></span>**ETS** (2)
</dt> </dl>

</dd> <dt>

**BandwidthPercentage**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MaxValue** (100), **Units** ("Percent")
</dt> </dl>

The assigned minimum bandwidth percentage value if the ETS algorithm is used. Otherwise, this must be zero.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the traffic class.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MaxValue** (7)
</dt> </dl>

The assigned priority values.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>Dcbwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DcbWmi.dll</dt> </dl> |



 

 




