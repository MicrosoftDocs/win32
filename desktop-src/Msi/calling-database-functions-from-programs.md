---
Description: 'Before calling any of the following Database Functions from a program, such as a custom action or an automation process, the installer must first run the CostInitialize action, FileCost action, and CostFinalize action.'
ms.assetid: 'b9795825-41fa-474b-a0c5-06770aa99bc1'
title: Calling Database Functions from Programs
---

# Calling Database Functions from Programs

Before calling any of the following [Database Functions](database-functions.md) from a program, such as a custom action or an automation process, the installer must first run the [CostInitialize action](costinitialize-action.md), [FileCost action](filecost-action.md), and [CostFinalize action](costfinalize-action.md).

The following is a list of database functions used in Windows Installer:

-   [**MsiGetComponentState**](msigetcomponentstate.md)
-   [**MsiGetFeatureCost**](msigetfeaturecost.md)
-   [**MsiGetFeatureState**](msigetfeaturestate.md)
-   [**MsiGetFeatureValidStates**](msigetfeaturevalidstates.md)
-   [**MsiGetSourcePath**](msigetsourcepath.md)
-   [**MsiGetTargetPath**](msigettargetpath.md)
-   [**MsiSetComponentState**](msisetcomponentstate.md)
-   [**MsiSetFeatureState**](msisetfeaturestate.md)
-   [**MsiSetInstallLevel**](msisetinstalllevel.md)
-   [**MsiSetTargetPath**](msisettargetpath.md)
-   [**MsiVerifyDiskSpace**](msiverifydiskspace.md)

Before calling [**MsiSetFeatureAttributes**](msisetfeatureattributes.md) from a program, the installer must first run the CostInitialize action. The installer then runs the CostFinalize action after **MsiSetFeatureAttributes**.

The following example illustrates the order in which function actions must be called when using [**MsiGetTargetPath**](msigettargetpath.md) in a program.


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



 

 



