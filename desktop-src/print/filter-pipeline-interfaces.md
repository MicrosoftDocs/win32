---
Description: Filter Pipeline Interfaces
ms.assetid: 0f7ded7d-5b06-4ba8-9e32-6a0239d28262
title: Filter Pipeline Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Filter Pipeline Interfaces

The following interfaces are provided for XPS Printer Driver (XPSDrv) filter pipeline filters. These interfaces are defined in the Filterpipeline.idl file, which is included in the Windows Driver Kit (WDK).

For more information about XPSDrv, see [Microsoft XPS Printer Driver](https://www.bing.com/search?q=Microsoft XPS Printer Driver).

### Filter-Related Interfaces

<dl>

[IInterFilterCommunicator](iinterfiltercommunicator.md)  
[IPrintPipelinePropertyBag](iprintpipelinepropertybag.md)  
[IPrintPipelineProgressReport](iprintpipelineprogressreport.md)  
[IPrintPipelineManagerControl](iprintpipelinemanagercontrol.md)  
[IPrintPipelineFilter](iprintpipelinefilter.md)  
</dl>

### General Interfaces

<dl>

[IPrintClassObjectFactory](iprintclassobjectfactory.md)  
</dl>

### Raw Stream Interfaces

<dl>

[IPrintReadStream](iprintreadstream.md)  
[IPrintWriteStream](iprintwritestream.md)  
[IPrintReadStreamFactory](iprintreadstreamfactory.md)  
</dl>

### XPS-Specific Interfaces

<dl>

[IXpsDocumentProvider](ixpsdocumentprovider.md)  
[IXpsDocumentConsumer](ixpsdocumentconsumer.md)  
[IXpsDocument](ixpsdocument.md)  
[IFixedDocumentSequence](ifixeddocumentsequence.md)  
[IFixedDocument](ifixeddocument.md)  
[IFixedPage](ifixedpage.md)  
[IPartBase](ipartbase.md)  
[IPartImage](ipartimage.md)  
[IPartThumbnail](ipartthumbnail.md)  
[IPartFont](ipartfont.md)  
[IPartPrintTicket](ipartprintticket.md)  
[IPartDiscardControl](ipartdiscardcontrol.md)  
[IPartColorProfile](ipartcolorprofile.md)  
[IPartResourceDictionary](ipartresourcedictionary.md)  
[IXpsPartIterator](ixpspartiterator.md)  
</dl>

### Enumerations

<dl>

[**EXpsCompressionOptions**](expscompressionoptions.md)  
[**EXpsFontOptions**](expsfontoptions.md)  
[**EXpsJobConsumption**](expsjobconsumption.md)  
</dl>

> [!Note]  
> A Filter should call Release on every interface that it retrieves. For example, the output of the [**IXpsDocumentProvider::GetXpsPart**](ixpsdocumentprovider-getxpspart.md) method needs to be released when the filter is done using it. Also, you should free strings of type BSTR after you use them by using SysFreeString, which is described in the Microsoft Windows SDK. For example, when you obtain a BSTR string from GetUri, free it once you are done with it.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Filter%20Pipeline%20Interfaces%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



