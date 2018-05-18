---
title: How-to work with encryption settings
description: This topic orients you to our encryption packages and shows some code snips for their use.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'B1D2C227-F43D-4B18-9956-767B35145792'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# How-to: work with encryption settings

This topic orients you to our encryption packages and shows some code snips for their use.

## Support for AES 256, the new default

No additional code is required to use *AES 256* based encryption as it is the new default, assuming you build against the RMS SDK 2.1 March 2015 update or later. We encourage you to seriously consider updating your applications with this release for the additional security benefits of *AES 256*.

> \[!Important\]
>
> Support for consumption of *AES 256* protected files has existed since the [October 2014 release](release-notes--rtm-.md). If you are running applications built with a version of the SDK from before October 2014, this update will break your application. Please make sure that customers of the applications you are building, are either using the updated SDK, or are willing to immediately update to the most recent version of your application.

 

## API encryption support

Beginning with the [March 2015 update](release-notes--rtm-.md), we have incorporated the following three flags into our API and their associated encryption packages:

-   IPC\_ENCRYPTION\_PACKAGE\_AES256\_CBC4K
-   IPC\_ENCRYPTION\_PACKAGE \_AES128\_CBC4K
-   IPC\_ENCRYPTION\_PACKAGE \_AES128\_ECB (Also known as, Deprecated Algorithms)

The encryption package flags, see [**Preferred encryption**](preferred-encryption.md), can be used in conjunction with our new, License Property flag **IPC\_LI\_PREFERRED\_ENCRYPTION\_PACKAGE**.

Following are some simple code snippets that demonstrates how to use the new license property.

## Deprecated Algorithms

We are no longer exposing the **IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS** flag in our API. This means that future applications will no longer compile if they reference this flag, but applications already built using it will continue to work since we honor the flag privately in the API code.

Getting the benefit of the old deprecated encryption algorithms flag can still be achieved simply by changing one flag. See the following code snippets for an examples.

## Protect Files with AES 256 CBC4K

No change in code needed, *AES 256* CBC4K is the default.


```C++
hr = IpcCreateLicenseFromTemplateID(pcTil->aTi[0].wszID, 
                                    0, 
                                    NULL, 
                                    &amp;pLicenseHandle);
```



## Protect Files with AES-128 CBC4K


```C++
hr = IpcCreateLicenseFromTemplateID(pcTil->aTi[0].wszID, 
                                    0, 
                                    NULL, 
                                    &amp;pLicenseHandle);

DWORD dwEncryptionMode = IPC_ENCRYPTION_PACKAGE_AES128_CBC4K; 

hr = IpcSetLicenseProperty(pLicenseHandle, 
                           false,
                           IPC_LI_PREFERRED_ENCRYPTION_PACKAGE,
                           &amp;dwEncryptionMode);
```



## Protect Files with AES-128 ECB (Deprecated Algorithms)

This sample also shows the new way of supporting *deprecated algorithms*.


```C++
hr = IpcCreateLicenseFromTemplateID(pcTil->aTi[0].wszID, 
                                    0, 
                                    NULL, 
                                    &amp;pLicenseHandle);

DWORD dwEncryptionMode = IPC_ENCRYPTION_PACKAGE_AES128_ECB;

hr = IpcSetLicenseProperty(pLicenseHandle, 
                           false,
                           IPC_LI_PREFERRED_ENCRYPTION_PACKAGE, 
                           &amp;dwEncryptionMode);
```



 

 




