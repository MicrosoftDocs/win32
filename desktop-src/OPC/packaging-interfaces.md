---
title: Packaging Interfaces
description: A listing of Packaging API interfaces.
ms.assetid: 62069595-0d1e-44e5-b68d-2bb0c355c565
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Packaging Interfaces

A listing of Packaging API interfaces.

## Contents



| [Core Packaging Interfaces](core-packaging-interfaces.md)                  |                                                                                                                                                                         |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOpcFactory**](/windows/previous-versions/msopc/nn-msopc-iopcfactory?branch=master)<br/>                               | Creates Packaging API objects and provides support for saving and loading packages. <br/>                                                                         |
| [**IOpcPackage**](/windows/previous-versions/msopc/nn-msopc-iopcpackage?branch=master)<br/>                               | Represents a package and provides methods to access the package's parts and relationships. <br/>                                                                  |
| [**IOpcPart**](/windows/previous-versions/msopc/nn-msopc-iopcpart?branch=master)<br/>                                     | Represents a part that contains data and is not a Relationships part. <br/>                                                                                       |
| [**IOpcPartEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcpartenumerator?branch=master)<br/>                 | A read-only enumerator of [**IOpcPart**](/windows/previous-versions/msopc/nn-msopc-iopcpart?branch=master) interface pointers. <br/>                                                                                  |
| [**IOpcPartSet**](/windows/previous-versions/msopc/nn-msopc-iopcpartset?branch=master)<br/>                               | An unordered set of [**IOpcPart**](/windows/previous-versions/msopc/nn-msopc-iopcpart?branch=master) interface pointers to part objects that represent the parts in a package that are not Relationships parts. <br/> |
| [**IOpcPartUri**](/windows/previous-versions/msopc/nn-msopc-iopcparturi?branch=master)<br/>                               | Represents the part name of a part. <br/>                                                                                                                         |
| [**IOpcRelationship**](/windows/previous-versions/msopc/nn-msopc-iopcrelationship?branch=master)<br/>                     | Represents a relationship, which is a link between a source, which is a part or the package, and a target. <br/>                                                  |
| [**IOpcRelationshipEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipenumerator?branch=master)<br/> | A read-only enumerator of [**IOpcRelationship**](/windows/previous-versions/msopc/nn-msopc-iopcrelationship?branch=master) interface pointers. <br/>                                                                  |
| [**IOpcRelationshipSet**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipset?branch=master)<br/>               | Represents a Relationships part as an unordered set of [**IOpcRelationship**](/windows/previous-versions/msopc/nn-msopc-iopcrelationship?branch=master) interface pointers to relationship objects. <br/>             |
| [**IOpcUri**](/windows/previous-versions/msopc/nn-msopc-iopcuri?branch=master)<br/>                                       | Represents the URI of the package root or of a part that is relative to the package root. <br/>                                                                   |



 



| [Packaging Digital Signature Interfaces](packaging-digital-signature-interfaces.md)                 |                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOpcCertificateEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopccertificateenumerator?branch=master)<br/>                            | A read-only enumerator of pointers to [CERT\_CONTEXT](http://msdn.microsoft.com/library/aa377189(vs.85).aspx) structures. <br/>                                                                                   |
| [**IOpcCertificateSet**](/windows/previous-versions/msopc/nn-msopc-iopccertificateset?branch=master)<br/>                                          | An unordered set of certificates to be used with a signature.<br/>                                                                                                                                                      |
| [**IOpcDigitalSignature**](/windows/previous-versions/msopc/nn-msopc-iopcdigitalsignature?branch=master)<br/>                                      | Represents a package digital signature. <br/>                                                                                                                                                                           |
| [**IOpcDigitalSignatureEnumerator**](/windows/previous-versions/msopc/nn-msopc-iopcdigitalsignatureenumerator?branch=master)<br/>                  | A read-only enumerator of [**IOpcDigitalSignature**](/windows/previous-versions/msopc/nn-msopc-iopcdigitalsignature?branch=master) interface pointers.<br/>                                                                                                                 |
| [**IOpcDigitalSignatureManager**](/windows/previous-versions/msopc/nn-msopc-iopcdigitalsignaturemanager?branch=master)<br/>                        | Provides access to [Packaging Digital Signature Interfaces](packaging-digital-signature-interfaces.md) for a package that is represented by Packaging API objects. <br/>                                               |
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

[Packaging API Reference](packaging-programming-reference.md)
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

[Packaging Digital Signature Interfaces](packaging-digital-signature-interfaces.md)
</dt> <dt>

[Packaging Enumerations](packaging-enumerations.md)
</dt> <dt>

[Packaging Errors](packaging-errors.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> </dl>

 

 





