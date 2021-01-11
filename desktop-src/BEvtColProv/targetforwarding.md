---
description: Retrieves forwarding data from a target computer.
ms.assetid: e9ed210d-09ad-4689-b6a0-f84c5cce86f5
ms.tgt_platform: multiple
title: TargetForwarding class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TargetForwarding
- TargetForwarding.TargetEndpoint
- TargetForwarding.TargetMac
- TargetForwarding.TargetGuid
- TargetForwarding.CollectorEndpoint
- TargetForwarding.Computer
- TargetForwarding.ForwarderType
- TargetForwarding.Destination
- TargetForwarding.DestinationPattern
- TargetForwarding.Error
- TargetForwarding.ConnectedSince
api_type: 
- DllExport
api_location: 
- BEvtCol.exe
---

# TargetForwarding class

Retrieves forwarding data from a target computer.

> [!Note]  
> A target computer may have multiple forwarders configured.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("BootEventCollectorWmiProvider"), Dynamic, AMENDMENT]
class TargetForwarding
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
};
```

## Members

The **TargetForwarding** class has these types of members:

-   [Properties](#properties)

### Properties

The **TargetForwarding** class has these properties.

<dl> <dt>

**CollectorEndpoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The endpoint information of the collector server. This property is formatted as a *host*:*port* string.

</dd> <dt>

**Computer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The computer name of the target computer.

</dd> <dt>

**ConnectedSince**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The timestamp that indicates when the connection was established for the forwarding data.

</dd> <dt>

**Destination**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The destination of the forwarding data, such as a file name.

</dd> <dt>

**DestinationPattern**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The format used to generate the destination of the forwarding data.

</dd> <dt>

**Error**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

An error message that describes an encountered error. This property is empty if no error was encountered.

</dd> <dt>

**ForwarderType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The file type that contains the forwarding data, such as ETL.

</dd> <dt>

**TargetEndpoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The endpoint information of the target computer, in human-readable format. This property is formatted as a *host*:*port* string. For example, "127.0.0.1:50000".

</dd> <dt>

**TargetGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The SMBIOS **GUID** of the target computer.

</dd> <dt>

**TargetMac**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Fixed**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

The MAC address of the target computer.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\BootEventCollector<br/>                                              |
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



## See also

<dl> <dt>

[Boot Event Collector WMI Provider](boot-event-collector-wmi-provider-portal.md)
</dt> </dl>

 

