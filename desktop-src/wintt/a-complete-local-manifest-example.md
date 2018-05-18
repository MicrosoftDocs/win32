---
title: A Complete Manifest Example Using a Local Troubleshooter
description: The following shows a complete manifest example that uses a local troubleshooter.
ms.assetid: '88b0d03e-a08d-4aa8-bf4f-7ef071b475f8'
---

# A Complete Manifest Example Using a Local Troubleshooter

The following shows a complete manifest example that uses a local troubleshooter.


```XML
<?xml version="1.0" encoding="utf-8"?>
<dcmPS:AdvDiagnosticPackage SchemaVersion="1.0" Localized="false" 
    xmlns:dcmPS="http://www.microsoft.com/schemas/dcm/package/2007" 
    xmlns:dcmRS="http://www.microsoft.com/schemas/dcm/resource/2007">

    <DiagnosticIdentification>
        <ID>PopupBlocker</ID>
        <Version>1.0</Version>
    </DiagnosticIdentification>

    <DisplayInformation>
        <Parameters/>
        <Name>Enable IE Popup Blocker</Name>
        <Description>Detects if the Popup Blocker feature of Internet Explorer is disabled. If the feature is disabled, the package enables it.</Description>
    </DisplayInformation>

    <PrivacyLink>http://URLTOYOURPRIVACYSTATEMENTGOESHERE</PrivacyLink>

    <PowerShellVersion>1.0</PowerShellVersion>

    <SupportedOSVersion clientSupported="true" serverSupported="true">6.1</SupportedOSVersion>

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

    <Interactions>
        <SingleResponseInteractions/>
        <MultipleResponseInteractions/>
        <TextInteractions/>
        <PauseInteractions/>
        <LaunchUIInteractions/>
    </Interactions>

    <ExtensionPoint/>

</dcmPS:AdvDiagnosticPackage>
```



 

 




