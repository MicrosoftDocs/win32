---
title: TraceLogging Wrapper Macros
description: Lists the wrapper macros for TraceLogging providers.
ms.assetid: 806F43F3-D376-4DBD-A4C5-B5F01E5D009D
ms.topic: article
ms.date: 06/06/2022
---

# TraceLogging Wrapper Macros

The
[**TraceLoggingWrite**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwrite)
and
[**TraceLoggingWriteActivity**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwriteactivity)
macros emit TraceLogging events configured according to the macro parameters.
Each of these macros accept a set of required parameters followed by up to 99
optional parameters. Each optional parameter either configures the event or adds
a field to the event. Each optional parameter must be one of the TraceLogging
Wrapper macros described on this page.

For example:

```c
TraceLoggingWrite(
    g_hProvider,
    "MyEvent1",
    TraceLoggingLevel(WINEVENT_LEVEL_WARNING), // Levels defined in <winmeta.h>
    TraceLoggingKeyword(MyNetworkingKeyword),
    TraceLoggingString(operationName), // Adds an "operationName" field.
    TraceLoggingHResult(hr, "NetStatus")); // Adds a "NetStatus" field.
```

In this example, `g_hProvider` and `"MyEvent1"` are the required parameters.
They specify the provider to use for the event and the event's name. Each of the
remaining parameters is a wrapper macro. The `TraceLoggingLevel` and
`TraceLoggingKeyword` parameters configure the event. The `TraceLoggingString`
and `TraceLoggingHResult` parameters each add a field to the event.

## Event Configuration macros

The following macros configure the event.

If a particular configuration macro is not provided in the
**TraceLoggingWrite**, a default is used for that event. For example, if no
**TraceLoggingLevel** parameter is used for an event, the event uses a default
level of 5 (VERBOSE).

- [**TraceLoggingLevel**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogginglevel)
  sets the event's
  [level](/windows/win32/api/evntprov/ns-evntprov-event_descriptor). The level
  is an 8-bit value indicating event severity. Levels from 1
  (WINEVENT_LEVEL_CRITICAL) to 5 (WINEVENT_LEVEL_VERBOSE) are defined in
  `<winmeta.h>`. If not specified, the event defaults to level 5 (VERBOSE).
  Level is an important part of ETW event routing and filtering, so all events
  should have a meaningful non-zero level.
- [**TraceLoggingKeyword**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingkeyword)
  sets the event's
  [keyword](/windows/win32/api/evntprov/ns-evntprov-event_descriptor). A keyword
  is a 64-bit value with each bit indicating a category to which the event
  belongs. The low 48 bits of the keyword are defined by the owner of the
  provider while the high 16 bits of the keyword are defined by Microsoft. For
  example, you might decide that all providers with name "MyCompany.MyComponent"
  will use keyword 0x1 to mean "Networking". If not specified, the event
  defaults to keyword 0x0 (None). Keyword is an important part of ETW event
  routing and filtering, so all events should have a meaningful non-zero
  keyword.
- [**TraceLoggingOpcode**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingopcode)
  sets the event's
  [opcode](/windows/win32/api/evntprov/ns-evntprov-event_descriptor). The opcode
  is an 8-bit value indicating special semantics for the event, e.g. that the
  event records the beginning (WINEVENT_OPCODE_START) or end
  (WINEVENT_OPCODE_STOP) of an
  [ETW activity](/windows/win32/api/evntprov/nf-evntprov-eventactivityidcontrol)
  (a group of related events). If not specified, the event defaults to opcode 0
  (WINEVENT_OPCODE_INFO) indicating that no special semantics are required.
- [**TraceLoggingChannel**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingchannel)
  sets the event's
  [channel](/windows/win32/api/evntprov/ns-evntprov-event_descriptor). The
  channel is an 8-bit value that is used for various purposes. If not specified,
  the event defaults to channel 11 (WINEVENT_CHANNEL_TRACELOGGING). Most events
  do not need to change the event's channel and should not use
  **TraceLoggingChannel**.
- [**TraceLoggingEventTag**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingeventtag)
  sets the event's tag. The tag is a 28-bit value with provider-defined
  semantics. For example, a provider might define tag bit 0x1000000 to indicate
  that the event potentially contains personally-identifiable information and
  should receive special treatment from provider-specific event processing
  tools. If not specified, the tag defaults to 0.
- [**TraceLoggingDescription**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingdescription)
  sets the event's description. The description is a string literal with a
  human-readable description of the event. This serves as a comment about the
  event purpose, and the description is also recorded as an annotation in your
  component's debug symbols (PDB). If not specified, the description defaults to
  `""`.
- [**TraceLoggingCustomAttribute**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingcustomattribute)
  adds a key-value annotation to the component's debug symbols (PDB).

## Field macros

TraceLogging supports many wrapper macros for adding fields to an event. Each
field is a name-value pair. For example, `TraceLoggingInt32(argc, "ArgCount")`
would add an "ArgCount" field to the event containing the value of `argc` stored
as an INT32 value in the event.

Most of the field wrapper macros accept similar parameters:

- **value:** An expression that will be evaluated at runtime to determine the
  data to include in the field. Most field wrapper macros use a single parameter
  to specify the value, but some macros require multiple parameters for the
  field value, e.g. a pointer and a length. The value parameter(s) are always
  required.
  - In some cases, the field value is specified as **pszValue**, in which case
    it is a pointer to a 0-terminated string of characters to include in the
    field. **pszValue** may be NULL, in which case the field value will be an
    empty string `""`.
  - In some cases, the field value is specified as **pchValue**, in which case
    it is a pointer to a string of **cchValue** characters to include in the
    field. **pchValue** may be NULL only if **cchValue** is 0.
  - In some cases, the field value is specified as **pValue** with an
    automatically-determined size (no **cbValue** parameter), in which case it
    is a pointer to the value to include in the field. **pValue** may not be
    NULL.
  - In some cases, the field value is specified as **pValue** with a **cbValue**
    parameter to specify the size (in bytes) of the data to include in the
    field. **pValue** may be NULL only if **cbValue** is 0.
- **name:** A string literal (compile-time constant) with the name to use for
  the field. Most field wrapper macros do not require a name parameter. If the
  name parameter is omitted, the field's name is determined based on the
  preprocessor text of the macro's **value**, **pszValue**, **pchValue**, or
  **pValue** parameter. For example, `TraceLoggingInt32(x[4] + y)` is equivalent
  to `TraceLoggingInt32(x[4] + y, "x[4] + y")`. Both would add a field named
  `"x[4] + y"` to the event with a value determined by evaluating the expression
  `x[4] + y`.
- **description:** A string literal (compile-time constant) with a description
  to use for the field. This is mostly used as a convenient place to put a
  comment for the field, but the description is also recorded as an annotation
  in the component's debug symbols (PDB). The description is optional. If the
  description parameter is omitted, the field's description defaults to `""`.
- **tag:** A 28-bit integer (compile-time constant) with provider-defined
  semantics. For example, a provider might define tag 0x2 to indicate that the
  field contains a telephone number and should receive special treatment from
  provider-specific event processing tools. If the tag parameter is omitted, the
  field's tag defaults to 0.

For example, the following wrapper macro invocations all have the same effect:

- `TraceLoggingInt32(argc)`
- `TraceLoggingInt32(argc, "argc")`
- `TraceLoggingInt32(argc, "argc", "")`
- `TraceLoggingInt32(argc, "argc", "", 0)`

### Scalars

- [**TraceLoggingValue(value, [name, ...]):**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingvalue)
  Adds a field with a type that is automatically-deduced from the type of the
  value parameter. **(C++ only)**
- **TraceLoggingInt8(value, [name, ...]):** Adds a field with an INT8 value.
- **TraceLoggingUInt8(value, [name, ...]):** Adds a field with a UINT8 value.
- **TraceLoggingInt16(value, [name, ...]):** Adds a field with an INT16 value.
- **TraceLoggingUInt16(value, [name, ...]):** Adds a field with a UINT16 value.
- **TraceLoggingInt32(value, [name, ...]):** Adds a field with an INT32 value.
- **TraceLoggingUInt32(value, [name, ...]):** Adds a field with a UINT32 value.
- **TraceLoggingInt64(value, [name, ...]):** Adds a field with an INT64 value.
- **TraceLoggingUInt64(value, [name, ...]):** Adds a field with a UINT64 value.
- **TraceLoggingIntPtr(value, [name, ...]):** Adds a field with an INT_PTR value
  (signed integer with the same size as a pointer).
- **TraceLoggingUIntPtr(value, [name, ...]):** Adds a field with a UINT_PTR
  value (unsigned integer with the same size as a pointer).
- **TraceLoggingLong(value, [name, ...]):** Adds a field with a LONG value
  (signed long int, 32-bits on Windows platforms).
- **TraceLoggingULong(value, [name, ...]):** Adds a field with a ULONG value
  (unsigned long int, 32-bits on Windows platforms).
- **TraceLoggingHexInt8(value, [name, ...]):** Adds a field with an INT8 value
  with a hexadecimal formatting hint.
- **TraceLoggingHexUInt8(value, [name, ...]):** Adds a field with a UINT8 value
  with a hexadecimal formatting hint.
- **TraceLoggingHexInt16(value, [name, ...]):** Adds a field with an INT16 value
  with a hexadecimal formatting hint.
- **TraceLoggingHexUInt16(value, [name, ...]):** Adds a field with a UINT16
  value with a hexadecimal formatting hint.
- **TraceLoggingHexInt32(value, [name, ...]):** Adds a field with an INT32 value
  with a hexadecimal formatting hint.
- **TraceLoggingHexUInt32(value, [name, ...]):** Adds a field with a UINT32
  value with a hexadecimal formatting hint.
- **TraceLoggingHexInt64(value, [name, ...]):** Adds a field with an INT64 value
  with a hexadecimal formatting hint.
- **TraceLoggingHexUInt64(value, [name, ...]):** Adds a field with a UINT64
  value with a hexadecimal formatting hint.
- **TraceLoggingHexIntPtr(value, [name, ...]):** Adds a field with an INT_PTR
  value with a hexadecimal formatting hint.
- **TraceLoggingHexUIntPtr(value, [name, ...]):** Adds a field with a UINT_PTR
  value with a hexadecimal formatting hint.
- **TraceLoggingHexLong(value, [name, ...]):** Adds a field with a LONG value
  with a hexadecimal formatting hint.
- **TraceLoggingHexULong(value, [name, ...]):** Adds a field with a ULONG value
  with a hexadecimal formatting hint.
- **TraceLoggingFloat32(value, [name, ...]):** Adds a field with a FLOAT (32-bit
  floating point) value.
- **TraceLoggingFloat64(value, [name, ...]):** Adds a field with a DOUBLE
  (64-bit floating point) value.
- **TraceLoggingBoolean(value, [name, ...]):** Adds a field with an 8-bit
  Boolean value (Win32 `BOOLEAN` or C++ `bool`).
- **TraceLoggingBool(value, [name, ...]):** Adds a field with a 32-bit Boolean
  value (Win32 `BOOL`).
- **TraceLoggingChar(value, [name, ...]):** Adds a field with a `char` value
  (8-bit integer with string formatting hint, typically treated as code page
  1252).
- **TraceLoggingChar16(value, [name, ...]):** Adds a field with a `char16_t`
  value (16-bit integer with string formatting hint, typically treated as
  UCS-2).
- **TraceLoggingWChar(value, [name, ...]):** Adds a field with a `wchar_t` value
  (same as `char16_t` on Windows platforms).
- **TraceLoggingPointer(value, [name, ...]):** Adds a field with a `void*` value
  (pointer-sized value with a hexadecimal formatting hint).
- **TraceLoggingCodePointer(value, [name, ...]):** Adds a field with a `void*`
  value (pointer-sized value with a code-pointer formatting hint).
- **TraceLoggingPid(value, [name, ...]):** Adds a field with an INT32 value with
  a process ID formatting hint.
- **TraceLoggingTid(value, [name, ...]):** Adds a field with an INT32 value with
  a thread ID formatting hint.
- **TraceLoggingIPv4Address(value, [name, ...]):** Adds a field with a UINT32
  value with an IPv4 formatting hint (network byte order).
- **TraceLoggingIPv6Address(pValue, [name, ...]):** Adds a field with a 16-byte
  binary value with an IPv6 formatting hint.
- **TraceLoggingPort(value, [name, ...]):** Adds a field with a UINT16 value
  with an IP port formatting hint (network byte order).
- [**TraceLoggingSocketAddress(pValue, cbValue, [name, ...]):**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingsocketaddress)
  Adds a field with a [SOCKADDR](/windows/win32/api/winsock/ns-winsock-sockaddr)
  value.
- **TraceLoggingWinError(value, [name, ...]):** Adds a field with a UINT32 value
  with a Win32 error code formatting hint.
- **TraceLoggingNTStatus(value, [name, ...]):** Adds a field with an NTSTATUS
  (LONG) value with a WinNT error code formatting hint.
- **TraceLoggingHResult(value, [name, ...]):** Adds a field with an HRESULT
  (LONG) value with a Windows HRESULT formatting hint.
- **TraceLoggingFileTime(value, [name, ...]):** Adds a field with a
  [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime) value. When
  used in C code, the `value` parameter must be an lvalue expression.
- **TraceLoggingFileTimeUtc(value, [name, ...]):** Adds a field with a
  [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime) value with a
  UTC time zone formatting hint. When used in C code, the `value` parameter must
  be an lvalue expression.
- **TraceLoggingSystemTime(value, [name, ...]):** Adds a field with a
  [SYSTEMTIME](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) value.
  When used in C code, the `value` parameter must be an lvalue expression.
- **TraceLoggingSystemTimeUtc(value, [name, ...]):** Adds a field with a
  [SYSTEMTIME](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) value
  with a UTC time zone formatting hint. When used in C code, the `value`
  parameter must be an lvalue expression.
- **TraceLoggingGuid(value, [name, ...]):** Adds a field with a
  [GUID](/windows/win32/api/guiddef/ns-guiddef-guid) value. When used in C code,
  the `value` parameter must be an lvalue expression.
- **TraceLoggingString(pszValue, [name, ...]):** Adds a field with a
  0-terminated `char` string (typically treated as code page 1252). If pszValue
  is NULL, an empty string `""` is used as the field value.
- **TraceLoggingUtf8String(pszValue, [name, ...]):** Adds a field with a
  0-terminated `char` string with a UTF-8 formatting hint. If pszValue is NULL,
  an empty string `""` is used as the field value.
- **TraceLoggingString16(pszValue, [name, ...]):** Adds a field with a
  0-terminated `char16_t` string (UTF-16). If pszValue is NULL, an empty string
  `u""` is used as the field value.
- **TraceLoggingWideString(pszValue, [name, ...]):** Adds a field with a
  0-terminated `wchar_t` string (UTF-16 on Windows). If pszValue is NULL, an
  empty string `L""` is used as the field value.
- **TraceLoggingCountedString(pchValue, cchValue, [name, ...]):** Adds a field
  with a counted `char` string (typically treated as code page 1252). pchValue
  may be NULL only if cchValue is 0.
- **TraceLoggingCountedUtf8String(pchValue, cchValue, [name, description,
  tag]):** Adds a field with a counted `char` string with a UTF-8 formatting
  hint. pchValue may be NULL only if cchValue is 0.
- **TraceLoggingCountedString16(pchValue, cchValue, [name, ...]):** Adds a field
  with a counted `char16_t` string (UTF-16). pchValue may be NULL only if
  cchValue is 0.
- **TraceLoggingCountedWideString(pchValue, cchValue, [name, description,
  tag]):** Adds a field with a counted `wchar_t` string (UTF-16 on Windows).
  pchValue may be NULL only if cchValue is 0.
- **TraceLoggingAnsiString(pValue, [name, ...]):** Adds a field with an
  [ANSI_STRING](/windows/win32/api/ntdef/ns-ntdef-string) value. The pValue
  pointer must not be NULL.
- **TraceLoggingUnicodeString(pValue, [name, ...]):** Adds a field with a
  [UNICODE_STRING](/windows/win32/api/ntdef/ns-ntdef-_unicode_string) value. The
  pValue pointer must not be NULL.
- **TraceLoggingSid(pValue, [name, ...]):** Adds a field with a
  [SID](/windows/win32/api/winnt/ns-winnt-sid) value. The pValue pointer must
  not be NULL and must point at a properly-initialized SID (Revision and
  SubAuthorityCount must be valid).
- [**TraceLoggingBinary(pValue, cbValue, [name, ...]):**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingbinary)
  Adds a field with binary data.
- **TraceLoggingBinaryEx(pValue, cbValue, outType, [name, ...]):** Adds a field
  with binary data with the formatting hint specified by `outType`.
- **TraceLoggingBinaryBuffer(pValue, StructType, [name, ...]):** Adds a field
  with binary data. `pValue` must be a non-NULL pointer to a `StructType`
  struct. `pValue->Buffer` must point at the start of the data and
  `pValue->Length` must be the number of bytes of data to be included in the
  field.
- **TraceLoggingBinaryBufferEx(pValue, StructType, outType, name, description,
  tag):** Adds a field with binary data with the formatting hint specified by
  `outType`. `pValue` must be a non-NULL pointer to a `StructType` struct.
  `pValue->Buffer` must point at the start of the data and `pValue->Length` must
  be the number of bytes of data to be included in the field.
- [**TraceLoggingCustom(pValue, cbValue, protocol, bSchema, cbSchema, [name, ...]):**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingcustom)
  Adds a field with binary data that has been serialized according to a
  serialization protocol. Compile-time constant decoding information will be
  included along with the event to allow deserialization by the event decoder.

### Structures

You can use the
[**TraceLoggingStruct(fieldCount, name, [...]**)](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingstruct)
macro to create a structure (group of fields) and assign a name to it. The
**fieldCount** parameter indicates how many of the subsequent fields should be
counted as part of the structure. Structures may be nested, in which case each
nested structure and its contained fields counts as a single field for the
purpose of defining the parent struct.

### Arrays

You can create a field that contains an array of scalar (single) values. For
example, you add an array of GUIDs as a single field in your event.

> [!NOTE]
> While the TraceLogging protocol supports arrays of all types,
> TraceLoggingProvider.h only provides wrapper macros for arrays of simple
> values, e.g. it provides macros for arrays of INT32 and GUID but it does not
> provide macros for arrays of String or arrays of structures. It is possible to
> create events with arrays of complex values by marshaling the data into a
> buffer and then using the `TraceLoggingPacked` macros described below.

TraceLogging supports fixed-length and variable-length arrays.

- Use the `Array` macro in cases where the array length is not known at
  compile-time and may be different each time the event is generated.
- Use the `FixedArray` macro in cases where the array length is known at
  compile-time (i.e. when the array length is a constant). This communicates to
  the event consumer that all events with a particular event name will have the
  same number of items in the array field.

All of the array macros require the **pValues** and **cValues** parameters to be
specified, with **pValues** pointing to the start of the array content and
**cValues** set to the number of items in the array. **pValues** may be NULL
only if **cValues** is 0.

All of the array macros optionally accept **name**, **description**, and **tag**
parameters as described for the Scalar macros. If **name** is not specified, the
field name is determined from the preprocessor text of **pValues**. If
**description** is not specified, the field description will be `""`. If **tag**
is not specified, the field tag will be `0`.

> [!NOTE]
> To ensure ETW does not drop your events, avoid creating events with
> large arrays. ETW does not support events that are larger than 64KB. Any such
> events will be silently dropped by ETW. In addition, events that are larger
> than the consumer session's
> [BufferSize](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties)
> will also be dropped by ETW. The event size is based on the sum of the event's
> headers, metadata (provider, event, and field names), and data (field values).

- **TraceLoggingInt8Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingInt8FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingUInt8Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingUInt8FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingInt16Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingInt16FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingUInt16Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingUInt16FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingInt32Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingInt32FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingUInt32Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingUInt32FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingInt64Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingInt64FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingUInt64Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingUInt64FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingIntPtrArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingIntPtrFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingUIntPtrArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingUIntPtrFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingLongArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingLongFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingULongArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingULongFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexInt8Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexInt8FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUInt8Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUInt8FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexInt16Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexInt16FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUInt16Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUInt16FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexInt32Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexInt32FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUInt32Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUInt32FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexInt64Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexInt64FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUInt64Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUInt64FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexIntPtrArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexIntPtrFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUIntPtrArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexUIntPtrFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexLongArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexLongFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexULongArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingHexULongFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingFloat32Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingFloat32FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingFloat64Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingFloat64FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingBooleanArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingBooleanFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingBoolArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingBoolFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingCharArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingCharFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingChar16Array(pValues, cValues, \[name, ...\])**
- **TraceLoggingChar16FixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingWCharArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingWCharFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingPointerArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingPointerFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingCodePointerArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingCodePointerFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingFileTimeArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingFileTimeFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingFileTimeUtcArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingFileTimeUtcFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingSystemTimeArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingSystemTimeFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingSystemTimeUtcArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingSystemTimeUtcFixedArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingGuidArray(pValues, cValues, \[name, ...\])**
- **TraceLoggingGuidFixedArray(pValues, cValues, \[name, ...\])**

## Packed macros

TraceLoggingProvider.h only provides field macros for blittable field types,
i.e. fields where each field macro corresponds to a single field and a single
contiguous region of memory with the field's value.

TraceLoggingProvider.h does not provide direct support for more complex cases
such as:

- Logging an array of a variable-length type such as an array of strings.
- Logging an array of structures.
- Passing multiple fields to ETW via a single buffer to reduce event logging
  overhead.

To support these scenarios, TraceLoggingProvider.h defines several
`TraceLoggingPacked` macros that allow you to directly manipulate the event
definition (metadata) and field values (data) of the event.

> [!WARNING]
> The `TraceLoggingPacked` macros are tricky to use correctly and
> require a good understanding of how TraceLogging events are created. If used
> incorrectly they will result in corrupt events that do not decode correctly.

For details on the use of these macros, refer to the comments in the
TraceLoggingProvider.h header.

- **TraceLoggingPackedField(pValue, cbValue, inType, [name, description,
  tags]):** Directly adds field data (pValue, cbValue) and field metadata (name,
  inType).
- **TraceLoggingPackedFieldEx(pValue, cbValue, inType, outType, [name, ...]):**
  Directly adds field data (pValue, cbValue) and field metadata (name, inType)
  along with a formatting hint (outType).
- **TraceLoggingPackedMetadata(inType, [name, ...]):** Directly adds field
  metadata (name, inType) without adding field data. Corresponding field data
  must be added via TraceLoggingPackedData.
- **TraceLoggingPackedMetadataEx(inType, outType, [name, ...]):** Directly adds
  field metadata (name, inType) and a formatting hint (outType) without adding
  field data. Corresponding field data must be added via TraceLoggingPackedData.
- **TraceLoggingPackedStruct(fieldCount, name, [...]):** Directly adds field
  metadata (name, fieldCount) for a struct.
- **TraceLoggingPackedStructArray(fieldCount, [name, ...]):** Directly adds
  field metadata (name, fieldCount) for a variable-length array of struct. The
  array length must be specified via TraceLoggingPackedData.
- **TraceLoggingPackedData(pValue, cbValue):** Directly adds field data to an
  event without adding any field metadata.
- **TraceLoggingPackedDataEx(pValue, cbValue, dataDescType):** Directly adds
  field data to an event without adding any field metadata, using a specific
  `Type` in the
  [EVENT_DATA_DESCRIPTOR](/windows/win32/api/evntprov/ns-evntprov-event_data_descriptor)
  for the data.
