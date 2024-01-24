---
description: 'Users and applications with administrative privileges can use Windows Installer functions to inventory the Windows Installer applications, features, components and patches installed on the system.Beginning with Windows Installer&\#160;3.0, users and applications that have administrator privileges can enumerate the Windows Installer applications, features, components and patches installed on the system by all users. Administrators and applications can obtain information on a product or patch for a particular user or all users in the system. Applications can obtain the feature state or component state for a particular user.The inventory functions available beginning with Windows Installer&\#160;3.0 can limit the scope of items to be found by installation context and user context. There are three possible installation contexts: per-user, per-machine, and per-user managed. The user context can be a particular user or all users in the system. The versions of the Windows Installer inventory functions earlier than Windows Installer&\#160;3.0 can only enumerate items installed on the system in the machine context or in the per-user context of the current user. This limitation prevents a complete inventory of all Windows Installer products and patches installed in the system by users other than the current user.Enumerating ProductsEnumerating PatchesObtaining Product InformationObtaining Patch InformationObtaining Component State InformationObtaining Feature State Information'
ms.assetid: ef95c3c8-b4c8-4305-8aa2-07ec74b3121b
title: Using Windows Installer to Inventory Products and Patches
ms.topic: article
ms.date: 05/31/2018
---

# Using Windows Installer to Inventory Products and Patches

Users and applications with administrative privileges can use Windows Installer functions to inventory the Windows Installer applications, features, components and patches installed on the system.

Beginning with Windows Installer 3.0, users and applications that have administrator privileges can enumerate the Windows Installer applications, features, components and patches installed on the system by all users. Administrators and applications can obtain information on a product or patch for a particular user or all users in the system. Applications can obtain the feature state or component state for a particular user.

The inventory functions available beginning with Windows Installer 3.0 can limit the scope of items to be found by installation context and user context. There are three possible installation contexts: per-user, per-machine, and per-user managed. The user context can be a particular user or all users in the system.

The versions of the Windows Installer inventory functions earlier than Windows Installer 3.0 can only enumerate items installed on the system in the machine context or in the per-user context of the current user. This limitation prevents a complete inventory of all Windows Installer products and patches installed in the system by users other than the current user.

-   [Enumerating Products](#enumerating-products)
-   [Enumerating Patches](#enumerating-patches)
-   [Obtaining Product Information](#obtaining-product-information)
-   [Obtaining Patch Information](#obtaining-patch-information)
-   [Obtaining Component State Information](#obtaining-component-state-information)
-   [Obtaining Feature State Information](#obtaining-feature-state-information)

## Enumerating Products

Use the [**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa) function to enumerate Windows Installer applications that are installed in the system. This function can find all the per-machine installations and per-user installations of applications (managed and unmanaged) for the current user and other users in the system. Use the *dwContext* parameter to specify the installation context to be found. You can specify any one or any combination of the possible installation contexts. Use the *szUserSid* parameter to specify the user context of applications to be found.

## Enumerating Patches

Use the [**MsiEnumPatchesEx**](/windows/desktop/api/Msi/nf-msi-msienumpatchesexa) function to find patches applied for an application. This function can find patches applied for a particular application or for all applications in the system. This function can find patches applied to all the per-machine installations and per-user installations of applications (managed and unmanaged) for the current user and other users in the system.

You can use the installation context and user context to restrict the patch enumeration to a particular context or across all contexts. Use the *dwContext* parameter to specify the installation context to be found. You can specify any one or any combination of the possible installation contexts. Use the *szUserSid* parameter to specify the user context of applications to be found.

**To enumerate patches applied for all products advertised or installed by all users in the system**

-   Call the [**MsiEnumPatchesEx**](/windows/desktop/api/Msi/nf-msi-msienumpatchesexa) function.
    -   Use **NULL** for the value of the *szProductCode* parameter.
    -   Use "s-1-1-0" for the value of the *szUserSid* parameter.
    -   Use "MSIINSTALLCONTEXT\_ALL" for the value of the *dwContext* parameter.

**To enumerate patches applied for all products advertised or installed by all users in the system**

1.  Call the [**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa) function.

    -   Use **NULL** for the value of the *szProductCode* parameter.
    -   Use "s-1-1-0" for the value of the *szUserSid* parameter.
    -   Use "MSIINSTALLCONTEXT\_ALL" for the value of the *dwContext* parameter.

    The function provides a product code, user context, and installation context for each application found.

2.  For each application enumerated in step 1, call [**MsiEnumPatchesEx**](/windows/desktop/api/Msi/nf-msi-msienumpatchesexa) to enumerate the patches.

    Use the product codes, user contexts and installation contexts obtained from [**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa) for the values of *szProductCode*, *szUserSid*, and *dwContext*, and each **MsiEnumProductsEx** function call.

## Obtaining Product Information

Use the [**MsiGetProductInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoexa) function to get information about applications that are advertised or installed on the system, and the properties that can be retrieved. This function can get information for an instance of an application installed under a user account other than the current user, but cannot query an instance of a product that is advertised under a per-user unmanaged context for a user account other than the current user.

You can specify the installation context and user context to restrict information for applications installed in a particular context. Use the *dwContext* parameter to specify the installation context to be found. You can specify only one of the possible installation contexts. Use the *szUserSid* parameter to specify the user context of applications to be found.

## Obtaining Patch Information

An application can call the [**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa) function to query for information about the application of a patch to a specified instance of a product. Properties such as **LocalPackage**, [**Transforms**](transforms.md), and **State** can be retrieved using this function. Not all property values are guaranteed to be available for per-user unmanaged applications if the user is not currently logged in to the machine. You can specify only one of the possible installation contexts.

You can specify the installation context and user context to restrict information to patches applied to applications installed in a particular context. Use the *dwContext* parameter to specify the installation context to be found. You can specify only one of the possible installation contexts. Use the *szUserSid* parameter to specify the user context of applications to be found.

## Obtaining Component State Information

Applications can call the [**MsiQueryComponentState**](/windows/desktop/api/Msi/nf-msi-msiquerycomponentstatea) function to get the installed state for a component. This function determines if the component is installed locally or installed to run from the source. The function can query for a component of an instance of an application that is installed under user accounts other than the current user, provided that the product is not advertised under the per-user unmanaged context for a user account other than the current user.

You can specify an installation context and user context to get the state of components for applications installed in a particular context. Use the *dwContext* parameter to specify the installation context to be found. You can specify only one of the possible installation contexts. Use the *szUserSid* parameter to specify the user context of applications to be found.

## Obtaining Feature State Information

Applications can call the [**MsiQueryFeatureStateEx**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestateexa) function to get the installed state for a product feature. This function determines if the feature is advertised, installed locally, or installed to run from the source. The function can be used to query any feature of an instance of an application installed under the machine account or any context under the current user account or the per-user managed context under any user account other than the current user. This function cannot query for an application installed under the per-user unmanaged context for a user account other than the current user. You can specify only one of the possible installation contexts.

You can specify an installation context and user context to get the state of features for applications installed in a particular context. Use the *dwContext* parameter to specify the installation context to be found. You can specify only one of the possible installation contexts. Use the *szUserSid* parameter to specify the user context of applications to be found.

 

 



