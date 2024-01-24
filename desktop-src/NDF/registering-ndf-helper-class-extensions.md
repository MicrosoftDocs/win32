---
title: Registering NDF Helper Class Extensions
description: Each helper class extension has a number of registry keys associated with it. Some keys are required by COM, and some keys are required by NDF.
ms.assetid: 9ff3266d-5ffc-4a00-be24-2f85461c6ea6
ms.topic: article
ms.date: 05/31/2018
---

# Registering NDF Helper Class Extensions

Each helper class extension has a number of registry keys associated with it. Some keys are required by COM, and some keys are required by NDF.

## COM Registry Keys

Helper class extensions must be implemented as COM servers. COM registration must be completed for each helper class extension. The object's CLSID, the [**INetDiagHelperInfo**](/windows/desktop/api/ndhelper/nn-ndhelper-inetdiaghelperinfo) interface, and the [**INetDiagHelper**](/windows/desktop/api/ndhelper/nn-ndhelper-inetdiaghelper) interface must be registered. Registration creates a number of COM-related registry keys for the NDF helper class extension.

## NDF Registry Keys

Helper class extensions must be registered before interacting with the Network Diagnostics Framework and with other related helper classes. This is accomplished by populating the registry.

The following procedure shows how to add helper class extensions to the registry.

1.  Publish the names of helper classes implemented by the DLL and their dependencies by creating a key for the DLL under

    **HKLM\\System\\CurrentControlSet\\Control\\NetDiagFx**\\*VendorName*\\**HostDLLs**\\*Helper Class DLL*\\**HelperClasses**\\*Helper Class Name*

    Replace *VendorName*, *Helper Class DLL*, and *Helper Class Name* with user-defined values as described below.

    | Value               | Type    | Meaning                                                                      |
    |---------------------|---------|------------------------------------------------------------------------------|
    | *VendorName*        | REG\_SZ | The name of the vendor.                                                      |
    | *Helper Class DLL*  | REG\_SZ | Name of the DLL, without extension.                                          |
    | *Helper Class Name* | REG\_SZ | The name of the helper class on which the current helper class is dependent. |

    

     

2.  Under each *Helper Class Name* key, publish the following information.

    

    | Value         | Type       | Meaning                                                                                                                                                                 |
    |---------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **CLSID**     | REG\_SZ    | A string that contains the COM class ID of the helper class.                                                                                                            |
    | **Version**   | REG\_SZ    | A string the contains the major and minor versions of the helper class in the format &lt;major&gt;&lt;minor&gt;.                                                        |
    | **Published** | REG\_DWORD | A value of 1 means that this helper class is expected to be directly invoked from the Diagnostics client. 0 means that it can be called only from another helper class. |
    | **Parent**    | REG\_SZ    | A string that names the Microsoft extensible helper class that is being extended.                                                                                       |

    

     

3.  For each helper class, publish the list of matching attributes by creating a key under

    **HKLM\\System\\CurrentControlSet\\Control\\NetDiagFx**\\*VendorName*\\**HostDLLs**\\*Helper Class DLL*\\**HelperClasses**\\*Helper Class Name*\\**MatchAttributes**

    They key must contain one or more values (one per attribute) of the following type.

    | Value             | Type                             | Meaning                                                                    |
    |-------------------|----------------------------------|----------------------------------------------------------------------------|
    | **AttributeName** | REG\_SZ\|REG\_DWORD\|REG\_BINARY | A value that completes the name and value pair for a particular attribute. |

    

     

 

 




