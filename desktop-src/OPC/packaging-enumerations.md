---
title: Packaging Enumerations
description: A listing of Packaging API enumerations.
ms.assetid: c84246dd-f34b-40ea-8530-f93483445533
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Packaging Enumerations

A listing of Packaging API enumerations.

## Contents



|                                                                                            |                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OPC\_CANONICALIZATION\_METHOD**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0001)<br/>            | Describes the canonicalization method to be applied to XML markup. <br/>                                                                                                                                                                                       |
| [**OPC\_CERTIFICATE\_EMBEDDING\_OPTION**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0004)<br/> | Describes the storage location of a certificate that is used in signing.<br/>                                                                                                                                                                                  |
| [**OPC\_COMPRESSION\_OPTIONS**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0002)<br/>                    | Describes ways to compress part content. <br/>                                                                                                                                                                                                                 |
| [**OPC\_READ\_FLAGS**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0004)<br/>                                      | Describes the read settings for caching package components and validating them against *ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC)* conformance requirements. <br/>                                                               |
| [**OPC\_RELATIONSHIP\_SELECTOR**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0002)<br/>                | Describes how to interpret the *selectionCriterion* parameter of the [**IOpcRelationshipSelector::GetSelectionCriterion**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcrelationshipselector-getselectioncriterion) method. <br/>                                                                   |
| [**OPC\_RELATIONSHIPS\_SIGNING\_OPTION**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0003)<br/> | Describes whether a reference represented by the [**IOpcSignatureRelationshipReference**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcsignaturerelationshipreference) interface refers to all or a subset of relationships represented as relationship objects in a relationship set object. <br/> |
| [**OPC\_SIGNATURE\_TIME\_FORMAT**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0001_0076_0005)<br/>               | Describes how to interpret the *signingTime* parameter, which is a record of when a signature was created, of the [**IOpcDigitalSignature::GetSigningTime**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcdigitalsignature-getsigningtime) method. <br/>                                            |
| [**OPC\_SIGNATURE\_VALIDATION\_RESULT**](/previous-versions/windows/desktop/api/msopc/ne-msopc-opc_signature_validation_result)<br/>   | Indicates the status of the signature.<br/>                                                                                                                                                                                                                    |
| [**OPC\_STREAM\_IO\_MODE**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0003)<br/>                             | Describes the read/write status of a stream.<br/>                                                                                                                                                                                                              |
| [**OPC\_URI\_TARGET\_MODE**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0001)<br/>                           | Indicates the target mode of a relationship. <br/>                                                                                                                                                                                                             |
| [**OPC\_WRITE\_FLAGS**](/previous-versions/windows/desktop/api/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0005)<br/>                                    | Describes the encoding method that is used by the serialization object to produce the package. <br/>                                                                                                                                                           |



 

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

 

 





