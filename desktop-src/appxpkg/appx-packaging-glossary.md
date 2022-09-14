---
title: Packaging, deployment, and query glossary
description: Provides definitions for terms related to packaging, deployment, and query for Windows apps.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 15E35DCF-C6C1-446A-B09B-6428F9C8A677
ms.topic: article
ms.date: 05/31/2018
---

# Packaging, deployment, and query glossary

<dl> <dt>

<span id="appxpkg.appx_packaging_glossary_application_user_model_id"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_APPLICATION_USER_MODEL_ID"></span>**application user model ID**
</dt> <dd>

The application user model ID uniquely identifies an app on the operating system so the operating system can send notifications and so on to the app.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_block_map"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_BLOCK_MAP"></span>**block map**
</dt> <dd>

Defines the indices and cryptographic hashes for blocks of executable code and data that are stored in the files of an app package. A BlockMap.xml file is required for every app package.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_dependency_package"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_DEPENDENCY_PACKAGE"></span>**dependency package**
</dt> <dd>

A package on which another package depends. The dependency is declared in the dependent package's manifest and not in the dependency package's manifest.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_dependent_package"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_DEPENDENT_PACKAGE"></span>**dependent package**
</dt> <dd>

A package that takes a dependency on another package. The dependency is declared in the dependent package's manifest.

</dd> <dt>

<span id="appxpkg_packaging_glossary_footpint_files"></span><span id="APPXPKG_PACKAGING_GLOSSARY_FOOTPINT_FILES"></span>**footprint files**
</dt> <dd>

Files within an app package that are not part of the app to be deployed. These files provide metadata pertaining to the package. Standard footprint files include the manifest, block map, stream map, and digital signature. Footprint files are created as part of the package build process. In addition per the OPC specification, \[Content\_Types\].xml and files whose names match the "\*\\\_rels\\\*.rels" pattern are footprint files.

</dd> <dt>

<span id="appxpkg_packaging_glossary_manifest"></span><span id="APPXPKG_PACKAGING_GLOSSARY_MANIFEST"></span>**manifest**
</dt> <dd>

An XML file that describes the contents and metadata associated with a package including the package ID. A manifest XML file is required for every app package.

</dd> <dt>

<span id="appxpkg_packaging_glossary_opc"></span><span id="APPXPKG_PACKAGING_GLOSSARY_OPC"></span>**OPC**
</dt> <dd>

Open Packaging Conventions (OPC) describes a container-file technology that is documented in the ISO/IEC 29500 and ECMA 376 standards. App packages are OPC-compliant.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_package"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_PACKAGE"></span>**package**
</dt> <dd>

The unit of deployment, management, and servicing software associated with the app packaging model. A package contains the files that constitute the app, along with a manifest file that describes the software to Windows.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_package_family_moniker"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_PACKAGE_FAMILY_MONIKER"></span>**package family name**
</dt> <dd>

A serialized form of the package ID that uniquely represents the package family on the computer. It is suitable for naming objects such as files and folders. The package family name is similar to the package full name, but includes only the name and publisher. Because it excludes info that changes with servicing (version, architecture, and resource info), it is useful for version-independent references to the package.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_package_moniker"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_PACKAGE_MONIKER"></span>**package full name**
</dt> <dd>

A serialized form of the package ID that uniquely represents this version of the package on the computer. It is suitable for naming objects such as files and folders.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_package_id"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_PACKAGE_ID"></span>**package ID**
</dt> <dd>

A globally unique identifier for a package. It is composed of a tuple of attributes for the package including name, publisher, supported architecture, resource info, and version. See package full name and package family name for serialized forms of the package ID.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_package_relative_application_id"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_PACKAGE_RELATIVE_APPLICATION_ID"></span>**package relative application ID**
</dt> <dd>

The **Id** attribute on the [**Application**](/uwp/schemas/appxpackage/appxmanifestschema2010-v2/element-application) element within the package manifest, which is also known as PRAID. This string uniquely identifies an app within a package. This attribute is required for the **Application** element.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_payload_file"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_PAYLOAD_FILE"></span>**payload files**
</dt> <dd>

The files within an app package that are part of the app to be deployed. These files are extracted and placed in the user's installation folder.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_resource_id"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_RESOURCE_ID"></span>**resource ID**
</dt> <dd>

An optional part of a package ID that is used to differentiate the resources in the package. For example, a resource ID can be used to specify the language or locale.

</dd> <dt>

<span id="appxpkg.appx_packaging_glossary_zip_central_directory"></span><span id="APPXPKG.APPX_PACKAGING_GLOSSARY_ZIP_CENTRAL_DIRECTORY"></span>**ZIP central directory**
</dt> <dd>

The byte sequences in a ZIP file that store metadata about the ZIP archive and its contents including name, size, compression settings, and location within the archive.

</dd> </dl>

 

 