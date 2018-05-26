---
title: Win32\_ShadowBy class
description: The Win32\_ShadowBy class associates a shadow copy and the provider that creates the shadow copy.
ms.assetid: 2c04c82e-aee6-419a-b075-fa98314ab115
keywords:
- Win32_ShadowBy class
- Win32_ShadowBy class, described
topic_type:
- apiref
api_name:
- Win32_ShadowBy
- Win32_ShadowBy.Antecedent
- Win32_ShadowBy.Dependent
api_location:
- Vsswmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_ShadowBy class

The **Win32\_ShadowBy** class associates a shadow copy and the provider that creates the shadow copy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_ShadowBy : CIM_Dependency
{
  Win32_ShadowProvider REF Antecedent;
  Win32_ShadowCopy     REF Dependent;
};
```

## Members

The **Win32\_ShadowBy** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ShadowBy** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ShadowProvider**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to a shadow copy provider.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ShadowCopy**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to a shadow copy.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vss.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vsswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ShadowProvider**](win32-shadowprovider.md)
</dt> <dt>

[**Win32\_ShadowCopy**](win32-shadowcopy.md)
</dt> <dt>

[**Win32\_ShadowContext**](win32-shadowcontext.md)
</dt> <dt>

[**Win32\_ShadowStorage**](win32-shadowstorage.md)
</dt> <dt>

[**Win32\_ShadowFor**](win32-shadowfor.md)
</dt> <dt>

[**Win32\_ShadowOn**](win32-shadowon.md)
</dt> <dt>

[**Win32\_ShadowVolumeSupport**](win32-shadowvolumesupport.md)
</dt> <dt>

[**Win32\_ShadowDiffVolumeSupport**](win32-shadowdiffvolumesupport.md)
</dt> </dl>

 

 





