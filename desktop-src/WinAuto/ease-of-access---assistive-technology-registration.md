---
title: Ease of Access   Assistive Technology Registration
description: This article explains how to register an accessibility application with the Ease of Access Center. It also explains how to tailor your accessibility application so it works well with the secure desktop.
ms.assetid: 6F1F2AAE-B2E4-4F26-8BDF-A3DE8F5C5460
ms.topic: article
ms.date: 04/02/2019
---

# Ease of Access   Assistive Technology Registration

This article explains how to register an accessibility application with the Ease of Access Center. It also explains how to tailor your accessibility application so it works well with the secure desktop.

The Ease of Access Center is a Control Panel application for Microsoft Windows brings together functionality for accessibility and ease of use. By using the Ease of Access Center, users can configure their computers to suit their physical and cognitive needs.

One function of the Ease of Access Center is to help users launch accessibility applications, including Narrator, On-Screen Keyboard, and Magnifier. Registered third-party applications also appear in the Ease of Access Center and can be launched directly from there.

Accessibility applications need to work smoothly with the secure desktop. The secure desktop is the user interface that appears when the computer is locked (at log-on or when the user has locked the desktop), and when the user is prompted to allow a potentially unsafe action. For security reasons, Windows places limits on third-party software running on the secure desktop. If you want your accessibility application to run on the secure desktop, you need to register the application with the Ease of Access Center.

## Registering with the Ease of Access Center

Accessibility applications register with the Ease of Access Center by creating one or more registry keys when the application is installed. The following table lists the information contained in the registry keys.



| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Mandatory/Optional | Language      |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|---------------|
| Application Name            | The name of the application, which is in a resource file. This registry value contains a string in a specified format. This could be a localized version of the application name, if the application is localized in languages other than English. The name appears in the Ease of Access Center.<br/>                                                                                                                                                                                                                                                                                       | Mandatory          | Localized     |
| ATExe                       | The name of the application executable file or image. Windows uses this value to determine whether the accessibility application is running.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                            | Mandatory          | Not localized |
| CopySettingsToLockedDesktop | A **DWORD** value that indicates whether to copy the accessibility application's settings to the locked desktop.<br/> If this value is 1, the application can write settings to a location in the user registry, and Windows copies the settings to the same location in the user registry for the locked desktop. This enables the application to persist its state from the "normal" desktop to the locked desktop.<br/>                                                                                                                                                             | Optional           | Not localized |
| Description                 | A brief description of the application, from a resource file. This registry value contains a string in a specified format. This could be a localized version of the description, if the application is localized in languages other than English. The length of this string must be less than 512 characters.<br/> The description appears in the Ease of Access Center to provide additional information about the accessibility application to the user.<br/> This value can also be used to notify the user that the application is not used on the secure desktop.<br/>      | Mandatory          | Localized     |
| Profile                     | A short piece of XML that specifies the accommodations that the application provides. It ensures that the application appears under the correct category in the Ease of Access Center.<br/>                                                                                                                                                                                                                                                                                                                                                                                                  | Mandatory          | Not localized |
| PassiveAutoStartBehavior    | <p>A **DWORD** value that indicates whether legacy auto-start behavior is enabled.</p><p>The default value is 0, which indicates that an AT requires legacy auto-start behavior. This  causes the “Start after sign-in” setting for that AT to be checked in the Out Of Box Experience (OOBE) and Control Panel (see **Control Panel -> Ease of Access -> Ease of Access Center -> Change sign-in settings**), and automatically starts the AT after UAC and lock-screen.</p><p>A value of 1 indicates that the AT should use the new auto-start behavior where the “Start after sign-in” setting for that AT is not checked in the Out Of Box Experience (OOBE) and Control Panel, and the AT is automatically started once per user session (at login) only if the “start after sign-in” setting is checked.</p>                                                                                                                                                                                                                                                                                                                                                                                                  | Optional          | Not localized |
| SecureDesktopAccommodation  | The name of an alternate accessibility application to run on the secure desktop in the place of this application. The alternate can be a different application, a different version of the same application, one of the accessibility applications that is included in Windows, or "none" if you do not want to run any accessibility application on the secure desktop. <br/>                                                                                                                                                                                                               | Optional           | Not localized |
| Simple Profile              | A value that describes how to classify the application in a word or two: Screen reader, Magnifier, or On-screen keyboard, for example.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Mandatory          | Not localized |
| StartExe                    | The full path of the executable. This value is used to launch the accessibility application.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Mandatory          | Not localized |
| StartParams                 | Command-line arguments. These values are used along with StartExe to start the application.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Optional           | Not localized |
| TerminateOnDesktopSwitch    | A **DWORD** value that specifies how the accessibility application responds to transitions to or from the secure desktop.<br/> If this value does not exist or is 1, Windows terminates and restarts the application on each transition to or from the secure desktop. This is the default behavior.<br/> If this value is 0, Windows does not terminate the accessibility application on a desktop transition. The application continues to run on the previous desktop, and Windows starts a new instance on the new desktop if an instance is not already running there.<br/> | Optional           | Not localized |


 

### Localization

The registry values of Application Name and Description need to be localizable to support Multilingual User Interface (MUI).

These strings are in the following format, where angle brackets signify required elements and square brackets signify an optional element.

*@<ResDllPath\\ResDLLFilename>,-&lt;resID&gt;\[;&lt;comment&gt;\]*

*<ResDllPath\\ResDLLFilename>* is the path to the resource DLL. The path can contain environmental variables.

*&lt;resID&gt;* is the resource ID for the string.

*\[comment\]* contains any optional comments.

Here is an example:


```
@%SystemRoot%\system32\anyAT.dll,-5020
```



For more information about MUI, see [Windows MUI Knowledge Center](../intl/about-multilingual-user-interface.md).

### HCI Profile

The Human Computer Interaction (HCI) profile is a way to determine what accommodations to provide based on the needs of the user. Accessibility applications should register information about the kind of disability the application helps to accommodate.

The Profile registry value contains XML that describes the kind of disability targeted by the accessibility application. This XML has the following format:


```XML
<HCIModel>
<Accommodation type="disability"/>
</HCIModel>
```



The valid values for the **Accommodation type** attribute are as follows:

-   mild vision
-   severe vision
-   mild cognitive
-   severe cognitive
-   mild dexterity
-   severe dexterity
-   mild hearing
-   severe hearing
-   mild speech
-   severe speech

> [!Note]  
> These values are case sensitive.

 

If an accessibility application supports multiple accommodations, the Profile registry value should include an **Accommodation type** attribute for each accommodation.

### Ease of Access registry details

To register your accessibility application, you need to create a key for your application at the following registry location and populate it with name-value pairs.

**HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Accessibility\\ATs\\**

Name your application's registry key using the following format:

*"CompanyName\_ProductName\_v\#"*

For example, "Contoso\_Magnifier\_v2.0".

To add registry values, your installation program must be running with elevated privileges.

### Secure desktop accommodation

The **SecureDesktopAccommodation** registry key lets you specify how your accessibility application responds to the secure desktop. By default, the Ease of Access Center launches your application on the secure desktop if it was already running on the normal desktop, or if it is configured to run on the logon desktop. By using the **SecureDesktopAccommodation** key, you can:

-   Specify an alternate version of your application for use on the secure desktop. For example, you might have an alternate version that disables unsecured features, or is optimized to use less memory and launch faster.

    To specify the alternate version, set the **SecureDesktopAccommodation** key to the name of the alternate version. For example, if you registered your application at the Contoso\_Screen Reader\_v1.0 key, you could register the alternate version at Contoso\_Screen ReaderSecure\_v1.0. Then, set the **SecureDesktopAccommodation** key of Contoso\_Screen Reader\_v1.0 to "Contoso\_Screen ReaderSecure\_v1.0".

-   Specify a Microsoft accessibility application to use on the secure desktop in place of your application. For this option, set **SecureDesktopAccommodation** to the name of the particular Microsoft accessibility application: "osk", "magnifierpane", or "Narrator".
-   Specify that your application should not run on the secure desktop, and neither should any alternate application. For this option, set **SecureDesktopAccommodation** to "none" (recommend) or the name of a nonexistent application.

If the **SecureDesktopAccommodation** registry key for your accessibility application specifies a Microsoft accessibility application to run on the secure desktop in place of your application, Windows notifies the user of this when making the transition to the secure desktop. To notify the user, Windows displays the string specified in the Description registry key for your application. For example, if the ScreenReader Deluxe 1.0 application uses Microsoft Narrator on the secure desktop, it would include a Description string such as, "Microsoft Narrator will be used in the locked, logon, and other secure desktops in place of ScreenReader Deluxe 1.0."

If your application's **SecureDesktopAccommodation** key is set to "none", use the **Description** key to tell the user your application is not available on the secure desktop and no alternative is provided.

Windows displays the Description text in the relevant locations in the Ease of Access Center.

### Running at installation and on the logon desktop

If you append your accessibility application's registered key name to the string at the following registry location, Windows will launch your application immediately after it is installed. Also, Windows will automatically run your application whenever the logon desktop is active.

**HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Accessibility\\Configuration**

The Configuration key is a comma-delimited string. To add your application, append a string that is the same as your application's registry key at HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Accessibility\\ATs\\.

### Running in a job

If the **TerminateOnDesktopSwitch** registry key is not present or is set to non-zero, Windows runs the application in the context of a job, terminating and restarting the application with each desktop transition. Running in a job ensures that only a single instance of the application is running at a particular time, and frees the application from having to monitor the desktop state. The disadvantages of running in a job include:

-   The application incurs a startup cost with each desktop transition.
-   The application can be started only through the Ease of Access Center.
-   The application must continually save its settings because it can be terminated at any time by a desktop transition.

If the **TerminateOnDesktopSwitch** key exists and is set to 0, Windows doesn't run the accessibility application in a job. This has the following advantages:

-   No startup costs are associated with desktop transitions.
-   The application can be started outside of the Ease of Access Center.

The disadvantages of not running in a job include:

-   Because the application isn t restarted on desktop transitions, it must detect when the current desktop is inactive and respond appropriately. For example, the application must relinquish control of hardware so the secure desktop version of the application can use it, and the application should enter sleep mode to avoid using processor resources.
-   If the application can be started through the Start menu, Windows Explorer, or the command line, the Ease of Access Center needs to be informed. For more information, see **Windows Logo key + U**.
-   Because multiple copies of the application can run simultaneously on different desktops, the application must be written to support multiple running copies.

### Windows Logo key + U

If your accessibility application is configured to run in a job, your application's startup code should include a call to the [**IsProcessInJob**](/windows/desktop/api/jobapi/nf-jobapi-isprocessinjob) function to determine whether the application is starting in a job. If it is, the application should start the Ease of Access Center and then exit. The following example shows how to call **IsProcessInJob**.


```C++
BOOL fAlreadyInJob;
BOOL fSuccess = IsProcessInJob(GetCurrentProcess(), NULL, &fAlreadyInJob); 
```



If the accessibility application is configured to run outside of a job, it should notify the Ease of Access Center that the application is starting and continue as normal.

Regardless of how the application is configured, if it provides a way to exit from within the application, such as a Close button, the application must notify the Ease of Access Center that it is exiting.

An application notifies the Ease of Access Center by setting a temporary registry key and then injecting the Windows Logo key + U key combination into the input stream.

The application should create the temporary key at the following location.

**HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\AccessibilityTemp**

The temporary key should have the same name as the registered application name, such as "Contoso\_Screen Reader\_v1.0". The value of the key is a **DWORD** set to 0x0003 when it is starting, or 0x0002 when the application is exiting.


```C++
INPUT input[4] = {0};

input[0].type = INPUT_KEYBOARD;
input[0].ki.wVk = VK_LWIN;
input[0].ki.dwFlags = 0;

input[1].type = INPUT_KEYBOARD;
input[1].ki.wVk = 0x55; // U key
input[1].ki.dwFlags = 0;

input[2].type = INPUT_KEYBOARD;
input[2].ki.wVk = 0x55; // U key
input[2].ki.dwFlags = KEYEVENTF_KEYUP;

input[3].type = INPUT_KEYBOARD;
input[3].ki.wVk = VK_LWIN;
input[3].ki.dwFlags = KEYEVENTF_KEYUP;

SendInput(ARRAYSIZE(input), input, sizeof(input[0]));
```



### Windows Logo key + Volume Up

When the user starts your accessibility application by pressing the Windows Logo key + Volume Up key combination (such as on a tablet device), the Ease of Access Center passes the following command-line argument to the application:

**/hardwarebuttonlaunch**

Your application can use this argument to determine whether to start normally, or to adjust behavior accordingly.

### Transferring secure desktop settings

If your accessibility application supports the secure desktop, you can use the registry to copy settings when the application transitions to the secure desktop. Copying settings helps makes the transition to the secure desktop more seamless for the user.

To copy settings, set the application's CopySettingsToLockedDesktop registry key to 1, and store the settings in the following registry location.

**HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Accessibility\\ATConfig\\\<AT Key Name>**

The Ease of Access Center monitors this registry location while the application is running. When a transition to the secure desktop occurs, the Ease of Access Center copies the settings to the same location in the secure desktop s HKCU hive. The application can then read the settings and resume its state.

Your accessibility application should write its settings at regular intervals or whenever the values change. Writing settings on application exit will not work. If the application is running in a job, it is terminated on the transition away from the secure desktop, before the exit code has a chance to run. If the application is not running in a job, the application is not terminated on the transition away from the secure desktop.

### Caution

Because the registry keys described here are written in user mode, they are not secure. If your accessibility application reads the contents of these keys, it should carefully check the data and use it with caution. Specifically, your application should do a bounds check on **DWORD** values, be careful with string lengths, should not read plug-in DLL names, and should not execute any commands found in strings.

## Registry Examples

The following example shows the possible registry values for a fictitious product called Contoso ScreenReader version 2.0, whose localized name is stored as a resource.

The values in the table are under the following key:

**HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Accessibility\\ATs\\Contoso\_Screen Reader\_v2.0**



<table>
<colgroup>
<col  />
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Type</th>
<th>Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ApplicationName</td>
<td>REG_SZ</td>
<td>@%SystemRoot%\system32\ContosoRes.dll,-5020</td>
</tr>
<tr class="even">
<td>Description</td>
<td>REG_SZ</td>
<td>@%SystemRoot%\system32\ContosoRes.dll,-5040</td>
</tr>
<tr class="odd">
<td>Profile</td>
<td>REG_SZ</td>
<td><span data-codelanguage="XML"></span>
<table>
<colgroup>
<col  />
</colgroup>
<thead>
<tr class="header">
<th>XML</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>&lt;HCIModel&gt;
   &lt;Accommodation type=&quot;low vision&quot;&gt;
   &lt;Accommodation type=&quot;severe vision&quot;&gt;
   &lt;Accommodation type=&quot;mild cognitive&quot;&gt;
&lt;/HCIModel&gt;</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td>SimpleProfile</td>
<td>REG_SZ</td>
<td>ScreenReader</td>
</tr>
<tr class="odd">
<td>StartExe</td>
<td>REG_SZ</td>
<td>C:\ContosoTools\Bin\ContosoSR.exe</td>
</tr>
<tr class="even">
<td>StartParams</td>
<td>REG_SZ</td>

</tr>
<tr class="odd">
<td>SecureDesktopAccommodation</td>
<td>REG_SZ</td>
<td>Narrator</td>
</tr>
</tbody>
</table>



 

If the application provides both a screen reader and a screen magnifier in a single executable, the values for the screen reader component might look like this:



<table>
<colgroup>
<col  />
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Type</th>
<th>Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ApplicationName</td>
<td>REG_SZ</td>
<td>@C:\Program Files\Contoso\Contosores.dll,-30</td>
</tr>
<tr class="even">
<td>Description</td>
<td>REG_SZ</td>
<td>@C:\Program Files\Contoso\Contosores.dll,-32</td>
</tr>
<tr class="odd">
<td>Profile</td>
<td>REG_SZ</td>
<td><span data-codelanguage="XML"></span>
<table>
<colgroup>
<col  />
</colgroup>
<thead>
<tr class="header">
<th>XML</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>&lt;HCIModel&gt;
   &lt;Accommodation type=&quot;low vision&quot;&gt;
   &lt;Accommodation type=&quot;severe vision&quot;&gt;
   &lt;Accommodation type=&quot;mild cognitive&quot;&gt;
&lt;/HCIModel&gt;</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td>SimpleProfile</td>
<td>REG_SZ</td>
<td>ScreenReader</td>
</tr>
<tr class="odd">
<td>StartExe</td>
<td>REG_SZ</td>
<td>C:\Program Files\Contoso\Bin\ContosoSR.exe</td>
</tr>
<tr class="even">
<td>StartParams</td>
<td>REG_SZ</td>
<td>/r</td>
</tr>
</tbody>
</table>



 

The values for the magnifier component would be in the following key:

**HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Contosoibility\\ATs\\Contoso\_Magnifier\_v2.0**



<table>
<colgroup>
<col  />
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Type</th>
<th>Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ApplicationName</td>
<td>REG_SZ</td>
<td>@c:\Program Files\Contoso\Contosores.dll,-31</td>
</tr>
<tr class="even">
<td>Description</td>
<td>REG_SZ</td>
<td>@c:\Program Files\Contoso\Contosores.dll,-42</td>
</tr>
<tr class="odd">
<td>Profile</td>
<td>REG_SZ</td>
<td><span data-codelanguage="XML"></span>
<table>
<colgroup>
<col  />
</colgroup>
<thead>
<tr class="header">
<th>XML</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>&lt;HCIModel&gt;
   &lt;Accommodation type=&quot;mild vision&quot;&gt;
&lt;/HCIModel&gt;</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td>SimpleProfile</td>
<td>REG_SZ</td>
<td>Magnification</td>
</tr>
<tr class="odd">
<td>StartExe</td>
<td>REG_SZ</td>
<td>c:\Program Files\Contoso\Bin\ContosoSR.exe</td>
</tr>
<tr class="even">
<td>StartParams</td>
<td>REG_SZ</td>
<td>/m</td>
</tr>
</tbody>
</table>



 

 

