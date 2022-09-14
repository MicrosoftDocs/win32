---
description: The Win32\_NetworkAdapterSetting association WMI class relates a network adapter and its configuration settings.
ms.assetid: 6fc646c3-05f9-4c92-8598-07ea20fffaca
ms.tgt_platform: multiple
title: Win32_NetworkAdapterSetting class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapterSetting
- Win32_NetworkAdapterSetting.Setting
- Win32_NetworkAdapterSetting.Element
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_NetworkAdapterSetting class

The **Win32\_NetworkAdapterSetting** association [WMI class](../wmisdk/retrieving-a-class.md) relates a network adapter and its configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C50A-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_NetworkAdapterSetting : Win32_DeviceSettings
{
  Win32_NetworkAdapterConfiguration REF Setting;
  Win32_NetworkAdapter              REF Element;
};
```

## Members

The **Win32\_NetworkAdapterSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NetworkAdapterSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NetworkAdapter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Element"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_NetworkAdapter")
</dt> </dl>

A [**Win32\_NetworkAdapter**](win32-networkadapter.md) that describes the properties of the network adapter that is using a particular network adapter setting.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NetworkAdapterConfiguration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Setting"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI\|Win32\_NetworkAdapterConfiguration")
</dt> </dl>

A [**Win32\_NetworkAdapterConfiguration**](win32-networkadapterconfiguration.md) that describes the configuration settings used on the network adapter.

</dd> </dl>

## Remarks

The **Win32\_NetworkAdapterSetting** class is derived from [**Win32\_DeviceSettings**](win32-devicesettings.md).

For information on how to use association classes, see [ASSOCIATORS OF Statement](../wmisdk/associators-of-statement.md).

## Examples

The following VBScript sample uses **Win32\_NetworkAdapterSetting** to identify the IP Address on the Local Area Connection.


```VB
strComputer = "."
Set objWMIService = GetObject( _
    "winmgmts:\\" & strComputer & "\root\cimv2")
Set colNics = objWMIService.ExecQuery _
    ("Select * From Win32_NetworkAdapter " _
        & "Where NetConnectionID = " & _
        "'Local Area Connection'")
 
For Each objNic in colNics
    Set colNicConfigs = objWMIService.ExecQuery _
      ("ASSOCIATORS OF " _
          & "{Win32_NetworkAdapter.DeviceID='" & _
      objNic.DeviceID & "'}" & _
      " WHERE AssocClass=Win32_NetworkAdapterSetting")
    For Each objNicConfig In colNicConfigs
        For Each strIPAddress in objNicConfig.IPAddress
            Wscript.Echo "IP Address: " &  strIPAddress
        Next
    Next
Next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_DeviceSettings**](win32-devicesettings.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> <dt>

[WMI Tasks: Networking](../wmisdk/wmi-tasks--networking.md)
</dt> </dl>

 

 
