---
title: Core Packaging Interfaces
description: Core Packaging Interfaces
ms.assetid: 62069595-0d1e-44e5-b68d-2bb0c355c565
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Core Packaging Interfaces

## 



| Core Packaging Interfaces                                                   |                                                                                                                                                                         |
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

 

 





