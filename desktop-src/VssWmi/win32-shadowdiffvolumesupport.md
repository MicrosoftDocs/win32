---
title: Win32\_ShadowDiffVolumeSupport class
description: The Win32\_ShadowDiffVolumeSupport class associates a shadow copy provider and a volume supported for differential storage area.
ms.assetid: '5845f8d2-4ce2-4ddf-a212-d05ec9ca2998'
keywords: ["Win32_ShadowDiffVolumeSupport class", "Win32_ShadowDiffVolumeSupport class, described"]
topic_type:
- apiref
api_name:
- Win32_ShadowDiffVolumeSupport
- Win32_ShadowDiffVolumeSupport.Antecedent
- Win32_ShadowDiffVolumeSupport.Dependent
api_location:
- Vsswmi.dll
api_type:
- DllExport
---

# Win32\_ShadowDiffVolumeSupport class

The **Win32\_ShadowDiffVolumeSupport** class associates a shadow copy provider and a volume supported for the differential storage area.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_ShadowDiffVolumeSupport : CIM_Dependency
{
  Win32_ShadowProvider REF Antecedent;
  Win32_Volume         REF Dependent;
};
```

## Members

The **Win32\_ShadowDiffVolumeSupport** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ShadowDiffVolumeSupport** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ShadowProvider**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the shadow copy provider.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Volume**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the volume supported by the provider.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
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

[**Win32\_ShadowOn**](win32-shadowon.md)
</dt> <dt>

[**Win32\_ShadowVolumeSupport**](win32-shadowvolumesupport.md)
</dt> </dl>

 

 





