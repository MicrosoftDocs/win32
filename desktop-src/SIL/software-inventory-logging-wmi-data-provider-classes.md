---
title: Software Inventory Logging WMI Data Provider Classes
description: The data provider provides enumerable data classes that gather Software Inventory Logging data from both host machines and guest machines. In addition, the data provider provides access to Software Inventory Logging settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'B65D9898-3800-4175-BAF6-5ABA256B1E0B'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# Software Inventory Logging WMI Data Provider Classes

The data provider provides enumerable data classes that gather Software Inventory Logging data from both host machines and guest machines. In addition, the data provider provides access to Software Inventory Logging settings. The classes are defined in SILProvider.mof. The Software Inventory Logging WMI data provider provides the following classes.

## In this section

<dl> <dt>

[**MsftSil\_Computer**](msftsil-computer.md)
</dt> <dd>

The [**MsftSil\_Computer**](msftsil-computer.md) WMI class retrieves system data about a server.

</dd> <dt>

[**MsftSil\_ComputerIdentity**](msftsil-computeridentity.md)
</dt> <dd>

The [**MsftSil\_ComputerIdentity**](msftsil-computeridentity.md) WMI class encapsulates identification properties of a computer.

</dd> <dt>

[**MsftSil\_Data**](msftsil-data.md)
</dt> <dd>

The [**MsftSil\_Data**](msftsil-data.md) WMI class is an abstract base class that retrieves Software Inventory Logging data from a server.

</dd> <dt>

[**MsftSil\_GuestData**](msftsil-guestdata.md)
</dt> <dd>

Deprecated. Exposes Software Inventory Logging data collected from a virtual machine.

</dd> <dt>

[**MsftSil\_GuestTasks**](msftsil-guesttasks.md)
</dt> <dd>

This class has been removed.

</dd> <dt>

[**MsftSil\_ManagementTasks**](msftsil-managementtasks.md)
</dt> <dd>

The [**MsftSil\_ManagementTasks**](msftsil-managementtasks.md) WMI class retrieves and configures settings for Software Inventory Logging.

</dd> <dt>

[**MsftSil\_Software**](msftsil-software.md)
</dt> <dd>

The [**MsftSil\_Software**](msftsil-software.md) WMI class retrieves installation data about the software installed on a server.

</dd> <dt>

[**MsftSil\_UalAccess**](msftsil-ualaccess.md)
</dt> <dd>

The [**MsftSil\_UalAccess**](msftsil-ualaccess.md) WMI class aggregates [User Access Logging](https://msdn.microsoft.com/library/hh437528) (UAL) data from a server, and then returns information about the number of unique users and devices that accessed a software product.

</dd> <dt>

[**MsftSil\_WindowsUpdate**](msftsil-windowsupdate.md)
</dt> <dd>

The [**MsftSil\_WindowsUpdate**](msftsil-windowsupdate.md) WMI class retrieves a list of the Quick Fix Engineering (QFE) updates installed on a server.

</dd> </dl>

## Related topics

<dl> <dt>

[Software Inventory Logging Reference](https://msdn.microsoft.com/library/windows/desktop/dn440663)
</dt> </dl>

 

 




