---
Description: Associates a video head with the video controller that includes it.
ms.assetid: D072DF7C-D55B-4203-9FE5-B395D1EC1632
title: Msvm_VideoHeadOnController class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VideoHeadOnController
- Msvm_VideoHeadOnController.Antecedent
- Msvm_VideoHeadOnController.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VideoHeadOnController class

Associates a video head with the video controller that includes it.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VideoHeadOnController : CIM_VideoHeadOnController
{
  CIM_DisplayController REF Antecedent;
  Msvm_VideoHead        REF Dependent;
};
```

## Members

The **Msvm\_VideoHeadOnController** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VideoHeadOnController** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_DisplayController**](https://docs.microsoft.com/previous-versions//cc136810(v=vs.85))**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://docs.microsoft.com/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**Min**](https://docs.microsoft.com/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Max**](https://docs.microsoft.com/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

The video controller that includes the head.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VideoHead**](msvm-videohead.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://docs.microsoft.com/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**Min**](https://docs.microsoft.com/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

The head on the video device.

</dd> </dl>

## Remarks

Access to the **Msvm\_VideoHeadOnController** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://docs.microsoft.com/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_VideoHeadOnController**](cim-videoheadoncontroller.md)
</dt> <dt>

[**CIM\_VideoHeadOnController**](https://docs.microsoft.com/previous-versions//cc136950(v=vs.85))
</dt> <dt>

[Video Classes](video-classes.md)
</dt> </dl>

 

 




