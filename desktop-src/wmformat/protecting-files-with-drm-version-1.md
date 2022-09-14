---
title: Protecting Files with DRM Version 1
description: Protecting Files with DRM Version 1
ms.assetid: 91de1c20-e926-4ff6-b0cd-e90fc9cbaad2
keywords:
- Windows Media Format SDK,creating protected files
- Windows Media Format SDK,protected files
- Advanced Systems Format (ASF),creating protected files
- ASF (Advanced Systems Format),creating protected files
- Advanced Systems Format (ASF),protected files
- ASF (Advanced Systems Format),protected files
- Advanced Systems Format (ASF),WMStubDRM.lib
- ASF (Advanced Systems Format),WMStubDRM.lib
- WMStubDRM.lib,creating protected files
- WMStubDRM.lib,protected files
- digital rights management (DRM),WMStubDRM.lib
- DRM (digital rights management),WMStubDRM.lib
ms.topic: article
ms.date: 05/31/2018
---

# Protecting Files with DRM Version 1

When this kind of protection is applied, a DRM version 1 license is generated that is valid only on the machine from which the license request was made. Because no key or key seed is set, there is no way to generate portable licenses for content protected using this technique. However, when using the Windows Media Format SDK 7.1 or later, the licenses are recoverable at the Microsoft License Migration service.

To protect ASF files using DRM version 1, perform the following steps:

1.  Link the WMStubDRM.lib file to your project and, if necessary, unlink wmvcore.lib.
2.  Call the [**WMCreateWriter**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriter) function to create the writer. The first argument is reserved and must be set to **NULL**.
3.  Set a profile for the writer to use by calling [**IWMWriter::SetProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setprofile) or [**IWMWriter::SetProfileByID**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmwriter-setprofilebyid). You must set a profile in the writer before setting any DRM attributes. DRM is supported only for profiles that use the Windows Media Audio or Windows Media Video codecs.
4.  Using the [**IWMHeaderInfo::SetAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-setattribute) method, set the following DRM properties. The **Use\_DRM** property instructs the DRM components to protect the content using DRM version 1. The **DRM\_Flags** property specifies the rights to be included in the local license that will be created for the content. The **DRM\_LEVEL** value is also stored in the license; it specifies the minimum level required to access the content. 150 is the recommended level for DRM version 1 content.

    | Attribute      | Value                                                                                       |
    |----------------|---------------------------------------------------------------------------------------------|
    | **Use\_DRM**   | **TRUE**                                                                                    |
    | **DRM\_Flags** | WMT\_RIGHT\_PLAYBACK \| WMT\_RIGHT\_COPY\_TO\_NON\_SDMI\_DEVICE \| WMT\_RIGHT\_COPY\_TO\_CD |
    | **DRM\_LEVEL** | 150                                                                                         |

    

     

The following example code shows how to create a DRM-enabled writer for DRM version 1 and set the DRM properties. Error checking has been omitted for the sake of clarify.


```C++
BOOL  fUseDRM    = TRUE;
// These are the rights we will apply to the file. See WMT_RIGHTS for
// the full set of possible rights.

DWORD dwDRMFlags = WMT_RIGHT_PLAYBACK | 
                   WMT_RIGHT_COPY_TO_NON_SDMI_DEVICE | 
                   WMT_RIGHT_COPY_TO_CD;

// Set the minimum required DRM level low enough
// to allow older players to access the content.
DWORD dwDRMLevel = 150;

IWMDRMWriter*  pWMDRMWriter  = NULL;
HRESULT hr = S_OK;

// Initialize COM.
hr = CoInitialize(NULL);

// Create a writer object.
hr = WMCreateWriter( NULL, &pWMDRMWriter);

// Obtain the IWMHeaderInfo interface.
hr = pWMDRMWriter -> QueryInterface(IID_IWMHeaderInfo, 
                                   (void**) &pWMHeaderInfo);

// Tell the SDK runtime to protect the file using DRM version 1.
hr= pWMHeaderInfo-> SetAttribute(0,
                                 g_wszWMUse_DRM,
                                 WMT_TYPE_BOOL,
                                 (BYTE*)&fUseDRM,
                                 sizeof(BOOL));

// Specify the rights that will be stored in the local license that is
// created automatically for the content.
hr= pWMHeaderInfo->SetAttribute( 0,
                                 g_wszWMDRM_Flags, 
                                 WMT_TYPE_DWORD,
                                 (BYTE *)&dwDRMFlags,
                                 sizeof(DWORD) );

// Set the DRM_Level attribute in the file's DRM header.
hr= pWMHeaderInfo->SetAttribute( 0,
                                 g_wszWMDRM_Level, 
                                 WMT_TYPE_DWORD,
                                 (BYTE *)&dwDRMLevel,
                                 sizeof(DWORD) );
```



 

 




