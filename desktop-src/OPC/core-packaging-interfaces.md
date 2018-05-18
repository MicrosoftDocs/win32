---
title: Core Packaging Interfaces
description: Core Packaging Interfaces
ms.assetid: '62069595-0d1e-44e5-b68d-2bb0c355c565'
---

# Core Packaging Interfaces

## 



| Core Packaging Interfaces                                                   |                                                                                                                                                                         |
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

[Packaging Digital Signature Interfaces](packaging-digital-signature-interfaces.md)
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> </dl>

 

 





