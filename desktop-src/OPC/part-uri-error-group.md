---
title: Part URI Error Group
description: When you use methods that process IOpcPartUri interfaces or take IOpcPartUri as an input parameter, the following error codes may be returned.
ms.assetid: 877447bb-d4e1-4277-b8ce-cb7a31a33fe0
topic_type:
- apiref
api_name:
- Part URI Error Group
api_location:
- Msopc.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Part URI Error Group

When you use methods that process [**IOpcPartUri**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcparturi) interfaces or take **IOpcPartUri** as an input parameter, the following error codes may be returned.



| Return code/value                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="OPC_E_NONCONFORMING_URI"></span><span id="opc_e_nonconforming_uri"></span><dl> <dt>**OPC\_E\_NONCONFORMING\_URI**</dt> <dt>0x80510001</dt> </dl>                          | The part name does not conform to the rules specified in the *OPC* standards.<br/>                                                                                                                             |
| <span id="OPC_E_RELATIONSHIP_URI_REQUIRED"></span><span id="opc_e_relationship_uri_required"></span><dl> <dt>**OPC\_E\_RELATIONSHIP\_URI\_REQUIRED**</dt> <dt>0x80510003</dt> </dl> | The part name of a Relationships part is required, but the part name is not that of a Relationships part.<br/> For more information about the part names of Relationships parts, see the *OPC*.<br/>     |
| <span id="OPC_E_RELATIVE_URI_REQUIRED"></span><span id="opc_e_relative_uri_required"></span><dl> <dt>**OPC\_E\_RELATIVE\_URI\_REQUIRED**</dt> <dt>0x80510002</dt> </dl>             | A part name cannot be an absolute URI. An absolute URI begins with a schema component followed by a ":", as described in [RFC 3986: URI Generic Syntax](http://go.microsoft.com/fwlink/p/?linkid=143950).<br/> |



 

## Remarks

For more information about error handling in COM, see the [Error Handling (COM)](https://www.bing.com/search?q=Error Handling (COM)) topic.

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Msopc.h</dt> </dl> |



## See also

<dl> <dt>

[Packaging Errors](packaging-errors.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Packaging API Programming Guide](packaging-programming-guide.md)
</dt> <dt>

**Reference**
</dt> <dt>

[Package Consumption Error Group](package-consumption-error-group.md)
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> <dt>

**External Resources**
</dt> <dt>

[ECMA-376 OpenXML standard](http://go.microsoft.com/fwlink/p/?linkid=123375)
</dt> <dt>

[RFC 3986: URI Generic Syntax](http://go.microsoft.com/fwlink/p/?linkid=143950)
</dt> </dl>

 

 





