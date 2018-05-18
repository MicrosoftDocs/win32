---
title: MSFT\_MTEventChannel class
description: Encapsulates the properties of the Windows event channel. Can also be used to perform operations related to the particular event channel.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b830af27-e690-430c-b166-9394f38721c8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_MTEventChannel class", "MSFT_MTEventChannel class, described"]
topic_type:
- apiref
api_name:
- MSFT_MTEventChannel
- MSFT_MTEventChannel.InstanceID
- MSFT_MTEventChannel.Caption
- MSFT_MTEventChannel.Description
- MSFT_MTEventChannel.ElementName
- MSFT_MTEventChannel.Name
- MSFT_MTEventChannel.DisplayName
- MSFT_MTEventChannel.DisplayPath
- MSFT_MTEventChannel.LogFilePath
- MSFT_MTEventChannel.Enabled
- MSFT_MTEventChannel.ClassicLog
- MSFT_MTEventChannel.Type
- MSFT_MTEventChannel.LogFileSize
- MSFT_MTEventChannel.EventsCount
api_location:
- MtTmProv.dll
api_type:
- DllExport
---

# MSFT\_MTEventChannel class

Encapsulates the properties of the Windows event channel. Can also be used to perform operations related to the particular event channel.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), dynamic, provider("mttmprov"), AMENDMENT]
class MSFT_MTEventChannel : CIM_ManagedElement
{
  string  InstanceID;
  string  Caption;
  string  Description;
  string  ElementName;
  string  Name;
  string  DisplayName;
  string  DisplayPath;
  string  LogFilePath;
  boolean Enabled;
  boolean ClassicLog;
  uint32  Type;
  uint64  LogFileSize;
  string  EventsCount;
};
```

## Members

The **MSFT\_MTEventChannel** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_MTEventChannel** class has these methods.



| Method                                                                         | Description                                                                                  |
|:-------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**ClearLogFile**](msft-mteventchannel-clearlogfile.md)                       | Clears the log file associated with the event channel.<br/>                            |
| [**Disable**](msft-mteventchannel-disable.md)                                 | Disables the logging associated with the event channel.<br/>                           |
| [**Enable**](msft-mteventchannel-enable.md)                                   | Enables the logging associated with the event channel.<br/>                            |
| [**GetEventRecords**](msft-mteventchannel-geteventrecords.md)                 | Retrieves the details of events generated in an event log by a particular source.<br/> |
| [**GetWindowsEventChannels**](msft-mteventchannel-getwindowseventchannels.md) | Gets the list of those event channels that are connected to Windows event logs.<br/>   |



 

### Properties

The **MSFT\_MTEventChannel** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ClassicLog**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flag that indicates whether the event channel is a classic event channel.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The localized display name of the event channel.

</dd> <dt>

**DisplayPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The localized display path of the event channel. The value of this property may or may not be different from the DisplayName.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the **Name** property of [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where **Name** exists and is not a Key (such as for instances of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)), the same information can be present in both the **Name** and **ElementName** properties. Note that if there is an associated instance of **CIM\_EnabledLogicalElementCapabilities**, restrictions on this properties may exist as defined in **ElementNameMask** and **MaxElementNameLen** properties defined in that class.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Flag that indicates whether the event channel is enabled.

</dd> <dt>

**EventsCount**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of events in the log file that backs the event channel.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**InstanceID** is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below. To ensure uniqueness within the NameSpace, the value of **InstanceID** should be constructed using the following "preferred" algorithm: "*OrgID*:*LocalID*" Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the **InstanceID** or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in **InstanceID** must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting **InstanceID** is not reused across any **InstanceID**s produced by this or other providers for the NameSpace of this instance. If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to "CIM".

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**LogFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path to the file that backs the event channel.

</dd> <dt>

**LogFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the file, in bytes, of the log file that backs the event channel.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The unique and language neutral identifier of the event channel.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of a channel.

<dt>

<span id="Admin"></span><span id="admin"></span><span id="ADMIN"></span>

**Admin** (0)


</dt> <dd></dd> <dt>

<span id="Operational"></span><span id="operational"></span><span id="OPERATIONAL"></span>

**Operational** (1)


</dt> <dd></dd> <dt>

<span id="Analytic"></span><span id="analytic"></span><span id="ANALYTIC"></span>

**Analytic** (2)


</dt> <dd></dd> <dt>

<span id="Debug"></span><span id="debug"></span><span id="DEBUG"></span>

**Debug** (3)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





