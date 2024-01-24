---
description: Methods defined by the IMSCEPSetup interface.
ms.assetid: 0d41243f-cff1-4608-bbe6-f99dc548b0e2
title: Methods of IMSCEPSetup
ms.topic: article
ms.date: 05/31/2018
---

# Methods of IMSCEPSetup

The following methods are defined by the [**IMSCEPSetup**](/windows/desktop/api/Casetup/nn-casetup-imscepsetup) interface. The property access methods are not shown here. To see the properties for **IMSCEPSetup**, see [Properties of IMSCEPSetup](properties-of-imscepsetup.md).



| Method                                                             | Description                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetKeyLengthList**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-getkeylengthlist)           | Gets the list of [*key lengths*](../secgloss/k-gly.md) supported by the specified [*cryptographic service provider*](../secgloss/c-gly.md) (CSP). |
| [**GetMSCEPSetupProperty**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-getmscepsetupproperty) | Gets a property value for a Network Device Enrollment Service (NDES) configuration.                                                                                                                                                                                               |
| [**GetProviderNameList**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-getprovidernamelist)     | Gets the list of CSPs that provide asymmetric key signature and exchange algorithms on the computer.                                                                                                                                                                              |
| [**InitializeDefaults**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-initializedefaults)       | Initializes a **CMSCEPSetup** object with default values to enable installation of an NDES role.                                                                                                                                                                                  |
| [**Install**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-install)                             | Installs a role as configured in the **CMSCEPSetup** object.                                                                                                                                                                                                                      |
| [**IsMSCEPStoreEmpty**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-ismscepstoreempty)         | Always returns **VARIANT\_TRUE** and should not be used.                                                                                                                                                                                                                          |
| [**PostUnInstall**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-postuninstall)                 | This method is not implemented. It is reserved for future use.                                                                                                                                                                                                                    |
| [**PreUnInstall**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-preuninstall)                   | Removes registry and IIS settings for the NDES role.                                                                                                                                                                                                                              |
| [**SetAccountInformation**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-setaccountinformation) | Sets the user account information used by the IIS NDES extension to perform enrollment on behalf of network devices.                                                                                                                                                              |
| [**SetMSCEPSetupProperty**](/windows/desktop/api/Casetup/nf-casetup-imscepsetup-setmscepsetupproperty) | Sets a property value for an NDES configuration.                                                                                                                                                                                                                                  |



 

 

 
