---
Description: 'A FaxTiff object represents a Tagged Image File Format Class F (TIFF Class F) file that the fax service has transmitted or received.'
ms.assetid: '98d385be-cebb-428e-92f7-22a1fc814c3c'
title: FaxTiff object
---

# FaxTiff object

A **FaxTiff** object represents a Tagged Image File Format Class F (TIFF Class F) file that the fax service has transmitted or received. The fax service embeds custom Tagged Image File Format (TIFF) tags in the file to store information about the fax transmission.

You do not need to be familiar with the structure of a TIFF file to access the attributes of a **FaxTiff** object. This object provides a convenient alternative to manually parsing the TIFF data in a fax file. The **FaxTiff** object has the following properties:

-   A property to return or set the name of the fax file described by the **FaxTiff** object.
-   Properties to return other attributes of the **FaxTiff** object, such as device and station identifiers, the fax number, and sender and recipient names.

> [!Note]  
> A fax client application must set the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property before retrieving another property for a **FaxTiff** object.

 

## Members

The **FaxTiff** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxTiff** object has these properties.



| Property                                                                    | Access type           | Description                                                                                                                                                                                                                                                                                                                                                            |
|:----------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallerId**](-mfax-ifaxtiff-get-callerid-vb.md)<br/>               | Read-only<br/>  | Retrieves the [**CallerId**](-mfax-ifaxtiff-get-callerid-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **CallerId** property is a string that identifies the calling device that sent a specified fax file.<br/>                                                                                                                               |
| [**Csid**](-mfax-ifaxtiff-get-csid-vb.md)<br/>                       | Read-only<br/>  | Retrieves the [**Csid**](-mfax-ifaxtiff-get-csid-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **Csid** property is a string that contains CSID information, which is typically the fax number of the device that received the specified fax file.<br/>                                                                                        |
| [**Image**](-mfax-ifaxtiff-get-image-vb.md)<br/>                     | Read/write<br/> | Sets or retrieves the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **Image** property is a null-terminated string that contains the full path and file name of the file represented by the FaxTiff object. The file is a TIFF Class F file.<br/>                                                         |
| [**RawReceiveTime**](-mfax-ifaxtiff-get-rawreceivetime-vb.md)<br/>   | Read-only<br/>  | Retrieves the [**RawReceiveTime**](-mfax-ifaxtiff-get-rawreceivetime-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **RawReceiveTime** property is the time at which reception began for an inbound fax file, expressed in UTC. This property can also be the time at which reception or transmission began for an archived file.<br/>          |
| [**ReceiveTime**](-mfax-ifaxtiff-get-receivetime-vb.md)<br/>         | Read-only<br/>  | Retrieves the [**ReceiveTime**](-mfax-ifaxtiff-get-receivetime-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **ReceiveTime** property is a null-terminated string that contains the time at which reception began for an inbound fax file. The string can contain the time at which reception or transmission began for an archived file.<br/> |
| [**RecipientName**](-mfax-ifaxtiff-get-recipientname-vb.md)<br/>     | Read-only<br/>  | Retrieves the [**RecipientName**](-mfax-ifaxtiff-get-recipientname-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **RecipientName** property is a null-terminated string that contains the name of the recipient for the specified fax file.<br/>                                                                                               |
| [**RecipientNumber**](-mfax-ifaxtiff-get-recipientnumber-vb.md)<br/> | Read-only<br/>  | Retrieves the [**RecipientNumber**](-mfax-ifaxtiff-get-recipientnumber-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **RecipientNumber** property is a null-terminated string that contains the fax number to which a fax was transmitted.<br/>                                                                                                |
| [**Routing**](-mfax-ifaxtiff-get-routing-vb.md)<br/>                 | Read-only<br/>  | Retrieves the [**Routing**](-mfax-ifaxtiff-get-routing-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **Routing** property is a null-terminated string that contains the inbound routing string for a specified fax file.<br/>                                                                                                                  |
| [**SenderName**](-mfax-ifaxtiff-get-sendername-vb.md)<br/>           | Read-only<br/>  | Retrieves the [**SenderName**](-mfax-ifaxtiff-get-sendername-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **SenderName** property is a null-terminated string that contains the name of the user who queued the fax transmission.<br/>                                                                                                        |
| [**TiffTagString**](-mfax-ifaxtiff-get-tifftagstring-vb.md)<br/>     | Read/write<br/> | Retrieves the [**TiffTagString**](-mfax-ifaxtiff-get-tifftagstring-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **TiffTagString** property is a null-terminated string that contains the value of a specified TIFF tag (field).<br/>                                                                                                          |
| [**Tsid**](-mfax-ifaxtiff-get-tsid-vb.md)<br/>                       | Read-only<br/>  | Retrieves the [**Tsid**](-mfax-ifaxtiff-get-tsid-vb.md) property for a [FaxTiff](-mfax-faxtiff.md) object. The **Tsid** property is a null-terminated string that contains TSID information, which is typically the fax number of the device that sent the specified fax file.<br/>                                                                            |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Microsoft Visual Basic Object Browser to view the **FaxTiff** object's type library information in Visual Basic syntax.

To create a **FaxTiff** object, call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function as illustrated in the following sample:


```
Dim FaxTiff as Object
Set FaxTiff = CreateObject("FaxTiff.FaxTiff")
```



## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




