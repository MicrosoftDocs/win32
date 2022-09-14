---
description: The CIM\_MonitorSetting class associates the monitor resolution with the desktop monitor to which it applies.
ms.assetid: 4bf0b2d5-b901-4294-a33b-9c8a87785af0
ms.tgt_platform: multiple
title: CIM_MonitorSetting class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MonitorSetting
- CIM_MonitorSetting.Setting
- CIM_MonitorSetting.Element
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_MonitorSetting class

The **CIM\_MonitorSetting** class associates the monitor resolution with the desktop monitor to which it applies.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{1008CCED-7BFF-11D2-AAD2-006008C78BC7}"), AMENDMENT]
class CIM_MonitorSetting : CIM_ElementSetting
{
  CIM_MonitorResolution REF Setting;
  CIM_DesktopMonitor    REF Element;
};
```

## Members

The **CIM\_MonitorSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_MonitorSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DesktopMonitor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Element")
</dt> </dl>

A [**CIM\_DesktopMonitor**](cim-desktopmonitor.md) describing the desktop monitor.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_MonitorResolution**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Setting")
</dt> </dl>

A [**CIM\_MonitorResolution**](cim-monitorresolution.md) describing the monitor resolution associated with the desktop monitor.

</dd> </dl>

## Remarks

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementSetting**](cim-elementsetting.md)
</dt> </dl>

 

