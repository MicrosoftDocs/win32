---
title: LogRecord class
description: Represents a log entry in the BMC system event log (SEL).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd968ba06-692a-4246-a17a-3a0bf3bd22ab'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["IPMI provider WS-Management", "LogRecord class", "LogRecord class, described"]
topic_type:
- apiref
api_name:
- LogRecord
- LogRecord.Caption
- LogRecord.Description
- LogRecord.ElementName
- LogRecord.LogCreationClassName
- LogRecord.LogName
- LogRecord.CreationClassName
- LogRecord.RecordID
- LogRecord.MessageTimestamp
- LogRecord.RecordFormat
- LogRecord.RecordData
- LogRecord.DataFormat
api_location:
- IpmiPrv.dll
api_type:
- DllExport
---

# LogRecord class

The **LogRecord** class represents a log entry in the BMC system event log (SEL).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("IPMIPrv"), UUID("{5efd8f2b-e1c7-46c1-a5cc-3aa70779c862}"), AMENDMENT]
class LogRecord : CIM_LogRecord
{
  string   Caption;
  string   Description;
  string   ElementName;
  string   LogCreationClassName;
  string   LogName;
  string   CreationClassName;
  string   RecordID;
  datetime MessageTimestamp;
  string   RecordFormat;
  string   RecordData;
  string   DataFormat;
};
```

## Members

The **LogRecord** class has these types of members:

-   [Properties](#properties)

### Properties

The **LogRecord** class has these properties.

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

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

**CreationClassName** indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**DataFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_LogRecord.RecordFormat")
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead, we recommend that you use the **RecordFormat** property.

 

A description of this data structure.

This property is inherited from [**CIM\_LogRecord**](cim-logrecord.md).

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

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name IN ADDITION TO its key properties/identity data, and description information.

Note that ManagedSystemElement's **Name** property is also defined as a user-friendly name. But, it is often subclassed to be a [**Key**](https://msdn.microsoft.com/library/aa392157). It is not reasonable that the same property can convey both identity and a user friendly name, without inconsistencies. Where **Name** exists and is not a **Key** (such as for instances of LogicalDevice), the same information MAY be present in both the **Name** and **ElementName** properties.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**LogCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_MessageLog.CreationClassName"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping Log's **CreationClassName**.

This property is inherited from [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**LogName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_MessageLog.Name"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping Log's **Name**.

This property is inherited from [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**MessageTimestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A **LogRecord**'s [**Key**](https://msdn.microsoft.com/library/aa392157) structure includes a timestamp for the entry.

This property is inherited from [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**RecordData**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogRecord**](cim-logrecord.md).**RecordFormat**")
</dt> </dl>

A string containing **LogRecord** data.

If the corresponding **RecordFormat** property is &lt;empty&gt;, or cannot be parsed according to the recommended format, **RecordData** should be interpreted as a free-form string. If the **RecordFormat** property contains parseable format information (as recommended in the **RecordFormat** Description qualifier), the **RecordData** string SHOULD be parsed in accordance with this format. In this case, RecordData SHOULD begin with the delimiter character and this character SHOULD be used to separate substrings in the manner described. The **RecordData** string can then be parsed by the data consumer and appropriately typed.

This property is inherited from [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**RecordFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogRecord**](cim-logrecord.md).**RecordData**")
</dt> </dl>

A string describing the data structure of the information in the property, RecordData. If the RecordFormat string is &lt;empty&gt;, RecordData should be interpreted as a free-form string.

To describe the data structure of **RecordData**, the **RecordFormat** string should be constructed as follows:

\- The first character is a delimiter character and is used to parse the remainder of the string into sub-strings.

\- Each sub-string is separated by the delimiter character and should be in the form of a CIM property declaration (i.e., datatype and property name). This set of declarations may be used to interpret the similarly delimited **RecordData** property.

For example, using a '\*' delimiter, **RecordFormat** = "\*string ThisDay\*uint32 ThisYear\*datetime SomeTime"

may be used to interpret: **RecordData** = "\*This is Friday\*2002\*20020807141000.000000-300".

This property is inherited from [**CIM\_LogRecord**](cim-logrecord.md).

</dd> <dt>

**RecordID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

**RecordID**, with the **MessageTimestamp** property, serve to uniquely identify the **LogRecord** within a MessageLog. Note that this property is different than the *RecordNumber* parameters of the MessageLog methods. The latter are ordinal values only, useful to track position when iterating through a Log. On the other hand, **RecordID** is truly an identifier for an instance of **LogRecord**. It may be set to the record's ordinal position, but this is not required.

This property is inherited from [**CIM\_LogRecord**](cim-logrecord.md).

</dd> </dl>

## Remarks

The following example shows the relationship between **RecordFormat** and **RecordData** for a system event **LogRecord** instance and an operating system shutdown event **LogRecord** instance.

### System SEL Event

The **RecordFormat** string is "\*string CIM\_Sensor.DeviceID\*uint8\[2\] IPMI\_RecordID\*uint8 IPMI\_RecordType\*uint8\[4\] IPMI\_Timestamp\*uint8\[2\] IPMI\_GeneratorID\*uint8 IPMI\_EvMRev\*uint8 IPMI\_SensorType\*uint8 IPMI\_SensorNumber\*boolean IPMI\_AssertionEvent\*uint8 IPMI\_EventType\*uint8 IPMI\_EventData1\*uint8 IPMI\_EventData2\*uint8 IPMI\_EventData3\*".

The **RecordData** string is "\*SEL(114.0.32)\*01 00\*02\*0F AC C1 49\*20 00\*04\*10\*72\*true\*6F\*02\*FF\*FF\*".



| **RecordFormat**                  | **RecordData** | Meaning                                                                                                                                                                               |
|-----------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \*string **CIM\_Sensor.DeviceID** | SEL(114.0.32)  | The ID of the sensor device that generated this event is 114.0.32.                                                                                                                    |
| \*uint8\[2\] IPMI\_RecordID       | 01 00          | The ID of this SEL Record is 1.                                                                                                                                                       |
| \*uint8 IPMI\_RecordType          | 02             | The record type of this event is "System Event Log".                                                                                                                                  |
| \*uint8\[4\] IPMI\_Timestamp      | 0F AC C1 49    | The event timestamp is 3/19/2009 2:21:03 AM.                                                                                                                                          |
| \*uint8\[2\] IPMI\_GeneratorID    | 20 00          | The ID is an I2C Slave Address, 0x20. This event message was received through the system interface, primary IPMB, or was internally generated by the BMC. The IPMB device LUN is 0x0. |
| \*uint8 IPMI\_EvMRev              | 04             | Event Message format version is IPMI v1.5/v2.0.                                                                                                                                       |
| \*uint8 IPMI\_SensorType          | 10             | The SensorType code that generated this event is 10,Event Logging Disabled.                                                                                                           |
| \*uint8 IPMI\_SensorNumber        | 72             | The number of the sensor that generated this event is 114.                                                                                                                            |
| \*boolean IPMI\_AssertionEvent    | true           | This is an assertion event.                                                                                                                                                           |
| \*uint8 IPMI\_EventType           | 6F             | The event type of this event is a sensor-specific. The sensor class is discrete.                                                                                                      |
| \*uint8 IPMI\_EventData1          | 02             | Event request message data.                                                                                                                                                           |
| \*uint8 IPMI\_EventData2          | FF             | Event request message data.                                                                                                                                                           |
| \*uint8 IPMI\_EventData3          | FF             | Event request message data.                                                                                                                                                           |



 

### Operating system shutdown SEL event

The **RecordFormat** string is "\*uint8\[2\] IPMI\_RecordID\*uint8 IPMI\_RecordType\*uint8\[4\] IPMI\_Timestamp\*uint8\[3\] IPMI\_ManufacturerID\*uint8\[6\] IPMI\_OEMDefinedData\*".

The **RecordData** string is "\*03 00\*DD\*7B FE C4 49\*37 01 00\*00 00 00 00 C0 00".



| **RecordFormat**                  | **RecordData**    | Meaning                                                                        |
|-----------------------------------|-------------------|--------------------------------------------------------------------------------|
| \*uint8\[2\] IPMI\_RecordID       | 03 00             | The ID of this SEL Record is 3.                                                |
| \*uint8 IPMI\_RecordType          | DD                | The record type of this event is "Timestamped OEM SEL" record.                 |
| \*uint8\[4\] IPMI\_Timestamp      | 7B FE C4 49       | The event timestamp is 3/21/2009 2:49:31 PM                                    |
| \*uint8\[3\] IPMI\_ManufacturerID | 37 01 00          | The manufacturer ID is 311, which is the IANA enterprise number for Microsoft. |
| \*uint8\[6\] IPMI\_OEMDefinedData | 00 00 00 00 C0 00 | The OEM defined data is a Windows Shutdown Reason: C0000000.                   |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogRecord**](cim-logrecord.md)
</dt> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> </dl>

 

 





