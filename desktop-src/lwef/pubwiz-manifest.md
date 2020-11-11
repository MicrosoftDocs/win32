---
title: Using the Transfer Manifest
description: The Web Publishing Wizard and Online Print Ordering Wizard use the transfer manifest to communicate details of data transfer between the client computer and the server site.
ms.assetid: b7bb541c-3bf4-4aab-ac70-c006517e772e
keywords:
- Web Publishing Wizard,transfer manifest
- Online Print Ordering Wizard,transfer manifest
- transfer manifest
- manifest
- window.external,transfer manifest
ms.topic: article
ms.date: 05/31/2018
---

# Using the Transfer Manifest

The Web Publishing Wizard and Online Print Ordering Wizard use the transfer manifest to communicate details of data transfer between the client computer and the server site.

## The Purpose of the Transfer Manifest

The transfer manifest describes files involved in the transfer, including details such as the destination hierarchy and the file's metadata. Server-side script can modify the manifest by removing inappropriate files from the list and adding information about how and where the files should be transferred.

The manifest is exposed as the property **window.external.Property("TransferManifest")**, an XML Document Object Model (DOM) document. For more information on the XML DOM, see the MSDN documentation for [IXMLDOMDocument/DOMDocument](/previous-versions/windows/desktop/ms756987(v=vs.85)).

The top-level organization of the transfer manifest is as follows:


```
<transfermanifest>
    <filelist/>
    <folderlist/>
    <uploadinfo/>
</transfermanifest>
```



The server-side HTML page can use the nodes in the manifest to obtain certain information about the files to be copied and then modify the service's UI accordingly. For instance, a photo printing site might use the information to display thumbnails of the chosen images, while a storage site might use the information to ensure that sufficient storage space is available for that user. For complete information on the transfer manifest nodes and attributes, see [Transfer Manifest Schema](/windows/desktop/shell/interfaces).

The transfer manifest schema is written as an open model so that elements not specifically defined in the schema may appear in the transfer manifest. Therefore, a provider site might add proprietary elements for its own use without disturbing the validity of the manifest. The schema is also defined so that the order of elements is not restricted.

> [!Note]  
> The manifest is re-created each time a new provider is chosen so that the provider has a chance to store site information in the manifest.

 

## Related topics

<dl> <dt>

[Transfer Manifest Schema](/windows/desktop/shell/interfaces)
</dt> </dl>

 

 