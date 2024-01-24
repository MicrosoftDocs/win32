---
description: ICE15 validates that content type and extension references in the MIME and Extension tables are reciprocal. The MIME table must reference a content type to an extension that the Extension table references back to the same content type.
ms.assetid: 8a38c8d2-324d-4de9-932b-d188ff5ccbaf
title: ICE15
ms.topic: article
ms.date: 05/31/2018
---

# ICE15

ICE15 validates that content type and extension references in the [MIME](mime-table.md) and [Extension](extension-table.md) tables are reciprocal. The MIME table must reference a content type to an extension that the Extension table references back to the same content type.

Multiple extensions can reference the same MIME type, as long as the MIME type references back to one of the extensions. Multiple MIME types can reference the same extension, as long as the extension references back to one of the MIME types.

Note that whenever a MIME references an extension, that extension cannot have the MIME\_ column in the Extension table set to Null.

## Result

ICE15 posts an error if the content type and extension references are not reciprocal.

## Example

ICE15 posts two error messages for the example shown:

-   The content type test/x-flaps in the MIME table references the extension tst, but the extension tst in the Extension table references flaps/x-flaps. This is not reciprocal.
-   The content type flaps/x-flaps references the extension flp, but that extension has a Null entry in the MIME\_ column of the Extension table.

[MIME Table](mime-table.md) (partial)



| ContentType   | Extension\_ |
|---------------|-------------|
| test/x-test   | tst         |
| flaps/x-flaps | flp         |



 

[Extension Table](extension-table.md) (partial)



| Extension | MIME\_        |
|-----------|---------------|
| tst       | flaps/x-flaps |
| flp       | Null          |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



