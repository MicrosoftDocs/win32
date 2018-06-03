---
title: TextInteraction Complex Type
description: Defines an interaction used to get text input from the user.
ms.assetid: 8e496cdf-a9e9-4366-a410-2af25214878e
keywords:
- TextInteraction complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- TextInteraction
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TextInteraction Complex Type

Defines an interaction used to get text input from the user.

``` syntax
<xs:complexType name="TextInteraction">
    <xs:sequence>
        <xs:element name="RegularExpression"
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
<td>ContextParameters</td>
<td>[<strong>dcmPS:Parameters</strong>](package-parameters-complextype.md)</td>
<td>Some extension points can contain substitution strings (for example, %param%). Each substitution string in the extension point is replaced with the value of the same named parameter specified in this list. <br/></td>
</tr>
<tr class="even">
<td>DisplayInformation</td>
<td>[<strong>dcmPS:DisplayInformation</strong>](package-displayinformation-complextype.md)</td>
<td>The name and description of this interaction that is used in the UI. The name is used as the prompt for the text box.<br/></td>
</tr>
<tr class="odd">
<td>ExtensionPoint</td>
<td>[<strong>dcmPS:ExtensionPoint</strong>](package-extensionpoint-complextype.md)</td>
<td>An extension point that extends this interaction. Each extension is a child element of <strong>ExtensionPoint</strong>. The extension points are MSDT specific and are not supported by the command-line client using the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet. You can specify one or more of the following extensions (but only one of each).<br/> 
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Extension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Browse</strong></td>
<td>Includes a <strong>Browse</strong> button with a single-line text box. The <strong>Browse</strong> element can contain one of the following items:
<ul>
<li>Computer   used to select a computer on the network (network discovery must be turned on for this option to work)</li>
<li>File   used to select a file in a folder</li>
<li>Folder   used to select a folder on the computer</li>
</ul>
<br/> For File and Folder, the path used is %HOMEDRIVE%%HOMEPATH%.<br/> If you specify File, you must include the <strong>FilterText</strong> and <strong>FilterExtension</strong> attributes. For example, &lt;Browse FilterText=&quot;@diag.dll,-123&quot; FilterExtension=&quot;*.exe&quot;&gt;File&lt;/Browse&gt;. For a description of allowed values for FilterExtension, see the <strong>lpstrFilter</strong> member of the <strong>OPENFILENAME</strong> structure.<br/></td>
</tr>
<tr class="even">
<td><strong>Default</strong></td>
<td>Provides the default text string to show in the text box. <br/> The default string can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/> The <strong>Default</strong> element can contain a literal string or a resource identifier for the localized text string (for example, &quot;@diag.dll,-123&quot;.<br/></td>
</tr>
<tr class="odd">
<td><strong>EditMode</strong></td>
<td>Determines whether the edit box is a single line or multiline edit box. The text value of the <strong>EditMode</strong> element can contain one of the following values:
<ul>
<li>Multi</li>
<li>Single</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td><strong>Eula</strong></td>
<td>Displays a EULA page to the user. The <strong>EditMode</strong> must be set to Multiple. If the user accepts the agreement, the interaction returns the string, &quot;Accept&quot;. The <strong>Description</strong> element of [<strong>DisplayInformation</strong>](package-displayinformation-complextype.md) contains the EULA text. The <strong>Eula</strong> element has no content.<br/></td>
</tr>
<tr class="odd">
<td><strong>Link</strong></td>
<td>Creates a link to the specified URL. The link is placed at the bottom of the interaction window. You must use this extension point in conjunction with the <strong>LinkText</strong> extension point.<br/> The URL can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/> The URL must begin with http, https, or mshelp.<br/></td>
</tr>
<tr class="even">
<td><strong>LinkText</strong></td>
<td>The text to use for a link. The contents of the <strong>LinkText</strong> element is the resource identifier of the localized string. You must use this extension point in conjunction with the <strong>Link</strong> extension point.<br/> The link text can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/></td>
</tr>
<tr class="odd">
<td><strong>NoCache</strong></td>
<td>By default, the answer to an interaction is cached. When running in MSDT, if the interaction is called more than one time, the interaction is shown the first time and the cached answer is used thereafter (without displaying the interaction). Use this extension point to force the interaction to display on subsequent requests and to not get the answer from the cache.<br/> This extension is ignored if you run the pack from a command-line and provide an answer file that provides an answer for the interaction.<br/> This extension's usage is <strong>NoCache/</strong>.<br/></td>
</tr>
<tr class="even">
<td><strong>NoUI</strong></td>
<td>Suppresses the interaction. Gets the responses to the interaction from the answer file rather than from the user. For details on using an answer file, see the [Get-TroubleshootingPack](get-troubleshootingpack-cmdlet.md) and [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlets. This extension's usage is <strong>NoUI/</strong>.<br/></td>
</tr>
<tr class="odd">
<td><strong>RTFDescription</strong></td>
<td>A rich text format string that replaces the <strong>Description</strong> element of [<strong>DisplayInformation</strong>](package-displayinformation-complextype.md). If the client does not support rich text, the description string is used.<br/> The RTF string can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/> The RTFDescription element can contain an RTF string or a localized resource string (for example, &quot;@diag.dll,-123&quot; or &quot;@diag.dll,RESOURCE.RTF&quot;)<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>ID</td>
<td>[<strong>dcmPS:ID</strong>](package-id-simpletype.md)</td>
<td><p>An identifier that identifies this interaction.</p></td>
</tr>
<tr class="odd">
<td>RegularExpression</td>
<td>xs:string</td>
<td><p>A regular expression string that specifies the type of input that the user is allowed to enter.</p></td>
</tr>
</tbody>
</table>



## Remarks

WTP uses the regular expression syntax supported by the **CAtlRegExp** class found in the ATL Server Library Reference.

The MSDT client will not prevent the user from entering text that does not conform to the regular expression, but the interaction will not proceed until the user enters the text correctly. If you use a regular expression, consider using the Description node of DisplayInformation to tell the user the type of input that they can enter.

The troubleshooting engine uses the regular expression to validate the text input after it is entered. If the input is not valid, the engine returns an error to the script.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**TextInteraction (TextInteractions) Element**](package-textinteraction-textinteractions-element.md)
</dt> <dt>

[**TextInteractions Complex Type**](package-textinteractions-complextype.md)
</dt> </dl>

 

 





