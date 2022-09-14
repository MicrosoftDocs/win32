---
description: An application can call the MsiEnumProducts or MsiEnumProductsEx functions to enumerate products that are installed or advertised on the system.
ms.assetid: 162bda20-0c62-4eac-8c1f-fd107e42c528
title: Determining Installation Context
ms.topic: article
ms.date: 05/31/2018
---

# Determining Installation Context

An application can call the [**MsiEnumProducts**](/windows/desktop/api/Msi/nf-msi-msienumproductsa) or [**MsiEnumProductsEx**](/windows/desktop/api/Msi/nf-msi-msienumproductsexa) functions to enumerate products that are installed or advertised on the system. This function can enumerate all the products installed in the per-machine [installation context](installation-context.md). It can enumerate the products installed in the per-user context for the current user. The application can retrieve information about the context of these products by calling the [**MsiGetProductInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoexa) or [**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa) functions.

The Windows Installer can install products to run with elevated (system) privileges for non-administrator users. This requires the permission of an administrator user. A product that is installed with elevated privileges is called "managed." All products installed per-machine are managed. Products installed per-user are only managed if a local system agent performs an advertisement while impersonating a user. This is the method used by software deployment through [Group Policy](/previous-versions/windows/desktop/Policy/group-policy-start-page). Per-user applications installed while the [AlwaysInstallElevated](alwaysinstallelevated.md) policies are set are not considered managed. By calling [**MsiIsProductElevated**](/windows/desktop/api/Msi/nf-msi-msiisproductelevateda), an application can check whether a particular product is managed.

The following sample demonstrates how an application determines context by using [**MsiEnumProducts**](/windows/desktop/api/Msi/nf-msi-msienumproductsa), [**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa), and [**MsiIsProductElevated**](/windows/desktop/api/Msi/nf-msi-msiisproductelevateda).


```C++
#ifndef UNICODE
#define UNICODE
#endif //UNICODE

#ifndef _WIN32_MSI
#define _WIN32_MSI 200
#endif //_WIN32_MSI

#include <stdio.h>
#include <windows.h>
#include <msi.h>
#pragma comment(lib, "msi.lib")

const int cchGUID = 38;

UINT DetermineContextForAllProducts()
{
    WCHAR wszProductCode[cchGUID+1] = {0};
    WCHAR wszAssignmentType[10] = {0};
    DWORD cchAssignmentType = 
            sizeof(wszAssignmentType)/sizeof(wszAssignmentType[0]);
    DWORD dwIndex = 0;

    DWORD cchProductName = MAX_PATH;
    WCHAR* lpProductName = new WCHAR[cchProductName];
    if (!lpProductName)
    {
        return ERROR_OUTOFMEMORY;
    }

    UINT uiStatus = ERROR_SUCCESS;

    // enumerate all visible products
    do
    {
        uiStatus = MsiEnumProducts(dwIndex,
                          wszProductCode);
        if (ERROR_SUCCESS == uiStatus)
        {
            cchAssignmentType = 
                sizeof(wszAssignmentType)/sizeof(wszAssignmentType[0]);
            BOOL fPerMachine = FALSE;
            BOOL fManaged = FALSE;

            // Determine assignment type of product
            // This indicates whether the product
            // instance is per-user or per-machine
            if (ERROR_SUCCESS == 
                MsiGetProductInfo(wszProductCode,INSTALLPROPERTY_ASSIGNMENTTYPE,wszAssignmentType,&cchAssignmentType))
            {
                if (L'1' == wszAssignmentType[0])
                    fPerMachine = TRUE;
            }
            else
            {
                // This halts the enumeration and fails. Alternatively the error
                // could be logged and enumeration continued for the
                // remainder of the products
                uiStatus = ERROR_FUNCTION_FAILED;
                break;
            }

            // determine the "managed" status of the product.
            // If fManaged is TRUE, product is installed managed
            // and runs with elevated privileges.
            // If fManaged is FALSE, product installation operations
            // run as the user.
            if (ERROR_SUCCESS != MsiIsProductElevated(wszProductCode,
                                         &fManaged))
            {
                // This halts the enumeration and fails. Alternatively the error
                // could be logged and enumeration continued for the
                // remainder of the products
                uiStatus = ERROR_FUNCTION_FAILED;
                break;
            }

            // obtain the user friendly name of the product
            UINT uiReturn = MsiGetProductInfo(wszProductCode,INSTALLPROPERTY_PRODUCTNAME,lpProductName,&cchProductName);
            if (ERROR_MORE_DATA == uiReturn)
            {
                // try again, but with a larger product name buffer
                delete [] lpProductName;

                // returned character count does not include
                // terminating NULL
                ++cchProductName;

                lpProductName = new WCHAR[cchProductName];
                if (!lpProductName)
                {
                    uiStatus = ERROR_OUTOFMEMORY;
                    break;
                }

                uiReturn = MsiGetProductInfo(wszProductCode,INSTALLPROPERTY_PRODUCTNAME,lpProductName,&cchProductName);
            }

            if (ERROR_SUCCESS != uiReturn)
            {
                // This halts the enumeration and fails. Alternatively the error
                // could be logged and enumeration continued for the
                // remainder of the products
                uiStatus = ERROR_FUNCTION_FAILED;
                break;
            }

            // output information
            wprintf(L" Product %s:\n", lpProductName);
            wprintf(L"\t%s\n", wszProductCode);
                        wprintf(L"\tInstalled %s %s\n", 
                fPerMachine ? L"per-machine" : L"per-user",
                fManaged ? L"managed" : L"non-managed");
        }
        dwIndex++;
    }
    while (ERROR_SUCCESS == uiStatus);

    if (lpProductName)
    {
        delete [] lpProductName;
        lpProductName = NULL;
    }

    return (ERROR_NO_MORE_ITEMS == uiStatus) ? ERROR_SUCCESS : uiStatus;
}
```



## Related topics

<dl> <dt>

[**MsiEnumProducts**](/windows/desktop/api/Msi/nf-msi-msienumproductsa)
</dt> <dt>

[**MsiGetProductInfo**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoa)
</dt> <dt>

[**MsiGetProductInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoexa)
</dt> <dt>

[**MsiIsProductElevated**](/windows/desktop/api/Msi/nf-msi-msiisproductelevateda)
</dt> <dt>

[Installing a Package with Elevated Privileges for a Non-Admin](installing-a-package-with-elevated-privileges-for-a-non-admin.md)
</dt> <dt>

[Advertising a Per-User Application To Be Installed with Elevated Privileges](advertising-a-per-user-application-to-be-installed-with-elevated-privileges.md)
</dt> <dt>

[Installation Context](installation-context.md)
</dt> </dl>

 

 
