---
title: Formats object
description: Contains a collection of supported FormatID Constants that you can use when calling Transfer on an Item object, or ShowTransfer on a CommonDialog object for this Item object.
ms.assetid: '8181a20a-b178-4162-ad21-45573952b5a6'
keywords: ["Formats object WIA Automation", "Formats object WIA Automation , described"]
topic_type:
- apiref
api_name:
- Formats
api_location:
- Wiaaut.h
api_type:
- COM
---

# Formats object

Contains a collection of supported [**FormatID Constants**](-wiaaut-consts-formatid.md) that you can use when calling [**Transfer**](-wiaaut-iitem-transfer.md) on an [**Item**](-wiaaut-item.md) object, or [**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md) on a [**CommonDialog**](-wiaaut-commondialog.md) object for this **Item** object.

## Members

The **Formats** object has these types of members:

-   [Properties](#properties)

### Properties

The **Formats** object has these properties.



| Property                                                     | Access type          | Description                                                                       |
|:-------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------|
| [**Count (Formats)**](-wiaaut-iformats-count.md)<br/> | Read-only<br/> | Retrieves the number of members in the **Formats** collection.<br/>         |
| [**Item (Formats)**](-wiaaut-iformats-item.md)<br/>   | Read-only<br/> | Retrieves the specified item in the **Formats** collection by position<br/> |



 

## Remarks

Note that while the formats supported vary from one imaging device to the next, all imaging devices must support wiaFormatBMP.

For example code, see [List the Supported Transfer Formats](-wiaaut-shared-samples.md#list-the-supported-transfer-formats) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Formats (Item)**](-wiaaut-iitem-formats.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Formats (Item)**](-wiaaut-iitem-formats.md)
</dt> </dl>

 

 





