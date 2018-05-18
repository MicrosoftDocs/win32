---
Description: 'This topic describes how to send a fax using the fax client Component Object Model (COM) implementation.'
ms.assetid: '792004d1-683f-4d4d-afed-48b4701ed454'
title: 'Sending a Fax to One Recipient (COM Implementation)'
---

# Sending a Fax to One Recipient (COM Implementation)

The [**IFaxDoc::FileName Property**](-mfax-ifaxdoc-mfax-ifaxdoc-get-filename-cpp.md) is required to send a fax transmission if you are using the fax client Component Object Model (COM) implementation. The [**IFaxDoc::FaxNumber Property**](-mfax-ifaxdoc-mfax-ifaxdoc-get-faxnumber-cpp.md) is also required. When you transmit a fax you can specify other optional properties such as cover page settings, fax recipient and sender information, and other data that appears only on the cover page. For more information, see [Sending a Cover Page](-mfax-sending-a-cover-page.md).

If you are writing a C/C++ application, after you create a connection to an active fax server, call the [**IFaxServer::CreateDocument**](-mfax-ifaxserver-client-mfax-ifaxserver-createdocument-cpp.md) method to create a [FaxDoc](-mfax-faxdoc.md) object. Call multiple [**IFaxDoc**](-mfax-ifaxdoc.md) interface methods to set required and optional properties of the object. To transmit the file, call the [**IFaxDoc::Send**](-mfax-ifaxdoc-mfax-ifaxdoc-send-cpp.md) method. For more information about the steps required to create a FaxDoc object, and for a list of properties and methods, see [**IFaxDoc**](-mfax-ifaxdoc.md).

If you are writing a Microsoft Visual Basic application, call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer**](-mfax-faxserver.md) object. Then call the [**CreateDocument**](-mfax-ifaxserver-client-mfax-ifaxserver-createdocument-cpp.md) method of the **FaxServer** object to create a [FaxDoc](-mfax-faxdoc.md) object. Set required and optional properties of the FaxDoc object. To transmit the file, call the [**Send**](-mfax-ifaxdoc-mfax-ifaxdoc-send-cpp.md) method of the FaxDoc object. See [**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md)) for more information about the steps required to create the object, and for a list of properties and methods of the object.

## Related topics

<dl> <dt>

[Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md)
</dt> </dl>

 

 



