---
title: LaunchUIInteraction Complex Type
description: Defines an interaction used to launch a related UI application that is external to the MSDT wizard.
ms.assetid: be9c5887-c741-4920-a1ba-77b3c533f6dc
keywords:
- LaunchUIInteraction complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- LaunchUIInteraction
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LaunchUIInteraction Complex Type

Defines an interaction used to launch a related UI application that is external to the MSDT wizard.

``` syntax
<xs:complexType name="LaunchUIInteraction">
    <xs:sequence>
        <xs:element name="Parameters"
            type="dcmPS:Parameters"
            minOccurs="0"
            maxOccurs="1"
        >
            <xs:unique name="No_cmdline_parameters_may_have_the_same_name">
                <xs:selector
                    xpath="Parameter"
                 />
                <xs:field
                    xpath="Name"
                 />
            </xs:unique>
        </xs:element>
        <xs:element name="CommandLine"
            type="xs:string"
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
<td>CommandLine</td>
<td>xs:string</td>
<td>The command line used to launch the Windows application. The application will appear in the foreground. The command line can include substitution strings.<br/></td>
</tr>
<tr class="even">
<td>ContextParameters</td>
<td>[<strong>dcmPS:Parameters</strong>](package-parameters-complextype.md)</td>
<td>Some extension points can contain substitution strings (for example, %param%). Each substitution string in the extension point is replaced with the value of the same named parameter specified in this list. <br/></td>
</tr>
<tr class="odd">
<td>DisplayInformation</td>
<td>[<strong>dcmPS:DisplayInformation</strong>](package-displayinformation-complextype.md)</td>
<td>The name and description of this interaction. The name is used as a prompt and describes the task that the application performs.<br/></td>
</tr>
<tr class="even">
<td>ExtensionPoint</td>
<td>[<strong>dcmPS:ExtensionPoint</strong>](package-extensionpoint-complextype.md)</td>
<td>An extension point that extends this interaction. Each extension is a child element of <strong>ExtensionPoint</strong>. The extension points are MSDT specific and are not supported by the command-line client using the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet. You can specify one or more of the following extensions (but only one of each).<br/> 
<table>
<thead>
<tr class="header">
<th>Extension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ButtonText</strong></td>
<td>Changes the default button text for the launch button. The button text is limited to 50 characters. The default text is &quot;Begin this action&quot;.<br/> The value of the <strong>ButtonText</strong> node can be a literal string or a localized resource string (for example, &quot;@diag.dll,-123&quot; or &quot;@diag.dll,RESOURCE.RTF&quot;)<br/></td>
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
<td>By default, the answer to an interaction is cached. When running in MSDT, if the interaction is called more than one time, the interaction is shown the first time and the cached answer is used thereafter (without displaying the interaction). Use this extension point to force the interaction to display on subsequent requests and to not get the answer from the cache. This extension's usage is <strong>NoCache/</strong>.<br/></td>
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

<p> </p></td>
</tr>
<tr class="odd">
<td>ID</td>
<td>[<strong>dcmPS:ID</strong>](package-id-simpletype.md)</td>
<td><p>An identifier that identifies this interaction.</p></td>
</tr>
<tr class="even">
<td>Parameters</td>
<td>[<strong>dcmPS:Parameters</strong>](package-parameters-complextype.md)</td>
<td><p>Specifies the substitution strings that you can use in your command line.</p></td>
</tr>
</tbody>
</table>



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**LaunchUIInteraction (LaunchUIInteractions) Element**](package-launchuiinteraction-launchuiinteractions-element.md)
</dt> <dt>

[**LaunchUIInteractions Complex Type**](package-launchuiinteractions-complextype.md)
</dt> </dl>

 

 





