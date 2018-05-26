---
Description: The following are the ImageHlp functions.
ms.assetid: 926f412e-25ba-4f9c-a118-b5a1bc723379
title: ImageHlp Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ImageHlp Functions

The following are the ImageHlp functions.

## Image Access

The image access functions access the data in an executable image. The functions provide high-level access to the base of images and very specific access to the most common parts of an image's data.

<dl>

[**GetImageConfigInformation**](/windows/win32/Imagehlp/nf-imagehlp-getimageconfiginformation?branch=master)  
[**GetImageUnusedHeaderBytes**](/windows/win32/Imagehlp/nf-imagehlp-getimageunusedheaderbytes?branch=master)  
[**ImageLoad**](/windows/win32/Imagehlp/nf-imagehlp-imageload?branch=master)  
[**ImageUnload**](/windows/win32/Imagehlp/nf-imagehlp-imageunload?branch=master)  
[**MapAndLoad**](/windows/win32/Imagehlp/nf-imagehlp-mapandload?branch=master)  
[**SetImageConfigInformation**](/windows/win32/Imagehlp/nf-imagehlp-setimageconfiginformation?branch=master)  
[**UnMapAndLoad**](/windows/win32/Imagehlp/nf-imagehlp-unmapandload?branch=master)  
</dl>

## Image Integrity

The image integrity functions manage the set of certificates in an image file.

<dl>

[**DigestFunction**](/windows/win32/Imagehlp/nc-imagehlp-digest_function?branch=master)  
[**ImageAddCertificate**](/windows/win32/Imagehlp/nf-imagehlp-imageaddcertificate?branch=master)  
[**ImageEnumerateCertificates**](/windows/win32/Imagehlp/nf-imagehlp-imageenumeratecertificates?branch=master)  
[**ImageGetCertificateData**](/windows/win32/Imagehlp/nf-imagehlp-imagegetcertificatedata?branch=master)  
[**ImageGetCertificateHeader**](/windows/win32/Imagehlp/nf-imagehlp-imagegetcertificateheader?branch=master)  
[**ImageGetDigestStream**](/windows/win32/Imagehlp/nf-imagehlp-imagegetdigeststream?branch=master)  
[**ImageRemoveCertificate**](/windows/win32/Imagehlp/nf-imagehlp-imageremovecertificate?branch=master)  
</dl>

## Image Modification

The image modification functions allow you to change the executable image.

<dl>

[**BindImage**](/windows/win32/Imagehlp/nf-imagehlp-bindimage?branch=master)  
[**BindImageEx**](/windows/win32/Imagehlp/nf-imagehlp-bindimageex?branch=master)  
[**CheckSumMappedFile**](/windows/win32/Imagehlp/nf-imagehlp-checksummappedfile?branch=master)  
[**MapFileAndCheckSum**](/windows/win32/Imagehlp/nf-imagehlp-mapfileandchecksuma?branch=master)  
[**ReBaseImage**](/windows/win32/Imagehlp/nf-imagehlp-rebaseimage?branch=master)  
[**ReBaseImage64**](/windows/win32/Imagehlp/nf-imagehlp-rebaseimage64?branch=master)  
[**SplitSymbols**](/windows/win32/Imagehlp/nf-imagehlp-splitsymbols?branch=master)  
[**StatusRoutine**](/windows/win32/Imagehlp/nc-imagehlp-pimagehlp_status_routine?branch=master)  
[**TouchFileTimes**](/windows/win32/Imagehlp/nf-imagehlp-touchfiletimes?branch=master)  
[**UpdateDebugInfoFile**](/windows/win32/Imagehlp/nf-imagehlp-updatedebuginfofile?branch=master)  
[**UpdateDebugInfoFileEx**](/windows/win32/Imagehlp/nf-imagehlp-updatedebuginfofileex?branch=master)  
</dl>

 

 



