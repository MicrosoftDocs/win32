---
title: Packaging Enumerations
description: A listing of Packaging API enumerations.
ms.assetid: c84246dd-f34b-40ea-8530-f93483445533
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Packaging Enumerations

A listing of Packaging API enumerations.

## Contents



|                                                                                            |                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OPC\_CANONICALIZATION\_METHOD**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0001?branch=master)<br/>            | Describes the canonicalization method to be applied to XML markup. <br/>                                                                                                                                                                                       |
| [**OPC\_CERTIFICATE\_EMBEDDING\_OPTION**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0004?branch=master)<br/> | Describes the storage location of a certificate that is used in signing.<br/>                                                                                                                                                                                  |
| [**OPC\_COMPRESSION\_OPTIONS**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0002?branch=master)<br/>                    | Describes ways to compress part content. <br/>                                                                                                                                                                                                                 |
| [**OPC\_READ\_FLAGS**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0004?branch=master)<br/>                                      | Describes the read settings for caching package components and validating them against *ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC)* conformance requirements. <br/>                                                               |
| [**OPC\_RELATIONSHIP\_SELECTOR**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0002?branch=master)<br/>                | Describes how to interpret the *selectionCriterion* parameter of the [**IOpcRelationshipSelector::GetSelectionCriterion**](/windows/previous-versions/msopc/nf-msopc-iopcrelationshipselector-getselectioncriterion?branch=master) method. <br/>                                                                   |
| [**OPC\_RELATIONSHIPS\_SIGNING\_OPTION**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0003?branch=master)<br/> | Describes whether a reference represented by the [**IOpcSignatureRelationshipReference**](/windows/previous-versions/msopc/nn-msopc-iopcsignaturerelationshipreference?branch=master) interface refers to all or a subset of relationships represented as relationship objects in a relationship set object. <br/> |
| [**OPC\_SIGNATURE\_TIME\_FORMAT**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0005?branch=master)<br/>               | Describes how to interpret the *signingTime* parameter, which is a record of when a signature was created, of the [**IOpcDigitalSignature::GetSigningTime**](/windows/previous-versions/msopc/nf-msopc-iopcdigitalsignature-getsigningtime?branch=master) method. <br/>                                            |
| [**OPC\_SIGNATURE\_VALIDATION\_RESULT**](/windows/previous-versions/msopc/ne-msopc-opc_signature_validation_result?branch=master)<br/>   | Indicates the status of the signature.<br/>                                                                                                                                                                                                                    |
| [**OPC\_STREAM\_IO\_MODE**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0003?branch=master)<br/>                             | Describes the read/write status of a stream.<br/>                                                                                                                                                                                                              |
| [**OPC\_URI\_TARGET\_MODE**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0001?branch=master)<br/>                           | Indicates the target mode of a relationship. <br/>                                                                                                                                                                                                             |
| [**OPC\_WRITE\_FLAGS**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0005?branch=master)<br/>                                    | Describes the encoding method that is used by the serialization object to produce the package. <br/>                                                                                                                                                           |



 

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

[Packaging Errors](packaging-errors.md)
</dt> <dt>

[Packaging Interfaces](packaging-interfaces.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> </dl>

 

 





