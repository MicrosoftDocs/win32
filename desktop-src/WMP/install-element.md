---
title: Install Element
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The Install element specifies values used by Windows Media Player to install an online store.
ms.assetid: 9a5e15ee-ec36-48d3-a1c2-bf20b6d2da48
keywords:
- Install Element Windows Media Player
topic_type:
- apiref
api_name:
- Install Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Install Element

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **Install** element specifies values used by Windows Media Player to install an online store.

``` syntax
<Install
    EULAURL = "URL"
    CodeURL = "URL"
    PrivacyInfoURL = "URL"
    InstallApp = "filename"
    InstallData = "commandline"
    CatalogURL = "URL"
/>
```

## Attributes

<dl> <dt>

<span id="EULAURL__required_"></span><span id="eulaurl__required_"></span><span id="EULAURL__REQUIRED_"></span>**EULAURL** (required)
</dt> <dd>

Fully qualified URL for a file with a .txt file name extension that Windows Media Player uses to display an End User License Agreement (EULA). This file must be encoded in ANSI format.

</dd> <dt>

<span id="CodeURL__required_"></span><span id="codeurl__required_"></span><span id="CODEURL__REQUIRED_"></span>**CodeURL** (required)
</dt> <dd>

Fully qualified URL for a package, with a .cab file name extension, that is used to install the online store. The package and all code modules in the package must be signed. For information about code signing, see [Introduction to Code Signing](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537361(v=vs.85)) in the MSDN Library.

</dd> <dt>

<span id="PrivacyInfoURL__required_"></span><span id="privacyinfourl__required_"></span><span id="PRIVACYINFOURL__REQUIRED_"></span>**PrivacyInfoURL** (required)
</dt> <dd>

Fully qualified URL for a webpage that contains privacy policy information for the online store.

</dd> <dt>

<span id="InstallApp__required_"></span><span id="installapp__required_"></span><span id="INSTALLAPP__REQUIRED_"></span>**InstallApp** (required)
</dt> <dd>

Name of the EXE or INF file to run. This file must be contained in the CAB file specified by the **CodeURL** attribute.

</dd> <dt>

<span id="InstallData__optional_"></span><span id="installdata__optional_"></span><span id="INSTALLDATA__OPTIONAL_"></span>**InstallData** (optional)
</dt> <dd>

Command-line string that is passed to the application specified by the **InstallApp** attribute. This attribute is only applicable when the value for **InstallApp** specifies an executable.

</dd> <dt>

<span id="CatalogURL__required_for_type_1__ignored_for_type_2_"></span><span id="catalogurl__required_for_type_1__ignored_for_type_2_"></span><span id="CATALOGURL__REQUIRED_FOR_TYPE_1__IGNORED_FOR_TYPE_2_"></span>**CatalogURL** (required for type 1, ignored for type 2)
</dt> <dd>

Fully qualified URL for the online store's compiled catalog.

</dd> </dl>

## Parent/Child Elements



| Hierarchy       | Element         |
|-----------------|-----------------|
| Parent elements | **ServiceInfo** |
| Child elements  | None            |



 

## Remarks

If any of the required attributes are missing or not available, Windows Media Player setup will not attempt to download and install the online store provider code. Setup will configure the offline default values as specified in the **ServiceInfo** document. **ServiceInfo** can be used when not connected to the Internet by passing the default provider name and the **ServiceInfo** information as command-line parameters. See [Redistributing Windows Media Player Software](redistributing-windows-media-player-software.md) for details about command-line options.

> [!Note]  
> Use of this element requires that you sign a redistribution agreement with Microsoft. Contact your business representative for details.

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 10 or later.<br/> |



## See also

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

