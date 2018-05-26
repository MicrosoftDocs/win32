---
title: Packaging Digital Signature Interfaces
description: Packaging Digital Signature Interfaces
ms.assetid: 76455a88-81be-45d9-a682-2ba43038b43f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Packaging Digital Signature Interfaces

## 



| Packaging Digital Signature Interfaces                                                               |                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOpcCertificateEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopccertificateenumerator?branch=master)<br/>                            | A read-only enumerator of pointers to [CERT\_CONTEXT](http://msdn.microsoft.com/library/aa377189(vs.85).aspx) structures. <br/>                                                                                   |
| [**IOpcCertificateSet**](/windows/previous-versions/msopc/nn-msopc-iopccertificateset?branch=master)<br/>                                          | An unordered set of certificates to be used with a signature.<br/>                                                                                                                                                      |
| [**IOpcDigitalSignature**](/windows/previous-versions/msopc/nn-msopc-iopcdigitalsignature?branch=master)<br/>                                      | Represents a package digital signature. <br/>                                                                                                                                                                           |
| [**IOpcDigitalSignatureEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcdigitalsignatureenumerator?branch=master)<br/>                  | A read-only enumerator of [**IOpcDigitalSignature**](/windows/previous-versions/msopc/nn-msopc-iopcdigitalsignature?branch=master) interface pointers.<br/>                                                                                                                 |
| [**IOpcDigitalSignatureManager**](/windows/previous-versions/msopc/nn-msopc-iopcdigitalsignaturemanager?branch=master)<br/>                        | Provides access to Packaging Digital Signature Interfaces for a package that is represented by Packaging API objects. <br/>                                                                                             |
| [**IOpcRelationshipSelector**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipselector?branch=master)<br/>                              | Represents how to select, from a Relationships part, the relationships to be referenced for signing. <br/>                                                                                                              |
| [**IOpcRelationshipSelectorEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipselectorenumerator?branch=master)<br/>          | A read-only enumerator of [**IOpcRelationshipSelector**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipselector?branch=master) interface pointers. <br/>                                                                                                        |
| [**IOpcRelationshipSelectorSet**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipselectorset?branch=master)<br/>                        | An unordered set of [**IOpcRelationshipSelector**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipselector?branch=master) interface pointers that represent the selection criteria that is used to identify relationships for signing. <br/>                     |
| [**IOpcSignatureCustomObject**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturecustomobject?branch=master)<br/>                            | Represents an application-specific **Object** element that has been or will be signed. <br/>                                                                                                                            |
| [**IOpcSignatureCustomObjectEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturecustomobjectenumerator?branch=master)<br/>        | A read-only enumerator of [**IOpcSignatureCustomObject**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturecustomobject?branch=master) interface pointers. <br/>                                                                                                      |
| [**IOpcSignatureCustomObjectSet**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturecustomobjectset?branch=master)<br/>                      | An unordered set of [**IOpcSignatureCustomObject**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturecustomobject?branch=master) interface pointers that contain the XML markup of application-specific **Object** elements. <br/>                                    |
| [**IOpcSignaturePartReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturepartreference?branch=master)<br/>                          | Represents a reference to a part that has been or will be signed. <br/>                                                                                                                                                 |
| [**IOpcSignaturePartReferenceEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturepartreferenceenumerator?branch=master)                 | A read-only enumerator of [**IOpcSignaturePartReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturepartreference?branch=master) interface pointers.<br/>                                                                                                     |
| [**IOpcSignaturePartReferenceSet**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturepartreferenceset?branch=master)<br/>                    | An unordered set of [**IOpcSignaturePartReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturepartreference?branch=master) interface pointers that represent references to parts to be signed. <br/>                                                          |
| [**IOpcSignatureReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturereference?branch=master)<br/>                                  | Represents a reference to XML markup that has been or will be signed. <br/>                                                                                                                                             |
| [**IOpcSignatureReferenceEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturereferenceenumerator?branch=master)                         | A read-only enumerator of [**IOpcSignatureReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturereference?branch=master) interface pointers.<br/>                                                                                                             |
| [**IOpcSignatureReferenceSet**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturereferenceset?branch=master)<br/>                            | An unordered set of [**IOpcSignatureReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturereference?branch=master) interface pointers that represent references to XML elements to be signed. <br/>                                                           |
| [**IOpcSignatureRelationshipReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturerelationshipreference?branch=master)<br/>          | Represents a reference to a Relationships part that contains relationships that have been or will be signed. <br/>                                                                                                      |
| [**IOpcSignatureRelationshipReferenceEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturerelationshipreferenceenumerator?branch=master) | A read-only enumerator of [**IOpcSignatureRelationshipReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturerelationshipreference?branch=master) interface pointers.<br/>                                                                                     |
| [**IOpcSignatureRelationshipReferenceSet**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturerelationshipreferenceset?branch=master)<br/>    | An unordered set of [**IOpcSignatureRelationshipReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturerelationshipreference?branch=master) interface pointers that represent references to Relationships parts that contain relationships to be signed. <br/> |
| [**IOpcSigningOptions**](/windows/previous-versions/msopc/nn-msopc-iopcsigningoptions?branch=master)<br/>                                          | Provides methods to set and access information required to generate a signature.<br/>                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Packaging Interfaces](packaging-interfaces.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Packaging API Programming Guide](packaging-programming-guide.md)
</dt> <dt>

**Reference**
</dt> <dt>

[Core Packaging Interfaces](core-packaging-interfaces.md)
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> </dl>

 

 





