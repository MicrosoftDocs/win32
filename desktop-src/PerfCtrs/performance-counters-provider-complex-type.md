---
description: Defines a provider and the counters that it provides.
ms.assetid: 85299b01-5679-40f8-8aec-5c2ff8d7cfc8
title: provider Complex Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# provider Complex Type

Defines a provider and the counters that it provides.

``` syntax
<xs:complexType name="provider">
    <xs:choice
        minOccurs="0"
        maxOccurs="unbounded"
    >
        <xs:element name="counterSet"
            type="man:counterSet"
        >
            <xs:key name="uniqueCounterID">
                <xs:selector
                    xpath="./man:counter"
                 />
                <xs:field
                    xpath="@id"
                 />
            </xs:key>
            <xs:unique name="uniqueCounterName">
                <xs:selector
                    xpath="./man:counter"
                 />
                <xs:field
                    xpath="@name"
                 />
            </xs:unique>
            <xs:keyref name="existBaseID">
                <xs:selector
                    xpath="./man:counter"
                 />
                <xs:field
                    xpath="@baseID"
                 />
            </xs:keyref>
            <xs:keyref name="existPerfTimeID">
                <xs:selector
                    xpath="./man:counter"
                 />
                <xs:field
                    xpath="@perfTimeID"
                 />
            </xs:keyref>
            <xs:keyref name="existPerfFreqID">
                <xs:selector
                    xpath="./man:counter"
                 />
                <xs:field
                    xpath="@perfFreqID"
                 />
            </xs:keyref>
            <xs:keyref name="existMultiCounterID">
                <xs:selector
                    xpath="./man:counter"
                 />
                <xs:field
                    xpath="@multiCounterID"
                 />
            </xs:keyref>
            <xs:key name="uniqueStructNames">
                <xs:selector
                    xpath="./man:structs/man:struct"
                 />
                <xs:field
                    xpath="@name"
                 />
            </xs:key>
            <xs:keyref name="existCounterName">
                <xs:selector
                    xpath="./man:counter"
                 />
                <xs:field
                    xpath="@struct"
                 />
            </xs:keyref>
        </xs:element>
    </xs:choice>
    <xs:attribute name="symbol"
        type="man:CSymbolType"
        use="optional"
     />
    <xs:attribute name="callback"
        use="optional"
        default="default"
    >
        <xs:simpleType>
            <xs:restriction
                base="xs:string"
            >
                <xs:enumeration
                    value="custom"
                 />
                <xs:enumeration
                    value="default"
                 />
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="providerGuid"
        type="man:GUIDType"
        use="required"
     />
    <xs:attribute name="applicationIdentity"
        type="xs:string"
        use="required"
     />
    <xs:attribute name="providerType"
        use="optional"
        default="userMode"
    >
        <xs:simpleType>
            <xs:restriction
                base="xs:string"
            >
                <xs:enumeration
                    value="userMode"
                 />
                <xs:enumeration
                    value="kernelMode"
                 />
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="providerName"
        type="xs:string"
        use="optional"
        default="Counters"
     />
    <xs:attribute name="resourceBase"
        type="man:UInt32Type"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element        | Type                                                                   | Description                                                                                 |
|----------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **counterSet** | [**man:counterSet**](performance-counters-counterset-complex-type.md) | Identifies the counter set that contains one or more logically related counters.<br/> |



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
<td>applicationIdentity</td>
<td><strong>xs:string</strong></td>
<td>The name of the binary file that contains the localized resource strings, either an .exe or .dll file (do not include the path to the binary).<br/> The Lodctr.exe utility uses the path from the optional [<em>path</em>] parameter to search for the binary file. For example, <strong>lodctr</strong> [<strong>/m:</strong><em>manifest</em> [<em>path</em>]]. If you do not include the [<em>path</em>] parameter, Lodctr.exe searches the folder that contains the manifest.<br/></td>
</tr>
<tr class="even">
<td>callback</td>

<td>This attribute indicates that you want to receive notification when a consumer performs certain actions. <br/> If you include this attribute, the CTRPP tool uses the alternate <a href="counterinitialize.md"><strong>CounterInitialize</strong></a> function signature, which you use to pass in the name of your function that implements the <a href="/windows/desktop/api/Perflib/nc-perflib-perflibrequest"><strong>ControlCallback</strong></a> callback function.<br/> As an alternative to specifying this attribute, you can use the <strong>-NotificationCallback</strong><a href="ctrpp.md">CTRPP</a> argument.<br/> <strong>Windows Vista:</strong> The only valid value for this attribute is &quot;custom&quot;. The <a href="ctrpp.md">CTRPP</a> utility generates the template for a <a href="/windows/desktop/api/Perflib/nc-perflib-perflibrequest"><strong>ControlCallback</strong></a> callback function. The template is included in the .c file that CTRPP generated. <br/> <br/></td>
</tr>
<tr class="odd">
<td>providerGuid</td>
<td><a href="performance-counters-guidtype-simple-type.md"><strong>man:GUIDType</strong></a></td>
<td>String GUID that uniquely identifies the provider in the manifest. The GUID must be unique within the manifest.<br/> You need to provide a new GUID only when the version of the application changes (if you support side-by-side installations).<br/></td>
</tr>
<tr class="even">
<td>providerName</td>
<td><strong>xs:string</strong></td>
<td>The name that is used to create the WMI Win32_PerfRawData class name. If you do not specify a name, &quot;Counters&quot; is used as the name of the class.<br/></td>
</tr>
<tr class="odd">
<td>providerType</td>

<td>Identifies whether the provider is a user-mode provider, kernel-mode provider, or driver provider. Possible values are as follows.<br/> 
<table>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="userMode"></span><span id="usermode"></span><span id="USERMODE"></span>userMode<br/></td>
<td>Specify this mode for a user-mode component such as an application, a DLL, or a user-mode driver. The typical extensions for user-mode components are .exe or .dll. This is the default.<br/></td>
</tr>
<tr class="even">
<td><span id="kernel"></span><span id="KERNEL"></span>kernel<br/></td>
<td>Specify this mode for a kernel-mode component such as a WDM or WDF driver. The typical extension for kernel-mode components is .sys.<br/> <strong>Windows Vista and Windows Server 2008:</strong> This value is not supported until Windows 7 and Windows Server 2008 R2.<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>resourceBase</td>
<td><a href="performance-counters-uint32type-simple-type.md"><strong>man:UInt32Type</strong></a></td>
<td><p>Defines the starting resource index value that <a href="ctrpp.md">CTRPP</a> uses to generate the resource identifiers.</p></td>
</tr>
<tr class="odd">
<td>symbol</td>
<td><a href="performance-counters-csymboltype-simple-type.md"><strong>man:CSymbolType</strong></a></td>
<td><p>A symbolic name that identifies the provider. The <a href="ctrpp.md">CTRPP</a> tool creates a HANDLE variable that you can use when calling functions that require a handle to the provider (for example, <a href="/windows/desktop/api/Perflib/nf-perflib-perfsetulongcountervalue"><strong>PerfSetULongCounterValue</strong></a>). The symbolic name is the name of the variable.</p>
<p>If you include the <strong>-prefix</strong> argument when calling <a href="ctrpp.md">CTRPP</a>, the prefix string is added to the beginning of the symbolic name.</p></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




