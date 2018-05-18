---
title: LocalDiagnosticPackage Complex Type
description: Defines the manifest as a local troubleshooting pack.
ms.assetid: 'bc82869f-2f8e-422e-81fc-c9e0a94cb43f'
keywords: ["LocalDiagnosticPackage complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- LocalDiagnosticPackage
api_type:
- Schema
---

# LocalDiagnosticPackage Complex Type

Defines the manifest as a local troubleshooting pack.

``` syntax
<xs:complexType name="LocalDiagnosticPackage">
    <xs:sequence>
        <xs:element name="DiagnosticIdentification"
            type="dcmPS:DiagnosticIdentification"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="DisplayInformation"
            type="dcmPS:DisplayInformation"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="PrivacyLink"
            type="xs:string"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="PowerShellVersion"
            type="dcmPS:Version"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="SupportedOSVersion"
            type="dcmPS:SupportedOSVersion"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="Rootcauses"
            type="dcmPS:LocalRootcauses"
            minOccurs="1"
            maxOccurs="1"
        >
            <xs:unique name="No_local_rootcause_may_have_the_same_ID">
                <xs:selector
                    xpath="Rootcause"
                 />
                <xs:field
                    xpath="ID"
                 />
            </xs:unique>
        </xs:element>
        <xs:element name="Interactions"
            type="dcmPS:Interactions"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="ExtensionPoint"
            type="dcmPS:ExtensionPoint"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
    <xs:attribute name="SchemaVersion"
        type="dcmPS:Version"
        use="required"
     />
    <xs:attribute name="Localized"
        type="xs:boolean"
        use="required"
     />
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
<td>DiagnosticIdentification</td>
<td>[<strong>dcmPS:DiagnosticIdentification</strong>](package-diagnosticidentification-complextype.md)</td>
<td>The identifier and version used to identify the pack.<br/></td>
</tr>
<tr class="even">
<td>DisplayInformation</td>
<td>[<strong>dcmPS:DisplayInformation</strong>](package-displayinformation-complextype.md)</td>
<td>The name and description of the pack. <br/></td>
</tr>
<tr class="odd">
<td>ExtensionPoint</td>
<td>[<strong>dcmPS:ExtensionPoint</strong>](package-extensionpoint-complextype.md)</td>
<td>One or more extensions that the client supports. Used by the client to extend the functionality of the AdvDiagnosticPackage node. The MSDT client supports the following extensions:<br/> 
<table>
<thead>
<tr class="header">
<th>Extension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>HelpKeywords</strong></td>
<td>Specifies a single keyword. The extension contains the localized resource identifier for the keyword (for example, &quot;@resource.dll,-123&quot;). To specify multiple keywords, include a <strong>HelpKeywords</strong> element for each keyword.<br/> The keywords are used only if the package fails. If the package fails and the user clicks <strong>Explore additional options</strong>, the keywords are used to find related information if the user then clicks <strong>Help and Support</strong>, <strong>Windows Communities</strong>, or <strong>Related Troubleshooters</strong>.<br/> For <strong>Help and Support</strong>, the keywords are used in a logical OR operation and for <strong>Windows Communities</strong> and <strong>Related Troubleshooters</strong>, the keywords are used in a logical AND operation.<br/> These keywords are used only if the root cause that failed does not specify keywords (see the <strong>ContextParameters</strong> child element of the [<strong>LocalRootcause</strong>](package-localrootcause-complextype.md) complex type).<br/></td>
</tr>
<tr class="even">
<td><strong>Icon</strong></td>
<td>An icon to display next to the package. The <strong>Icon</strong> element contains the resource identifier for the icon (for example, &quot;@resource.dll,-123&quot;).<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>Interactions</td>
<td>[<strong>dcmPS:Interactions</strong>](package-interactions-complextype.md)</td>
<td><p>The interactions that the pack uses.</p></td>
</tr>
<tr class="odd">
<td>PowerShellVersion</td>
<td>[<strong>dcmPS:Version</strong>](package-version-simpletype.md)</td>
<td><p>The minimum Windows PowerShell version required to run the pack.</p></td>
</tr>
<tr class="even">
<td>PrivacyLink</td>
<td>xs:string</td>
<td><p>The URL to the privacy information that tells the user how the data collected by your troubleshooting pack will be used.</p></td>
</tr>
<tr class="odd">
<td>Rootcauses</td>
<td>[<strong>dcmPS:LocalRootcauses</strong>](package-localrootcauses-complextype.md)</td>
<td><p>The collection of root causes to detect, resolve, and verify.</p></td>
</tr>
<tr class="even">
<td>SupportedOSVersion</td>
<td>[<strong>dcmPS:SupportedOSVersion</strong>](package-supportedosversion-complextype.md)</td>
<td><p>The minimum operating system version on which the pack can run.</p></td>
</tr>
</tbody>
</table>



## Attributes



| Name          | Type                                                | Description                                                                                                                                                                                                                                                                                                                                          |
|---------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Localized     | xs:boolean                                          | Determines whether the strings specified in the manifest are resource strings (true) or literals (false). If true, all UI elements in the manifest must specify a resource identifier (for example, @resource.dll,-123). For localization details, see [Localizing the Troubleshooting Pack](localizing-the-troubleshooting-package.md).<br/> |
| SchemaVersion | [**dcmPS:Version**](package-version-simpletype.md) | The version of the troubleshooting pack schema used to write this manifest. For Windows 7, the version is 1.0. <br/>                                                                                                                                                                                                                           |



## Remarks

A manifest that contains this node contains multiple troubleshooters and each troubleshooter detects a single root cause. WTP runs all the troubleshooters in the package in the order they are defined in the manifest. Because the troubleshooter scripts each focus on a single root cause, you can use the same script for troubleshooting and verification.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**AdvDiagnosticPackage Element**](package-advdiagnosticpackage-element.md)
</dt> </dl>

 

 





