---
title: Packaging Interfaces
description: A listing of Packaging API interfaces.
ms.assetid: '62069595-0d1e-44e5-b68d-2bb0c355c565'
---

# Packaging Interfaces

A listing of Packaging API interfaces.

## Contents



| [Core Packaging Interfaces](core-packaging-interfaces.md)                  |                                                                                                                                                                         |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOpcFactory**](iopcfactory.md)<br/>                               | Creates Packaging API objects and provides support for saving and loading packages. <br/>                                                                         |
| [**IOpcPackage**](iopcpackage.md)<br/>                               | Represents a package and provides methods to access the package's parts and relationships. <br/>                                                                  |
| [**IOpcPart**](iopcpart.md)<br/>                                     | Represents a part that contains data and is not a Relationships part. <br/>                                                                                       |
| [**IOpcPartEnumerator**](iopcpartenumerator.md)<br/>                 | A read-only enumerator of [**IOpcPart**](iopcpart.md) interface pointers. <br/>                                                                                  |
| [**IOpcPartSet**](iopcpartset.md)<br/>                               | An unordered set of [**IOpcPart**](iopcpart.md) interface pointers to part objects that represent the parts in a package that are not Relationships parts. <br/> |
| [**IOpcPartUri**](iopcparturi.md)<br/>                               | Represents the part name of a part. <br/>                                                                                                                         |
| [**IOpcRelationship**](iopcrelationship.md)<br/>                     | Represents a relationship, which is a link between a source, which is a part or the package, and a target. <br/>                                                  |
| [**IOpcRelationshipEnumerator**](iopcrelationshipenumerator.md)<br/> | A read-only enumerator of [**IOpcRelationship**](iopcrelationship.md) interface pointers. <br/>                                                                  |
| [**IOpcRelationshipSet**](iopcrelationshipset.md)<br/>               | Represents a Relationships part as an unordered set of [**IOpcRelationship**](iopcrelationship.md) interface pointers to relationship objects. <br/>             |
| [**IOpcUri**](iopcuri.md)<br/>                                       | Represents the URI of the package root or of a part that is relative to the package root. <br/>                                                                   |



 



| [Packaging Digital Signature Interfaces](packaging-digital-signature-interfaces.md)                 |                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOpcCertificateEnumerator**](iopccertificateenumerator.md)<br/>                            | A read-only enumerator of pointers to [CERT\_CONTEXT](http://msdn.microsoft.com/library/aa377189(vs.85).aspx) structures. <br/>                                                                                   |
| [**IOpcCertificateSet**](iopccertificateset.md)<br/>                                          | An unordered set of certificates to be used with a signature.<br/>                                                                                                                                                      |
| [**IOpcDigitalSignature**](iopcdigitalsignature.md)<br/>                                      | Represents a package digital signature. <br/>                                                                                                                                                                           |
| [**IOpcDigitalSignatureEnumerator**](iopcdigitalsignatureenumerator.md)<br/>                  | A read-only enumerator of [**IOpcDigitalSignature**](iopcdigitalsignature.md) interface pointers.<br/>                                                                                                                 |
| [**IOpcDigitalSignatureManager**](iopcdigitalsignaturemanager.md)<br/>                        | Provides access to [Packaging Digital Signature Interfaces](packaging-digital-signature-interfaces.md) for a package that is represented by Packaging API objects. <br/>                                               |
| [**IOpcRelationshipSelector**](iopcrelationshipselector.md)<br/>                              | Represents how to select, from a Relationships part, the relationships to be referenced for signing. <br/>                                                                                                              |
| [**IOpcRelationshipSelectorEnumerator**](iopcrelationshipselectorenumerator.md)<br/>          | A read-only enumerator of [**IOpcRelationshipSelector**](iopcrelationshipselector.md) interface pointers. <br/>                                                                                                        |
| [**IOpcRelationshipSelectorSet**](iopcrelationshipselectorset.md)<br/>                        | An unordered set of [**IOpcRelationshipSelector**](iopcrelationshipselector.md) interface pointers that represent the selection criteria that is used to identify relationships for signing. <br/>                     |
| [**IOpcSignatureCustomObject**](iopcsignaturecustomobject.md)<br/>                            | Represents an application-specific **Object** element that has been or will be signed. <br/>                                                                                                                            |
| [**IOpcSignatureCustomObjectEnumerator**](iopcsignaturecustomobjectenumerator.md)<br/>        | A read-only enumerator of [**IOpcSignatureCustomObject**](iopcsignaturecustomobject.md) interface pointers. <br/>                                                                                                      |
| [**IOpcSignatureCustomObjectSet**](iopcsignaturecustomobjectset.md)<br/>                      | An unordered set of [**IOpcSignatureCustomObject**](iopcsignaturecustomobject.md) interface pointers that contain the XML markup of application-specific **Object** elements. <br/>                                    |
| [**IOpcSignaturePartReference**](iopcsignaturepartreference.md)<br/>                          | Represents a reference to a part that has been or will be signed. <br/>                                                                                                                                                 |
| [**IOpcSignaturePartReferenceEnumerator**](iopcsignaturepartreferenceenumerator.md)                 | A read-only enumerator of [**IOpcSignaturePartReference**](iopcsignaturepartreference.md) interface pointers.<br/>                                                                                                     |
| [**IOpcSignaturePartReferenceSet**](iopcsignaturepartreferenceset.md)<br/>                    | An unordered set of [**IOpcSignaturePartReference**](iopcsignaturepartreference.md) interface pointers that represent references to parts to be signed. <br/>                                                          |
| [**IOpcSignatureReference**](iopcsignaturereference.md)<br/>                                  | Represents a reference to XML markup that has been or will be signed. <br/>                                                                                                                                             |
| [**IOpcSignatureReferenceEnumerator**](iopcsignaturereferenceenumerator.md)                         | A read-only enumerator of [**IOpcSignatureReference**](iopcsignaturereference.md) interface pointers.<br/>                                                                                                             |
| [**IOpcSignatureReferenceSet**](iopcsignaturereferenceset.md)<br/>                            | An unordered set of [**IOpcSignatureReference**](iopcsignaturereference.md) interface pointers that represent references to XML elements to be signed. <br/>                                                           |
| [**IOpcSignatureRelationshipReference**](iopcsignaturerelationshipreference.md)<br/>          | Represents a reference to a Relationships part that contains relationships that have been or will be signed. <br/>                                                                                                      |
| [**IOpcSignatureRelationshipReferenceEnumerator**](iopcsignaturerelationshipreferenceenumerator.md) | A read-only enumerator of [**IOpcSignatureRelationshipReference**](iopcsignaturerelationshipreference.md) interface pointers.<br/>                                                                                     |
| [**IOpcSignatureRelationshipReferenceSet**](iopcsignaturerelationshipreferenceset.md)<br/>    | An unordered set of [**IOpcSignatureRelationshipReference**](iopcsignaturerelationshipreference.md) interface pointers that represent references to Relationships parts that contain relationships to be signed. <br/> |
| [**IOpcSigningOptions**](iopcsigningoptions.md)<br/>                                          | Provides methods to set and access information required to generate a signature.<br/>                                                                                                                                   |



 

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

 

 





