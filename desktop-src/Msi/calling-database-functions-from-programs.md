---
Description: Before calling any of the following Database Functions from a program, such as a custom action or an automation process, the installer must first run the CostInitialize action, FileCost action, and CostFinalize action.
ms.assetid: b9795825-41fa-474b-a0c5-06770aa99bc1
title: Calling Database Functions from Programs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Calling Database Functions from Programs

Before calling any of the following [Database Functions](database-functions.md) from a program, such as a custom action or an automation process, the installer must first run the [CostInitialize action](costinitialize-action.md), [FileCost action](filecost-action.md), and [CostFinalize action](costfinalize-action.md).

The following is a list of database functions used in Windows Installer:

-   [**MsiGetComponentState**](/windows/win32/Msiquery/nf-msiquery-msigetcomponentstatea?branch=master)
-   [**MsiGetFeatureCost**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturecosta?branch=master)
-   [**MsiGetFeatureState**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturestatea?branch=master)
-   [**MsiGetFeatureValidStates**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturevalidstatesa?branch=master)
-   [**MsiGetSourcePath**](/windows/win32/Msiquery/nf-msiquery-msigetsourcepatha?branch=master)
-   [**MsiGetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msigettargetpatha?branch=master)
-   [**MsiSetComponentState**](/windows/win32/Msiquery/nf-msiquery-msisetcomponentstatea?branch=master)
-   [**MsiSetFeatureState**](/windows/win32/Msiquery/nf-msiquery-msisetfeaturestatea?branch=master)
-   [**MsiSetInstallLevel**](/windows/win32/Msiquery/nf-msiquery-msisetinstalllevel?branch=master)
-   [**MsiSetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msisettargetpatha?branch=master)
-   [**MsiVerifyDiskSpace**](/windows/win32/Msiquery/nf-msiquery-msiverifydiskspace?branch=master)

Before calling [**MsiSetFeatureAttributes**](/windows/win32/Msiquery/nf-msiquery-msisetfeatureattributesa?branch=master) from a program, the installer must first run the CostInitialize action. The installer then runs the CostFinalize action after **MsiSetFeatureAttributes**.

The following example illustrates the order in which function actions must be called when using [**MsiGetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msigettargetpatha?branch=master) in a program.


```C++
#include <windows.h>
#include <Msiquery.h>
#include <tchar.h>
#pragma comment(lib, "msi.lib") 

int main()  
{ 

MSIHANDLE hInstall;
TCHAR *szBuf;
DWORD cch  = 0 ;
 
if(MsiOpenPackage(_T("PathToPackage...."), &amp;hInstall) == ERROR_SUCCESS)
{
    if(MsiDoAction(hInstall, _T("CostInitialize"))==ERROR_SUCCESS  
        &amp;&amp; MsiDoAction(hInstall, _T("FileCost"))==ERROR_SUCCESS  
        &amp;&amp; MsiDoAction(hInstall, _T("CostFinalize"))==ERROR_SUCCESS)   
    { 
        if(MsiGetTargetPath(hInstall, _T("FolderName"), _T(""),&amp;cch)==ERROR_MORE_DATA)
        { 
            cch++; // add 1 to include null terminator since MsiGetTargetPath does not include it on return 
            szBuf = (TCHAR *) malloc(cch*sizeof(TCHAR));
            if(szBuf)
            {
                if(MsiGetTargetPath(hInstall, _T("FolderName"), szBuf,&amp;cch)==ERROR_SUCCESS)
                {
                    // Add code to use szBuf here
                }
                free(szBuf);
            }
        } 
    } 
    MsiCloseHandle(hInstall);
}

return 0;  
}
```



 

 



