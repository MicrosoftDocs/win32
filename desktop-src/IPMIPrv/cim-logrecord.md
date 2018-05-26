---
title: CIM\_LogRecord class
description: The LogRecord object can describe the definitional format for entries in a MessageLog, or can be used to instantiate the actual records in the Log.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8d3db379-40f2-4fab-b15a-3c07f28b8e7e
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_LogRecord class
- CIM_LogRecord class, described
topic_type:
- apiref
api_name:
- CIM_LogRecord
- CIM_LogRecord.Caption
- CIM_LogRecord.Description
- CIM_LogRecord.ElementName
- CIM_LogRecord.LogCreationClassName
- CIM_LogRecord.LogName
- CIM_LogRecord.CreationClassName
- CIM_LogRecord.RecordID
- CIM_LogRecord.MessageTimestamp
- CIM_LogRecord.DataFormat
- CIM_LogRecord.RecordFormat
- CIM_LogRecord.RecordData
api_location:
- IpmiPrv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_LogRecord class

The LogRecord object can describe the definitional format for entries in a MessageLog, or can be used to instantiate the actual records in the Log. The latter approach provides a great deal more semantic definition and management control over the individual entries in a MessageLog, than do the record manipulation methods of the Log class. It is recommended that the data in individual Log entries be modeled using subclasses of LogRecord, to avoid the creation of LogRecords with one property (such as RecordData) without semantics.

Definitional formats for LogRecords could be specified by establishing a naming convention for the RecordID and Message Timestamp key properties.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.8.1000"), UUID("{93e5f37b-7071-4c21-8733-d2eea2691e1a}"), AMENDMENT]
class CIM_LogRecord : CIM_ManagedElement
{
  string   Caption;
  string   Description;
  string   ElementName;
  string   LogCreationClassName;
  string   LogName;
  string   CreationClassName;
  string   RecordID;
  datetime MessageTimestamp;
  string   DataFormat;
  string   RecordFormat;
  string   RecordData;
};
```

## Members

The **CIM\_LogRecord** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_LogRecord** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

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

The name of the class used to create an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

</dd> <dt>

**DataFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_LogRecord.RecordFormat")
</dt> </dl>

A free-form string describing the log record's data structure.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties/identity data, and description information.

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

The **CreationClassName** of the scoping Log

</dd> <dt>

**LogName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_MessageLog.Name"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The **Name** of the scoping Log

</dd> <dt>

**MessageTimestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A **datetime** that, along with the **RecordID** property, serves to uniquely identify the log record within the log.

</dd> <dt>

**RecordData**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LogRecord.RecordFormat")
</dt> </dl>

A string containing log record data.

The **RecordData** string should be parsed according to the **RecordFormat** property. **RecordData** should begin with the defined delimiter and the delimiter should separate substrings in the manner described.

If the corresponding **RecordFormat** property is empty, or cannot be parsed, **RecordData** should be interpreted as a free-form string.

</dd> <dt>

**RecordFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LogRecord.RecordData")
</dt> </dl>

Defines the data structure of the information in the **RecordData** property. If the **RecordFormat** string is empty, **RecordData** should be interpreted as a free-form string.

The **RecordFormat** string should be constructed as follows:

-   The first character is a delimiter character. Use this character to split the rest of the string into sub-strings.

-   Each delimited sub-string should be in the form of a CIM property declaration, that is &lt;*datatype*&gt; &lt;*property name*&gt;.

This set of declarations can be used to interpret the similarly delimited **RecordData** property.

For example, using a '\*' delimiter, **RecordFormat** = "\*string ThisDay\*uint32 ThisYear\*datetime SomeTime" may be used to interpret: **RecordData** = "\*This is Friday\*2002\*20020807141000.000000-300".

</dd> <dt>

**RecordID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Along with the **MessageTimestamp** property, serves to uniquely identify the log record within the log.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





