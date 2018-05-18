---
title: Resolvers Complex Type
description: Specifies a list of resolver scripts to run.
ms.assetid: '814da48e-9bab-49e3-a434-33fd1e5fe0b4'
keywords: ["Resolvers complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Resolvers
api_type:
- Schema
---

# Resolvers Complex Type

Specifies a list of resolver scripts to run.

``` syntax
<xs:complexType name="Resolvers">
    <xs:sequence>
        <xs:element name="Resolver"
            minOccurs="0"
            maxOccurs="unbounded"
        >
            <xs:complexType>
                <xs:sequence>
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
                    <xs:element name="RequiresConsent"
                        type="xs:boolean"
                        minOccurs="1"
                        maxOccurs="1"
                     />
                    <xs:element name="Script"
                        type="dcmPS:Script"
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
        </xs:element>
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
<td>The name and description of the resolver to use in the UI.<br/></td>
</tr>
<tr class="even">
<td>ExtensionPoint</td>
<td>[<strong>dcmPS:ExtensionPoint</strong>](package-extensionpoint-complextype.md)</td>
<td>Used by the client to extend the functionality of the Resolver node. These extension points apply only to resolver nodes that have an empty script block. Each extension is a child element of <strong>ExtensionPoint</strong>. You can specify one or more of the following extensions (but only one of each).<br/> 
<table>
<thead>
<tr class="header">
<th>Extension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Link</strong></td>
<td>Creates a link to the specified URL. The link is placed at the bottom of the interaction window. You must use this extension point in conjunction with the <strong>LinkText</strong> extension point.<br/> The URL can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/> The URL must begin with http, https, or mshelp.<br/></td>
</tr>
<tr class="even">
<td><strong>LinkText</strong></td>
<td>The text to use for a link. The contents of the <strong>LinkText</strong> element is the resource identifier of the localized string. You must use this extension point in conjunction with the <strong>Link</strong> extension point.<br/> The link text can contain substitution strings (for example, %param%) that are specified in the <strong>ContextParameters</strong> element.<br/></td>
</tr>
<tr class="odd">
<td><strong>LinkFlushWithText</strong></td>
<td>By default, the link is displayed at the bottom of the interaction window. Use this element to align the link flush with the resolver's description text in the case where the resolver script is not specified. This element is valid only if the <strong>Link</strong> element is specified.<br/> This extension's usage is <strong>LinkFlushWithText/</strong>.<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>ID</td>
<td>[<strong>dcmPS:ID</strong>](package-id-simpletype.md)</td>
<td><p>A string used to identify the resolver.</p></td>
</tr>
<tr class="even">
<td>RequiresConsent</td>
<td>xs:boolean</td>
<td><p>Determines whether the user must provide consent to proceed with fixing the root cause issue. Typically used if the procedure can be risky.</p></td>
</tr>
<tr class="odd">
<td>Resolver</td>

<td><p>A resolver script to run.</p></td>
</tr>
<tr class="even">
<td>Script</td>
<td>[<strong>dcmPS:Script</strong>](package-script-complextype.md)</td>
<td><p>The name of the resolver script to run. If you do not specify a script, the name and description in the [<strong>DisplayInformation</strong>](package-displayinformation-complextype.md) element is displayed to the user. You might not provide a script in cases where the issue must be resolved manually by the user. In this case, the description would instruct the user on how to fix the issue.</p></td>
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

[**Resolver (Resolvers) Element**](package-resolver-resolvers-element.md)
</dt> <dt>

[**Resolvers (GlobalRootcause) Element**](package-resolvers-globalrootcause-element.md)
</dt> <dt>

[**Resolvers (LocalRootcause) Element**](package-resolvers-localrootcause-element.md)
</dt> </dl>

 

 





