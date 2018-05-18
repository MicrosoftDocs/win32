---
title: SingleResponseInteraction Complex Type
description: Defines an interaction that lets the user select a single choice from a list of choices.
ms.assetid: 'e6c5b0d6-65d1-4f2b-9fa8-ca650e11237b'
keywords: ["SingleResponseInteraction complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- SingleResponseInteraction
api_type:
- Schema
---

# SingleResponseInteraction Complex Type

Defines an interaction that lets the user select a single choice from a list of choices.

``` syntax
<xs:complexType name="SingleResponseInteraction">
    <xs:sequence>
        <xs:element name="AllowDynamicResponses"
            type="xs:boolean"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="Choices"
            type="dcmPS:Choices"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="ID"
            type="dcmPS:ID"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="DisplayInformation"
            type="dcmPS:DisplayInformation"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="ContextParameters"
            type="dcmPS:Parameters"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="ExtensionPoint"
            type="dcmPS:ExtensionPoint"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AllowDynamicResponses</td>
<td>xs:boolean</td>
<td>Set to true if the script can add choices at run time; otherwise, false if the list is static. The dynamic choices are shown before the static choices in the list. Note that if you specify true, the interaction cannot be included in an answer file.<br/></td>
</tr>
<tr class="even">
<td>Choices</td>
<td>[<strong>dcmPS:Choices</strong>](package-choices-complextype.md)</td>
<td>The static list of choices. <br/></td>
</tr>
<tr class="odd">
<td>ContextParameters</td>
<td>[<strong>dcmPS:Parameters</strong>](package-parameters-complextype.md)</td>
<td>Some extension points can contain substitution strings (for example, %param%). Each substitution string in the extension point is replaced with the value of the same named parameter specified in this list. <br/></td>
</tr>
<tr class="even">
<td>DisplayInformation</td>
<td>[<strong>dcmPS:DisplayInformation</strong>](package-displayinformation-complextype.md)</td>
<td>The name and description of this interaction that is used in the UI. The name is used as the prompt for the list.<br/></td>
</tr>
<tr class="odd">
<td>ExtensionPoint</td>
<td>[<strong>dcmPS:ExtensionPoint</strong>](package-extensionpoint-complextype.md)</td>
<td>An extension point that extends the functionality of this interaction. Each extension is a child element of <strong>ExtensionPoint</strong>. The extension points are MSDT specific and are not supported by the command-line client using the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet. You can specify one or more of the following extensions (but only one of each).<br/> 
<table>
<thead>
<tr class="header">
<th>Extension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CommandLinks</strong></td>
<td>Use to change the choices from radio buttons to command links. The list of choices must contain at least two choices and no more than three choices. <br/></td>
</tr>
<tr class="even">
<td><strong>Link</strong></td>
<td>Creates a link to the specified URL. The link is placed at the bottom of the interaction window. You must use this extension point in conjunction with the <strong>LinkText</strong> extension point.<br/> The URL can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/> The URL must begin with http, https, or mshelp.<br/></td>
</tr>
<tr class="odd">
<td><strong>LinkText</strong></td>
<td>The text to use for a link. The contents of the <strong>LinkText</strong> element is the resource identifier of the localized string. You must use this extension point in conjunction with the <strong>Link</strong> extension point.<br/> The link text can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/></td>
</tr>
<tr class="even">
<td><strong>NoCache</strong></td>
<td>By default, the answer to an interaction is cached. When running in MSDT, if the interaction is called more than one time, the interaction is shown the first time and the cached answer is used thereafter (without displaying the interaction). Use this extension point to force the interaction to display on subsequent requests and to not get the answer from the cache.<br/> This extension is ignored if you run the pack from a command-line and provide an answer file that provides an answer for the interaction.<br/> This extension's usage is <strong>NoCache/</strong>.<br/></td>
</tr>
<tr class="odd">
<td><strong>NoUI</strong></td>
<td>Suppresses the interaction. Gets the responses to the interaction from the answer file rather than from the user. For details on using an answer file, see the [Get-TroubleshootingPack](get-troubleshootingpack-cmdlet.md) and [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlets. This extension's usage is <strong>NoUI/</strong>.<br/></td>
</tr>
<tr class="even">
<td><strong>RTFDescription</strong></td>
<td>A rich text format string that replaces the <strong>Description</strong> element of [<strong>DisplayInformation</strong>](package-displayinformation-complextype.md). If the client does not support rich text, the description string is used.<br/> The RTF string can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/> The RTFDescription element can contain an RTF string or a localized resource string (for example, &quot;@diag.dll,-123&quot; or &quot;@diag.dll,RESOURCE.RTF&quot;)<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>ID</td>
<td>[<strong>dcmPS:ID</strong>](package-id-simpletype.md)</td>
<td><p>An identifier that identifies this interaction.</p></td>
</tr>
</tbody>
</table>



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SingleResponseInteraction (SingleResponseInteractions) Element**](package-singleresponseinteraction-singleresponseinteractions-element.md)
</dt> <dt>

[**SingleResponseInteractions Complex Type**](package-singleresponseinteractions-complextype.md)
</dt> </dl>

 

 





