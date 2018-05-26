---
Description: This section contains information about the Windows Imaging Component (WIC) functions.
ms.assetid: 6f948df6-5b70-4f1e-b01d-3841d7819acb
title: Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions

This section contains information about the Windows Imaging Component (WIC) functions.

## In this section



| Topic                                                                                      | Description                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*ProgressNotificationCallback*](/windows/win32/Wincodec/nc-wincodec-pfnprogressnotification?branch=master)<br/>   | Application defined callback function called when codec component progress is made.<br/>                                                                                                                        |
| [**WICConvertBitmapSource**](/windows/win32/Wincodec/nf-wincodec-wicconvertbitmapsource?branch=master)<br/>             | Obtains a [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) in the desired pixel format from a given **IWICBitmapSource**.<br/>                                                                           |
| [**WICCreateBitmapFromSection**](/windows/win32/Wincodec/nf-wincodec-wiccreatebitmapfromsection?branch=master)<br/>     | Returns a [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) that is backed by the pixels of a Windows Graphics Device Interface (GDI) section handle.<br/>                                                |
| [**WICCreateBitmapFromSectionEx**](/windows/win32/Wincodec/nf-wincodec-wiccreatebitmapfromsectionex?branch=master)<br/> | Returns a [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) that is backed by the pixels of a GDI section handle.<br/>                                                                                    |
| [**WICGetMetadataContentSize**](/windows/win32/wincodecsdk/nf-wincodecsdk-wicgetmetadatacontentsize?branch=master)<br/>       | Returns the size of the metadata content contained by the specified [**IWICMetadataWriter**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatawriter?branch=master). The returned size accounts for the header and the length of the metadata.<br/> |
| [**WICMapGuidToShortName**](/windows/win32/WinCodec/nf-wincodec-wicmapguidtoshortname?branch=master)<br/>               | Obtains the short name associated with a given GUID.<br/>                                                                                                                                                       |
| [**WICMapSchemaToName**](/windows/win32/Wincodec/nf-wincodec-wicmapschematoname?branch=master)<br/>                     | Obtains the name associated with a given schema.<br/>                                                                                                                                                           |
| [**WICMapShortNameToGuid**](/windows/win32/Wincodec/nf-wincodec-wicmapshortnametoguid?branch=master)<br/>               | Obtains the GUID associated with the given short name.<br/>                                                                                                                                                     |
| [**WICMatchMetadataContent**](/windows/win32/wincodecsdk/nf-wincodecsdk-wicmatchmetadatacontent?branch=master)<br/>           | Obtains a metadata format GUID for a specified container format and vendor that best matches the content within a given stream.<br/>                                                                            |
| [**WICSerializeMetadataContent**](/windows/win32/wincodecsdk/nf-wincodecsdk-wicserializemetadatacontent?branch=master)<br/>   | Writes metadata into a given stream.<br/>                                                                                                                                                                       |
| [WIC Proxy Functions](wic-proxy-functions.md)<br/>                                  | This section contains the WIC proxy functions.<br/>                                                                                                                                                             |



 

 

 




