---
description: This IXpsOMPrintTicketResource interface of the XPS Document API provides access to an existing print ticket and also the ability to create a print ticket in an XPS OM.
ms.assetid: 53c95da0-1601-4945-83a1-e3266d251aee
title: XPS OM Print Ticket Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# XPS OM Print Ticket Interfaces

This [**IXpsOMPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomprintticketresource) interface of the XPS Document API provides access to an existing print ticket and also the ability to create a print ticket in an XPS OM.

## Print Ticket Resources

The [**IXpsOMPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomprintticketresource) interface enables a program to read the contents of an existing print ticket by calling the **GetPrintTicketResource** method of an interface that supports a print ticket. New print ticket resources can be added to a document part by calling **SetPrintTicketResource**.

There are three print ticket levels, which specify the scope of the print ticket. The print ticket levels are: the job (or package) level, the document level, and the page level. The following table shows the relationship between the print ticket level, the corresponding XPS OM interface, and the methods used to access the print ticket resource.

| Print Ticket Level | Interface                                                | Get Method                                                                      | Set Method                                                                      |
|--------------------|----------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Job                | [**IXpsOMDocumentSequence**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence) | [**GetPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomdocumentsequence-getprintticketresource) | [**SetPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomdocumentsequence-setprintticketresource) |
| Document           | [**IXpsOMDocument**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocument)                 | [**GetPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomdocument-getprintticketresource)         | [**SetPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomdocument-setprintticketresource)         |
| Page               | [**IXpsOMPageReference**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereference)       | [**GetPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompagereference-getprintticketresource)    | [**SetPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompagereference-setprintticketresource)    |



 

## Print Ticket Content

The content of an existing print ticket resource can be accessed by reading from the stream associated with the resource. The [**GetStream**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomprintticketresource-getstream) method of the [**IXpsOMPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomprintticketresource) interface returns the pointer to a read-only stream that contains the XML-formatted contents of the print ticket. The format of the print ticket content is described in the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A new print ticket resource can be created by creating a new [**IXpsOMPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomprintticketresource) interface. A valid, XML-formatted print ticket is written to a stream and a part URI is created to identify the print ticket part. For more information about the content of a valid print ticket, refer to the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip). The stream and the part URI are passed as parameters of the [**SetContent**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomprintticketresource-setcontent) call to set the new print ticket resource and the print ticket resource is added to the corresponding document part by calling the **SetPrintTicketResource** method shown in the preceding table.

## Print Ticket Inheritance

Print tickets inherit the properties of print tickets with greater scope. For example, a document-level print ticket inherits the properties of the job-level print ticket that is associated with the document's document sequence. Likewise, a page-level print ticket inherits the properties of the document-level print ticket that is associated with the page's document. In this inheritance process, properties that are specified in the lower-level print ticket override the corresponding properties that would otherwise be inherited from the higher-level print ticket.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> <dt>

[**IXpsOMDocument**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocument)
</dt> <dt>

[**IXpsOMDocumentSequence**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence)
</dt> <dt>

[**IXpsOMPageReference**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereference)
</dt> <dt>

[**IXpsOMPrintTicketResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomprintticketresource)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

 



