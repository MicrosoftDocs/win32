---
description: ICE39 validates the Summary Information Stream of the database.
ms.assetid: 9de72de6-fd9c-4d94-92f7-61b85dff0f6a
title: ICE39
ms.topic: article
ms.date: 05/31/2018
---

# ICE39

ICE39 validates the [Summary Information Stream](summary-information-stream.md) of the database.

ICE39 checks the format of the following properties:

-   [**Word Count Summary**](word-count-summary.md)
-   [**Page Count Summary**](page-count-summary.md)
-   [**Template Summary**](template-summary.md)
-   [**Revision Number Summary**](revision-number-summary.md)
-   [**Create Time/Date Summary**](create-time-date-summary.md)
-   [**Last Saved Time/Date Summary**](last-saved-time-date-summary.md)
-   [**Last Printed Summary**](last-printed-summary.md)

If the [**Word Count Summary**](word-count-summary.md) Property specifies that the source is compressed, ICE39 posts a warning if any files are also marked as compressed in the Attributes column of the [File table](file-table.md). See [Using Cabinets and Compressed Sources](using-cabinets-and-compressed-sources.md).

ICE39 posts a warning if the [**Word Count Summary**](word-count-summary.md) Property specifies that the package is UAC compliant and the [MsiPackageCertificate Table](msipackagecertificate-table.md) is not empty.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



