---
description: The Win32\_TCPIPPrinterPort&\#32;WMI class represents a TCP/IP service access point.
ms.assetid: b1be18b6-47de-461c-a90b-c7e0537130ef
ms.tgt_platform: multiple
title: Win32_TCPIPPrinterPort class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_TCPIPPrinterPort
- Win32_TCPIPPrinterPort.Caption
- Win32_TCPIPPrinterPort.Description
- Win32_TCPIPPrinterPort.InstallDate
- Win32_TCPIPPrinterPort.Status
- Win32_TCPIPPrinterPort.CreationClassName
- Win32_TCPIPPrinterPort.Name
- Win32_TCPIPPrinterPort.SystemCreationClassName
- Win32_TCPIPPrinterPort.SystemName
- Win32_TCPIPPrinterPort.Type
- Win32_TCPIPPrinterPort.ByteCount
- Win32_TCPIPPrinterPort.HostAddress
- Win32_TCPIPPrinterPort.PortNumber
- Win32_TCPIPPrinterPort.Protocol
- Win32_TCPIPPrinterPort.Queue
- Win32_TCPIPPrinterPort.SNMPCommunity
- Win32_TCPIPPrinterPort.SNMPDevIndex
- Win32_TCPIPPrinterPort.SNMPEnabled
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_TCPIPPrinterPort class

The **Win32\_TCPIPPrinterPort** [WMI class](../wmisdk/retrieving-a-class.md) represents a TCP/IP service access point.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_TCPIPPrinterPort : CIM_ServiceAccessPoint
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Status;
  string   CreationClassName;
  string   Name;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   Type;
  boolean  ByteCount;
  string   HostAddress;
  uint32   PortNumber;
  uint32   Protocol;
  string   Queue;
  string   SNMPCommunity;
  uint32   SNMPDevIndex;
  boolean  SNMPEnabled;
};
```

## Members

The **Win32\_TCPIPPrinterPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TCPIPPrinterPort** class has these properties.

<dl> <dt>

**ByteCount**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the computer counts the bytes in a document before sending them to the printer and the printer reports back the number of bytes actually read. This capability is used for diagnostics when missing bytes are detected in the print output.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Caption")
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Description")
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**HostAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Address of the device or print server.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Install Date")
</dt> </dl>

Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/key-qualifier.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Uniquely identifies the service access point and provides an indication of the functionality that is managed. This functionality is described in more detail in the object's Description property.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**PortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of the TCP ports used by the port monitor to communicate with the device.

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Printing protocol used. Some printers support only LPR.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

RAW

Printing directly to a device or print server.

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

LPR

Legacy protocol, which is eventually replaced by RAW.

</dd> </dl>

</dd> <dt>

**Queue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the print queue on the server when used with the LPR protocol.

</dd> <dt>

**SNMPCommunity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security level value for the device.

Example: "public'"

</dd> <dt>

**SNMPDevIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SNMP index number of this device for the SNMP agent.

</dd> <dt>

**SNMPEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this printer supports [RFC 1759](https://www.ietf.org/rfc/rfc1759.txt) (Simple Network Management Protocol) and can provide rich status information from the device.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (10), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Status")
</dt> </dl>

String that indicates the current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

The scoping system's creation class name.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_System**](cim-system.md).**Name**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

The scoping system's name.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](../wmisdk/standard-qualifiers.md) ("Win32")
</dt> </dl>

Type of SAP, such as attached or redirected.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

<dt>

<span id="Write"></span><span id="write"></span><span id="WRITE"></span>

**Write** (1)


</dt> <dd></dd> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>

**Read** (2)


</dt> <dd></dd> <dt>

<span id="Redirected"></span><span id="redirected"></span><span id="REDIRECTED"></span>

**Redirected** (4)


</dt> <dd></dd> <dt>

<span id="Net_Attached"></span><span id="net_attached"></span><span id="NET_ATTACHED"></span>

**Net\_Attached** (8)


</dt> <dd></dd> <dt>

<span id="unknown"></span><span id="UNKNOWN"></span>

**unknown** (16)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **Win32\_TCPIPPrinterPort** class is derived from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) which derives from [**CIM\_LogicalElement**](cim-logicalelement.md).

The **SeLoadDriverPrivilege** privilege is required to delete an instance of this WMI class. The following script snippet demonstrates how to make a connection to WMI that uses this privilege.

`Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate, (LoadDriver)}")`

## Examples

The following PowerShell sample removes a printer and the associated TCPIP printer port.


```PowerShell
function Remove-PrinterAndPort{
    Param( $printername )
   $printer=gwmi win32_Printer -filter "name='HPDJ600'"
   $printer.Delete()
   $port=gwmi win32_tcpipprinterport -filter "name='$($printer.portname)'" -enableall
   $port.Delete()
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>Win32\_Printer.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl>       |



## See also

<dl> <dt>

[**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
