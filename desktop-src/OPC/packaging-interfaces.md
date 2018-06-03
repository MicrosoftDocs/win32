---
title: Packaging Interfaces
description: A listing of Packaging API interfaces.
ms.assetid: 62069595-0d1e-44e5-b68d-2bb0c355c565
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Packaging Interfaces

A listing of Packaging API interfaces.

## Contents



| [Core Packaging Interfaces](core-packaging-interfaces.md)                  |                                                                                                                                                                         |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOpcFactory**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcfactory)<br/>                               | Creates Packaging API objects and provides support for saving and loading packages. <br/>                                                                         |
| [**IOpcPackage**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpackage)<br/>                               | Represents a package and provides methods to access the package's parts and relationships. <br/>                                                                  |
| [**IOpcPart**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpart)<br/>                                     | Represents a part that contains data and is not a Relationships part. <br/>                                                                                       |
| [**IOpcPartEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpartenumerator)<br/>                 | A read-only enumerator of [**IOpcPart**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpart) interface pointers. <br/>                                                                                  |
| [**IOpcPartSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpartset)<br/>                               | An unordered set of [**IOpcPart**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpart) interface pointers to part objects that represent the parts in a package that are not Relationships parts. <br/> |
| [**IOpcPartUri**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcparturi)<br/>                               | Represents the part name of a part. <br/>                                                                                                                         |
| [**IOpcRelationship**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationship)<br/>                     | Represents a relationship, which is a link between a source, which is a part or the package, and a target. <br/>                                                  |
| [**IOpcRelationshipEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationshipenumerator)<br/> | A read-only enumerator of [**IOpcRelationship**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationship) interface pointers. <br/>                                                                  |
| [**IOpcRelationshipSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationshipset)<br/>               | Represents a Relationships part as an unordered set of [**IOpcRelationship**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationship) interface pointers to relationship objects. <br/>             |
| [**IOpcUri**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcuri)<br/>                                       | Represents the URI of the package root or of a part that is relative to the package root. <br/>                                                                   |



 



| [Packaging Digital Signature Interfaces](packaging-digital-signature-interfaces.md)                 |                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOpcCertificateEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopccertificateenumerator)<br/>                            | A read-only enumerator of pointers to [CERT\_CONTEXT](http://msdn.microsoft.com/library/aa377189(vs.85).aspx) structures. <br/>                                                                                   |
| [**IOpcCertificateSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopccertificateset)<br/>                                          | An unordered set of certificates to be used with a signature.<br/>                                                                                                                                                      |
| [**IOpcDigitalSignature**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcdigitalsignature)<br/>                                      | Represents a package digital signature. <br/>                                                                                                                                                                           |
| [**IOpcDigitalSignatureEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcdigitalsignatureenumerator)<br/>                  | A read-only enumerator of [**IOpcDigitalSignature**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcdigitalsignature) interface pointers.<br/>                                                                                                                 |
| [**IOpcDigitalSignatureManager**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcdigitalsignaturemanager)<br/>                        | Provides access to [Packaging Digital Signature Interfaces](packaging-digital-signature-interfaces.md) for a package that is represented by Packaging API objects. <br/>                                               |
| [**IOpcRelationshipSelector**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationshipselector)<br/>                              | Represents how to select, from a Relationships part, the relationships to be referenced for signing. <br/>                                                                                                              |
| [**IOpcRelationshipSelectorEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationshipselectorenumerator)<br/>          | A read-only enumerator of [**IOpcRelationshipSelector**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationshipselector) interface pointers. <br/>                                                                                                        |
| [**IOpcRelationshipSelectorSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationshipselectorset)<br/>                        | An unordered set of [**IOpcRelationshipSelector**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationshipselector) interface pointers that represent the selection criteria that is used to identify relationships for signing. <br/>                     |
| [**IOpcSignatureCustomObject**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturecustomobject)<br/>                            | Represents an application-specific **Object** element that has been or will be signed. <br/>                                                                                                                            |
| [**IOpcSignatureCustomObjectEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturecustomobjectenumerator)<br/>        | A read-only enumerator of [**IOpcSignatureCustomObject**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturecustomobject) interface pointers. <br/>                                                                                                      |
| [**IOpcSignatureCustomObjectSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturecustomobjectset)<br/>                      | An unordered set of [**IOpcSignatureCustomObject**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturecustomobject) interface pointers that contain the XML markup of application-specific **Object** elements. <br/>                                    |
| [**IOpcSignaturePartReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturepartreference)<br/>                          | Represents a reference to a part that has been or will be signed. <br/>                                                                                                                                                 |
| [**IOpcSignaturePartReferenceEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturepartreferenceenumerator)                 | A read-only enumerator of [**IOpcSignaturePartReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturepartreference) interface pointers.<br/>                                                                                                     |
| [**IOpcSignaturePartReferenceSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturepartreferenceset)<br/>                    | An unordered set of [**IOpcSignaturePartReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturepartreference) interface pointers that represent references to parts to be signed. <br/>                                                          |
| [**IOpcSignatureReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturereference)<br/>                                  | Represents a reference to XML markup that has been or will be signed. <br/>                                                                                                                                             |
| [**IOpcSignatureReferenceEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturereferenceenumerator)                         | A read-only enumerator of [**IOpcSignatureReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturereference) interface pointers.<br/>                                                                                                             |
| [**IOpcSignatureReferenceSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturereferenceset)<br/>                            | An unordered set of [**IOpcSignatureReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturereference) interface pointers that represent references to XML elements to be signed. <br/>                                                           |
| [**IOpcSignatureRelationshipReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturerelationshipreference)<br/>          | Represents a reference to a Relationships part that contains relationships that have been or will be signed. <br/>                                                                                                      |
| [**IOpcSignatureRelationshipReferenceEnumerator**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturerelationshipreferenceenumerator) | A read-only enumerator of [**IOpcSignatureRelationshipReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturerelationshipreference) interface pointers.<br/>                                                                                     |
| [**IOpcSignatureRelationshipReferenceSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturerelationshipreferenceset)<br/>    | An unordered set of [**IOpcSignatureRelationshipReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturerelationshipreference) interface pointers that represent references to Relationships parts that contain relationships to be signed. <br/> |
| [**IOpcSigningOptions**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsigningoptions)<br/>                                          | Provides methods to set and access information required to generate a signature.<br/>                                                                                                                                   |



 

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

 

 





