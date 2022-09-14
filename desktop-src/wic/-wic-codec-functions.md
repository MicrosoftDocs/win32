---
title: WIC functions
description: This section contains information about the Windows Imaging Component (WIC) functions.
ms.assetid: 6f948df6-5b70-4f1e-b01d-3841d7819acb
ms.topic: article
ms.date: 05/31/2018
---

# WIC functions

This section contains information about the Windows Imaging Component (WIC) functions.

## In this section



| Topic                                                                                      | Description                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*ProgressNotificationCallback*](/windows/desktop/api/Wincodec/nc-wincodec-pfnprogressnotification)<br/>   | Application defined callback function called when codec component progress is made.<br/>                                                                                                                        |
| [**WICConvertBitmapSource**](/windows/desktop/api/Wincodec/nf-wincodec-wicconvertbitmapsource)<br/>             | Obtains a [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) in the desired pixel format from a given **IWICBitmapSource**.<br/>                                                                           |
| [**WICCreateBitmapFromSection**](/windows/desktop/api/Wincodec/nf-wincodec-wiccreatebitmapfromsection)<br/>     | Returns a [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) that is backed by the pixels of a Windows Graphics Device Interface (GDI) section handle.<br/>                                                |
| [**WICCreateBitmapFromSectionEx**](/windows/desktop/api/Wincodec/nf-wincodec-wiccreatebitmapfromsectionex)<br/> | Returns a [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) that is backed by the pixels of a GDI section handle.<br/>                                                                                    |
| [**WICGetMetadataContentSize**](/windows/desktop/api/wincodecsdk/nf-wincodecsdk-wicgetmetadatacontentsize)<br/>       | Returns the size of the metadata content contained by the specified [**IWICMetadataWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatawriter). The returned size accounts for the header and the length of the metadata.<br/> |
| [**WICMapGuidToShortName**](/windows/desktop/api/WinCodec/nf-wincodec-wicmapguidtoshortname)<br/>               | Obtains the short name associated with a given GUID.<br/>                                                                                                                                                       |
| [**WICMapSchemaToName**](/windows/desktop/api/Wincodec/nf-wincodec-wicmapschematoname)<br/>                     | Obtains the name associated with a given schema.<br/>                                                                                                                                                           |
| [**WICMapShortNameToGuid**](/windows/desktop/api/Wincodec/nf-wincodec-wicmapshortnametoguid)<br/>               | Obtains the GUID associated with the given short name.<br/>                                                                                                                                                     |
| [**WICMatchMetadataContent**](/windows/desktop/api/wincodecsdk/nf-wincodecsdk-wicmatchmetadatacontent)<br/>           | Obtains a metadata format GUID for a specified container format and vendor that best matches the content within a given stream.<br/>                                                                            |
| [**WICSerializeMetadataContent**](/windows/desktop/api/wincodecsdk/nf-wincodecsdk-wicserializemetadatacontent)<br/>   | Writes metadata into a given stream.<br/>                                                                                                                                                                       |
| [WIC Proxy Functions](wic-proxy-functions.md)<br/>                                  | This section contains the WIC proxy functions.<br/>                                                                                                                                                             |



 

 

 




