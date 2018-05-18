---
Description: 'The DCB Willing state.'
ms.assetid: '174673aa-9d38-451e-aae0-8be17832a06a'
title: 'MSFT\_NetQosDcbxSettingData class'
---

# MSFT\_NetQosDcbxSettingData class

The DCB Willing state.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("DcbQosCim")]
class MSFT_NetQosDcbxSettingData : MSFT_NetSettingData
{
  boolean Willing;
};
```

## Members

The **MSFT\_NetQosDcbxSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetQosDcbxSettingData** class has these properties.

<dl> <dt>

**Willing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The local machine is Willing to accept remote DCBX settings.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>Dcbwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DcbWmi.dll</dt> </dl> |



 

 




