---
title: Choice Complex Type
description: Defines a choice for a single selection or multiple selection list.
ms.assetid: 5422f5b8-02f5-467e-970d-2ab273fd68cf
keywords:
- Choice complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Choice
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Choice Complex Type

Defines a choice for a single selection or multiple selection list.

``` syntax
<xs:complexType name="Choice">
    <xs:sequence>
        <xs:element name="DisplayInformation"
            type="dcmPS:DisplayInformation"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="Value"
            type="xs:string"
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
<td>DisplayInformation</td>
<td>[<strong>dcmPS:DisplayInformation</strong>](package-displayinformation-complextype.md)</td>
<td>The name and description of the choice. <br/></td>
</tr>
<tr class="even">
<td>ExtensionPoint</td>
<td>[<strong>dcmPS:ExtensionPoint</strong>](package-extensionpoint-complextype.md)</td>
<td>An extension point that extends the single-response or multiple-response choice. Each extension is a child element of <strong>ExtensionPoint</strong>. The extension points are MSDT specific and are not supported by the command-line client using the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet. You can specify one or more of the following extensions.<br/> 
<table>
<thead>
<tr class="header">
<th>Extension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Default</strong></td>
<td>Specifies the default selection for a single-response interaction or default selections for a multiple-response interaction. If you specify a default choice for more than one choice in a single-response interaction, the behavior is undefined. The default has no effect if you also specify the <strong>CommandLinks</strong> extension point.<br/> The <strong>Default</strong> element has no content.<br/></td>
</tr>
<tr class="even">
<td><strong>Icon</strong></td>
<td>An icon to display next to the choice. If you specify the <strong>CommandLinks</strong> extension point, the icon replaces the green arrow icon. <br/> The <strong>Icon</strong> element contains the resource identifier for the icon (for example, &quot;@resource.dll,-123&quot;).<br/></td>
</tr>
<tr class="odd">
<td><strong>RTFDescription</strong></td>
<td>A rich text format string that replaces the <strong>Description</strong> element of [<strong>DisplayInformation</strong>](package-displayinformation-complextype.md). If the client does not support rich text, the description string is used.<br/> The RTF string can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element of the single-response or multiple-response interaction.<br/> The RTFDescription element can contain an RTF string or a localized resource string (for example, &quot;@diag.dll,-123&quot; or &quot;@diag.dll,RESOURCE.RTF&quot;).<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>Value</td>
<td>xs:string</td>
<td><p>The value to return if the choice is selected from the list.</p></td>
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

[**Choice (Choices) Element**](package-choice-choices-element.md)
</dt> </dl>

 

 





