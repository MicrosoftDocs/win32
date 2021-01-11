---
description: This tutorial demonstrates how to take a monolingual application and make it world-ready. This application is in the form of a complete solution that is built within Microsoft Visual Studio.
ms.assetid: 6d71aa90-8444-4f30-a2f8-f1a2aab015b0
title: Adding Multilingual User Interface Support to an Application
ms.topic: article
ms.date: 05/31/2018
---

# Adding Multilingual User Interface Support to an Application

This tutorial demonstrates how to take a monolingual application and make it world-ready. This application is in the form of a complete solution that is built within Microsoft Visual Studio.

-   [Overview](#splitting-the-various-language-resource-modules-an-overview)
    -   [The Idea Behind Hello MUI](#the-idea-behind-hello-mui)
-   [Setting up the Hello MUI Solution](#setting-up-the-hello-mui-solution)
    -   [Platform Requirements](#platform-requirements)
    -   [Prerequisites](#prerequisites)
-   [Step 0: Creating the Hard-coded Hello MUI](#step-0-creating-the-hard-coded-hello-mui)
-   [Step 1: Implementing the Basic Resource Module](#step-1-implementing-the-basic-resource-module)
-   [Step 2: Building the Basic Resource Module](#step-2-building-the-basic-resource-module)
    -   [Splitting the Various Language Resource Modules: An Overview](#splitting-the-various-language-resource-modules-an-overview)
    -   [Splitting the Various Language Resource Modules: Creating the Files](#splitting-the-various-language-resource-modules-creating-the-files)
-   [Step 3: Creating a Resource-Savvy "Hello MUI"](#step-3-creating-a-resource-savvy-hello-mui)
-   [Step 4: Globalizing "Hello MUI"](#step-4-globalizing-hello-mui)
-   [Step 5: Customizing "Hello MUI"](#step-5-customizing-hello-mui)
-   [Additional Considerations for MUI](#additional-considerations-for-mui)
    -   [Support for Console Applications](#support-for-console-applications)
    -   [Determination of Languages to Support at Run-Time](#determination-of-languages-to-support-at-run-time)
    -   [Complex Script Support in Versions Prior to Windows Vista](#complex-script-support-in-versions-prior-to-windows-vista)
-   [Summary](#summary)

## Overview

Beginning with Windows Vista, the Windows operating system itself was built from the ground up to be a multilingual platform, with additional support that enables you to create multilingual applications that use the Windows MUI resource model.

This tutorial illustrates this new support for multilingual applications by covering the following aspects:

-   Uses the improved MUI platform support to easily enable multilingual applications.
-   Extends multilingual applications to run on versions of Windows prior to Windows Vista.
-   Touches on the additional considerations involved in developing specialized multilingual applications such as console applications.

These links help provide a quick refresher on the concepts on internationalization and MUI:

-   [Quick overview of internationalization](understanding-internationalization.md).
-   [MUI Concepts](understanding-mui.md).
-   [Using MUI to develop Win32 applications](using-multilingual-user-interface.md).

### The Idea Behind Hello MUI

You are probably familiar with the classic Hello World application, which illustrates basic programming concepts. This tutorial takes a similar approach to illustrate how to use the MUI resource model to update a monolingual application to create a multilingual version called Hello MUI.

> [!Note]  
> The tasks in this tutorial are described in detailed steps because of the precision with which these activities must be performed, and the need to explain the details to developers who have little experience with these tasks.

 

## Setting up the Hello MUI Solution

These steps outline how to prepare to create the Hello MUI solution.

### Platform Requirements

You must compile the code samples in this tutorial using the Windows Software Development Kit (SDK) for Windows 7 and Visual Studio 2008. The Windows 7 SDK will install on Windows XP, Windows Vista and Windows 7, and the sample solution can be built on any of these operating system versions.

All code samples in this tutorial are designed to be executed on x86 and x64 versions of Windows XP, Windows Vista and Windows 7. Specific parts that will not work on Windows XP are called out where appropriate.

### Prerequisites

1.  Install Visual Studio 2008.

    For more information, see the [Visual Studio Developer Center](https://msdn.microsoft.com/vstudio/default.aspx).

2.  Install the Windows SDK for Windows 7.

    You can install it from the Windows SDK page of the [Windows Developer Center](https://msdn.microsoft.com/windowsserver/bb980924.aspx). The SDK includes utilities to develop applications for OS versions starting from Windows XP through the most recent.

    > [!Note]  
    > If you are not installing the package to the default location, or if you are not installing on the system drive, which is usually the C drive, make note of the install path.

     

3.  Configure the Visual Studio command line parameters.

    1.  Open a Visual Studio command window.
    2.  Type **set path**.
    3.  Confirm that the path variable includes the path of the bin folder of the Windows 7 SDK: ...Microsoft SDKs\\Windows\\v7.0\\bin

4.  Install the Microsoft NLS downlevel APIs add-on package.
    > [!Note]  
    > In the context of this tutorial, this package is necessary only if you will be customizing the application to run on Windows versions prior to Windows Vista. See [Step 5: Customizing Hello MUI](#step-5-customizing-hello-mui).

     

    1.  Download and install the package from its [download site](https://www.microsoft.com/downloads/details.aspx?FamilyID=eb72cda0-834e-4c35-9419-ff14bc349c9d&amp;DisplayLang=en).
    2.  As with the Windows SDK, if you are not installing the package to the default location, or if you are not installing on the system drive, which is usually the C drive, make note of the install path.
    3.  If your development platform is Windows XP or Windows Server 2003, confirm that Nlsdl.dll is installed and registered correctly.

        1.  Browse to the "redist" folder under the install path location.
        2.  Run the appropriate redistributable Nlsdl.\*.exe, such as nlsdl.x86.exe. This step installs and registers Nlsdl.dll.

    > [!Note]  
    > If you develop an application that uses MUI and that must run on Windows versions prior to Windows Vista, Nlsdl.dll must be present on the destination Windows platform. In most cases, this means that the application needs to carry and install the redistributable Nlsdl installer (and not merely copy Nlsdl.dll itself).

     

## Step 0: Creating the Hard-coded Hello MUI

This tutorial begins with the monolingual version of the Hello MUI application. The application assumes the use of the C++ programming language, wide character strings, and the [**MessageBoxW**](/windows/win32/api/winuser/nf-winuser-messagebox) function for output.

Begin by creating the initial GuiStep\_0 application, as well as the HelloMUI solution, which contain all of the applications in this tutorial.

1.  In Visual Studio 2008, create a new project. Use the following settings and values:

    1.  Project type: Under Visual C++ select Win32, and then under Visual Studio installed templates select Win32 Project.
    2.  Name: GuiStep\_0.
    3.  Location: *ProjectRootDirectory* (Later steps reference this directory).
    4.  Solution Name: HelloMUI.
    5.  Select Create directory for solution.
    6.  In the Win32 Application Wizard, select the default Application type: Windows application.

2.  Configure the project threading model:

    1.  In the Solution Explorer, right-click the project GuiStep\_0, and then select Properties.
    2.  In the project Property Pages dialog box:

        1.  In the top left drop-down, set Configuration to All Configurations.
        2.  Under Configuration Properties expand C/C++, select Code Generation, and set Runtime Library: Multi-threaded Debug (/MTd).

3.  Replace the contents of GuiStep\_0.cpp with the following code:
    ```C++
    // GuiStep_0.cpp : Defines the entry point for the application.
    //

    #include "stdafx.h"
    #include "GuiStep_0.h"

    int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
    {
        UNREFERENCED_PARAMETER(hInstance);
        UNREFERENCED_PARAMETER(hPrevInstance);
        UNREFERENCED_PARAMETER(lpCmdLine);
        UNREFERENCED_PARAMETER(nCmdShow);

        MessageBoxW(NULL,L"Hello MUI",L"HelloMUI!",MB_OK | MB_ICONINFORMATION);
        return 0;
    }
    ```

    

4.  Build and run the application.

The straightforward source code above makes the simplistic design choice of hard-coding, or embedding, all the output the user will see—in this case the text "Hello MUI". This choice limits the utility of the application for users who don't recognize the English word "Hello." Because MUI is a technology-based English acronym, it is assumed for this tutorial that the string remains "MUI" for all languages.

## Step 1: Implementing the Basic Resource Module

Microsoft Win32 has long exposed the capability for application developers to separate their UI resource data from application source code. This separation comes in the form of the Win32 resource model, in which strings, bitmaps, icons, messages and other items normally displayed to a user are packaged into a distinct section of the executable, separated from executable code.

To illustrate this separation between executable code and resource data packaging, in this step the tutorial places the previously hard-coded "Hello" string (the "en-US" resource) into the resource section of a DLL module in the HelloModule\_en\_us project.

This Win32 DLL could also contain library type executable functionality (as any other DLL might). But to help focus on the Win32 resource-related aspects, we leave the run-time DLL code stubbed out in dllmain.cpp. Subsequent sections of this tutorial make use of the HelloModule resource data being built here and also present appropriate runtime code.

To construct a Win32 resource module, start by creating a DLL with a stubbed out dllmain:

1.  Add a new project to the HelloMUI solution:

    1.  From the File menu, select Add, and then New Project.
    2.  Project type: Win32 Project.
    3.  Name: HelloModule\_en\_us.
    4.  Location: *ProjectRootDirectory*\\HelloMUI.
    5.  In the Win32 Application Wizard, select Application type: DLL.

2.  Configure this project's threading model:

    1.  In the Solution Explorer, right-click the project HelloModule\_en\_us and select Properties.
    2.  In the project's Property Pages dialog box:

        1.  In the top left drop-down, set Configuration to All Configurations.
        2.  Under Configuration Properties expand C/C++, select Code Generation, and set Runtime Library: Multi-threaded Debug (/MTd).

3.  Examine dllmain.cpp. (You may want to add the UNREFERENCED\_PARAMETER macros to the generated code, as we have here, to enable it to compile at warning level 4.)
    ```C++
    // dllmain.cpp : Defines the entry point for the DLL application.
    #include "stdafx.h"

    BOOL APIENTRY DllMain( HMODULE hModule,
                           DWORD  ul_reason_for_call,
                           LPVOID lpReserved
                         )
    {
        UNREFERENCED_PARAMETER(hModule);
        UNREFERENCED_PARAMETER(lpReserved);

        switch (ul_reason_for_call)
        {
        case DLL_PROCESS_ATTACH:
        case DLL_THREAD_ATTACH:
        case DLL_THREAD_DETACH:
        case DLL_PROCESS_DETACH:
            break;
        }
        return TRUE;
    }
    ```

    

4.  Add a resource-definition file HelloModule.rc to the project:

    1.  Under the project HelloModule\_en\_us, right-click the Resource Files folder, and select Add, and then select New Item.
    2.  In the Add New Item dialog box, choose the following:

        1.  Categories: Under Visual C++ select Resource, and then under "Visual Studio installed templates" select Resource File (.rc).
        2.  Name: HelloModule.
        3.  Location: accept the default.
        4.  Click Add.

    3.  Specify that the new HelloModule.rc file is to be saved as Unicode:

        1.  In the Solution Explorer, right-click HelloModule.rc, and select View Code.
        2.  If you see a message that tells you that the file is already open, and asks whether you want to close it, click Yes.
        3.  With the file displayed as text, make the menu selection File and then Advanced Save Options.
        4.  Under Encoding, specify Unicode - Codepage 1200.
        5.  Click OK.
        6.  Save and close HelloModule.rc.

    4.  Add a string table containing the "Hello" string:

        1.  In the Resource View, right-click HelloModule.rc and select Add Resource.
        2.  Select String Table.
        3.  Click New.
        4.  Add a string to the String Table:

            1.  ID: HELLO\_MUI\_STR\_0.
            2.  Value: 0.
            3.  Caption: Hello.

        If you view HelloModule.rc as text now, you will see various pieces of resource-specific source code. The one of greatest interest is the section that describes the "Hello" string:

        ```C++
        /////////////////////////////////////////////////////////////////////////////
        //
        // String Table
        //

        STRINGTABLE 
        BEGIN
            HELLO_MUI_STR_0         "Hello"
        END
        ```

        

        This "Hello" string is the resource that needs to be localized (that is, translated) into every language that the application hopes to support. For example, the HelloModule\_ta\_in project (which you will create in the next step) will contain its own localized version of HelloModule.rc for "ta-IN":

        ```C++
        /////////////////////////////////////////////////////////////////////////////
        //
        // String Table
        //

        STRINGTABLE 
        BEGIN
            HELLO_MUI_STR_0         "வணக்கம்"
        END
        ```

        

    5.  Build the HelloModule\_en\_us project to be sure there are no errors.

5.  Create six more projects in the HelloMUI solution (or as many of them as you wish) to create six more resource DLLs for additional languages. Use the values in this table:

    | Project name        | Name of .rc file | String ID          | String value | String caption |
    |---------------------|------------------|--------------------|--------------|----------------|
    | HelloModule\_de\_de | HelloModule      | HELLO\_MUI\_STR\_0 | 0            | Hallo          |
    | HelloModule\_es\_es | HelloModule      | HELLO\_MUI\_STR\_0 | 0            | Hola           |
    | HelloModule\_fr\_fr | HelloModule      | HELLO\_MUI\_STR\_0 | 0            | Bonjour        |
    | HelloModule\_hi\_in | HelloModule      | HELLO\_MUI\_STR\_0 | 0            | नमस्           |
    | HelloModule\_ru\_ru | HelloModule      | HELLO\_MUI\_STR\_0 | 0            | Здравствуйте   |
    | HelloModule\_ta\_in | HelloModule      | HELLO\_MUI\_STR\_0 | 0            | வணக்கம்        |

    

     

For more about .rc file structure and syntax, see [About Resource Files](../menurc/about-resource-files.md).

## Step 2: Building the Basic Resource Module

Using previous resource models, building any one of the seven HelloModule projects would result in seven separate DLLs. Each DLL would contain a resource section with a single string localized into the appropriate language. Although appropriate for the historic Win32 resource model, this design does not take advantage of MUI.

In the Windows Vista SDK and later, MUI provides the ability to split executables into source code and localizable content modules. With the additional customization that is covered later in Step 5, applications can be enabled for multi-lingual support to run on versions prior to Windows Vista.

The primary mechanisms available to split resources from executable code, starting with Windows Vista, are:

-   Using rc.exe (the RC Compiler) with specific switches, or
-   Using a post-build style splitting tool named muirct.exe.

See [Resource Utilities](resource-utilities.md) for more information.

For the sake of simplicity, this tutorial uses muirct.exe to split the "Hello MUI" executable.

### Splitting the Various Language Resource Modules: An Overview

A multi-part process is involved in splitting the DLLs into one executable HelloModule.dll, plus a HelloModule.dll.mui for each of the seven supported languages within this tutorial. This overview describes the required steps; the next section presents a command file that performs those steps.

First, split the English-only HelloModule.dll module by using the command:


```C++
mkdir .\en-US
muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x0409 -g 0x0407 .\HelloModule_en_us.dll .\HelloModule.dll .\en-US\HelloModule.dll.mui
```



The command line above uses the configuration file DoReverseMuiLoc.rcconfig. This type of configuration file is typically used by muirct.exe to split resources between the language-neutral (LN) DLL and the language-dependent .mui files. In this case, the DoReverseMuiLoc.rcconfig xml file (listed in the next section) indicates many resource types, but they all fall into the "localizedResources" or .mui file category, and there are no resources in the language-neutral category. For more information about how to prepare a resource configuration file, see [Preparing a Resource Configuration File](preparing-a-resource-configuration-file.md).

In addition to creating a HelloModule.dll.mui file which contains the English string "Hello", muirct.exe also embeds a MUI resource into the HelloModule.dll module during the splitting. In order to properly load at run-time the appropriate resources from the language-specific HelloModule.dll.mui modules, each .mui file must have its checksums fixed-up to match the checksums in the baseline language-neutral LN module. This is done by a command such as:


```C++
muirct.exe -c HelloModule.dll -e en-US\HelloModule.dll.mui
```



Similarly, muirct.exe is invoked to create a HelloModule.dll.mui file for each of the other languages. However, in those cases the language-neutral DLL is discarded, as only the first one created will be needed. The commands that process the Spanish and French resources look like this:


```C++
mkdir .\es-ES
muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x0C0A -g 0x0407 .\HelloModule_es_es.dll .\HelloModule_discard.dll .\es-ES\HelloModule.dll.mui
muirct.exe -c HelloModule.dll -e es-ES\HelloModule.dll.mui

mkdir .\fr-FR
muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x040C -g 0x0407 .\HelloModule_fr_fr.dll .\HelloModule_discard.dll .\fr-FR\HelloModule.dll.mui
muirct.exe -c HelloModule.dll -e fr-FR\HelloModule.dll.mui
```



One of the most important things to notice in the muirct.exe command lines above is that the -x flag is used to specify a target language ID. The value provided to muirct.exe is different for each language-specific HelloModule.dll module. This language value is central and is used by muirct.exe to appropriately mark the .mui file during splitting. An incorrect value produces resource loading failures for that particular .mui file at run-time. See [Language Identifier Constants and Strings](language-identifier-constants-and-strings.md) for more details on mapping language name to LCID.

Each split .mui file ends up being placed into a directory corresponding to its language name, immediately underneath the directory in which the language-neutral HelloModule.dll will reside. For more about .mui file placement, see [Application Deployment](application-deployment.md).

### Splitting the Various Language Resource Modules: Creating the Files

For this tutorial you create a command file containing the commands to split the various DLLs, and you invoke it manually. Note that in actual development work, you could reduce the potential for build errors by including these commands as pre-build or post-build events in the HelloMUI solution, but that is beyond the scope of this tutorial.

Create the files for the debug build:

1.  Create a command file DoReverseMuiLoc.cmd containing the following commands:
    ```C++
    mkdir .\en-US
    muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x0409 -g 0x0407 .\HelloModule_en_us.dll .\HelloModule.dll .\en-US\HelloModule.dll.mui
    muirct.exe -c HelloModule.dll -e en-US\HelloModule.dll.mui

    mkdir .\de-DE
    muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x0407 -g 0x0407 .\HelloModule_de_de.dll .\HelloModule_discard.dll .\de-DE\HelloModule.dll.mui
    muirct.exe -c HelloModule.dll -e de-DE\HelloModule.dll.mui

    mkdir .\es-ES
    muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x0C0A -g 0x0407 .\HelloModule_es_es.dll .\HelloModule_discard.dll .\es-ES\HelloModule.dll.mui
    muirct.exe -c HelloModule.dll -e es-ES\HelloModule.dll.mui

    mkdir .\fr-FR
    muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x040C -g 0x0407 .\HelloModule_fr_fr.dll .\HelloModule_discard.dll .\fr-FR\HelloModule.dll.mui
    muirct.exe -c HelloModule.dll -e fr-FR\HelloModule.dll.mui

    mkdir .\hi-IN
    muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x0439 -g 0x0407 .\HelloModule_hi_in.dll .\HelloModule_discard.dll .\hi-IN\HelloModule.dll.mui
    muirct.exe -c HelloModule.dll -e hi-IN\HelloModule.dll.mui

    mkdir .\ru-RU
    muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x0419 -g 0x0407 .\HelloModule_ru_ru.dll .\HelloModule_discard.dll .\ru-RU\HelloModule.dll.mui
    muirct.exe -c HelloModule.dll -e ru-RU\HelloModule.dll.mui

    mkdir .\ta-IN
    muirct.exe -q DoReverseMuiLoc.rcconfig -v 2 -x 0x0449 -g 0x0407 .\HelloModule_ta_in.dll .\HelloModule_discard.dll .\ta-IN\HelloModule.dll.mui
    muirct.exe -c HelloModule.dll -e ta-IN\HelloModule.dll.mui
    pause
    ```

    

2.  Create an xml file DoReverseMuiLoc.rcconfig containing the following lines:
    ```C++
    <?xml version="1.0" encoding="utf-8"?>
        <localization>
            <resources>
                <win32Resources fileType="Application">
                    <neutralResources>
                    </neutralResources>
                    <localizedResources>
                        <resourceType typeNameId="#1"/>
                        <resourceType typeNameId="#10"/>
                        <resourceType typeNameId="#1024"/>
                        <resourceType typeNameId="#11"/>
                        <resourceType typeNameId="#12"/>
                        <resourceType typeNameId="#13"/>
                        <resourceType typeNameId="#14"/>
                        <resourceType typeNameId="#15"/>
                        <resourceType typeNameId="#16"/>
                        <resourceType typeNameId="#17"/>
                        <resourceType typeNameId="#18"/>
                        <resourceType typeNameId="#19"/>
                        <resourceType typeNameId="#2"/>
                        <resourceType typeNameId="#20"/>
                        <resourceType typeNameId="#2110"/>
                        <resourceType typeNameId="#23"/>
                        <resourceType typeNameId="#240"/>
                        <resourceType typeNameId="#3"/>
                        <resourceType typeNameId="#4"/>
                        <resourceType typeNameId="#5"/>
                        <resourceType typeNameId="#6"/>
                        <resourceType typeNameId="#7"/>
                        <resourceType typeNameId="#8"/>
                        <resourceType typeNameId="#9"/>
                        <resourceType typeNameId="HTML"/>
                        <resourceType typeNameId="MOFDATA"/>
                    </localizedResources>
                </win32Resources>
            </resources>
        </localization>
    ```

    

3.  Copy DoReverseMuiLoc.cmd and DoReverseMuiLoc.rcconfig to *ProjectRootDirectory*\\HelloMUI\\Debug.
4.  Open the Visual Studio 2008 command prompt and navigate to the Debug directory.
5.  Run DoReverseMuiLoc.cmd.

When you create a release build, you copy the same DoReverseMuiLoc.cmd and DoReverseMuiLoc.rcconfig files to the Release directory and run the command file there.

## Step 3: Creating a Resource-Savvy "Hello MUI"

Building on the initial hard-coded GuiStep\_0.exe example from above, you could extend the reach of the application to multiple language users by choosing to incorporate the Win32 resource model. The new run-time code presented in this step includes the module loading ([**LoadLibraryEx**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexa)) and string retrieval ([**LoadString**](/windows/win32/api/winuser/nf-winuser-loadstringa)) logic.

1.  Add a new project to the HelloMUI solution (using the menu selection File, Add, and New Project) with the following settings and values:

    1.  Project type: Win32 Project.
    2.  Name: GuiStep\_1.
    3.  Location: accept the default.
    4.  In the Win32 Application Wizard, select the default Application type: Windows application.

2.  Set this project to run from within Visual Studio, and configure its threading model:

    1.  In the Solution Explorer, right-click the project GuiStep\_1 and select Set as StartUp Project.
    2.  Right-click it again and select Properties.
    3.  In the project's Property Pages dialog box:

        1.  In the top left drop-down, set Configuration to All Configurations.
        2.  Under Configuration Properties expand C/C++, select Code Generation, and set Runtime Library: Multi-threaded Debug (/MTd).

3.  Replace the contents of GuiStep\_1.cpp with the following code:
    ```C++
    // GuiStep_1.cpp : Defines the entry point for the application.
    //

    #include "stdafx.h"
    #include "GuiStep_1.h"
    #include "..\HelloModule_en_us\resource.h"

    #define SUFFICIENTLY_LARGE_STRING_BUFFER (MAX_PATH*2)
    #define SUFFICIENTLY_LARGE_ERROR_BUFFER (1024*2)
    #define HELLO_MODULE_CONTRIVED_FILE_PATH  (L"HelloModule.dll")

    int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
    {
        UNREFERENCED_PARAMETER(hInstance);
        UNREFERENCED_PARAMETER(hPrevInstance);
        UNREFERENCED_PARAMETER(lpCmdLine);
        UNREFERENCED_PARAMETER(nCmdShow);

        // The following code presents a hypothetical, yet common use pattern of MUI technology
        WCHAR displayBuffer[SUFFICIENTLY_LARGE_ERROR_BUFFER];

        // 1. Basic application obtains access to the proper resource container 
        // for standard Win32 resource loading this is normally a PE module - use LoadLibraryEx
        // LoadLibraryEx is the preferred alternative for resource modules as used below because it
        // provides increased security and performance over that of LoadLibrary
        HMODULE resContainer = LoadLibraryExW(HELLO_MODULE_CONTRIVED_FILE_PATH,NULL,LOAD_LIBRARY_AS_IMAGE_RESOURCE | LOAD_LIBRARY_AS_DATAFILE);
        if(!resContainer)
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to load the resource container module, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }

        // 2. Application parses the resource container to find the appropriate item
        WCHAR szHello[SUFFICIENTLY_LARGE_STRING_BUFFER];
        if(LoadStringW(resContainer,HELLO_MUI_STR_0,szHello,SUFFICIENTLY_LARGE_STRING_BUFFER) == 0)
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to load the resource string, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            FreeLibrary(resContainer);
            return 1; // exit
        }

        // 3. Application presents the discovered resource to the user via UI
        swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"%s MUI",szHello);
        MessageBoxW(NULL,displayBuffer,L"HelloMUI",MB_OK | MB_ICONINFORMATION);

        // 4. Application cleans up memory associated with the resource container after this item is no longer needed.
        if(!FreeLibrary(resContainer))
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to unload the resource container, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }

        return 0;
    }
    ```

    

4.  Build and run the application. The output will be displayed in the language currently set as the display language of the computer (provided it is one of the seven languages we have built).

## Step 4: Globalizing "Hello MUI"

Although the previous example is able to display its output in different languages, it falls short in a number of areas. Perhaps the most noticeable is that the application is only available in a small subset of languages when compared to the Windows operating system itself. If, for example, the GuiStep\_1 application from the previous step were installed on a Japanese build of Windows, resource location failures would be likely.

To address this situation, you have two primary options:

-   Ensure that resources in a predetermined ultimate fallback language are included.
-   Provide a way for the end user to configure their language preferences from among the subset of languages specifically supported by the application.

Of these options, the one providing an ultimate fallback language is highly advisable and is implemented in this tutorial by passing the -g flag to muirct.exe, as seen above. This flag tells muirct.exe to make a specific language (de-DE / 0x0407) the ultimate fallback language associated with the language-neutral dll module (HelloModule.dll). At run-time this parameter is used as a last resort to generate text to display to the user. In the event that an ultimate fallback language is not found and no appropriate resource is available in the language-neutral binary, loading of the resource fails. Therefore you should carefully determine the scenarios that your application might encounter and plan the ultimate fallback language accordingly.

The other option of allowing for configurable language preferences and loading resources based on this user-defined hierarchy can greatly increase customer satisfaction. Unfortunately, it also complicates the functionality needed within the application.

This step of the tutorial uses a simplified text file mechanism to enable custom user language configuration. The text file is parsed at run-time by the application, and the parsed and validated language list is used in establishing a custom fallback list. After the custom fallback list is established, the Windows APIs will load resources according to the language precedence set forth in this list. The remainder of the code is similar to that found in the preceding step.

1.  Add a new project to the HelloMUI solution (using the menu selection File, Add, and New Project) with the following settings and values:

    1.  Project type: Win32 Project.
    2.  Name: GuiStep\_2.
    3.  Location: accept the default.
    4.  In the Win32 Application Wizard, select the default Application type: Windows application.

2.  Set this project to run from within Visual Studio, and configure its threading model:

    1.  In the Solution Explorer, right-click the project GuiStep\_2 and select Set as StartUp Project.
    2.  Right-click it again and select Properties.
    3.  In the project's Property Pages dialog box:

        1.  In the top left drop-down, set Configuration to All Configurations.
        2.  Under Configuration Properties expand C/C++, select Code Generation, and set Runtime Library: Multi-threaded Debug (/MTd).

3.  Replace the contents of GuiStep\_2.cpp with the following code:
    ```C++
    // GuiStep_2.cpp : Defines the entry point for the application.
    //

    #include "stdafx.h"
    #include "GuiStep_2.h"
    #include <strsafe.h>
    #include "..\HelloModule_en_us\resource.h"

    #define SUFFICIENTLY_LARGE_STRING_BUFFER (MAX_PATH*2)
    #define USER_CONFIGURATION_STRING_BUFFER (((LOCALE_NAME_MAX_LENGTH+1)*5)+1)
    #define SUFFICIENTLY_LARGE_ERROR_BUFFER (1024*2)
    #define HELLO_MODULE_CONTRIVED_FILE_PATH  (L"HelloModule.dll")

    BOOL GetMyUserDefinedLanguages(WCHAR * langStr, DWORD langStrSize);
    BOOL ConvertMyLangStrToMultiLangStr(WCHAR * langStr, WCHAR * langMultiStr, DWORD langMultiStrSize);

    int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
    {
        UNREFERENCED_PARAMETER(hInstance);
        UNREFERENCED_PARAMETER(hPrevInstance);
        UNREFERENCED_PARAMETER(lpCmdLine);
        UNREFERENCED_PARAMETER(nCmdShow);

        // The following code presents a hypothetical, yet common use pattern of MUI technology
        WCHAR displayBuffer[SUFFICIENTLY_LARGE_ERROR_BUFFER];

        // 1. Application starts by applying any user defined language preferences
        // (language setting is potentially optional for an application that wishes to strictly use OS system language fallback)
        // 1a. Application looks in pre-defined location for user preferences (registry, file, web, etc.)
        WCHAR userLanguagesString[USER_CONFIGURATION_STRING_BUFFER*2];
        if(!GetMyUserDefinedLanguages(userLanguagesString,USER_CONFIGURATION_STRING_BUFFER*2))
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to find the user defined language configuration, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }
        // 1b. Application converts the user defined 'readable' languages to the proper multi-string 'less readable' language name format
        WCHAR userLanguagesMultiString[USER_CONFIGURATION_STRING_BUFFER];
        if(!ConvertMyLangStrToMultiLangStr(userLanguagesString,userLanguagesMultiString,USER_CONFIGURATION_STRING_BUFFER))
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to convert the user defined language configuration to multi-string, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }
        // 1c. Application now sets the appropriate fallback list
        DWORD langCount = 0;
        // next commented out line of code could be used on Windows 7 and later
        // using SetProcessPreferredUILanguages is recomended for new applications (esp. multi-threaded applications)
    //    if(!SetProcessPreferredUILanguages(MUI_LANGUAGE_NAME,userLanguagesMultiString,&langCount) || langCount == 0)
        // the following line of code is supported on Windows Vista and later
        if(!SetThreadPreferredUILanguages(MUI_LANGUAGE_NAME,userLanguagesMultiString,&langCount) || langCount == 0)
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to set the user defined languages, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }
        // NOTES on step #1:
        // an application developer that makes the assumption the fallback list provided by the
        // system / OS is entirely sufficient may or may not be making a good assumption based 
        // mostly on:
        // A. your choice of languages installed with your application
        // B. the languages on the OS at application install time
        // C. the OS users propensity to install/uninstall language packs
        // D. the OS users propensity to change laguage settings

        // 2. Application obtains access to the proper resource container 
        // for standard Win32 resource loading this is normally a PE module - use LoadLibraryEx
        // LoadLibraryEx is the preferred alternative for resource modules as used below because it
        // provides increased security and performance over that of LoadLibrary
        HMODULE resContainer = LoadLibraryExW(HELLO_MODULE_CONTRIVED_FILE_PATH,NULL,LOAD_LIBRARY_AS_IMAGE_RESOURCE | LOAD_LIBRARY_AS_DATAFILE);
        if(!resContainer)
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to load the resource container module, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }

        // 3. Application parses the resource container to find the appropriate item
        WCHAR szHello[SUFFICIENTLY_LARGE_STRING_BUFFER];
        if(LoadStringW(resContainer,HELLO_MUI_STR_0,szHello,SUFFICIENTLY_LARGE_STRING_BUFFER) == 0)
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to load the resource string, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            FreeLibrary(resContainer);
            return 1; // exit
        }

        // 4. Application presents the discovered resource to the user via UI
        swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"%s MUI",szHello);
        MessageBoxW(NULL,displayBuffer,L"HelloMUI",MB_OK | MB_ICONINFORMATION);

        // 5. Application cleans up memory associated with the resource container after this item is no longer needed.
        if(!FreeLibrary(resContainer))
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to unload the resource container, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }

        return 0;
    }

    BOOL GetMyUserDefinedLanguages(WCHAR * langStr, DWORD langStrSize)
    {
        BOOL rtnVal = FALSE;
        // very simple implementation - assumes that first 'langStrSize' characters of the 
        // L".\\langs.txt" file comprises a string of one or more languages
        HANDLE langConfigFileHandle = CreateFileW(L".\\langs.txt", GENERIC_READ, 0, 
            NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
        if(langConfigFileHandle != INVALID_HANDLE_VALUE)
        {
            // clear out the input variables
            DWORD bytesActuallyRead = 0;
            if(ReadFile(langConfigFileHandle,langStr,langStrSize*sizeof(WCHAR),&bytesActuallyRead,NULL) && bytesActuallyRead > 0)
            {
                rtnVal = TRUE;
                DWORD nullIndex = (bytesActuallyRead/sizeof(WCHAR) < langStrSize) ? bytesActuallyRead/sizeof(WCHAR) : langStrSize;
                langStr[nullIndex] = L'\0';
            }
            CloseHandle(langConfigFileHandle);
        }
        return rtnVal;
    }
    BOOL ConvertMyLangStrToMultiLangStr(WCHAR * langStr, WCHAR * langMultiStr, DWORD langMultiStrSize)
    {
        BOOL rtnVal = FALSE;
        size_t strLen = 0;
        rtnVal = SUCCEEDED(StringCchLengthW(langStr,USER_CONFIGURATION_STRING_BUFFER*2,&strLen));
        if(rtnVal && strLen > 0 && langMultiStr && langMultiStrSize > 0)
        {
            WCHAR * langMultiStrPtr = langMultiStr;
            WCHAR * last = langStr + (langStr[0] == 0xFEFF ? 1 : 0);
            WCHAR * context = last;
            WCHAR * next = wcstok_s(last,L",; :",&context);
            while(next && rtnVal)
            {
                // make sure you validate the user input
                if(SUCCEEDED(StringCchLengthW(last,LOCALE_NAME_MAX_LENGTH,&strLen)) && 
                    IsValidLocaleName(next))
                {
                    langMultiStrPtr[0] = L'\0';
                    rtnVal &= SUCCEEDED(StringCchCatW(langMultiStrPtr,(langMultiStrSize - (langMultiStrPtr - langMultiStr)),next));
                    langMultiStrPtr += strLen + 1;
                }
                next = wcstok_s(NULL,L",; :",&context);
                if(next)
                    last = next;
            }
            if(rtnVal && (langMultiStrSize - (langMultiStrPtr - langMultiStr))) // make sure there is a double null term for the multi-string
            {
                langMultiStrPtr[0] = L'\0';
            }
            else // fail and guard anyone whom might use the multi-string
            {
                langMultiStr[0] = L'\0';
                langMultiStr[1] = L'\0';
            }
        }
        return rtnVal;
    }
    ```

    

4.  Create a Unicode text file langs.txt containing the following line:

    ``` syntax
    hi-IN ta-IN ru-RU fr-FR es-ES en-US
    ```

    > [!Note]  
    > Be sure to save the file as Unicode.

     

    Copy langs.txt to the directory from which the program will run:

    -   If running from within Visual Studio, copy it to *ProjectRootDirectory*\\HelloMUI\\GuiStep\_2.
    -   If running from Windows Explorer, copy it to the same directory as GuiStep\_2.exe.

5.  Build and run the project. Try editing langs.txt so that different languages appear at the front of the list.

## Step 5: Customizing "Hello MUI"

A number of the run-time features mentioned so far within this tutorial are available only on Windows Vista and later. You may wish to re-use the effort invested in localizing and splitting resources by making the application work on downlevel Windows operating system versions, such as Windows XP. This process involves adjusting the previous example in two key areas:

-   The pre-Windows Vista resource loading functions (such as [**LoadString**](/windows/win32/api/winuser/nf-winuser-loadstringa), [**LoadIcon**](/windows/win32/api/winuser/nf-winuser-loadicona), [**LoadBitmap**](/windows/win32/api/winuser/nf-winuser-loadbitmapa), [**FormatMessage**](/windows/win32/api/winbase/nf-winbase-formatmessage), and others) are non-MUI aware. Applications that ship with split resources (LN and .mui files) must load resource modules using one of these two functions:

    -   If the application is to be run only on Windows Vista and later, it should load resource modules with [**LoadLibraryEx**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexa).
    -   If the application is to be run on versions prior to Windows Vista, as well as Windows Vista or later, it must use [**LoadMUILibrary**](/windows/desktop/api/Muiload/nf-muiload-loadmuilibrarya), which is a specific downlevel function provided in the Windows 7 SDK.

-   The language management and language fallback order support offered in pre-Windows Vista versions of the Windows operating system differs significantly from that in Windows Vista and later. For this reason, applications that allow user-configured language fallback must adjust their language management practices:

    -   If the application is to be run only on Windows Vista and later, setting the language list using [**SetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setthreadpreferreduilanguages) is sufficient.
    -   If the application is to be run on all Windows versions, code must be constructed that will run on downlevel platforms to iterate through the user configured language list and probe for the desired resource module. This can be seen in sections 1c and 2 of the code provided later in this step.

Create a project that can use the localized resource modules on any version of Windows:

1.  Add a new project to the HelloMUI solution (using the menu selection File, Add, and New Project) with the following settings and values:

    1.  Project type: Win32 Project.
    2.  Name: GuiStep\_3.
    3.  Location: accept the default.
    4.  In the Win32 Application Wizard, select the default Application type: Windows application.

2.  Set this project to run from within Visual Studio, and configure its threading model. Also, configure it to add the necessary headers and libraries.

    > [!Note]  
    > The paths used in this tutorial assume that the Windows 7 SDK and the Microsoft NLS downlevel APIs package were installed to their default directories. If that is not the case, modify the paths appropriately.

     

    1.  In the Solution Explorer, right-click the project GuiStep\_3 and select Set as StartUp Project.
    2.  Right-click it again and select Properties.
    3.  In the project's Property Pages dialog box:

        1.  In the top left drop-down, set Configuration to All Configurations.
        2.  Under Configuration Properties expand C/C++, select Code Generation, and set Runtime Library: Multi-threaded Debug (/MTd).
        3.  Select General and add to Additional Include Directories:

            -   "C:\\Microsoft NLS Downlevel APIs\\Include".

        4.  Select Language and set Treat wchar\_t as Built-in Type: No (/Zc:wchar\_t-).
        5.  Select Advanced and set Calling Convention: \_stdcall (/Gz).
        6.  Under Configuration Properties expand Linker, select Input, and add to Additional Dependencies:

            -   "C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Lib\\MUILoad.lib".
            -   "C:\\Microsoft NLS Downlevel APIs\\Lib\\x86\\Nlsdl.lib".

3.  Replace the contents of GuiStep\_3.cpp with the following code:
    ```C++
    // GuiStep_3.cpp : Defines the entry point for the application.
    //

    #include "stdafx.h"
    #include "GuiStep_3.h"
    #include <strsafe.h>
    #include <Nlsdl.h>
    #include <MUILoad.h>
    #include "..\HelloModule_en_us\resource.h"

    #define SUFFICIENTLY_LARGE_STRING_BUFFER (MAX_PATH*2)
    #define USER_CONFIGURATION_STRING_BUFFER (((LOCALE_NAME_MAX_LENGTH+1)*5)+1)
    #define SUFFICIENTLY_LARGE_ERROR_BUFFER (1024*2)
    #define HELLO_MODULE_CONTRIVED_FILE_PATH  (L"HelloModule.dll")

    BOOL GetMyUserDefinedLanguages(WCHAR * langStr, DWORD langStrSize);
    BOOL ConvertMyLangStrToMultiLangStr(WCHAR * langStr, WCHAR * langMultiStr, DWORD langMultiStrSize);

    int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
    {
        UNREFERENCED_PARAMETER(hInstance);
        UNREFERENCED_PARAMETER(hPrevInstance);
        UNREFERENCED_PARAMETER(lpCmdLine);
        UNREFERENCED_PARAMETER(nCmdShow);

        // The following code presents a hypothetical, yet common use pattern of MUI technology
        WCHAR displayBuffer[SUFFICIENTLY_LARGE_ERROR_BUFFER];

        // 1. Application starts by applying any user defined language preferences
        // (language setting is potentially optional for an application that wishes to strictly use OS system language fallback)
        // 1a. Application looks in pre-defined location for user preferences (registry, file, web, etc.)
        WCHAR userLanguagesString[USER_CONFIGURATION_STRING_BUFFER*2];
        if(!GetMyUserDefinedLanguages(userLanguagesString,USER_CONFIGURATION_STRING_BUFFER*2))
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to find the user defined language configuration, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }
        // 1b. Application converts the user defined 'readable' languages to the proper multi-string 'less readable' language name format
        WCHAR userLanguagesMultiString[USER_CONFIGURATION_STRING_BUFFER];
        if(!ConvertMyLangStrToMultiLangStr(userLanguagesString,userLanguagesMultiString,USER_CONFIGURATION_STRING_BUFFER))
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to convert the user defined language configuration to multi-string, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }
        // 1c. Application now attempts to set the fallback list - this is much different for a down-level 
        // shipping application when compared to a Windows Vista or Windows 7 only shipping application    
        BOOL setSuccess = FALSE;
        DWORD setLangCount = 0;
        HMODULE hDLL = GetModuleHandleW(L"kernel32.dll");
        if( hDLL )
        {
            typedef BOOL (* SET_PREFERRED_UI_LANGUAGES_PROTOTYPE ) ( DWORD, PCWSTR, PULONG );
            SET_PREFERRED_UI_LANGUAGES_PROTOTYPE fp_SetPreferredUILanguages = (SET_PREFERRED_UI_LANGUAGES_PROTOTYPE)NULL;
            fp_SetPreferredUILanguages = (SET_PREFERRED_UI_LANGUAGES_PROTOTYPE) GetProcAddress(hDLL,"SetProcessPreferredUILanguages");
            if( fp_SetPreferredUILanguages )
            {
                // call SetProcessPreferredUILanguages if it is available in Kernel32.dll's export table - Windows 7 and later
                setSuccess = fp_SetPreferredUILanguages(MUI_LANGUAGE_NAME,userLanguagesMultiString,&setLangCount);
            }
            else
            {
                fp_SetPreferredUILanguages = (SET_PREFERRED_UI_LANGUAGES_PROTOTYPE) GetProcAddress(hDLL,"SetThreadPreferredUILanguages");
                // call SetThreadPreferredUILanguages if it is available in Kernel32.dll's export table - Windows Vista and later
                if(fp_SetPreferredUILanguages)
                    setSuccess = fp_SetPreferredUILanguages(MUI_LANGUAGE_NAME,userLanguagesMultiString,&setLangCount);
            }
        }

        // 2. Application obtains access to the proper resource container 
        // for standard Win32 resource loading this is normally a PE module
        // LoadMUILibrary is the preferred alternative for loading of resource modules
        // when the application is potentially run on OS versions prior to Windows Vista
        // LoadMUILibrary is available via Windows SDK releases in Windows Vista and later
        // When available, it is advised to get the most up-to-date Windows SDK (e.g., Windows 7)
        HMODULE resContainer = NULL;
        if(setSuccess) // Windows Vista and later OS scenario
        {
            resContainer = LoadMUILibraryW(HELLO_MODULE_CONTRIVED_FILE_PATH,MUI_LANGUAGE_NAME,0);
        }
        else // this block should only be hit on Windows XP and earlier OS platforms as setSuccess will be TRUE on Windows Vista and later
        {
            // need to provide your own fallback mechanism such as the implementation below
            // in essence the application will iterate through the user configured language list
            WCHAR * next = userLanguagesMultiString;
            while(!resContainer && *next != L'\0')
            {
                // convert the language name to an appropriate LCID
                // DownlevelLocaleNameToLCID is available via standalone download package 
                // and is contained in Nlsdl.h / Nlsdl.lib
                LCID nextLcid = DownlevelLocaleNameToLCID(next,DOWNLEVEL_LOCALE_NAME);
                // then have LoadMUILibrary attempt to probe for the right .mui module
                resContainer = LoadMUILibraryW(HELLO_MODULE_CONTRIVED_FILE_PATH,MUI_LANGUAGE_NAME,(LANGID)nextLcid);
                // increment to the next language name in our list
                size_t nextStrLen = 0;
                if(SUCCEEDED(StringCchLengthW(next,LOCALE_NAME_MAX_LENGTH,&nextStrLen)))
                    next += (nextStrLen + 1);
                else
                    break; // string is invalid - need to exit
            }
            // if the user configured list did not locate a module then try the languages associated with the system
            if(!resContainer)
                resContainer = LoadMUILibraryW(HELLO_MODULE_CONTRIVED_FILE_PATH,MUI_LANGUAGE_NAME,0);
        }
        if(!resContainer)
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to load the resource container module, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }

        // 3. Application parses the resource container to find the appropriate item
        WCHAR szHello[SUFFICIENTLY_LARGE_STRING_BUFFER];
        if(LoadStringW(resContainer,HELLO_MUI_STR_0,szHello,SUFFICIENTLY_LARGE_STRING_BUFFER) == 0)
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to load the resource string, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            FreeLibrary(resContainer);
            return 1; // exit
        }

        // 4. Application presents the discovered resource to the user via UI
        swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"%s MUI",szHello);
        MessageBoxW(NULL,displayBuffer,L"HelloMUI",MB_OK | MB_ICONINFORMATION);

        // 5. Application cleans up memory associated with the resource container after this item is no longer needed.
        if(!FreeMUILibrary(resContainer))
        {
            swprintf_s(displayBuffer,SUFFICIENTLY_LARGE_ERROR_BUFFER,L"FAILURE: Unable to unload the resource container, last error = %d.",GetLastError());
            MessageBoxW(NULL,displayBuffer,L"HelloMUI ERROR!",MB_OK | MB_ICONERROR);
            return 1; // exit
        }

        return 0;
    }

    BOOL GetMyUserDefinedLanguages(WCHAR * langStr, DWORD langStrSize)
    {
        BOOL rtnVal = FALSE;
        // very simple implementation - assumes that first 'langStrSize' characters of the 
        // L".\\langs.txt" file comprises a string of one or more languages
        HANDLE langConfigFileHandle = CreateFileW(L".\\langs.txt", GENERIC_READ, 0, 
            NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
        if(langConfigFileHandle != INVALID_HANDLE_VALUE)
        {
            // clear out the input variables
            DWORD bytesActuallyRead = 0;
            if(ReadFile(langConfigFileHandle,langStr,langStrSize*sizeof(WCHAR),&bytesActuallyRead,NULL) && bytesActuallyRead > 0)
            {
                rtnVal = TRUE;
                DWORD nullIndex = (bytesActuallyRead/sizeof(WCHAR) < langStrSize) ? bytesActuallyRead/sizeof(WCHAR) : langStrSize;
                langStr[nullIndex] = L'\0';
            }
            CloseHandle(langConfigFileHandle);
        }
        return rtnVal;
    }
    BOOL ConvertMyLangStrToMultiLangStr(WCHAR * langStr, WCHAR * langMultiStr, DWORD langMultiStrSize)
    {
        BOOL rtnVal = FALSE;
        size_t strLen = 0;
        rtnVal = SUCCEEDED(StringCchLengthW(langStr,USER_CONFIGURATION_STRING_BUFFER*2,&strLen));
        if(rtnVal && strLen > 0 && langMultiStr && langMultiStrSize > 0)
        {
            WCHAR * langMultiStrPtr = langMultiStr;
            WCHAR * last = langStr + (langStr[0] == 0xFEFF ? 1 : 0);
            WCHAR * context = last;
            WCHAR * next = wcstok_s(last,L",; :",&context);
            while(next && rtnVal)
            {
                // make sure you validate the user input
                if(SUCCEEDED(StringCchLengthW(last,LOCALE_NAME_MAX_LENGTH,&strLen)) 
                    && DownlevelLocaleNameToLCID(next,0) != 0)
                {
                    langMultiStrPtr[0] = L'\0';
                    rtnVal &= SUCCEEDED(StringCchCatW(langMultiStrPtr,(langMultiStrSize - (langMultiStrPtr - langMultiStr)),next));
                    langMultiStrPtr += strLen + 1;
                }
                next = wcstok_s(NULL,L",; :",&context);
                if(next)
                    last = next;
            }
            if(rtnVal && (langMultiStrSize - (langMultiStrPtr - langMultiStr))) // make sure there is a double null term for the multi-string 
            {
                langMultiStrPtr[0] = L'\0';
            }
            else // fail and guard anyone whom might use the multi-string
            {
                langMultiStr[0] = L'\0';
                langMultiStr[1] = L'\0';
            }
        }
        return rtnVal;
    }
    ```

    

4.  Create or copy langs.txt to the appropriate directory, as previously described in [Step 4: Globalizing "Hello MUI"](#step-4-globalizing-hello-mui).
5.  Build and run the project.

> [!Note]  
> If the application should run on Windows versions prior to Windows Vista, be sure to read the documents that came with the [Microsoft NLS downlevel APIs](https://www.microsoft.com/downloads/details.aspx?FamilyID=eb72cda0-834e-4c35-9419-ff14bc349c9d&amp;DisplayLang=en) package on how to redistribute Nlsdl.dll.

 

## Additional Considerations for MUI

### Support for Console Applications

The techniques covered in this tutorial can also be used in console applications. However, unlike most standard GUI controls, the Windows command window cannot display characters for all languages. For this reason, multilingual console applications require special attention.

Calling the APIs [**SetThreadUILanguage**](/windows/desktop/api/Winnls/nf-winnls-setthreaduilanguage) or [**SetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setthreadpreferreduilanguages) with specific filtering flags causes the resource loading functions to remove language resource probes for specific languages that are not normally displayed within a command window. When these flags are set, the language-setting algorithms allow only those languages that will display properly in the command window to be on the fallback list.

For more information on using these APIs to build a multilingual console application, see the remarks sections of [**SetThreadUILanguage**](/windows/desktop/api/Winnls/nf-winnls-setthreaduilanguage) and [**SetThreadPreferredUILanguages**](/windows/desktop/api/Winnls/nf-winnls-setthreadpreferreduilanguages).

### Determination of Languages to Support at Run-Time

You can adopt one of the following design suggestions to determine which languages your application should support at run-time:

-   **During installation, enable the end user to select the preferred language from a list of supported languages**

-   **Read a language list from a configuration file**

    Some of the projects in this tutorial contain a function used to parse a langs.txt configuration file, which contains a language list.

    Because this function takes external input, validate the languages that are provided as input. See the [**IsValidLocaleName**](/windows/desktop/api/Winnls/nf-winnls-isvalidlocalename) or [**DownLevelLocaleNameToLCID**](downlevellocalenametolcid.md) functions for more details on performing that validation.

-   **Query the operating system to determine which languages are installed**

    This approach helps the application use the same language as the operating system. Although this does not require user prompting, if you choose this option, be aware that operating system languages can be added or removed at any time and can change after the user installs the application. Also, be aware that in some cases, the operating system is installed with limited language support, and the application offers more value if it supports languages that the operating system does not support.

    For more information on how to determine the currently installed languages in the operating system, see the [**EnumUILanguages**](/windows/desktop/api/Winnls/nf-winnls-enumuilanguagesa) function.

### Complex Script Support in Versions Prior to Windows Vista

When an application that supports certain complex scripts runs on a version of Windows prior to Windows Vista, text in that script may not display properly in GUI components. For example, in the downlevel project within this tutorial, hi-IN and ta-IN scripts may not display in the message box due to issues with processing complex scripts and the lack of related fonts. Normally, problems of this nature present themselves as square boxes in the GUI component.

More information about how to enable complex script processing can be found at [Script and Font Support in Windows](https://msdn.microsoft.com/goglobal/bb688099.aspx).

## Summary

This tutorial globalized a monolingual application and demonstrated the following best practices.

-   Design the application to take advantage of the Win32 resource model.
-   Utilize MUI splitting of resources into satellite binaries (.mui files).
-   Ensure that the localization process updates the resources in the .mui files to be appropriate for the target language.
-   Ensure that packaging and deployment of the application, associated .mui files, and configuration content is done correctly to allow the resource loading APIs to find the localized content.
-   Provide the end user a mechanism to adjust the language configuration of the application.
-   Adjust the run-time code to take advantage of language configuration, to make the application more responsive to end user needs.

 

 
