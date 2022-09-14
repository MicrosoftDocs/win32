---
description: The known destinations containing the collected data. Available only if the collector is running with the status log enabled.
ms.assetid: ab0d2949-9808-49c3-8a0c-f2ce9c300a2a
ms.tgt_platform: multiple
title: TargetForwardingDestination class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TargetForwardingDestination
- TargetForwardingDestination.TargetEndpoint
- TargetForwardingDestination.TargetMac
- TargetForwardingDestination.TargetGuid
- TargetForwardingDestination.CollectorEndpoint
- TargetForwardingDestination.Computer
- TargetForwardingDestination.ForwarderType
- TargetForwardingDestination.Destination
- TargetForwardingDestination.DestinationPattern
- TargetForwardingDestination.Error
- TargetForwardingDestination.ConnectedSince
- TargetForwardingDestination.DisconnectedSince
- TargetForwardingDestination.WmiDateTime
api_type: 
- DllExport
api_location: 
- BEvtCol.exe
---

# TargetForwardingDestination class

The known destinations containing the collected data. Available only if the collector is running with the status log enabled.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("BootEventCollectorWmiProvider"), Dynamic, AMENDMENT]
class TargetForwardingDestination
{
  string   TargetEndpoint;
  string   TargetMac;
  string   TargetGuid;
  string   CollectorEndpoint;
  string   Computer;
  string   ForwarderType;
  string   Destination;
  string   DestinationPattern;
  string   Error;
  DATETIME ConnectedSince;
  DATETIME DisconnectedSince;
  DATETIME WmiDateTime;
};
```

## Members

The **TargetForwardingDestination** class has these types of members:

-   [Properties](#properties)

### Properties

The **TargetForwardingDestination** class has these properties.

<dl> <dt>

**CollectorEndpoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The host:port information of the endpoint on the collector side.

</dd> <dt>

**Computer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Target computer name, as determined by the collector according to its configuration.

</dd> <dt>

**ConnectedSince**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Timestamp of when the connection was established.

</dd> <dt>

**Destination**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Destination of the data. The meaning depends on the forwarder type. May be a file name or some other identification.

</dd> <dt>

**DestinationPattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Pattern used to generate the destination of the data. The meaning depends on the forwarder type and configuration. For a fixed destination, would be the same as the destination itself. For the destination with rotation of the files would contain the pattern characters that will be replaced with the actual index in the destination.

</dd> <dt>

**DisconnectedSince**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Timestamp of when the connection was dropped.

</dd> <dt>

**Error**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Error message if an error was encountered. Otherwise will be empty.

</dd> <dt>

**ForwarderType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Type of the forwarder (such as 'etl').

</dd> <dt>

**TargetEndpoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The endpoint information of the target computer, in human-readable format. This property is formatted as a *host*:*port* string. For example, "127.0.0.1:50000".

</dd> <dt>

**TargetGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The target computer's SMBIOS GUID (if known).

</dd> <dt>

**TargetMac**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The target computer's MAC address (if known).

</dd> <dt>

**WmiDateTime**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Timestamp of when this state change was recorded.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\BootEventCollector<br/>                                              |
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



 

