---
title: Win32\_ShadowOn class
description: The Win32\_ShadowOn class associates a shadow copy and the volume on which the differential data is written.
ms.assetid: 7ab39296-d888-4857-8d38-d4d50665954c
keywords:
- Win32_ShadowOn class
- Win32_ShadowOn class, described
topic_type:
- apiref
api_name:
- Win32_ShadowOn
- Win32_ShadowOn.Antecedent
- Win32_ShadowOn.Dependent
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

# Win32\_ShadowOn class

The **Win32\_ShadowOn** class associates a shadow copy and the volume on which the differential data is written.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_ShadowOn : CIM_Dependency
{
  Win32_Volume     REF Antecedent;
  Win32_ShadowCopy REF Dependent;
};
```

## Members

The **Win32\_ShadowOn** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ShadowOn** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Volume**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the original volume.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ShadowCopy**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the shadow copy.

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

[**Win32\_ShadowBy**](win32-shadowby.md)
</dt> <dt>

[**Win32\_ShadowFor**](win32-shadowfor.md)
</dt> <dt>

[**Win32\_ShadowVolumeSupport**](win32-shadowvolumesupport.md)
</dt> <dt>

[**Win32\_ShadowDiffVolumeSupport**](win32-shadowdiffvolumesupport.md)
</dt> </dl>

 

 





