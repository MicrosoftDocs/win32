---
Description: 'The event type class for the ViewStateFailureAuditEvent event. View State Failure Audit Event.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'ab43c8d7-7618-43bd-9b0e-90738ec248bb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'asp.net'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: ViewStateFailureAuditEvent class
---

# ViewStateFailureAuditEvent class

The event type class for the **ViewStateFailureAuditEvent** event. View State Failure Audit Event

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, EventType(84), EventLevel(3), EventVersion(1), EventTypeName("ViewStateFailureAuditEvent")]
class ViewStateFailureAuditEvent : FailureAuditEvent
{
  uint8   SECURITY_DESCRIPTOR[];
  uint64  TIME_CREATED;
  string  EventTime;
  string  EventID;
  sint64  SequenceNumber;
  sint64  Occurrence;
  sint32  EventCode;
  sint32  EventDetailCode;
  string  EventMessage;
  string  ApplicationDomain;
  string  TrustLevel;
  string  ApplicationVirtualPath;
  string  ApplicationPath;
  string  MachineName;
  string  CustomEventDetails;
  string  SecurityDescriptor = "O:BAG:BAD:(A;;0x10000001;;;S-1-5-11)";
  sint32  ProcessID;
  string  ProcessName;
  string  AccountName;
  string  RequestUrl;
  string  RequestPath;
  string  UserHostAddress;
  string  UserName;
  boolean UserAuthenticated;
  string  UserAuthenticationType;
  string  RequestThreadAccountName;
  string  ViewStateExceptionMessage;
  string  RemoteAddress;
  string  RemotePort;
  string  UserAgent;
  string  PersistedState;
  string  Referer;
  string  Path;
};
```

## Members

The **ViewStateFailureAuditEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **ViewStateFailureAuditEvent** class has these properties.

<dl> <dt>

**AccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The account name.

</dd> <dt>

**ApplicationDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (8), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The application domain.

</dd> <dt>

**ApplicationPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (11), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The application path.

</dd> <dt>

**ApplicationVirtualPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (10), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The application virtual path.

</dd> <dt>

**CustomEventDetails**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (13), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

Custom event details.

</dd> <dt>

**EventCode**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

The event code.

</dd> <dt>

**EventDetailCode**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6)
</dt> </dl>

The event detail code.

</dd> <dt>

**EventID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The identifier of the event.

</dd> <dt>

**EventMessage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The message that describes the event.

</dd> <dt>

**EventTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The time the event occurred.

</dd> <dt>

**MachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (12), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The name of the machine.

</dd> <dt>

**Occurrence**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

The *n*th occurrence of the event.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The path.

</dd> <dt>

**PersistedState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The persisted state.

</dd> <dt>

**ProcessID**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1)
</dt> </dl>

The process identifier.

</dd> <dt>

**ProcessName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The name of the process.

</dd> <dt>

**Referer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The referrer.

</dd> <dt>

**RemoteAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The remote address.

</dd> <dt>

**RemotePort**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The remote port.

</dd> <dt>

**RequestPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The path of the request.

</dd> <dt>

**RequestThreadAccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The name of the account that requested the thread.

</dd> <dt>

**RequestUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The URL of the request.

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](wmi.__event). For more information about constants used to set this security descriptor, see [WMI Security Constants](wmi.wmi_security_constants).

</dd> <dt>

**SecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event.

</dd> <dt>

**SequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

The event sequence number.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](wmi.__event).

For more information about using **uint64** values in scripts, see [Scripting in WMI](wmi.scripting_in_wmi).

</dd> <dt>

**TrustLevel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (9), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The level of code access security (CAS) that is applied to the application.

</dd> <dt>

**UserAgent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The user agent.

</dd> <dt>

**UserAuthenticated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

Is the user authenticated.

</dd> <dt>

**UserAuthenticationType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The type of user authentication.

</dd> <dt>

**UserHostAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The user host address.

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The user name.

</dd> <dt>

**ViewStateExceptionMessage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1), **StringTermination** ("NullTerminated"), **format** ("w")
</dt> </dl>

The ViewState exception message.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\aspnet<br/>                                                                |
| MOF<br/>                      | <dl> <dt>AspNet.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MSCoree.dll</dt> </dl> |



 

 




