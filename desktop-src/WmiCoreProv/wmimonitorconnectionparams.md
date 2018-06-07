---
Description: Contains the connection type of the monitor.
ms.assetid: f5658246-fbb8-4530-8dfb-f1ca792fe9d5
title: WmiMonitorConnectionParams class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WmiMonitorConnectionParams class

The WmiMonitorConnectionParams WMI class contains the connection type of the monitor.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class WmiMonitorConnectionParams
{
  boolean Active;
  string  InstanceName;
  uint32  VideoOutputTechnology;
};
```

## Members

The **WmiMonitorConnectionParams** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorConnectionParams** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the active monitor.

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Name of the specific monitor instance.

</dd> <dt>

**VideoOutputTechnology**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Video output technology connection type. Valid values are documented in the [D3DKMDT\_VIDEO\_OUTPUT\_TECHNOLOGY](http://go.microsoft.com/fwlink/p/?linkid=105876) enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSMonitorClass**](msmonitorclass.md)
</dt> </dl>

 

 




