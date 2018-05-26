---
Description: The LogRecord object can describe the definitional format for entries in a MessageLog, or can be used to instantiate the actual records in the Log.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d8a4000a-cdb9-442f-b89c-b452ebf2f24c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_PCSVLogRecord class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_PCSVLogRecord class

The LogRecord object can describe the definitional format for entries in a MessageLog, or can be used to instantiate the actual records in the Log. The latter approach provides a great deal more semantic definition and management control over the individual entries in a MessageLog, than do the record manipulation methods of the Log class. It is recommended that the data in individual Log entries be modeled using subclasses of LogRecord, to avoid the creation of LogRecords with one property (such as RecordData) without semantics. Definitional formats for LogRecords could be specified by establishing a naming convention for the RecordID and Message Timestamp key properties.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::System::Logs"), AMENDMENT]
class MSFT_PCSVLogRecord : CIM_LogRecord
{
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
  string   RecordFormat;
  string   RecordData;
  string   Locale;
  uint16   PerceivedSeverity;
  string   LogCreationClassName;
  string   LogName;
  string   CreationClassName;
  string   RecordID;
  datetime MessageTimestamp;
  string   DataFormat;
  uint8    RawData[];
};
```

## Members

The **MSFT\_PCSVLogRecord** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_PCSVLogRecord** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256)
</dt> </dl>

CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This member is introduced in [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**DataFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Deprecated** (CIM\_LogRecord.RecordFormat)
</dt> </dl>

A free-form string describing the LogRecord's data structure.

This member is introduced in [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM\_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**Locale**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

This member is introduced in [**CIM\_RecordForLog**](cim-recordforlog.md).

</dd> <dt>

**LogCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256), **Override**
</dt> </dl>

The scoping Log's CreationClassName.

This member is introduced in [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**LogName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256), **Override**
</dt> </dl>

The scoping Log's Name.

This member is introduced in [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**MessageTimestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A LogRecord's key structure includes a timestamp for the entry. If the timestamp for the entry is unknown, the value 99990101000000.000000+000 SHOULD be used.

This member is introduced in [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumerated value that describes the severity of the Indication from the notifier's point of view: 1 - Other, by CIM convention, is used to indicate that the Severity's value can be found in the OtherSeverity property. 3 - Degraded/Warning should be used when its appropriate to let the user decide if action is needed. 4 - Minor should be used to indicate action is needed, but the situation is not serious at this time. 5 - Major should be used to indicate action is needed NOW. 6 - Critical should be used to indicate action is needed NOW and the scope is broad (perhaps an imminent outage to a critical resource will result). 7 - Fatal/NonRecoverable should be used to indicate an error occurred, but it's too late to take remedial action. 2 and 0 - Information and Unknown (respectively) follow common usage. Literally, the Indication is purely informational or its severity is simply unknown.

This member is introduced in [**CIM\_RecordForLog**](cim-recordforlog.md).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

Other

</dd> <dt>

2
</dt> <dd>

Information

</dd> <dt>

3
</dt> <dd>

Degraded/Warning

</dd> <dt>

4
</dt> <dd>

Minor

</dd> <dt>

5
</dt> <dd>

Major

</dd> <dt>

6
</dt> <dd>

Critical

</dd> <dt>

7
</dt> <dd>

Fatal/NonRecoverable

</dd> </dl>

</dd> <dt>

**RawData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**RecordData**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_RecordForLog.RecordFormat)
</dt> </dl>

A string containing LogRecord data. If the corresponding RecordFormat property is &lt;empty&gt;, or cannot be parsed according to the recommended format, RecordData should be interpreted as a free-form string. If the RecordFormat property contains parseable format information (as recommended in the RecordFormat Description qualifier), the RecordData string SHOULD be parsed in accordance with this format. In this case, RecordData SHOULD begin with the delimiter character and this character SHOULD be used to separate substrings in the manner described. The RecordData string can then be parsed by the data consumer and appropriately typed.

This member is introduced in [**CIM\_RecordForLog**](cim-recordforlog.md).

</dd> <dt>

**RecordFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_RecordForLog.RecordData)
</dt> </dl>

A string describing the data structure of the information in the property, RecordData. If the RecordFormat string is &lt;empty&gt;, RecordData should be interpreted as a free-form string. To describe the data structure of RecordData, the RecordFormat string should be constructed as follows: - The first character is a delimiter character and is used to parse the remainder of the string into sub-strings. - Each sub-string is separated by the delimiter character and should be in the form of a CIM property declaration (i.e., datatype and property name). This set of declarations may be used to interpret the similarly delimited RecordData property. For example, using a '\*' delimiter, RecordFormat = "\*string ThisDay\*uint32 ThisYear\*datetime SomeTime" may be used to interpret: RecordData = "\*This is Friday\*2002\*20020807141000.000000-300".

This member is introduced in [**CIM\_RecordForLog**](cim-recordforlog.md).

</dd> <dt>

**RecordID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256)
</dt> </dl>

RecordID, with the MessageTimestamp property, serve to uniquely identify the LogRecord within a MessageLog. Note that this property is different than the RecordNumber parameters of the MessageLog methods. The latter are ordinal values only, useful to track position when iterating through a Log. On the other hand, RecordID is truly an identifier for an instance of LogRecord. It may be set to the record's ordinal position, but this is not required.

This member is introduced in [**CIM\_LogRecord**](cim-logrecord.md).

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



 

 




