---
Description: 'You can use the Windows Installer to detect missing components or files, and then reinstall features that contain the missing components.'
ms.assetid: 'b197c9d0-fcc2-4ca7-a870-e1af82343455'
title: Installing a Missing Component
---

# Installing a Missing Component

You can use the Windows Installer to detect missing components or files, and then reinstall features that contain the missing components. Because the Installer installs features and not components, it must first resolve to which component a missing file belongs, and then install the feature that contains the component. If more than one feature is linked to the component, the Installer installs the feature that requires the least disk space.

If you call [**MsiGetComponentPath**](msigetcomponentpath.md), you can verify that the key file of a component is present. However, it is still possible that other files belonging to the component are missing. In that scenario, call [**MsiInstallMissingFile**](msiinstallmissingfile.md). The Installer then resolves to which component the file belongs, and installs the feature that is linked to the component that requires the least disk space.

If the [**MsiGetComponentPath**](msigetcomponentpath.md) function unexpectedly fails, you must install any missing components.

The following procedure shows you how to install missing components.

**To detect and install a missing component**

1.  Call [**MsiGetComponentPath**](msigetcomponentpath.md) to verify that the key file of a component is present. However, even if the key file of the component is present, it is still possible that other files belonging to the component are missing.
2.  Call the [**MsiInstallMissingComponent**](msiinstallmissingcomponent.md) function if the feature associated with the component is unknown.
3.  Call the [**MsiConfigureFeature**](msiconfigurefeature.md) or [**MsiProvideComponent**](msiprovidecomponent.md) function if the feature associated with the component is known.
4.  Call [**MsiInstallMissingFile**](msiinstallmissingfile.md) if an application is unable to open a file.

 

 



