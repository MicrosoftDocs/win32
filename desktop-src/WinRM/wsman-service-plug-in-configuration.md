---
title: WinRM Service Plug-in Configuration
description: A Windows Remote Management (WinRM) plug-in must be registered in the WinRM catalog to enable the infrastructure to dynamically determine the set of available plug-ins and the resource URIs that they support.
ms.assetid: d71cd244-3f10-40e3-a756-36cdf41b9cad
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# WinRM Service Plug-in Configuration

A Windows Remote Management (WinRM) plug-in must be registered in the WinRM catalog to enable the infrastructure to dynamically determine the set of available plug-ins and the [*resource URIs*](windows-remote-management-glossary.md) that they support. All [*resource URIs*](windows-remote-management-glossary.md) for WinRM plug-ins should conform to the format that is defined in RFC 3986 ([https://www.ietf.org/rfc/rfc3986.txt](https://www.ietf.org/rfc/rfc3986.txt)). Configuration is done through the main WinRM service.

The following command registers a plug-in configuration with the WinRM service:

```console
winrm create http://schemas.microsoft.com/wbem/wsman/1/config/plugin?name=MyPlugIn -file:myplugin.xml
```

> [!NOTE]
> The WinRM service needs to be restarted to expose the newly registered plug-ins.

Plug-in configuration is specified in XML. The following is an example.

```XML
<PlugInConfiguration xmlns="http://schemas.microsoft.com/wbem/wsman/1/config/PluginConfiguration" 
                     Name="MyPlugIn"
                     Filename="%systemroot%\system32\myplugin.dll" 
                     SDKVersion="1"
                     XmlRenderingType="text"
                     Architecture="64"
                     Enabled="true">

 <InitializationParameters>
  <Param Name="myParam1" Value="myValue1"/>
  <Param Name="myParam2" Value="myValue2"/>
 </InitializationParameters>

 <Resources>
  <Resource ResourceUri="https://schemas.MyCompany.com/MyUri1" SupportsOptions="true" ExactMatch="false">
   <Capability Type="Get" SupportsFragment="true"/>
   <Capability Type="Put" SupportsFragment="true"/>
   <Capability Type="Create"/>
   <Capability Type="Delete"/>
   <Capability Type="Invoke"/>
   <Capability Type="Enumerate" SupportsFiltering="true"/>
  </Resource>

  <Resource ResourceUri="https://schemas.MyCompany.com/MyUri2" SupportsOptions="false" ExactMatch="true">
   <Security Uri="https://schemas.MyCompany.com/MyUri2" Sddl="O:NSG:BAD:P(A;;GA;;;BA)"/>
   <Security Uri="https://schemas.MyCompany.com/MyUri2/MoreSpecific" Sddl="O:NSG:BAD:P(A;;GR;;;BA)" ExactMatch="true"/>
   <Capability Type="Shell"/>
  </Resource>
 </Resources>
</PlugInConfiguration>
```



The following list describes the XML elements in more detail and is followed by the configuration schema specified as an XSD.

<dl> <dt>

<span id="PlugInConfiguration_OperationsConfiguration"></span><span id="pluginconfiguration_operationsconfiguration"></span><span id="PLUGINCONFIGURATION_OPERATIONSCONFIGURATION"></span>**PlugInConfiguration**/**OperationsConfiguration**
</dt> <dd>

Specifies the file name of the operations plug-in. Any environment variables that are put in this entry will be expanded in the users' context when a request comes in. Each user could have a different version of the same environment variable, so each user could end up with a different plug-in. This entry cannot be blank and must point to a valid plug-in.

</dd> <dt>

<span id="PlugInConfiguration_Name"></span><span id="pluginconfiguration_name"></span><span id="PLUGINCONFIGURATION_NAME"></span>**PlugInConfiguration**/**Name**
</dt> <dd>

Specifies the display name to use for the plug-in. If an error is returned from the plug-in, this name will be put into the error XML that is returned to the client application. The name is not locale specific.

</dd> <dt>

<span id="PlugInConfiguration_Architecture"></span><span id="pluginconfiguration_architecture"></span><span id="PLUGINCONFIGURATION_ARCHITECTURE"></span>**PlugInConfiguration**/**Architecture**
</dt> <dd>

Specifies whether the operations plug-in is 32-bit or 64-bit. If this element is not specified, the value will default to "32" on x86 systems and to "64" on 64-bit systems. For x86 systems, the only valid value is "32". If the value is "32" on an 64-bit system, wow64 redirection needs to be taken into account when entering the **Filename** information. The underlying file system will use wow64 redirection to translate system32 to syswow64. For example, if **Filename** is "%windir%\\system32\\myplugin.dll" and **Architecture** is "32", the actual plug-in file is located at "%windir%\\syswow64\\myplugin.dll".

</dd> <dt>

<span id="PlugInConfiguration_XmlRenderingType"></span><span id="pluginconfiguration_xmlrenderingtype"></span><span id="PLUGINCONFIGURATION_XMLRENDERINGTYPE"></span>**PlugInConfiguration**/**XmlRenderingType**
</dt> <dd>

Configures the format in which XML is passed to plug-ins through the [**WSMAN\_DATA**](/windows/desktop/api/Wsman/ns-wsman-wsman_data) object. The following types are available:

<dl> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text
</dt> <dd>

Incoming XML data is contained in a WSMAN\_DATA\_TYPE\_TEXT structure, which represents the XML as a **PCWSTR** memory buffer.

</dd> <dt>

<span id="XMLReader"></span><span id="xmlreader"></span><span id="XMLREADER"></span>XMLReader
</dt> <dd>

Incoming XML data is contained in a WSMAN\_DATA\_TYPE\_WS\_XML\_READER structure, which represents the XML as an **XmlReader** object, which is defined in the WebServices.h header file.

</dd> </dl> </dd> <dt>

<span id="PlugInConfiguration_InitializationXml"></span><span id="pluginconfiguration_initializationxml"></span><span id="PLUGINCONFIGURATION_INITIALIZATIONXML"></span>**PlugInConfiguration**/**InitializationXml**
</dt> <dd>

This node is optional and allows a plug-in to configure extra XML that will be passed in to the [**WSManPluginStartup**](/windows/desktop/api/Wsman/nc-wsman-wsman_plugin_startup)method. Most plug-ins will not need this extra information, but if a plug-in needs to be used under more than one scenario that requires different run-time semantics, this XML will give the plug-in the flexibility to do this.

</dd> <dt>

<span id="PlugInConfiguration_Resources"></span><span id="pluginconfiguration_resources"></span><span id="PLUGINCONFIGURATION_RESOURCES"></span>**PlugInConfiguration**/**Resources**
</dt> <dd>

Specifies a list of [*resource URIs*](windows-remote-management-glossary.md)that this plug-in supports. At least one **ResourceUri**entry must be specified; otherwise, the XML will be rejected.

</dd> <dt>

<span id="PlugInConfiguration_Resources_Resource"></span><span id="pluginconfiguration_resources_resource"></span><span id="PLUGINCONFIGURATION_RESOURCES_RESOURCE"></span>**PlugInConfiguration**/**Resources**/**Resource**
</dt> <dd>

Represents a single [*resource URI*](windows-remote-management-glossary.md)configuration.

> [!Note]  
> The **SupportsOptions**attribute can be set to false. If **SupportsOptions**is set to false, this attribute is not listed when the resource is enumerated.

 

</dd> <dt>

<span id="PlugInConfiguration_Resources_Resource_ResourceUri"></span><span id="pluginconfiguration_resources_resource_resourceuri"></span><span id="PLUGINCONFIGURATION_RESOURCES_RESOURCE_RESOURCEURI"></span>**PlugInConfiguration**/**Resources**/**Resource**/**ResourceUri**
</dt> <dd>

Specifies a single [*resource URI*](windows-remote-management-glossary.md) either in full or as a partial match string based on the **ExactMatch** attribute. If **ExactMatch** is not present, it defaults to **False**, which means the WinRM SOAP processor will do a partial match to the start of the *resource URI* and, if there is a match, pass it to the plug-in. The **SupportsOptions** attribute can be specified if this *resource URI* is allowed to have any options passed in. By default, no options are supported, and if any are present in the client request, an error will be returned. If options are supported by the plug-in, it is important that the plug-in returns the correct error if an option is present that the plug-in does not understand when the **mustUnderstand** flag is set to **True**.

</dd> <dt>

<span id="PlugInConfiguration_Resources_Resource_Capability"></span><span id="pluginconfiguration_resources_resource_capability"></span><span id="PLUGINCONFIGURATION_RESOURCES_RESOURCE_CAPABILITY"></span>**PlugInConfiguration**/**Resources**/**Resource**/**Capability**
</dt> <dd>

Specifies a capability that is available on this [*resource URI*](windows-remote-management-glossary.md). There will be one entry for each type of operation that it supports. The following options are available:

<dl> <dt>

<span id="Get"></span><span id="get"></span><span id="GET"></span>Get
</dt> <dd>

Get operations are supported on the [*resource URI*](windows-remote-management-glossary.md). The **SupportFragment** attribute is used if the get operation supports the concept. The **SupportFiltering** attribute is not valid and should be set to false. This capability is not valid for a *resource URI* if shell operations are also supported.

</dd> <dt>

<span id="Put"></span><span id="put"></span><span id="PUT"></span>Put
</dt> <dd>

Put operations are supported on the [*resource URI*](windows-remote-management-glossary.md). The **SupportFragment**attribute is used if the put operation supports the concept. The **SupportFiltering** attribute is not valid and should be set to **False**. This capability is not valid for a *resource URI* if shell operations are also supported.

</dd> <dt>

<span id="Create"></span><span id="create"></span><span id="CREATE"></span>Create
</dt> <dd>

Create operations are supported on the [*resource URI*](windows-remote-management-glossary.md). The **SupportFragment** attribute is used if the create operation supports the concept. The **SupportFiltering** attribute is not valid and should be set to **False**. This capability is not valid for a *resource URI* if shell operations are also supported.

</dd> <dt>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>Delete
</dt> <dd>

Delete operations are supported on the [*resource URI*](windows-remote-management-glossary.md). The **SupportFragment** attribute is used if the delete operation supports the concept. The **SupportFiltering** attribute is not valid and should be set to **False**. This capability is not valid for a *resource URI* if shell operations are also supported.

</dd> <dt>

<span id="Invoke"></span><span id="invoke"></span><span id="INVOKE"></span>Invoke
</dt> <dd>

Invoke operations are supported on the [*resource URI*](windows-remote-management-glossary.md). The **SupportFragment** attribute is not supported for invoke operations and should be set to false. The **SupportFiltering** attribute is not valid and should be set to **False**. This capability is not valid for a *resource URI* if shell operations are also supported.

</dd> <dt>

<span id="Enumerate"></span><span id="enumerate"></span><span id="ENUMERATE"></span>Enumerate
</dt> <dd>

Enumerate operations are supported on the [*resource URI*](windows-remote-management-glossary.md). The **SupportFragment** attribute is not supported for enumerate operations and should be set to **False**. The **SupportFiltering** attribute is valid, and if the plug-in supports filtering this attribute should be set to **True**. This capability is not valid for a *resource URI* if shell operations are also supported.

</dd> <dt>

<span id="Subscribe"></span><span id="subscribe"></span><span id="SUBSCRIBE"></span>Subscribe
</dt> <dd>

Subscribe operations are supported on the [*resource URI*](windows-remote-management-glossary.md). The **SupportFragment** attribute is not supported for subscribe operations and should be set to **False**. The **SupportFiltering** attribute is not valid and should be set to **False**. This capability is not valid for a *resource URI* if shell operations are also supported.

</dd> <dt>

<span id="Shell"></span><span id="shell"></span><span id="SHELL"></span>Shell
</dt> <dd>

Shell operations are supported on the [*resource URI*](windows-remote-management-glossary.md). The **SupportFragment** attribute is not supported for shell operations and should be set to **False**. The **SupportFiltering** attribute is not valid and should be set to **False**. This capability is not valid for a *resource URI* if any other operation capability is also supported. If a shell operation capability is configured for a *resource URI*, then get, put, create, delete, invoke, and enumerate operations are processed internally within the WinRm service to manage shells. As a result, the plug-in cannot deal with the operations itself.

</dd> </dl> </dd> <dt>

<span id="PlugInConfiguration_Resources_Resource_Security"></span><span id="pluginconfiguration_resources_resource_security"></span><span id="PLUGINCONFIGURATION_RESOURCES_RESOURCE_SECURITY"></span>**PlugInConfiguration**/**Resources**/**Resource**/**Security**
</dt> <dd>

This element defines the security descriptor (via the **Sddl** attribute) that should be applied to determine access to a particular [*resource URI*](windows-remote-management-glossary.md) (via the **Uri** attribute). If **ExactMatch** is not present, the **Security** element defaults to **False**, which means that the **Sddl** applies to all *resource URIs* that share **Uri** as a prefix. If **ExactMatch** is set to true, the **Sddl** applies only to the exact **Uri** specified. If there are multiple **Security** entries that could apply to a particular *resource URIs*, the longest-prefix match is used to determine the appropriate **Sddl**. As a result of the longest-prefix match, if an exact-match **Uri** entry exists, it will always be chosen as the appropriate Security element.

</dd> </dl>

The following is the plug-in configuration schema specified as an XSD.

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<xs:schema attributeFormDefault="unqualified" 
           elementFormDefault="qualified" 
           targetNamespace="http://schemas.microsoft.com/wbem/wsman/1/config/PluginConfiguration" 
           xmlns="http://schemas.microsoft.com/wbem/wsman/1/config/PluginConfiguration" 
           xmlns:xs="https://www.w3.org/2001/XMLSchema">
 <xs:element name="PlugInConfiguration">
  <xs:complexType>
   <xs:sequence>
    <xs:element name="InitializationParameters" minOccurs="0" maxOccurs="1">
     <xs:complexType>
      <xs:sequence>
       <xs:element name="Param">
        <xs:complexType>
         <xs:sequence></xs:sequence>
         <xs:attribute name="Name" type="xs:string"/>
         <xs:attribute name="Value" type="xs:string"/>
        </xs:complexType>
       </xs:element>
      </xs:sequence>
     </xs:complexType>
    </xs:element>
    <xs:element name="Resources">
     <xs:complexType>
      <xs:sequence>
       <xs:element minOccurs="1" maxOccurs="unbounded" name="Resource">
        <xs:complexType>
         <xs:sequence>
          <xs:element name="Capability" minOccurs="1" maxOccurs="unbounded">
           <xs:complexType>
            <xs:simpleContent>
             <xs:extension base="ResourceCapabilityType">
              <xs:attribute name="SupportsFragment" type="xs:boolean" use="optional" default="false"/>
              <xs:attribute name="SupportsFiltering" type="xs:boolean" use="optional" default="false"/>
              <xs:attribute name="Type" type="ResourceCapabilityType"/>
             </xs:extension>
            </xs:simpleContent>
           </xs:complexType>
          </xs:element>
          <xs:element name="Security" minOccurs="0" maxOccurs="unbounded">
           <xs:complexType>
            <xs:sequence></xs:sequence>
            <xs:attribute name="Uri" type="xs:string"/>
            <xs:attribute name="Sddl" type="xs:string"/>
            <xs:attribute name="ExactMatch" type="xs:boolean" use="optional" default="false"/>
           </xs:complexType>
          </xs:element>
         </xs:sequence>
         <xs:attribute name="ResourceUri" type="xs:string"/>
         <xs:attribute name="ExactMatch" type="xs:boolean" use="optional" default="false"/>
         <xs:attribute name="SupportOptions" type="xs:boolean" use="optional" default="false"/>
        </xs:complexType>
       </xs:element>
      </xs:sequence>
     </xs:complexType>
    </xs:element>
   </xs:sequence>
   <xs:attribute name="Filename" type="xs:token"/>
   <xs:attribute name="SDKVersion" type="xs:unsignedInt"/>
   <xs:attribute name="Name" type="xs:string"/>
   <xs:attribute name="XmlRenderingType" type="XmlRenderingTypeType" use="optional" default="text"/>
   <!--Architecture will default to 32 on x86 systems; 64 on 64-bit systems.-->
   <xs:attribute name="Architecture" type="ArchitectureType" use="optional" default="32"/>
  </xs:complexType>
 </xs:element>
 <xs:simpleType name="ResourceCapabilityType">
  <xs:restriction base="xs:token">
   <xs:enumeration value="Get"/>
   <xs:enumeration value="Put"/>
   <xs:enumeration value="Create"/>
   <xs:enumeration value="Delete"/>
   <xs:enumeration value="Invoke"/>
   <xs:enumeration value="Enumerate"/>
   <xs:enumeration value="Subscribe"/>
   <xs:enumeration value="Shell"/>
  </xs:restriction>
 </xs:simpleType>
 <xs:simpleType name="XmlRenderingTypeType">
  <xs:restriction base="xs:token">
   <xs:enumeration value="text"/>
   <xs:enumeration value="XmlReader"/>
  </xs:restriction>
 </xs:simpleType>
 <xs:simpleType name="ArchitectureType">
  <xs:restriction base="xs:token">
   <xs:enumeration value="32"/>
   <xs:enumeration value="64"/>
  </xs:restriction>
 </xs:simpleType>
</xs:schema>
```

 

 




