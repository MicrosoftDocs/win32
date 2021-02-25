---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: f1b94241-5376-423f-b10a-336dc47f3d59
title: Note to GPD Authors
ms.topic: article
ms.date: 05/31/2018
---

# Note to GPD Authors

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

For those authors of PrintCapabilities documents who are familiar with GPD files, some GPD keywords have no equivalents in the PrintCapabilities document. The following table contains the GPD keywords without a PrintCapabilities document equivalent, and the reason there is no equivalent.



| GPD keyword                                                                            | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \*Constraints<br/> \*InvalidCombination<br/> \*ConflictPriority<br/> | Constraints are not defined in the PrintCapabilities document because PrintCapabilities clients are not expected to process, enforce, or resolve them. These tasks are left for the PrintTicket provider to perform during PrintTicket validation. Unidrv plug-ins can provide their own PrintTicket validation code, or they can rely on Unidrv to carry out this validation. In the latter case, Unidrv enforces any constraints defined in the GPD file.<br/> Monolithic drivers must provide their own PrintTicket validation code, and must provide their own method of expressing and enforcing constraints.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \*DefaultOption<br/>                                                             | There is a PrintTicket method that returns a default PrintTicket, which by definition has all the default settings for each Feature.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \*FeatureType<br/>                                                               | A Feature can be divided into three different categories:<br/> A Feature whose settings are defined in a PrintTicket. This type of Feature is called document-sticky because these settings directly determine the manner in which a document is processed.<br/> A Feature whose settings reflect physical device attributes that are not user controlled, such as the amount of memory in the device, or that indicate the presence of optional add-ons such as paper feeders or duplexers. This type of Feature is called device-sticky or printer-sticky. The state of this type of Feature is important because it can constrain an Option belonging to a document-sticky Feature.<br/> A device-sticky or printer-sticky Feature can be further categorized as either a user interface (UI) printer-sticky Feature or an auto printer-sticky Feature. A UI printer-sticky Feature must be displayed in a user interface that an administrator can set. The device automatically detects an auto printer-sticky Feature.<br/> |
| \*Switch ... \*Case<br/>                                                         | A PrintCapabilities provider must implement a method that creates a PrintCapabilities document that enumerates either printer-sticky or document-sticky Features, depending on the type specified by the caller. For this reason there is no need to present the same information through the PrintCapabilities document itself.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




