---
description: Use the qualifiers defined in this section when creating your provider MOF class, event MOF class, event type MOF class, and the properties of the event type MOF class.
ms.assetid: 3bc82074-05a7-411f-884f-5da1fd08112b
title: Event Tracing MOF Qualifiers
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Event Tracing MOF Qualifiers

Use the qualifiers defined in this section when creating your [provider MOF class](#provider-mof-class-qualifiers), [event MOF class](#event-mof-class-qualifiers), [event type MOF class](#event-type-mof-class-qualifiers), and [the properties of the event type MOF class](#property-qualifiers). For an example that includes some of these qualifiers, see [Publishing Your Event Schema](publishing-your-event-schema.md).

## Provider MOF class qualifiers

The following table lists the qualifiers you can specify on a provider MOF class.



| Qualifier | Data type  | Description                                                                                                                                                                                                                                                  |
|-----------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Guid**  | **String** | Required. String Guid that uniquely identifies a provider. For example, Guid("{3F92E6E0-9886-434e-85DB-0D11D3904C0A}"). This is the same GUID you use when you call the [**RegisterTraceGuids**](/windows/win32/api/evntrace/nf-evntrace-registertraceguidsa) function to register your provider. |



 

## Event MOF class qualifiers

The following table lists the qualifiers you can specify on an event class (the parent class that groups related event type classes).

| Qualifier        | Data type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Guid**         | **String**  | Required. String Guid that identifies a class of events. For example, Guid("{3F92E6E0-9886-434e-85DB-0D11D3904C0A}"). Event providers use the Guid to set the [**EVENT\_TRACE\_HEADER.Guid**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) member, so that consumers can determine the class of events they are receiving.                                                                                                                                                                                                                                                                                  |
| **EventVersion** | **Integer** | This qualifier is optional for the latest version of an event trace class and is required for all older versions of the class. The latest version of the class either does not specify the **EventVersion** qualifier or has the highest version number. Version numbers begin with 0, for example, EventVersion(0).Typically, when you create a new version of the class, you also rename the previous version to <classname>\_Vn, where n is an incremental number starting at 0. For an example, see [**FileIo**](fileio.md) and [**FileIo\_V0**](fileio-v0.md).<br/> |



 

## Event type MOF class qualifiers

The following table lists the qualifiers you can specify on an event type class (the class that defines the event property data).



| Qualifier         | Value       | Description                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EventType**     | **Integer** | Required. Identifies the event type class. For example, EventType(1). The event provider uses the same event type value to set [**EVENT\_TRACE\_HEADER.Class.Type**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header). If the same MOF class is used for multiple event types (because they use the same event data), specify the event type value as an array of integers, for example, EventType{12,15}. |
| **EventTypeName** | **String**  | Optional. Describes the event type. For example, EventTypeName("Start"). If the same MOF class is used for multiple event types (because they use the same event data), specify the event type name value as an array of strings, for example, EventTypeName{"Start", "End"}. The elements of the EventTypeName array correspond directly to the EventType array.                 |



 

## Property qualifiers

The following table lists the qualifiers you can specify on a property.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Qualifier</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>BitMap</strong></td>
<td>Specifies the bit positions that map to string values. If you specify this qualifier, you must also specify the <strong>BitValues</strong> qualifier.</td>
</tr>
<tr class="even">
<td><strong>BitValues</strong></td>
<td>String values. If the <strong>BitMap</strong> qualifier is also specified, the strings correspond directly to the values in the <strong>BitMap</strong> qualifier. Otherwise, assume the property value is a one-based index into the value strings (bit one corresponds to the first string in the list).</td>
</tr>
<tr class="odd">
<td><strong>Extension</strong></td>
<td>Provides additional information on how to consume (interpret) the data. The extension value is case-insensitive. Include the value in quotes, for example, Extension(&quot;Guid&quot;). Possible extension values are: <dl> <dt><span id="Guid"></span><span id="guid"></span><span id="GUID"></span>Guid</dt> <dd> Indicates the property data is a Guid. The MOF data type must be <strong>object</strong>. The payload is expected to be a <strong>GUID</strong> structure.<br/> </dd> <dt><span id="IPAddr_and_IPAddrV4"></span><span id="ipaddr_and_ipaddrv4"></span><span id="IPADDR_AND_IPADDRV4"></span>IPAddr and IPAddrV4</dt> <dd> The data is an IP V4 address. The MOF data type must be <strong>object</strong>. The payload is expected to be an unsigned long. Each byte of the unsigned long represents one of the four parts of the IP address (p1.p2.p3.p4). The low-order byte contains the value for p1, the next byte contains the value for p2, and so on.<br/> <strong>Prior to Windows Vista:</strong> The IPAddrV4 extension is not supported.<br/> </dd> <dt><span id="IPAddrV6"></span><span id="ipaddrv6"></span><span id="IPADDRV6"></span>IPAddrV6</dt> <dd> The data is an IP V6 address. The MOF data type must be <strong>object</strong>. The payload is expected to be an <strong>IN6_ADDR</strong> structure. <br/> <strong>Prior to Windows Vista:</strong> The IPAddrV6 extension is not supported.<br/> </dd> <dt><span id="NoPrint"></span><span id="noprint"></span><span id="NOPRINT"></span>NoPrint</dt> <dd> Indicates that the consumer should not print this data.<br/> </dd> <dt><span id="Port"></span><span id="port"></span><span id="PORT"></span>Port</dt> <dd> The data identifies a port number. The MOF data type must be <strong>object</strong>. The payload is expected to be an unsigned short.<br/> </dd> <dt><span id="RString"></span><span id="rstring"></span><span id="RSTRING"></span>RString</dt> <dd> Newline characters were replaced with spaces. The payload is expected to be a null-terminated, ANSI string.<br/> </dd> <dt><span id="RWString"></span><span id="rwstring"></span><span id="RWSTRING"></span>RWString</dt> <dd> Newline characters were replaced with spaces. The payload is expected to be a null-terminated, wide-character string.<br/> </dd> <dt><span id="Sid"></span><span id="sid"></span><span id="SID"></span>Sid</dt> <dd> The data represents a binary blob SID. The MOF data type must be <strong>object</strong>. <br/> The SID is of a variable length. The value contained in the first 4-bytes (<strong>ULONG</strong>) indicates whether the blob contains a SID. If the first 4-bytes (<strong>ULONG</strong>) of the blob is nonzero, the blob contains a SID. The first part of the blob contains the TOKEN_USER (the structure is aligned on an 8-byte boundary) and the second part contains the SID. To address the SID portion of the blob:<br/>
<ul>
<li>Set a byte pointer to the beginning of the blob</li>
<li>Multiply the pointer size for the event log by 2 and add the product to the byte pointer (the <strong>PointerSize</strong> member of <a href="/windows/win32/api/evntrace/ns-evntrace-trace_logfile_header"><strong>TRACE_LOGFILE_HEADER</strong></a> contains the pointer size value)</li>
</ul>
<br/> You can use the following macro to determine the length of the SID. <br/>
<pre class="syntax" data-space="preserve"><code>#define SeLengthSid( Sid ) \
  (8 + (4 * ((SID *)Sid)->SubAuthorityCount))</code></pre>
</dd> <dt><span id="SizeT"></span><span id="sizet"></span><span id="SIZET"></span>SizeT</dt> <dd> Indicates that the property contains a pointer value. The size of the pointer value depends on the operating system used to log the event; the payload will contain a 4-byte value for 32-bit systems or an 8-byte value for 64-bit systems. The MOF data type must be <strong>object</strong>.<br/> Consumers should ignore the data type and <strong>Format</strong> qualifier if the property includes the <strong>SizeT</strong> extension. To determine the size of data to read for the property, use:
<ul>
<li>The <strong>PointerSize</strong> member of <a href="/windows/win32/api/evntrace/ns-evntrace-trace_logfile_header"><strong>TRACE_LOGFILE_HEADER</strong></a></li>
<li>The <strong>Flags</strong> member of <a href="/windows/desktop/api/evntcons/ns-evntcons-event_header"><strong>EVENT_HEADER</strong></a></li>
</ul>
<br/> <strong>Prior to Windows Vista:</strong> The <strong>PointerSize</strong> value may not be accurate. For example, on a 64-bit computer, a 32-bit application will log 4-byte pointers; however, the session will set <strong>PointerSize</strong> to 8.<br/> </dd> <dt><span id="Variant"></span><span id="variant"></span><span id="VARIANT"></span>Variant</dt> <dd> The data represents a blob. The first four bytes (uint32) indicate the size of the blob. The MOF data type must be <strong>object</strong>. <br/> </dd> <dt><span id="WmiTime"></span><span id="wmitime"></span><span id="WMITIME"></span>WmiTime</dt> <dd> Translates the time stamp to system time. The MOF data type must be <strong>object</strong>. The payload is expected to be an unsigned 64-bit integer.<br/> <strong>Prior to Windows Vista:</strong> Not available.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>Format</strong></td>
<td>Defines the format of the property data. For example, including Format(&quot;w&quot;) on a string property indicates the string is a wide string. Possible values are: 
<table>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="c"></span><span id="C"></span>c<br/></td>
<td>Display the property value as an ASCII character. You can use this qualifier with <strong>uint8</strong> data types.<br/></td>
</tr>
<tr class="even">
<td><span id="s"></span><span id="S"></span>s<br/></td>
<td>Treat the array of characters as a null-terminated string. The string is a wide-character string if the data type is <strong>char16</strong>; otherwise, the string is an ASCII character string.<br/></td>
</tr>
<tr class="odd">
<td><span id="w"></span><span id="W"></span>w<br/></td>
<td>The property value is a wide-character string. You can use this qualifier with <strong>string</strong> data types. <br/></td>
</tr>
<tr class="even">
<td><span id="x"></span><span id="X"></span>x<br/></td>
<td>Display the property value as a hexadecimal number. You can use this qualifier with 16-, 32-, and 64-bit integer data types.<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td><strong>Pointer</strong></td>
<td><p>Indicates that the property contains a pointer value. The size of the pointer value depends on the operating system used to log the event; the payload will contain a 4-byte value for 32-bit systems or an 8-byte value for 64-bit systems. The MOF data type must be <strong>object</strong>.</p>
<p>Consumers should ignore the data type and <strong>Format</strong> qualifier if the property includes the <strong>SizeT</strong> extension. To determine the size of data to read for the property, use:</p>
<ul>
<li>The <strong>PointerSize</strong> member of <a href="/windows/win32/api/evntrace/ns-evntrace-trace_logfile_header"><strong>TRACE_LOGFILE_HEADER</strong></a></li>
<li>The <strong>Flags</strong> member of <a href="/windows/desktop/api/evntcons/ns-evntcons-event_header"><strong>EVENT_HEADER</strong></a></li>
</ul>
<p><strong>Prior to Windows Vista:</strong> The <strong>PointerSize</strong> value may not be accurate. For example, on a 64-bit computer, a 32-bit application will log 4-byte pointers; however, the session will set <strong>PointerSize</strong> to 8.</p>
<p>Note that some events use <strong>PointerType</strong> instead of <strong>Pointer</strong>; do not use <strong>PointerType</strong>.</p></td>
</tr>
<tr class="even">
<td><strong>StringTermination</strong></td>
<td>Indicates how the string property is terminated. For example, StringTermination(&quot;NullTerminated&quot;) indicates the string property is null-terminated. Possible values are:
<dl> <dt><span id="Counted"></span><span id="counted"></span><span id="COUNTED"></span><strong>Counted</strong></dt> <dd>
<p>The length of the string is embedded at the beginning of the string as a <strong>USHORT</strong> value.</p>
</dd> <dt><span id="NotCounted"></span><span id="notcounted"></span><span id="NOTCOUNTED"></span><strong>NotCounted</strong></dt> <dd>
<p>The string is not null-terminated and the length of the string is not embedded at the beginning of the string. In this case, the string should be the last element and occupy all the space to the end of the event data.</p>
</dd> <dt><span id="NullTerminated"></span><span id="nullterminated"></span><span id="NULLTERMINATED"></span><strong>NullTerminated</strong></dt> <dd>
<p>The string is null-terminated. If you do not specify the <strong>StringTermination</strong> qualifier, the string is assumed to be null-terminated.</p>
</dd> <dt><span id="ReverseCounted"></span><span id="reversecounted"></span><span id="REVERSECOUNTED"></span><strong>ReverseCounted</strong></dt> <dd>
<p>The length of the string is embedded at the beginning of the string as a <strong>USHORT</strong> value in big-endian format.</p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>ValueDescriptions</strong></td>
<td>Provides descriptions for each value in the <strong>Values</strong> qualifier. The <a href="/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfieldinformation"><strong>TdhEnumerateProviderFieldInformation</strong></a> and <a href="/windows/desktop/api/Tdh/nf-tdh-tdhqueryproviderfieldinformation"><strong>TdhQueryProviderFieldInformation</strong></a> functions return these descriptions when you try to retrieve keyword and level information. The descriptions are optional. If you do not provide the descriptions, the functions return <strong>NULL</strong>. See <a href="#specifying-level-and-enable-flags-values-for-a-provider">Specifying level and enable flags values for a provider</a> for more details.</td>
</tr>
<tr class="even">
<td><strong>ValueMap</strong></td>
<td>Specifies the integer index or flag values that map to string values. If you specify this qualifier, you must also specify the <strong>Values</strong> qualifier, and optionally the <strong>ValueType</strong> qualifier. Note that ETW does not support the WMI option of having strings for value map values.
<p>The following example shows how to use the ValueMap, Values, and ValueType qualifiers.</p>
<pre class="syntax" data-space="preserve"><code>ValueType(&quot;flag&quot;),
ValueMap {&quot;0x01&quot;, &quot;0x02&quot;, &quot;0x04&quot;, &quot;0x08&quot;},
Values {&quot;ValueMapFlag1&quot;, &quot;ValueMapFlag2&quot;, &quot;ValueMapFlag4&quot;, &quot;ValueMapFlag8&quot;}]</code></pre></td>
</tr>
<tr class="odd">
<td><strong>Values</strong></td>
<td>String values. If the <strong>ValueMap</strong> qualifier is also specified, the strings correspond directly to the values in the <strong>ValueMap</strong> qualifier. Otherwise, assume the property value is a zero-based index into the value strings.</td>
</tr>
<tr class="even">
<td><strong>ValueType</strong></td>
<td>Indicates if the <strong>ValueMap</strong> values are integer index values or bit flag values. If you do not specify this qualifier, integer index values are assumed. To specify that the values are integer index values, use ValueType(&quot;index&quot;). To specify that the values are bit flag values, use ValueType(&quot;flag&quot;).</td>
</tr>
<tr class="odd">
<td><strong>WmiDataId</strong></td>
<td>Each property must contain the <strong>WmiDataId</strong> qualifier. <strong>WmiDataId</strong> defines the order in which the consumer reads the event data. The value for <strong>WmiDataId</strong> starts at 1 and increments for each property in the class. For example, WmiDataId(1).</td>
</tr>
<tr class="even">
<td><strong>XMLFragment</strong></td>
<td>Indicates that the data is in XML format and ready to display without further formatting.</td>
</tr>
</tbody>
</table>



 

## Specifying level and enable flags values for a provider

To document the level and enable flags that a controller would use to enable your provider, include the "Level" and "Flags" properties in your provider MOF class. The Level and Flags property names are case sensitive. The properties must include the **Values** and **ValueMap** qualifiers, which specify the possible level and enable flag values. The **ValueMap** for the enable flag values must be bit (flag) values. The **ValueDescriptions** qualifier is optional but you should use it to provide descriptions for each possible value. The descriptions are used when someone calls the [**TdhEnumerateProviderFieldInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfieldinformation) and [**TdhQueryProviderFieldInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhqueryproviderfieldinformation) functions to get the possible level and enable flags (keywords) values for the provider.

The following shows a provider class that specifies the possible level and enable flags values.

``` syntax
[Dynamic,
 Description("IIS_Trace") : amended,
 guid("{3a2a4e84-4c21-4981-ae10-3fda0d9b0f83}"),
 locale("MS\\0x409")]
class IIS_Trace : EventTrace
{
    [Description ("Enable Flags") : amended,
        ValueDescriptions{
             "Allow_tracing_only_selected_requests ",
             "IIS_authentication_events ",
             "IIS_security_events ",
             "IIS_filter_events ",
             "IIS_static_file_events ",
             "IIS_CGI_events ",
             "IIS_compression_events ",
             "IIS_cache_events ",
             "IIS_request_notifications_events ",
             "IIS_module_events ",
             "IIS_FastCGI_events "},
        DefineValues{
             "UseUrlFilter",
             "IISAuthentication",
             "IISSecurity",
             "IISFilter",
             "IISStaticFile",
             "IISCGI",
             "IISCompression",
             "IISCache",
             "IISRequestNotification",
             "IISModule",
             "IISFastCGI"},
        Values{
             "UseUrlFilter",
             "IISAuthentication",
             "IISSecurity",
             "IISFilter",
             "IISStaticFile",
             "IISCGI",
             "IISCompression",
             "IISCache",
             "IISRequestNotification",
             "IISModule",
             "IISFastCGI"},
        ValueMap{
             "0x00000001",
             "0x00000002",
             "0x00000004",
             "0x00000008",
             "0x00000010",
             "0x00000020",
             "0x00000040",
             "0x00000080",
             "0x00000100",
             "0x00000200",
             "0x00001000"}: amended
    ]
    uint32 Flags;

    [Description ("Levels") : amended,
        ValueDescriptions{
            "Abnormal exit or termination",
            "Severe errors that need logging",
            "Warnings such as allocation failure",
            "Includes non-error cases",
            "Detailed traces from intermediate steps" } : amended,
         DefineValues{
            "TRACE_LEVEL_FATAL",
            "TRACE_LEVEL_ERROR",
            "TRACE_LEVEL_WARNING"
            "TRACE_LEVEL_INFORMATION",
            "TRACE_LEVEL_VERBOSE" },
        Values{
            "Fatal",
            "Error",
            "Warning",
            "Information",
            "Verbose" },
        ValueMap{
            "0x1",
            "0x2",
            "0x3",
            "0x4",
            "0x5" },
        ValueType("index")
    ]
    uint32 Level;
};
```

 

 
