---
title: Localizing Message Strings
description: Each message string that you specify in the manifest must reference a string in the localization section of the manifest.
ms.assetid: aeae9ef6-6ef7-46f5-a9ab-fabe418549b2
ms.topic: article
ms.date: 05/31/2018
---

# Localizing Message Strings

Each message string that you specify in the manifest must reference a string in the **localization** section of the manifest. The localization section contains a string table section for each locale that you support.

The following example shows how to define a string table. You must specify the string's **id** and **value** attributes. You use the value of the **id** attribute to reference the string in your manifest. The **value** attribute contains the localized string.


```XML
<instrumentationManifest
    xmlns="http://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="http://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    >

    <instrumentation>
        <events>
            <provider name="Microsoft-Windows-SampleProvider" 
                guid="{1db28f2e-8f80-4027-8c5a-a11f7f10f62d}" 
                symbol="PROVIDER_GUID" 
                resourceFileName="<path to the exe or dll that contains the metadata resources>" 
                messageFileName="<path to the exe or dll that contains the string resources>"
                message="$(string.ProviderName)">

                . . .

            </provider>
        </events>
    </instrumentation>

    <localization>
        <resources culture="en-US">
            <stringTable>
                <string id="ProviderName" value="Sample Provider"/>
                <string id="PathNotFound" value="The path %1 was not found."/>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```


Instead of adding localized strings to the manifest, you should create a multilingual user interface (MUI) file for each language that you support. Use a message text file to specify your localized strings.

The following procedure describes how to create a MUI file for English and French.

**To create a MUI file for English and French**

1.  Create a message text file that creates the French message strings. For details on creating a message text file, see [Message Text Files](/windows/desktop/EventLog/message-text-files). The message identifiers that you specify in the message text file must match the resource identifiers that the message compiler generated for the same strings in the manifest. To determine the resource identifiers used for the strings in the manifest, see the .h file that the message compiler generated when you compiled the manifest.
    ```Text
    LanguageNames=(French=0x40C:MSG0040C)

    ; // The following are message definitions.

    MessageId=0x00000065
    SymbolicName=MSG_ProviderName
    Language=French
    <FRENCH STRING GOES HERE>
    .


    MessageId=0x00000066
    SymbolicName=MSG_PathNotFound
    Language=French
    <FRENCH STRING GOES HERE>
    .
    
    ```


2.  Run the following commands to create the resource DLL that contains your localized strings. The messages.mc file is the message text file that you created in step 1.
    ```cmd
    mc -u -U messages.mc

    rc -r messages.rc

    link -dll -noentry -out:messages.dll messages.res
    ```

    

3.  In the folder that contains your provider, create a subfolder for each locale that you support. The name of the subfolder must be the language name for that locale. For example, for 0x0409, use en-US as the folder name.
4.  Create a .rcconfig file that tells the Muirct.exe tool that you want to split the message string resources from the executable and the resource DLLs. The following is an example .rcconfig file.
    ```XML
    <localization>
          <resources>
                <win32Resources fileType="Application">
                      <neutralResources>
                      </neutralResources>
                      <localizedResources>
                            <resourceType typeNameId="#11"/>
                      </localizedResources>
                </win32Resources>
          </resources>
    </localization>
    ```
  

5.  Run the following Muirct.exe commands to split the English strings from the provider executable file.
    ```cmd
    muirct -q split.rcconfig -v 2 -x 0x0409 -g 0x0409 provider.exe provider.exe.ln en-US\provider.exe.mui

    muirct -c provider.exe.ln -e en-US\provider.exe.mui
    ```
 

6.  Run the following Muirct.exe commands to split the French strings from the resource DLL. Remove the language neutral file (fr-FR\\messages.dll) after the MUI file is created.
    ```cmd
    muirct -q split.rcconfig -v 2 -x 0x040C -g 0x0409 messages.dll fr-FR\messages.dll fr-FR\provider.exe.mui

    muirct -c provider.exe.ln -e fr-FR\provider.exe.mui
    ```
  

7.  Rename provider.exe.ln to provider.exe.
