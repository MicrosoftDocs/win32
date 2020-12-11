---
title: ChannelType Complex Type
description: Defines a channel to which providers can log events.
ms.assetid: 882506e5-222b-45c8-af4b-59db8baa1dae
keywords:
- ChannelType complex type EventLog
topic_type:
- apiref
api_name:
- ChannelType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ChannelType Complex Type

Defines a channel to which providers can log events.

``` syntax
<xs:complexType name="ChannelType"
    mixed="true"
>
    <xs:sequence>
        <xs:element name="logging"
            type="ChannelLoggingType"
            minOccurs="0"
         />
        <xs:element name="publishing"
            type="ChannelPublishingType"
            minOccurs="0"
         />
    </xs:sequence>
    <xs:attribute name="name"
        type="anyURI"
        use="required"
     />
    <xs:attribute name="chid"
        type="token"
        use="optional"
     />
    <xs:attribute name="type"
        type="string"
        use="required"
     />
    <xs:attribute name="symbol"
        type="CSymbolType"
        use="optional"
     />
    <xs:attribute name="access"
        type="string"
        use="optional"
     />
    <xs:attribute name="isolation"
        type="string"
        use="optional"
     />
    <xs:attribute name="enabled"
        type="boolean"
        default="false"
        use="optional"
     />
    <xs:attribute name="value"
        type="UInt8Type"
        use="optional"
     />
    <xs:attribute name="message"
        type="string"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                                  | Type                                                                                   | Description                                                                                                                                                                                                |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**logging**](eventmanifestschema-logging-channeltype-element.md)       | [**ChannelLoggingType**](eventmanifestschema-channelloggingtype-complextype.md)       | Defines the properties of the log file that backs the channel, such as its capacity and whether the log file is sequential or circular.<br/>                                                         |
| [**publishing**](eventmanifestschema-publishing-channeltype-element.md) | [**ChannelPublishingType**](eventmanifestschema-channelpublishingtype-complextype.md) | Defines the logging properties for the session that the channel uses. Only Debug and Analytic channels and channels that use Custom isolation can specify logging properties for their session.<br/> |



## Attributes



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>access</td>
<td>string</td>
<td>A <a href="/windows/desktop/SecAuthZ/security-descriptor-definition-language">Security Descriptor Definition Language</a> (SDDL) access descriptor that controls access to the log file that backs the channel. If the <strong>isolation</strong> attribute is set to Application or System, the access descriptor controls read access to the file (the write permissions are ignored). If the <strong>isolation</strong> attribute is set to Custom, the access descriptor controls write access to the channel and read access to the file.<br/></td>
</tr>
<tr class="even">
<td>chid</td>
<td>token</td>
<td>An identifier that uniquely identifies the channel in the list of channels that the provider defines or imports. Use this value when referencing the channel in an event. If you do not specify a channel identifier, use the channel's name to reference this channel in an event definition.<br/></td>
</tr>
<tr class="odd">
<td>enabled</td>
<td>boolean</td>
<td>Determines whether the channel is enabled. Set to <strong>true</strong> to allow logging to the channel; otherwise, <strong>false</strong>. The default is <strong>false</strong> (logging is disabled).<br/> Because Debug and Analytic channel types are high volume channels, you should enable the channel only when investigating an issue with a component that writes to that channel; otherwise, the channel should remain disabled.<br/> Each time you enable a Debug and Analytic channel, the service clears the events from the channel.<br/></td>
</tr>
<tr class="even">
<td>isolation</td>
<td>string</td>
<td>The isolation value defines the default access permissions for the channel. You can specify one of the following values:
<ul>
<li><strong>Application</strong></li>
<li><strong>System</strong></li>
<li><strong>Custom</strong></li>
</ul>
The default isolation is <strong>Application</strong>. The default permissions for <strong>Application</strong> are (shown using SDDL): <br/> <span data-codelanguage="Text"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Text</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>            L&quot;O:BAG:SYD:&quot;
            L&quot;(A;;0xf0007;;;SY)&quot;                // local system               (read, write, clear)
            L&quot;(A;;0x7;;;BA)&quot;                    // built-in admins            (read, write, clear)
            L&quot;(A;;0x7;;;SO)&quot;                    // server operators           (read, write, clear)
            L&quot;(A;;0x3;;;IU)&quot;                    // INTERACTIVE LOGON          (read, write)
            L&quot;(A;;0x3;;;SU)&quot;                    // SERVICES LOGON             (read, write)
            L&quot;(A;;0x3;;;S-1-5-3)&quot;               // BATCH LOGON                (read, write)
            L&quot;(A;;0x3;;;S-1-5-33)&quot;              // write restricted service   (read, write)
            L&quot;(A;;0x1;;;S-1-5-32-573)&quot;;         // event log readers          (read) </code></pre></td>
</tr>
</tbody>
</table>

<p>The default permissions for <strong>System</strong> are (shown using SDDL):</p>
<div class="code">
<span data-codelanguage="Text"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Text</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>            L&quot;O:BAG:SYD:&quot;
            L&quot;(A;;0xf0007;;;SY)&quot;                // local system             (read, write, clear)
            L&quot;(A;;0x7;;;BA)&quot;                    // built-in admins          (read, write, clear)
            L&quot;(A;;0x3;;;BO)&quot;                    // backup operators         (read, write)
            L&quot;(A;;0x5;;;SO)&quot;                    // server operators         (read, clear) 
            L&quot;(A;;0x1;;;IU)&quot;                    // INTERACTIVE LOGON        (read)
            L&quot;(A;;0x3;;;SU)&quot;                    // SERVICES LOGON           (read, write)
            L&quot;(A;;0x1;;;S-1-5-3)&quot;               // BATCH LOGON              (read)
            L&quot;(A;;0x2;;;S-1-5-33)&quot;              // write restricted service (write)
            L&quot;(A;;0x1;;;S-1-5-32-573)&quot;;         // event log readers        (read)</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>The default permissions for <strong>Custom</strong> isolation is the same as Application.</p>
<p>Channels that specify <strong>Application</strong> isolation use the same ETW session. The same is true for <strong>System</strong> isolation. However, if you specify <strong>Custom</strong> isolation, the service creates a separate ETW session for the channel. Using <strong>Custom</strong> isolation lets you control the access permissions for the channel and backing file. Because there are only 64 ETW sessions available, you should limit your use of <strong>Custom</strong> isolation.</p></td>
</tr>
<tr class="odd">
<td>message</td>
<td>string</td>
<td><p>The localized display name for the channel. The message string references a localized string in the <a href="eventmanifestschema-stringtable-resources-element.md"><strong>stringTable</strong></a> section of the manifest.</p></td>
</tr>
<tr class="even">
<td>name</td>
<td>anyURI</td>
<td><p>The name of the channel. The name must be unique within the list of channels that the provider uses. The convention for naming channels is to append the channel type to the provider's name. For example. if the provider's name is Company-Product-Component and you are defining an operational channel, the name would be Company-Product-Component/Operational.</p>
<p>Channel names must be less that 255 characters and cannot contain the following characters: '>', '<', '&', '&quot;', '|', '\', ':', '`', '?', '*', or characters with codes less than 31.</p></td>
</tr>
<tr class="odd">
<td>symbol</td>
<td><a href="eventmanifestschema-csymboltype-simpletype.md"><strong>CSymbolType</strong></a></td>
<td><p>The symbol to use to reference the channel in your application. The <a href="message-compiler--mc-exe-.md"><strong>Message Compiler (MC.exe)</strong></a> uses the symbol to create a constant for the channel in the header file that the compiler generates. If you do not specify a symbol, the compiler generates the name for you.</p></td>
</tr>
<tr class="even">
<td>type</td>
<td>string</td>
<td><p>Identifies the channel's type. You can specify one of the following types:</p>
<ul>
<li><strong>Admin</strong></li>
<li><strong>Operational</strong></li>
<li><strong>Analytic</strong></li>
<li><strong>Debug</strong></li>
</ul>
<p>Admin type channels support events that target end users, administrators, and support personnel. Events written to the Admin channels should have a well-defined solution on which the administrator can act. An example of an admin event is an event that occurs when an application fails to connect to a printer. These events are either well-documented or have a message associated with them that gives the reader direct instructions of what must be done to rectify the problem.</p>
<p>Operational type channels support events that are used for analyzing and diagnosing a problem or occurrence. They can be used to trigger tools or tasks based on the problem or occurrence. An example of an operational event is an event that occurs when a printer is added or removed from a system.</p>
<p>Analytic type channels support events that are published in high volume. They describe program operation and indicate problems that cannot be handled by user intervention.</p>
<p>Debug type channels support events that are used solely by developers to diagnose a problem for debugging.</p>
<p>Analytic and debug channels are disabled by default and should only enabled to determine the cause of an issue. For example, you would enable the channel, run the scenario that is causing the issue, disable the channel, and then query the events. Note that enabling the channel clears the channel of existing events. If the analytic and debug channel uses a circular backing file, you must disable the channel to query its events.</p>
<p>All Admin channels use the same ETW session; the same is true for Operational channels. However, each Analytic and Debug channel uses a separate ETW session, which is another reason to only enable these channel types when needed (there is a limited number of ETW sessions available).</p></td>
</tr>
<tr class="odd">
<td>value</td>
<td><a href="eventmanifestschema-hexint8type-simpletype.md"><strong>UInt8Type</strong></a></td>
<td><p>A numeric identifier that uniquely identifies the channel within the list of channels that the provider defines. The message compiler assigns the value if not specified.</p></td>
</tr>
</tbody>
</table>



## Remarks

If the channel's name follows the channel naming convention, the Windows Event Viewer will list the channel using the string that follows the backslash. For example, if the channel name is Company-Product-Component/Operational, then the Event Viewer will list the channel as Operational under the Company-Product-Component provider. Otherwise, the entire channel name is shown under the provider. The localized display name is used if provided.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




`
