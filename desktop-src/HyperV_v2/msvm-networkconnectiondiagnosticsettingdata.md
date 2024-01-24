---
description: Represents the settings used to test the network connectivity of a virtual machine.
ms.assetid: d719d9c9-7ca9-40a0-ada8-185b8cd44c22
title: Msvm_NetworkConnectionDiagnosticSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_NetworkConnectionDiagnosticSettingData
- Msvm_NetworkConnectionDiagnosticSettingData.IsSender
- Msvm_NetworkConnectionDiagnosticSettingData.SenderIP
- Msvm_NetworkConnectionDiagnosticSettingData.ReceiverIP
- Msvm_NetworkConnectionDiagnosticSettingData.ReceiverMac
- Msvm_NetworkConnectionDiagnosticSettingData.IsolationId
- Msvm_NetworkConnectionDiagnosticSettingData.SequenceNumber
- Msvm_NetworkConnectionDiagnosticSettingData.PayloadSize
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_NetworkConnectionDiagnosticSettingData class

Represents the settings used to test the network connectivity of a virtual machine. Used by the [**DiagnoseNetworkConnection**](msvm-virtualsystemmanagementservice-diagnosenetworkconnection.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_NetworkConnectionDiagnosticSettingData : CIM_SettingData
{
  boolean IsSender;
  string  SenderIP;
  string  ReceiverIP;
  string  ReceiverMac;
  uint32  IsolationId;
  uint32  SequenceNumber;
  uint32  PayloadSize;
};
```

## Members

The **Msvm\_NetworkConnectionDiagnosticSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_NetworkConnectionDiagnosticSettingData** class has these properties.

<dl> <dt>

**IsolationId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Isolation ID.

</dd> <dt>

**IsSender**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether this method is being invoked at the sender or the receiver.

</dd> <dt>

**PayloadSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The payload size.

</dd> <dt>

**ReceiverIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The receiver IP address.

</dd> <dt>

**ReceiverMac**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The receiver MAC address.

</dd> <dt>

**SenderIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The sender IP address.

</dd> <dt>

**SequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The sequence number.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> </dl>

 

 




