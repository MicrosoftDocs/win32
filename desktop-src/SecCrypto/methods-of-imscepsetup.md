---
Description: Methods defined by the IMSCEPSetup interface.
ms.assetid: 0d41243f-cff1-4608-bbe6-f99dc548b0e2
title: Methods of IMSCEPSetup
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Methods of IMSCEPSetup

The following methods are defined by the [**IMSCEPSetup**](/windows/win32/Casetup/nn-casetup-imscepsetup?branch=master) interface. The property access methods are not shown here. To see the properties for **IMSCEPSetup**, see [Properties of IMSCEPSetup](properties-of-imscepsetup.md).



| Method                                                             | Description                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetKeyLengthList**](/windows/win32/Casetup/nf-casetup-imscepsetup-getkeylengthlist?branch=master)           | Gets the list of [*key lengths*](security.k_gly#-security-key-length-gly) supported by the specified [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP). |
| [**GetMSCEPSetupProperty**](/windows/win32/Casetup/nf-casetup-imscepsetup-getmscepsetupproperty?branch=master) | Gets a property value for a Network Device Enrollment Service (NDES) configuration.                                                                                                                                                                                               |
| [**GetProviderNameList**](/windows/win32/Casetup/nf-casetup-imscepsetup-getprovidernamelist?branch=master)     | Gets the list of CSPs that provide asymmetric key signature and exchange algorithms on the computer.                                                                                                                                                                              |
| [**InitializeDefaults**](/windows/win32/Casetup/nf-casetup-imscepsetup-initializedefaults?branch=master)       | Initializes a **CMSCEPSetup** object with default values to enable installation of an NDES role.                                                                                                                                                                                  |
| [**Install**](/windows/win32/Casetup/nf-casetup-imscepsetup-install?branch=master)                             | Installs a role as configured in the **CMSCEPSetup** object.                                                                                                                                                                                                                      |
| [**IsMSCEPStoreEmpty**](/windows/win32/Casetup/nf-casetup-imscepsetup-ismscepstoreempty?branch=master)         | Always returns **VARIANT\_TRUE** and should not be used.                                                                                                                                                                                                                          |
| [**PostUnInstall**](/windows/win32/Casetup/nf-casetup-imscepsetup-postuninstall?branch=master)                 | This method is not implemented. It is reserved for future use.                                                                                                                                                                                                                    |
| [**PreUnInstall**](/windows/win32/Casetup/nf-casetup-imscepsetup-preuninstall?branch=master)                   | Removes registry and IIS settings for the NDES role.                                                                                                                                                                                                                              |
| [**SetAccountInformation**](/windows/win32/Casetup/nf-casetup-imscepsetup-setaccountinformation?branch=master) | Sets the user account information used by the IIS NDES extension to perform enrollment on behalf of network devices.                                                                                                                                                              |
| [**SetMSCEPSetupProperty**](/windows/win32/Casetup/nf-casetup-imscepsetup-setmscepsetupproperty?branch=master) | Sets a property value for an NDES configuration.                                                                                                                                                                                                                                  |



 

 

 



