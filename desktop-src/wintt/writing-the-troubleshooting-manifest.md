---
title: Writing a Troubleshooting Manifest
description: WTP provides a troubleshooting experience that is based on detecting and resolving root causes.
ms.assetid: 617d6ee6-3485-4365-9fdb-48afd0913b81
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Troubleshooting Manifest

WTP provides a troubleshooting experience that is based on detecting and resolving root causes. Because root causes are the key component of any troubleshooting pack, the first step in writing a troubleshooting manifest is to determine the root causes that you want to address. A root cause is a potential issue that a user may experience, and can be detected by querying the state of the computer or asking the user questions.

After determining the root causes that you want to detect and resolve, you need to determine whether they fit into the local or global troubleshooting model. A manifest that uses the local troubleshooting model contains one or more root causes and each root cause specifies a troubleshooter script that is used to detect only that root cause. WTP detects the root causes in the order they are defined in the manifest. The troubleshooter scripts each focus on a single root cause, therefore you can use the same script for troubleshooting and verification. The benefit of using a single troubleshooter per root cause is that you can reuse the root cause in another pack.

A manifest that uses the global troubleshooting model also contains one or more root causes but uses a single troubleshooter to detect the root causes. The troubleshooter script determines the order in which the root causes are detected. The script can detect all the root causes or skip individual root causes (for example, the script might skip RootCauseB if RootCauseB depends on first detecting RootCauseA). You cannot use the troubleshooter script for the verification phase.

If you do not require flow control between root causes, use the local model instead of the global model.

The troubleshooting manifest is an XML document. The extension for the manifest file must be DIAGPKG. For details of the XML elements used in the manifest, see [Package Schema](package-schema.md). WTP includes the Windows Troubleshooting Pack Designer tool in the \\Bin\\TSPDesigner folder of the Windows SDK that you can use to author manifests and build troubleshooting packs. If you use Visual Studio as your XML editor, add the package and resource schemas to the project (see the XML menu). The XML editor provides Intellisense, inline schema validation, and other features to make writing the manifest easy and accurate.

If you are creating a manifest with local troubleshooters, the following example shows the root tag that you would use. For a complete example, see [A Complete Manifest Example Using a Local Troubleshooter](a-complete-local-manifest-example.md).


```XML
<?xml version="1.0" encoding="utf-8"?>
<dcmPS:AdvDiagnosticPackage SchemaVersion="1.0" Localized="false" 
    xmlns:dcmPS="http://www.microsoft.com/schemas/dcm/package/2007" 
    xmlns:dcmRS="http://www.microsoft.com/schemas/dcm/resource/2007">

    <DiagnosticIdentification></DiagnosticIdentification>
    <DisplayInformation></DisplayInformation>
    <PrivacyLink></PrivacyLink>
    <PowerShellVersion></PowerShellVersion>
    <SupportedOSVersion></SupportedOSVersion>
    <RootCauses></RootCauses>
    <Interactions></Interactions>
    <ExtensionPoint></ExtensionPoint>

</dcmPS:AdvDiagnosticPackage>
```



If you are creating a manifest with a global troubleshooter, the following example shows the root tag that you would use. For a complete example, see [A Complete Manifest Example Using a Global Troubleshooter](a-complete-global-manifest-example.md).

The following sections provide information about each component of the manifest:


```XML
<?xml version="1.0" encoding="utf-8"?>
<dcmPS:DiagnosticPackage SchemaVersion="1.0" Localized="false" 
    xmlns:dcmPS="http://www.microsoft.com/schemas/dcm/package/2007" 
    xmlns:dcmRS="http://www.microsoft.com/schemas/dcm/resource/2007">

    <DiagnosticIdentification></DiagnosticIdentification>
    <DisplayInformation></DisplayInformation>
    <PrivacyLink></PrivacyLink>
    <PowerShellVersion></PowerShellVersion>
    <SupportedOSVersion></SupportedOSVersion>
    <Troubleshooter></Troubleshooter>
    <RootCauses></RootCauses>
    <Interactions></Interactions>
    <ExtensionPoint></ExtensionPoint>

</dcmPS:DiagnosticPackage>
```



-   [Identifying the troubleshooting pack](#identifying-the-troubleshooting-pack)
-   [Providing a description of the troubleshooting pack](#providing-a-description-of-the-troubleshooting-pack)
-   [Providing privacy information](#providing-privacy-information)
-   [Specifying the minimum Windows PowerShell requirements](#specifying-the-minimum-windows-powershell-requirements)
-   [Specifying the minimum supported operating system](#specifying-the-minimum-supported-operating-system)
-   [Specifying the troubleshooter for a manifest with a global troubleshooter](#specifying-the-troubleshooter-for-a-manifest-with-a-global-troubleshooter)
-   [Defining the root causes](#defining-the-root-causes)
-   [Defining the interactions used in the scripts](#defining-the-interactions-used-in-the-scripts)
-   [Specifying extension points](#specifying-extension-points)

### Identifying the troubleshooting pack

To identify the pack, use the [**DiagnosticIdentification**](package-diagnosticidentification-complextype.md) element. The identification section contains a string identifier and a version string that identifies the manifest.

The following shows an example of the [**DiagnosticIdentification**](package-diagnosticidentification-complextype.md) section of the manifest.


```XML
    <DiagnosticIdentification>
        <ID>PopupBlocker</ID>
        <Version>1.0</Version>
    </DiagnosticIdentification>
```



### Providing a description of the troubleshooting pack

To identify the pack in a client application (for example, in MSDT.exe), use the [**DisplayInformation**](package-displayinformation-complextype.md) element. The display section contains a name and description that are displayed in the client. The name should be short and describe the purpose of the pack. The description should be a more verbose description of the pack (maybe one to two sentences). Specify parameters if the description contains substitution strings. (You should avoid using substitution strings in the name.)

The following shows an example of the [**DisplayInformation**](package-displayinformation-complextype.md) section of the manifest.


```XML
    <DisplayInformation>
        <Parameters/>
        <Name>Enable IE Popup Blocker</Name>
        <Description>Detects if the Popup Blocker feature of Internet Explorer is disabled. If the feature is disabled, the package enables it.</Description>
    </DisplayInformation>
```



### Providing privacy information

To provide a link to your privacy statement, use the **PrivacyLink** element. The element's text contains the URL to your privacy statement.

The following shows an example of the **PrivacyLink** element in a manifest.


```XML
    <PrivacyLink>PRIVACYURLGOESHERE</PrivacyLink>
```



### Specifying the minimum Windows PowerShell requirements

To specify the minimum version of Windows PoweShell that your scripts require, use the [**PowerShellVersion**](package-version-simpletype.md) element. The section contains a version string that identifies the minimum version of Windows PoweShell that your scripts require.

The following shows an example of the [**PowerShellVersion**](package-version-simpletype.md) section of the manifest.


```XML
    <PowerShellVersion>1.0</PowerShellVersion>
```



### Specifying the minimum supported operating system

To specify the minimum operating system version on which your package can run, use the [**SupportedOSVersion**](package-supportedosversion-complextype.md) element. The section contains a version string that identifies the minimum version of Windows that your package requires. You also specify whether the package runs on the client or server versions of Windows.

The following shows an example of the [**SupportedOSVersion**](package-supportedosversion-complextype.md) section of the manifest.


```XML
    <SupportedOSVersion clientSupported="true" serverSupported="true">6.1</SupportedOSVersion>
```



### Specifying the troubleshooter for a manifest with a global troubleshooter

A manifest with a global troubleshooter detects all the root causes defined in the manifest. To specify the troubleshooter, use the [**Troubleshooter**](package-troubleshooter-complextype.md) element. The section identifies the script to run in the troubleshooting phase. Set **RequiresInteractivity** to true if your troubleshooter uses the [Get-DiagInput](get-diaginput-cmdlet.md) cmdlet.

The following shows an example of the [**Troubleshooter**](package-troubleshooter-complextype.md) section of the manifest.


```XML
    <Troubleshooter>
        <Script>
            <Parameters/>
            <ProcessArchitecture>Any</ProcessArchitecture>
            <RequiresElevation>false</RequiresElevation>
            <RequiresInteractivity>false</RequiresInteractivity>
            <FileName>DetectPopupBlockerSettings.ps1</FileName>
            <ExtensionPoint/>
        </Script>
        <ExtensionPoint/>
    </Troubleshooter>
```



### Defining the root causes

The contents of this section of the manifest depends on whether the manifest uses local or global troubleshooters. If the manifest uses local troubleshooters, this section specifies the root causes that you want to detect, and for each root cause, it specifies the troubleshooter script, one or more resolver scripts, and the verifier script. If the manifest uses a global troubleshooter, the contents are the same except that because only one troubleshooter script is used to detect all root causes, it is defined globally (outside of this section).

The following shows an example of the [**Rootcauses**](package-localrootcauses-complextype.md) section of a local manifest.


```XML
    <Rootcauses>
        <Rootcause>
            <ID>DetectPopupBlocker</ID>

            <DisplayInformation>
                <Parameters/>
                <Name>Detect IE Popup Blocker Settings</Name>
                <Description>Detects if the Popup Blocker feature of Internet Explorer is disabled.</Description>
            </DisplayInformation>
           
            <Troubleshooter>
                <Script>
                    <Parameters/>
                    <ProcessArchitecture>Any</ProcessArchitecture>
                    <RequiresElevation>false</RequiresElevation>
                    <RequiresInteractivity>false</RequiresInteractivity>
                    <FileName>DetectPopupBlockerSettings.ps1</FileName>
                    <ExtensionPoint/>
                </Script>
                <ExtensionPoint/>
            </Troubleshooter>

            <Resolvers>
                <Resolver>
                    <ID>ResolvePopupBlocker</ID>

                    <DisplayInformation>
                        <Parameters/>
                        <Name>Enable IE Popup Blocker</Name>
                        <Description>Enables the Popup Blocker feature of Internet Explorer if it is disabled.</Description>
                    </DisplayInformation>

                    <RequiresConsent>false</RequiresConsent>

                    <Script>
                        <Parameters/>
                        <ProcessArchitecture>Any</ProcessArchitecture>
                        <RequiresElevation>false</RequiresElevation>
                        <RequiresInteractivity>false</RequiresInteractivity>
                        <FileName>ResolvePopupBlockerSettings.ps1</FileName>
                        <ExtensionPoint/>
                    </Script>
                    <ExtensionPoint/>
                </Resolver>
            </Resolvers>

            <Verifier>
                <Script>
                    <Parameters/>
                    <ProcessArchitecture>Any</ProcessArchitecture>
                    <RequiresElevation>false</RequiresElevation>
                    <RequiresInteractivity>false</RequiresInteractivity>
                    <FileName>DetectPopupBlockerSettings.ps1</FileName>
                    <ExtensionPoint/>
                </Script>
                <ExtensionPoint/>
            </Verifier>

            <ContextParameters/>
            <ExtensionPoint/>
        </Rootcause>
    </Rootcauses>
    
```



### Defining the interactions used in the scripts

If your scripts interact with the user (for example, request input from the user), you need to specify the interactions in the manifest. To specify the interactions, use the [**Interactions**](package-interactions-complextype.md) element. For details on using interactions, see [Interacting with the User](interacting-with-the-user.md).

The following shows an example of the [**Interactions**](package-interactions-complextype.md) section of the manifest.


```XML
    <Interactions>
        <SingleResponseInteractions/>
        <MultipleResponseInteractions/>
        <TextInteractions/>
        <PauseInteractions/>
        <LaunchUIInteractions/>
    </Interactions>
```



### Specifying extension points

To specify extensions that are specific to the client consuming the pack, use the [**ExtensionPoint**](package-extensionpoint-complextype.md) element. The MSDT client supports extensions for interactions, to specify an icon for the package, and to provide help keywords that you can define at the package or root cause level (the keywords are used to search for additional information related to a root cause that was not fixed).

 

 




