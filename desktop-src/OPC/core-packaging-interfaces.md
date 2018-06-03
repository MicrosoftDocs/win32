---
title: Core Packaging Interfaces
description: Core Packaging Interfaces
ms.assetid: 62069595-0d1e-44e5-b68d-2bb0c355c565
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Core Packaging Interfaces

## 



| Core Packaging Interfaces                                                   |                                                                                                                                                                         |
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

 

 





