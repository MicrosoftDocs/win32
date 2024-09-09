---
description: An assembly manifest is an XML file that describes a side-by-side assembly.
ms.assetid: f7973019-0a80-498e-adf1-c66267c813f4
title: Assembly Manifests
ms.topic: article
ms.date: 05/31/2018
---

# Assembly Manifests

An assembly manifest is an XML file that describes a side-by-side assembly. Assembly manifests describe the names and versions of side-by-side assemblies, files, and resources of the assembly, as well as the dependence of the assembly on other side-by-side assemblies. Correct installation, activation, and execution of side-by-side assemblies requires that the assembly manifest always accompany an assembly on the system.

For a complete listing of the XML schema, see [Manifest File Schema](manifest-file-schema.md).

Assembly manifests have the following elements and attributes.



| Element                           | Attributes                | Required |
|-----------------------------------|---------------------------|----------|
| **assembly**                      |                           | Yes      |
|                                   | **manifestVersion**       | Yes      |
| **noInheritable**                 |                           | No       |
| **assemblyIdentity**              |                           | Yes      |
|                                   | **type**                  | Yes      |
|                                   | **name**                  | Yes      |
|                                   | **language**              | No       |
|                                   | **processorArchitecture** | No       |
|                                   | **version**               | Yes      |
|                                   | **publicKeyToken**        | No       |
| **dependency**                    |                           | No       |
| **dependentAssembly**             |                           | No       |
| **file**                          |                           | No       |
|                                   | **name**                  | Yes      |
|                                   | **hashalg**               | No       |
|                                   | **hash**                  | No       |
| **comClass**                      |                           | No       |
|                                   | **description**           | No       |
|                                   | **clsid**                 | Yes      |
|                                   | **threadingModel**        | No       |
|                                   | **tlbid**                 | No       |
|                                   | **progid**                | No       |
|                                   | **miscStatus**            | No       |
|                                   | **miscStatusIcon**        | No       |
|                                   | **miscStatusContent**     | No       |
|                                   | **miscStatusDocPrint**    | No       |
|                                   | **miscStatusThumbnail**   | No       |
| **typelib**                       |                           | No       |
|                                   | **tlbid**                 | Yes      |
|                                   | **version**               | Yes      |
|                                   | **helpdir**               | Yes      |
|                                   | **resourceid**            | No       |
|                                   | **flags**                 | No       |
| **comInterfaceExternalProxyStub** |                           | No       |
|                                   | **iid**                   | Yes      |
|                                   | **baseInterface**         | No       |
|                                   | **numMethods**            | No       |
|                                   | **name**                  | No       |
|                                   | **tlbid**                 | No       |
|                                   | **proxyStubClsid32**      | No       |
| **comInterfaceProxyStub**         |                           | No       |
|                                   | **iid**                   | Yes      |
|                                   | **name**                  | Yes      |
|                                   | **tlbid**                 | No       |
|                                   | **baseInterface**         | No       |
|                                   | **numMethods**            | No       |
|                                   | **proxyStubClsid32**      | No       |
|                                   | **threadingModel**        | No       |
| **windowClass**                   |                           | No       |
|                                   | **versioned**             | No       |



 

## File Location

Assembly manifests can be installed in three locations:

-   As manifests that accompany [shared assemblies](/windows/desktop/Msi/shared-assemblies), assembly manifests should be installed as a separate file in the side-by-side assembly cache. This is usually the WinSxS folder in the Windows directory.
-   As manifests that accompany [private assemblies](/windows/desktop/Msi/private-assemblies), assembly manifests should installed in the directory structure of the application. This is usually a separate file in the same folder as the application's executable file.
-   As a resource in a DLL, the assembly is available for the private use of the DLL. An assembly manifest cannot be included as a resource in an EXE. An EXE file may include an [application manifest](application-manifests.md) as a resource.

## File Name Syntax

The name of an assembly manifest is any valid file name followed by `.manifest`.

For example, an assembly manifest that refers to myassembly would use the following file name syntax: `myassembly.<resource ID>.manifest`.
You can omit the `<resource ID>` field if the assembly manifest is being installed as a separate file or if the resource ID is 1.

> [!Note]  
> Because of the way side-by-side searches for private assemblies, the following naming restrictions apply when packaging a DLL as a private assembly. A recommended way of doing this is to put the assembly manifest in the DLL as a resource. In this case, the resource ID must equal 1 and the name of the private assembly may be the same as the name of the DLL. For example, if the name of the DLL is Microsoft.Windows.mysample.dll, the value of the name attribute used in the **assemblyIdentity** element of the manifest may also be Microsoft.Windows.mysample. An alternate way is to put the assembly manifest in a separate file. In this case, the name of the assembly and its manifest must be different than the name of the DLL. For example, Microsoft.Windows.mysampleAsm, Microsoft.Windows.mysampleAsm.manifest, and Microsoft.Windows.Mysample.dll. For more information about how side-by-side searches for private assemblies, see [Assembly Searching Sequence](assembly-searching-sequence.md).

 

## Elements

Names of elements and attributes are case-sensitive. The values of elements and attributes are case-insensitive, except for the value of the type attribute.

<dl> <dt>

<span id="assembly"></span><span id="ASSEMBLY"></span>**assembly**
</dt> <dd>

A container element. Its first subelement must be an **assemblyIdentity** or **noInheritable** element. The assembly manifest uniquely describes the side-by-side assembly identified by the **assemblyIdentity**. Required.

The assembly element must be in the namespace "urn:schemas-microsoft-com:asm.v1". Child elements of the assembly must also be in this namespace, by inheritance or by tagging.

The **assembly** element has the following attribute.



| Attribute           | Description                                           |
|---------------------|-------------------------------------------------------|
| **manifestVersion** | The **manifestVersion** attribute must be set to 1.0. |



 

</dd> <dt>

<span id="noInheritable"></span><span id="noinheritable"></span><span id="NOINHERITABLE"></span>**noInheritable**
</dt> <dd>

Include this element in an assembly manifest to indicate that the assembly manages the [activation contexts](activation-contexts.md) and its objects. The **noInheritable** element must be a subelement of an **assembly** element. The **assemblyIdentity** element should come after any **noInheritable** element. The **noInheritable** element is required in the assembly manifest if the assembly is used by any [application manifests](application-manifests.md) that include the **noInherit** element. A **noInheritable** element in an application manifest has no effect. A **noInheritable** element has no child elements.

</dd> <dt>

<span id="assemblyIdentity"></span><span id="assemblyidentity"></span><span id="ASSEMBLYIDENTITY"></span>**assemblyIdentity**
</dt> <dd>

Describes and uniquely identifies a side-by-side assembly.

As the first subelement of an **assembly** element, **assemblyIdentity** describes and uniquely identifies the side-by-side assembly that owns this assembly manifest. This is called the DEF-context **assemblyIdentity** of the assembly manifest.

As the first subelement of a **dependentAssembly** element, **assemblyIdentity** describes and uniquely identifies a side-by-side assembly that is used by the DEF-context **assemblyIdentity**. This is called a REF-context **assemblyIdentity** of the assembly manifest. The DEF-context assembly requires the REF-context assembly to work correctly. Note that every REF-context **assemblyIdentity** must exactly match a corresponding DEF-context **assemblyIdentity** in the referenced assembly's own assembly manifest.

This element has no subelements. The **assemblyIdentity** element does have the following attributes.



| Attribute                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **type**                  | Specifies the assembly type. The value must be win32 and in lower case. Required.                                                                                                                                                                                                                                                                                                                                                         |
| **name**                  | Uniquely names the assembly. Use the following format for the assembly name: Organization.Division.Name. For example, Microsoft.Windows.mysampleAsm. Required. Note that in the case of a DLL packaged as a private assembly with a separate manifest file, the name of the assembly must be different than the name of the DLL and the manifest.<br/>                                                                              |
| **language**              | Identifies the language of the assembly. Optional. If the assembly is language-specific, specify the DHTML language code. In the DEF-context **assemblyIdentity** of an assembly manifest intended for worldwide use (language neutral) omit the language attribute.<br/> In a REF-context **assemblyIdentity** of an assembly manifest intended for worldwide use (language neutral) set the value of language to "\*".<br/> |
| **processorArchitecture** | Specifies the processor. The valid values are x86 for 32-bit Windows and ia64 for 64-bit Windows. Optional.                                                                                                                                                                                                                                                                                                                               |
| **version**               | Specifies the assembly version. Use the four-part version format: mmmmm.nnnnn.ooooo.ppppp. Each of the parts separated by periods can be 0-65535 inclusive. For more information, see [Assembly Versions](assembly-versions.md). Required.                                                                                                                                                                                               |
| **publicKeyToken**        | A 16-character hexadecimal string representing the last 8 bytes of the SHA-1 hash of the public key under which the assembly is signed. The public key used to sign the catalog must be 2048 bits or greater. Required for shared side-by-side assemblies.                                                                                                                                                                                |



 

</dd> <dt>

<span id="dependency"></span><span id="DEPENDENCY"></span>**dependency**
</dt> <dd>

A container element including at least one **dependentAssembly**. The first subelement must be a **dependentAssembly** element. A **dependency** has no attributes. Optional.

</dd> <dt>

<span id="dependentAssembly"></span><span id="dependentassembly"></span><span id="DEPENDENTASSEMBLY"></span>**dependentAssembly**
</dt> <dd>

The first subelement must be an **assemblyIdentity** element that describes and uniquely identifies a side-by-side assembly that is used by the side-by-side assembly that owns this assembly manifest. Every **dependentAssembly** must be inside exactly one **dependency**. Optional.

</dd> <dt>

<span id="file"></span><span id="FILE"></span>**file**
</dt> <dd>

Contains files used by a side-by-side assembly. Contains **comClass**, **typelib**, **windowClass**, **comInterfaceProxyStub** subelements. Optional.

The **file** element has the following attributes.



| Attribute   | Description                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------|
| **name**    | Name of the file, for example, Conctl32.dll.                                                            |
| **hashalg** | Algorithm used to create a hash of the file. This value should be SHA1.                                 |
| **hash**    | A hash of the file referred to by name. A hexadecimal string of length depending on the hash algorithm. |



 

</dd> <dt>

<span id="comClass"></span><span id="comclass"></span><span id="COMCLASS"></span>**comClass**
</dt> <dd>

A subelement of a **file** element. Optional.

The **comClass** element has the following attributes.



| Attribute               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **description**         | Class name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **clsid**               | The GUID that uniquely identifies the Class. Required. The value must be in the format of a valid GUID.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **threadingModel**      | The threading model used by in-process COM classes. If this property is null, then no threading model is used. The component is created on the main thread of the client and calls from other threads are marshaled to this thread. Optional. Valid values are: "Apartment", "Free", "Both", and "Neutral".                                                                                                                                                                                                                         |
| **tlbid**               | GUID for the type library for this COM component. The value must be in the format of a GUID. Optional.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **progid**              | Version-dependent programmatic identifier associated with the COM component. The format of a ProgID is <*vendor*>.<*component*>.<*version*>.                                                                                                                                                                                                                                                                                                                                                                      |
| **miscStatus**          | Duplicates in the assembly manifest the information provided by the MiscStatus registry key. If values for the **miscStatusIcon**, **miscStatusContent**, **miscStatusDocprint**, or **miscStatusThumbnail** attributes are not found, the corresponding default value listed in **miscStatus** is used for the missing attributes. The value can be a comma-delimited list of the attribute values from the table below. You can use this attribute if the COM class is an OCX class that requires Miscstatus registry key values. |
| **miscStatusIcon**      | Duplicates in the assembly manifest the information provided by DVASPECT\_ICON. It can provide an icon of an object. The value can be a comma-delimited list of the attribute values from the table below. You can use this attribute if the COM class is an OCX class that requires Miscstatus registry key values.                                                                                                                                                                                                                |
| **miscStatusContent**   | Duplicates in the assembly manifest the information provided by DVASPECT\_CONTENT. It can provide a compound document displayable for a screen or printer. The value can be a comma-delimited list of the attribute values from the table below. You can use this attribute if the COM class is an OCX class that requires Miscstatus registry key values.                                                                                                                                                                          |
| **miscStatusDocprint**  | Duplicates in the assembly manifest the information provided by DVASPECT\_DOCPRINT. It can provide an object representation displayable on the screen as though printed to a printer. The value can be a comma-delimited list of the attribute values from the table below. You can use this attribute if the COM class is an OCX class that requires Miscstatus registry key values.                                                                                                                                               |
| **miscStatusThumbnail** | Duplicates in an assembly manifest the information provided by DVASPECT\_THUMBNAIL. It can provide a thumbnail of an object displayable in a browsing tool. The value can be a comma-delimited list of the attribute values from the table below. You can use this attribute if the COM class is an OCX class that requires Miscstatus registry key values.                                                                                                                                                                         |



 

The **comClass** element can have &lt;progid&gt;...</progid> elements as children, which list the version dependent progids.

The following example shows a **comClass** element included in a **file** element.

``` syntax
<file name="sampleu.dll">
        <comClass description="Font Property Page"
    clsid="{0BE35200-8F91-11CE-9DE3-00AA004BB851}"
          threadingModel = "Both"
             tlbid = "{44EC0535-400F-11D0-9DCD-00A0C90391D3}"/>
        <comClass description="Color Property Page"
    clsid="{0BE35201-8F91-11CE-9DE3-00AA004BB851}" 
    progid="ABC.Registrar"/>
    </file>
```

If your COM class is an OCX class that requires the MiscStatus registry subkey to specify how to create and display an object, you can enable the object by duplicating this information in the assembly manifest. Specify the object's characteristics by using the **miscStatus**, **miscStatusIcon**, **miscStatusContent**, **miscStatusDocprint**, and **miscStatusThumbnail** attributes of the **comClass** element. Set these attributes to a comma-separated list of attribute values from the following table. These attributes duplicate the information that would be provided by a DVASPECT enumeration. If a no value is found for **miscStatusIcon**, **miscStatusContent**, **miscStatusDocprint**, or **miscStatusThumbnail**, the default values specified in **miscStatus** is used. Use attribute values from the following table. These correspond to the bit flags of a [**OLEMISC**](/windows/win32/api/oleidl/ne-oleidl-olemisc) enumeration.



| Attribute Value              | OLEMISC Constant                      |
|------------------------------|---------------------------------------|
| recomposeonresize            | OLEMISC\_RECOMPOSEONRESIZE            |
| onlyiconic                   | OLEMISC\_ONLYICONIC                   |
| insertnotreplace             | OLEMISC\_INSERTNOTREPLACE             |
| static                       | OLEMISC\_STATIC                       |
| cantlinkinside               | OLEMISC\_CANTLINKINSIDE               |
| canlinkbyole1                | OLEMISC\_CANLINKBYOLE1                |
| islinkobject                 | OLEMISC\_ISLINKOBJECT                 |
| insideout                    | OLEMISC\_INSIDEOUT                    |
| activatewhenvisible          | OLEMISC\_ACTIVATEWHENVISIBLE          |
| renderingisdeviceindependent | OLEMISC\_RENDERINGISDEVICEINDEPENDENT |
| invisibleatruntime           | OLEMISC\_INVISIBLEATRUNTIME           |
| alwaysrun                    | OLEMISC\_ALWAYSRUN                    |
| actslikebutton               | OLEMISC\_ACTSLIKEBUTTON               |
| actslikelabel                | OLEMISC\_ACTSLIKELABEL                |
| nouiactivate                 | OLEMISC\_NOUIACTIVATE                 |
| alignable                    | OLEMISC\_ALIGNABLE                    |
| simpleframe                  | OLEMISC\_SIMPLEFRAME                  |
| setclientsitefirst           | OLEMISC\_SETCLIENTSITEFIRST           |
| imemode                      | TOLEMISC\_IMEMODE                     |
| ignoreativatewhenvisible     | OLEMISC\_IGNOREACTIVATEWHENVISIBLE    |
| wantstomenumerge             | OLEMISC\_WANTSTOMENUMERGE             |
| supportsmultilevelundo       | OLEMISC\_SUPPORTSMULTILEVELUNDO       |



 

</dd> <dt>

<span id="typelib"></span><span id="TYPELIB"></span>**typelib**
</dt> <dd>

A subelement of a **file** element. Optional.

The **typelib** element has the attributes shown in the following table.



| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **tlbid**      | The unique ID of the type library. Required.                                                                                                                                                                                                                                                                                                                                                                                    |
| **version**    | The two-part version number of the type library. If only the minor version number increases, all the features of the previous type library are supported in a compatible way. If the major version number changes, code that compiled against the type library must be recompiled. The version number of the type library may differ from the version number of the application. Required.                                      |
| **helpdir**    | The directory where the Help file for the types in the type library is located. If the application supports type libraries for multiple languages, the libraries may refer to different file names in the Help file directory. If no value, then specify "". Required.                                                                                                                                                          |
| **resourceid** | The hexadecimal string representation of the locale identifier (LCID). It is one to four hexadecimal digits with no 0x prefix and no leading zeros. The LCID may have a neutral sublanguage identifier. For more information, see [Locale Identifiers](/windows/desktop/Intl/locale-identifiers). Optional.                                                                                                                                      |
| **flags**      | The string representation of the type library flags for this type library. Specifically, it should be one of "RESTRICTED", "CONTROL", "HIDDEN" and "HASDISKIMAGE". These are the values of the [**LIBFLAGS**](/windows/win32/api/oaidl/ne-oaidl-libflags) enumeration, and are the same flags specified in the *uLibFlags* parameter of the [**ICreateTypeLib::SetLibFlags**](/windows/win32/api/oaidl/nf-oaidl-icreatetypelib-setlibflags) method. Optional. |



 

The following example shows a **typelib** element included in a **file** element.

``` syntax
<file name="sampleu.dll">
       <typelib tlbid="{44EC0535-400F-11D0-9DCD-00A0C90391D3}"
       version="1.0" helpdir=""/>
</file>
```

</dd> <dt>

<span id="comInterfaceExternalProxyStub"></span><span id="cominterfaceexternalproxystub"></span><span id="COMINTERFACEEXTERNALPROXYSTUB"></span>**comInterfaceExternalProxyStub**
</dt> <dd>

The **comInterfaceExternalProxyStub** is a subelement of an **assembly** element and is used for automation interfaces. For example, [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) and its derived interfaces. Optional.

The default proxy-stub implementation is adequate for most automation interfaces, such as interfaces derived from [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch). The interface proxy stub, and all other external proxy-stub interface implementations, must be listed in the **comInterfaceExternalProxyStub**. The **comInterfaceExternalProxyStub** element has the attributes shown in the following table.



| Attribute         | Description                                                                                                                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iid**           | The IID of the interface for which the proxy is being declared. Required. The value should be in the form: "{iid}".                                                                         |
| **baseInterface** | The IID of the interface from which the one described by the **iid** attribute is derived. This attribute is optional. The value should be in the form: "{iid}".                            |
| **numMethods**    | The number of methods implemented by the interface. This attribute is optional. The value should be in the form: "n".                                                                       |
| **name**          | Name of the interface as it would appear in code. For example, "IViewObject". This should not be a descriptive string. This attribute is optional. The value should be in the form: "name". |
| **tlbid**         | The type library that contains the description of the interface specified by the **iid** attribute. This attribute is optional. The value should be in the form: "{tlbid}" .                |
| proxyStubClsid32  | Maps an IID to a CLSID in 32-bit proxy DLLs.                                                                                                                                                |



 

The following example shows a **comInterfaceExternalProxyStub** element.

``` syntax
<comInterfaceExternalProxyStub 
  name="IAxWinAmbientDispatch" 
    iid="{B6EA2051-048A-11D1-82B9-00C04FB9942E}" 
    numMethods="35" 
  baseInterface="{00000000-0000-0000-C000-000000000046}"/>
```

</dd> <dt>

<span id="comInterfaceProxyStub"></span><span id="cominterfaceproxystub"></span><span id="COMINTERFACEPROXYSTUB"></span>**comInterfaceProxyStub**
</dt> <dd>

A subelement of a **file** element. Optional.

If a file in the assembly implements a proxy stub, the corresponding file tag must include a **comInterfaceProxyStub** subelement having attributes that are identical to a **comInterfaceProxyStub** element. Marshaling interfaces between processes and threads may not work as expected if you omit some of the **comInterfaceProxyStub** dependencies for your component.

The **comInterfaceProxyStub** element has the following attributes.



| Attribute            | Description                                                                                                                                                                                                                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iid**              | The .IID of the interface for which the proxy is being declared. Required. The value should be in the form: "{iid}".                                                                                                                                                                                        |
| **name**             | Name of the interface as it would appear in code. For example, "IViewObject". This should not be a descriptive string. This attribute is optional. The value should be in the form: "name".                                                                                                                 |
| **tlbid**            | The type library that contains the description of the interface specified by the **iid** attribute. This attribute is optional. The value should be in the form: "{tlbid}".                                                                                                                                 |
| **baseInterface**    | The IID of the interface from which the one described by the **iid** attribute is derived. This attribute is optional. The value should be in the form: "{iid}".                                                                                                                                            |
| **numMethods**       | The number of methods implemented by the interface. This attribute is optional. The value should be in the form: "n".                                                                                                                                                                                       |
| **proxyStubClsid32** | Maps an IID to a CLSID in 32-bit proxy DLLs.                                                                                                                                                                                                                                                                |
| **threadingModel**   | The threading model used by in-process COM classes. If this property is null, then no threading model is used. The component is created on the main thread of the client and calls from other threads are marshaled to this thread. Optional. Valid values are: "Apartment", "Free", "Both", and "Neutral". |



 

</dd> <dt>

<span id="windowclass"></span><span id="WINDOWCLASS"></span>**windowclass**
</dt> <dd>

The name of a windows class that is to be versioned. The **windowclass** element has the following attribute.



| Attribute     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **versioned** | This attribute controls whether or not the internal window class name used in registration contains the version of the assembly containing the window class. The value of this attribute can be "yes" or "no". The default is "yes". The value "no" should only be used if the same window class is defined by a side-by-side component and an equivalent non-side-by-side component and you wish to treat them as the same window class. Note that the usual rules about window class registration apply only the first component that registers the window class will be able to register it since it is not versioned. |



 

The following example shows a **windowclass** element included in a **file** element.

``` syntax
<file name="comctl32.dll">
        <windowClass versioned="no">ToolbarWindow32</windowClass>
</file>
```

</dd> </dl>

## Example

The following is an example of an assembly manifest.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" 
manifestVersion="1.0">
    <assemblyIdentity type="win32" name="Microsoft.Tools.SampleAssembly" version="6.0.0.0" processorArchitecture="x86" publicKeyToken="0000000000000000"/>
    <file name="sampleu.dll" hash="3eab067f82504bf271ed38112a4ccdf46094eb5a" hashalg="SHA1">
        <comClass description="Font Property Page" clsid="{0BE35200-8F91-11CE-9DE3-00AA004BB851}"/>
        <comClass description="Color Property Page" clsid="{0BE35201-8F91-11CE-9DE3-00AA004BB851}"/>
        <comClass description="Picture Property Page" clsid="{0BE35202-8F91-11CE-9DE3-00AA004BB851}"/>
    </file>
    <file name="bar.dll" hash="ac72753e5bb20446d88a48c8f0aaae769a962338" hashalg="SHA1"/>
    <file name="foo.dll" hash="a7312a1f6cfb46433001e0540458de60adcd5ec5" hashalg="SHA1">
        <comClass description="Registrar Class" clsid="{44EC053A-400F-11D0-9DCD-00A0C90391D3}" progid="ATL.Registrar"/>
    <comInterfaceProxyStub iid="{B6EA2051-048A-11D1-82B9-00C04FB9942E}" name=" IAxWinAmbientDispatch " tlbid="{34EC053A-400F-11D0-9DCD-00A0C90391D3}"/>
        <typelib tlbid="{44EC0535-400F-11D0-9DCD-00A0C90391D3}" version="1.0" helpdir=""/>
    </file>
    <file name="sampledll.dll" hash="ba62960ceb15073d2598379307aad84f3a73dfcb" hashalg="SHA1"/>
<windowClass>ToolbarWindow32</windowClass>
        <windowClass>ComboBoxEx32</windowClass>
        <windowClass>sample_trackbar32</windowClass>
        <windowClass>sample_updown32</windowClass>
</assembly>
```

 

