---
description: This section provides an overview of the XPS Digital Signature API.
ms.assetid: 895974df-d5e8-4974-b057-ec7e5e59d805
title: About XPS Digital Signature API
ms.topic: article
ms.date: 05/31/2018
---

# About XPS Digital Signature API

XPS documents can have digital signatures to allow users to sign a document, verify the identity of the signer, and indicate whether an XPS document has changed since it was signed. A native Windows application can use the interfaces of the XPS Digital Signature API to perform digital signature operations on an XPS document. This section provides an overview of the XPS Digital Signature API.

The [**IXpsSignatureManager**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssignaturemanager) interface manages the digital signature operations on an XPS document. Before an application can access the digital signatures of an XPS document, the application must call [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to create an **IXpsSignatureManager** and then call [**IXpsSignatureManager::LoadPackageFile**](/windows/desktop/api/xpsdigitalsignature/nf-xpsdigitalsignature-ixpssignaturemanager-loadpackagefile) or [**IXpsSignatureManager::LoadPackageStream**](/windows/desktop/api/xpsdigitalsignature/nf-xpsdigitalsignature-ixpssignaturemanager-loadpackagestream) to load the XPS document. For more information about this initialization process, see [Initialize the Signature Manager](initialize-the-signature-manager.md).

After an XPS document has been loaded into an [**IXpsSignatureManager**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssignaturemanager) interface, an application can then access the document's digital signatures and digital signature requests. You can access the digital signatures by using an [**IXpsSignature**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssignature) interface from the signature manager's [**IXpsSignatureCollection**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssignaturecollection) interface. An application can also add and remove **IXpsSignature** interfaces from the collection. Signature requests are accessed by using [**IXpsSignatureRequest**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssignaturerequest) which are collected in an [**IXpsSignatureRequestCollection**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssignaturerequestcollection) interface. The **IXpsSignatureRequestCollection** is part of an [**IXpsSignatureBlock**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssignatureblock) interface which are collected in the [**IXpsSignatureBlockCollection**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssignatureblockcollection) of the signature manager.

Applications can use the [**IXpsSigningOptions**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssigningoptions) of the signature manager to access and set digital signature options.

For examples of how to access the digital signatures of an XPS document, see [Common Digital Signature Programming Tasks](basic-digital-signature-programming-tasks.md).

## Related topics

<dl> <dt>

[Using XPS Digital Signature API](using-digital-signatures-in-xps-documents.md)
</dt> <dt>

[XPS Digital Signature API Reference](xps-digital-signatures-programming-reference.md)
</dt> <dt>

[Packaging](/previous-versions/windows/desktop/opc/packaging)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> <dt>

[Standard ECMA-376, Office Open XML File Formats](https://www.ecma-international.org/publications/standards/Ecma-376.htm)
</dt> </dl>

 

 
