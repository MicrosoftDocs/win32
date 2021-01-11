---
description: Beginning with Windows Installer 3.0, it is possible to uninstall some patches from applications.
ms.assetid: 11e995b7-30c7-4992-b436-3af289ac3966
title: Uninstalling Patches
ms.topic: article
ms.date: 05/31/2018
---

# Uninstalling Patches

Beginning with Windows Installer 3.0, it is possible to uninstall some patches from applications. The patch must be an [uninstallable patch](uninstallable-patches.md). When using a Windows Installer version less than version 3.0, [removing patches](removing-patches.md) requires uninstalling the patch product and reinstalling the product without applying the patch.

**Windows Installer 2.0:** Not supported. Patches applied using a version of Windows Installer that is earlier than Windows Installer 3.0 are not uninstallable.

When you invoke an uninstallation of a patch by any of the following methods, the installer attempts to remove the patch from the first product visible to the application or user requesting the uninstallation. The installer searches for patched products in the following order: per-user managed, per-user unmanaged, per-machine.

## Uninstalling a patch using MSIPATCHREMOVE on a command line

You can uninstall patches from a command by using msiexec.exe and the [Command Line Options](command-line-options.md). The following sample command line removes an [uninstallable patch](uninstallable-patches.md), example.msp, from an application, example.msi, using the [**MSIPATCHREMOVE**](msipatchremove.md) property and the /i command line option. When using /i, the patched application can be identified by the path to the application's package (.msi file) or the application's [product code](product-codes.md). In this example, the application's installation package is located at "\\\\server\\share\\products\\example\\example.msi" and the application's [**ProductCode**](productcode.md) property is "{0C9840E7-7F0B-C648-10F0-4641926FE463}". The patch package is located at "\\\\server\\share\\products\\example\\patches\\example.msp" and the patch code GUID is "{EB8C947C-78B2-85A0-644D-86CEEF8E07C0}".

**Msiexec /I {0C9840E7-7F0B-C648-10F0-4641926FE463} MSIPATCHREMOVE={EB8C947C-78B2-85A0-644D-86CEEF8E07C0} /qb**

## Uninstalling a patch using the standard command line options

Beginning with Windows Installer version 3.0, you can use the [standard command line options](standard-installer-command-line-options.md) used by Microsoft Windows Operating System Updates (update.exe) to uninstall Windows Installer patches from a command line.

The following command line is the standard command line equivalent of the Windows Installer command line used to uninstall a patch using the [**MSIPATCHREMOVE**](msipatchremove.md) property. The /uninstall option used with the /package option denotes the uninstallation of a patch. The patch can be referenced by the full path to the patch or by the patch code GUID.

**Msiexec /package {0C9840E7-7F0B-C648-10F0-4641926FE463} /uninstall {EB8C947C-78B2-85A0-644D-86CEEF8E07C0} /passive**

> [!Note]  
> The /passive standard option is not an exact equivalent of the Windows Installer /qb option.

 

## Uninstalling a patch using the RemovePatches method

You can uninstall patches from script by using the Windows Installer [Automation Interface](automation-interface.md). The following scripting sample removes an [uninstallable patch](uninstallable-patches.md), example.msp, from an application, example.msi, using the [**RemovePatches**](installer-removepatches.md) method of the [Installer](installer-object.md) object. Each patch being uninstalled can be represented by either the full path to the patch package or the patch code GUID. In this example, the application's installation package is located at "\\\\server\\share\\products\\example\\example.msi" and the application's [**ProductCode**](productcode.md) property is "{0C9840E7-7F0B-C648-10F0-4641926FE463}". The patch package is located at "\\\\server\\share\\products\\example\\patches\\example.msp" and the patch code GUID is "{EB8C947C-78B2-85A0-644D-86CEEF8E07C0}".


```VB
const msiInstallTypeSingleInstance = 2
const PatchList = "{EB8C947C-78B2-85A0-644D-86CEEF8E07C0}"
const Product = "{0C9840E7-7F0B-C648-10F0-4641926FE463}"

Dim installer
Set installer = CreateObject("WindowsInstaller.Installer")

installer.RemovePatches(PatchList, Product, msiInstallTypeSingleInstance, "")
```



## Uninstalling a patch using Add/Remove Programs

With Windows XP, you can uninstall patches using Add/Remove programs.

## Uninstalling a patch using the MsiRemovePatches function

Your applications can uninstall patches from other applications by using the [Windows Installer Functions](installer-functions.md). The following code example removes an [uninstallable patch](uninstallable-patches.md), example.msp, from an application, example.msi, using the [**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa) function. A patch can be referenced by the full path to the patch package or the patch code GUID. In this example, the application's installation package is located at "\\\\server\\share\\products\\example\\example.msi" and the application's [**ProductCode**](productcode.md) property is "{0C9840E7-7F0B-C648-10F0-4641926FE463}". The patch package is located at "\\\\server\\share\\products\\example\\patches\\example.msp" and the patch code GUID is "{EB8C947C-78B2-85A0-644D-86CEEF8E07C0}".


```C++
    UINT uiReturn = MsiRemovePatches(
          /*szPatchList=*/TEXT("\\server\\share\\products\\example\\patches\\example.msp"),
          /*szProductCode=*/  TEXT("{0C9840E7-7F0B-C648-10F0-4641926FE463}"),
          /*eUninstallType=*/ INSTALLTYPE_SINGLE_INSTANCE,
          /*szPropertyList=*/ NULL);
```



## Uninstalling a patch from all applications using MsiRemovePatches function

A single patch can update more than one product on the computer. An application can use [**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa) to enumerate all the products on the computer and determine whether a patch has been applied to a particular instance of the product. The application can then uninstall the patch using [**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa). For example, a single patch can update multiple products if the patch updates a file in a component that is shared by multiple products and the patch is distributed to update both products.

The following example demonstrates how an application can use the Windows Installer to remove a patch from all applications that are available to the user. It does not remove the patch from applications installed per-user for another user.


```C++
#ifndef UNICODE
#define UNICODE
#endif //UNICODE

#ifndef _WIN32_MSI
#define _WIN32_MSI 300
#endif //_WIN32_MSI

#include <stdio.h>
#include <windows.h>
#include <msi.h>

#pragma comment(lib, "msi.lib")

const int cchGUID = 38;

///////////////////////////////////////////////////////////////////
// RemovePatchFromAllVisibleapplications:
//
// Arguments:
//    wszPatchToRemove - GUID of patch to remove
//
///////////////////////////////////////////////////////////////////
//
UINT RemovePatchFromAllVisibleapplications(LPCWSTR wszPatchToRemove)
{
    if (!wszPatchToRemove)
        return ERROR_INVALID_PARAMETER;

    UINT uiStatus = ERROR_SUCCESS;
    DWORD dwIndex = 0;
    WCHAR wszapplicationCode[cchGUID+1] = {0};

    DWORD dwapplicationSearchContext = MSIINSTALLCONTEXT_ALL;
    MSIINSTALLCONTEXT dwInstallContext = MSIINSTALLCONTEXT_NONE;

    do
    {
        // Enumerate all visible applications in all contexts for the caller.
        // NULL for szUserSid defaults to using the caller's SID
        uiStatus = MsiEnumProductsEx(/*szapplicationCode*/NULL,
         /*szUserSid*/NULL,
         dwapplicationSearchContext,
         dwIndex,
         wszapplicationCode,
         &dwInstallContext,
         /*szSid*/NULL,
         /*pcchSid*/NULL);

        if (ERROR_SUCCESS == uiStatus)
        {
            // check to see if the provided patch is
            // registered for this application instance
            UINT uiPatchStatus = MsiGetPatchInfoEx(wszPatchToRemove,
             wszapplicationCode,
             /*szUserSid*/NULL,
             dwInstallContext,
             INSTALLPROPERTY_PATCHSTATE,
             NULL,
             NULL);

            if (ERROR_SUCCESS == uiPatchStatus)
            {
                // patch is registered to this application; remove patch
                wprintf(L"Removing patch %s from application %s...\n",
                 wszPatchToRemove, wszapplicationCode);
                                
                UINT uiRemoveStatus = MsiRemovePatches(
                 wszPatchToRemove,
                 wszapplicationCode,
                 INSTALLTYPE_SINGLE_INSTANCE,
                 L"");

                if (ERROR_SUCCESS != uiRemoveStatus)
                {
                    // This halts the enumeration and fails. Alternatively
                    // you could output an error and continue the
                    // enumeration
                     return ERROR_FUNCTION_FAILED;
                }
            }
            else if (ERROR_UNKNOWN_PATCH != uiPatchStatus)
            {
                // Some other error occurred during processing. This
                // halts the enumeration and fails. Alternatively you
                // could output an error and continue the enumeration
                 return ERROR_FUNCTION_FAILED;
            }
            // else patch was not applied to this application
            // (ERROR_UNKNOWN_PATCH returned)
        }

        dwIndex++;
    }
    while (uiStatus == ERROR_SUCCESS);

    if (ERROR_NO_MORE_ITEMS != uiStatus)
        return ERROR_FUNCTION_FAILED;

    return ERROR_SUCCESS;
}
```



## Related topics

<dl> <dt>

[Patch Sequencing](sequencing-patches.md)
</dt> <dt>

[Removing Patches](removing-patches.md)
</dt> <dt>

[Uninstallable Patches](uninstallable-patches.md)
</dt> <dt>

[Patch Uninstall Custom Actions](patch-uninstall-custom-actions.md)
</dt> <dt>

[**MSIPATCHREMOVE**](msipatchremove.md)
</dt> <dt>

[**MsiEnumapplicationsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa)
</dt> <dt>

[**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa)
</dt> <dt>

[**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa)
</dt> </dl>

 

 



