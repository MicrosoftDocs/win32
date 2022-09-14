---
description: The MTS Administration Library shipped with the COM+ Administration interfaces provides backward compatibility with the MTS 2.0 Administration Library.
ms.assetid: 5eb9e68c-4f3b-4d57-bd51-704211d817fe
title: MTS Administration Library
ms.topic: article
ms.date: 05/31/2018
---

# MTS Administration Library

The MTS Administration Library shipped with the COM+ Administration interfaces provides backward compatibility with the MTS 2.0 Administration Library. Most existing MTS 2.0 administration code will still work with the MTSAdmin Library that is provided; however, some functionality has changed.

To take advantage of new functionality or if you are writing administration code for the first time, you should use the COMAdmin Library.

The following elements in the current MTS Administration Library are changed from the MTS 2.0 Administration Library:

-   The **IRemoteComponentUtil** interface is no longer available.
-   The **RemoteComponents** collection is no longer available.
-   The RoleID property is no longer available, the Role Name is now used as the key for this.
-   The **ExportPackage** method no longer exports a client.exe.
-   The RemoteComponentInstallPath property is no longer exposed on the [**LocalComputer**](localcomputer.md) collection.
-   The ApplicationInstallPath property will no longer be exposed on the [**LocalComputer**](localcomputer.md) collection.
-   The System package is now named System Application.
-   The Utilities package is now named COM+ Utilities.
-   The IsSystem property exists in the [**Components**](components.md) collection in MTSAdmin but will return "NotImpl" when checked and will not be saved if set.
-   The PackageName property is no longer supported by the [**Components**](components.md) collection. To figure out the package's name, you will now need to get the PackageID and then find the matching package in the Packages collection.
-   The following properties no longer exist on the [**InterfacesForComponent**](interfacesforcomponent.md) collection:
    -   **ProxyCLSID**
    -   **ProxyDLL**
    -   **ProxyThreadingModel**
    -   **TypeLibFile**
    -   **TypeLibID**
    -   **TypeLibLangID**
    -   **TypeLibPlatform**
    -   **TypeLibVersion**

## Related topics

<dl> <dt>

[Automatic Conversion from MTS](automatic-conversion-from-mts.md)
</dt> <dt>

[COM+ Conversion Results and Issues](com--conversion-results-and-issues.md)
</dt> <dt>

[Manual Conversion from MTS](manual-conversion-from-mts.md)
</dt> </dl>

 

 



