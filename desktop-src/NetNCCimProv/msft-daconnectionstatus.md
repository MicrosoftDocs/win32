---
Description: Represents the connection status for DirectAccess.
ms.assetid: aea5bce8-791c-4df7-b7e5-cceb28a26271
title: MSFT\_DAConnectionStatus class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DAConnectionStatus class

Represents the connection status for DirectAccess.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetNCCim")]
class MSFT_DAConnectionStatus : MSFT_NetSettingData
{
  uint32 Status;
  uint32 Substatus;
};
```

## Members

The **MSFT\_DAConnectionStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DAConnectionStatus** class has these properties.

<dl> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the connection status for DirectAccess.

</dd> <dt>

**Substatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the connection substatus for DirectAccess.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetNCCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetNCCim.dll</dt> </dl> |



 

 




