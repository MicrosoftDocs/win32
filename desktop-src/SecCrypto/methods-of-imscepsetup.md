---
Description: 'Methods defined by the IMSCEPSetup interface.'
ms.assetid: '0d41243f-cff1-4608-bbe6-f99dc548b0e2'
title: Methods of IMSCEPSetup
---

# Methods of IMSCEPSetup

The following methods are defined by the [**IMSCEPSetup**](imscepsetup.md) interface. The property access methods are not shown here. To see the properties for **IMSCEPSetup**, see [Properties of IMSCEPSetup](properties-of-imscepsetup.md).



| Method                                                             | Description                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetKeyLengthList**](imscepsetup-getkeylengthlist.md)           | Gets the list of [*key lengths*](security.k_gly#-security-key-length-gly) supported by the specified [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP). |
| [**GetMSCEPSetupProperty**](imscepsetup-getmscepsetupproperty.md) | Gets a property value for a Network Device Enrollment Service (NDES) configuration.                                                                                                                                                                                               |
| [**GetProviderNameList**](imscepsetup-getprovidernamelist.md)     | Gets the list of CSPs that provide asymmetric key signature and exchange algorithms on the computer.                                                                                                                                                                              |
| [**InitializeDefaults**](imscepsetup-initializedefaults.md)       | Initializes a **CMSCEPSetup** object with default values to enable installation of an NDES role.                                                                                                                                                                                  |
| [**Install**](imscepsetup-install.md)                             | Installs a role as configured in the **CMSCEPSetup** object.                                                                                                                                                                                                                      |
| [**IsMSCEPStoreEmpty**](imscepsetup-ismscepstoreempty.md)         | Always returns **VARIANT\_TRUE** and should not be used.                                                                                                                                                                                                                          |
| [**PostUnInstall**](imscepsetup-postuninstall.md)                 | This method is not implemented. It is reserved for future use.                                                                                                                                                                                                                    |
| [**PreUnInstall**](imscepsetup-preuninstall.md)                   | Removes registry and IIS settings for the NDES role.                                                                                                                                                                                                                              |
| [**SetAccountInformation**](imscepsetup-setaccountinformation.md) | Sets the user account information used by the IIS NDES extension to perform enrollment on behalf of network devices.                                                                                                                                                              |
| [**SetMSCEPSetupProperty**](imscepsetup-setmscepsetupproperty.md) | Sets a property value for an NDES configuration.                                                                                                                                                                                                                                  |



 

 

 



