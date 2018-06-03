---
Description: Represents an IMPlatform Provider.
ms.assetid: 4626332f-797f-4072-a797-51cb930ddf41
title: MSFT\_NetImPlatProvider class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetImPlatProvider class

Represents an IMPlatform Provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract]
class MSFT_NetImPlatProvider : CIM_ManagedElement
{
  string InstanceID;
  string Name;
};
```

## Members

The **MSFT\_NetImPlatProvider** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetImPlatProvider** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The NetcfgInstanceId of the LWF.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The display name of this LWF.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>MsNetImPlatform.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NdisIMPlatCim.dll</dt> </dl>   |



 

 




