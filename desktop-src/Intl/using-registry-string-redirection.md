---
description: Storage of hard-coded strings in the registry is part of a pre-Windows Vista localization model.
ms.assetid: 70185942-7d32-4151-a4e1-f71cf45e87af
title: Using Registry String Redirection
ms.topic: article
ms.date: 05/31/2018
---

# Using Registry String Redirection

Storage of hard-coded strings in the registry is part of a pre-Windows Vista localization model. It is not supported by MUI. In the current model, the user interface for the operating system runs in language-specific resource files on top of a language-neutral base. The components of the operating system use the registry in a language-neutral manner.

MUI uses only redirected registry strings defined by Win32 PE resources in the base language resource file. Redirection is defined separately, for example, in an .inf file. This type of storage allows the resource loader to select the correct language resources automatically during resource module loading.

> [!Note]  
> This topic pertains only to Win32 PE resources. If using non-Win32 PE resources, you must provide customized registry string redirection, if required.

 

## Create a Language-Neutral Resource

A MUI application running on Windows Vista and later uses a language-neutral string resource to allow access to language-specific strings stored in a string resource table. Application code that reads these values from the registry is described in the Load a Language-Neutral Registry Value section of [Locating Redirected Strings](locating-redirected-strings.md).

The data for a language-neutral registry value has the format "`@<PE-path>,-<stringID>[;<comment>]`", where:

-   *PE-path* specifies the path of the executable. You can specify the path using an environment variable, such as %ProgramFiles%, to support deployment. An alternative for making your string reference is to leave out the file path information. In this case, your application must have some means, for example, another registry value, to communicate its own install directory.
-   *stringID* specifies the numeric resource identifier of the relevant string resource, which is implemented just like any other localizable string resource.
-   *comment* specifies optional information for debugging or readability of the registry value. The registry API functions ignore the comment when loading the string.

> [!Note]  
> The data for the registry value makes no explicit reference to the language-specific resource file. The correct file is determined at runtime, based on the current user interface language preferences.

 

A registry value is entered without a space between the "," and "-". A correct registry value is:

`shell32.dll,-22912`

An incorrect registry value is:

`shell32.dll, -22912`

An example from Windows Vista is the registry value with the following data:

`@%SystemRoot%\system32\input.dll,-5020`

## Create Resources for Shortcut Strings

When the MUI application displays its name in the shell user interface, an InfoTip string is displayed for the application icon. You should create string resources for your application display name and associated InfoTip string for each supported language. When the resources are ready, your application can use the strings as described in the Use Shell API to Load Shortcut Strings from the Registry section of [Locating Redirected Strings](locating-redirected-strings.md).

### Prepare Resources for a Shortcut Created with Windows Installer

If you use Windows Installer (MSI) to create a shortcut, string resources include shortcut display name and description. In the [MSI shortcut table](../msi/shortcut-table.md), the resource DLL is referenced in the appropriate columns and the resource identifiers for your shortcut display name and description are used in the corresponding resource identifier columns.

So that the application shortcut works properly with MUI resource technology, keep the following points in mind when preparing the shortcut strings:

-   Use either environment variables or a relative path to register the DLL. You can specify @%systemroot%\\system32\\shell32.dll as long as the registry string type is REG\_EXPAND\_SZ. The string resource identifier for "Text Document" in Shell32.dll is 12345.
-   Do not use spaces around the "," and "-" symbols. A correct example is "shell32.dll,-22912".
-   Do not use a short file name. This type of name does not work with the resource loader.

### Prepare Resources for a Shortcut Using INF Format

If you use the INF file format to create shortcut strings, the resource file should make the following registry settings. These instructions assume the use of the ProfileItems syntax of Setup API.

1.  Change the InfoTip value to point to the string redirection reference, using the path and resource identifier.
2.  Add the new value DisplayResource under the ProfileItems installation sections.

The following is an example showing the addition of the Calculator application to the **Start** menu:


```C++
[CalcInstallItems]
"Name" = %Calc_DESC%
"CmdLine" = 11, calc.exe
"SubDir" = %Access_GROUP%
"WorkingDir" = 11

"InfoTip" = "@%systemroot%\system32\shell32.dll,-22531"

"DisplayResource" = "%systemroot%\system32\shell32.dll",22019
```



Use the syntax shown below when using INF to add items, for example, an Access Group folder, to the **Start** menu. This syntax assumes the use of \[StartMenuItems\] support from Setup, similar to the syntax used in Syssetup.inf.


```C++
[StartMenuItems]
<description> = <binary>,<commandline>,<iconfile>,<iconnum>,<infotip>,<resDLL,resID>
```



Set the value *infotip* to the string reference "`@<path>,-resID`".

The display name is determined by the *resDLL* and *resID* values. The *resID* value specifies the resource identifier for a string resource associated with the language-neutral file. The *resDLL* value specifies the path to the language-neutral file.

## Create Resources for Friendly Document Type Names

You must implement friendly name and InfoTip strings for your application as string resources. To allow friendly document type names to react to the user interface language, the application must register the names using the FriendlyTypeName value under the program identifier key for the file type. The default value for the program identifier key should be retained to keep backward compatibility. For information about accessing the names from your application, see the Query Friendly Document Type Names in the Registry section of [Locating Redirected Strings](locating-redirected-strings.md).

The specific work involves the following steps:

1.  Implement the friendly name and InfoTip strings as language-specific string resources.
2.  Add the FriendlyTypeName value under the document type registry key. The data for the value follows the pattern "`@<path>,-<resID>`", where *path* indicates the executable and *resID* is the resource identifier of a localizable string resource associated with that executable.
3.  Specify the InfoTip registry value according to the format "`@<path>,-<resID>`".

The following example shows the registry settings for a .txt file:


```C++
HKCR\.txt
@="txtfile"
"Content Type"="text/plain"

HKCR\txtfile
@="Text Document"

"FriendlyTypeName" = "@%systemroot%\system32\shell32.dll,-12345"

"InfoTip" = "@%systemroot%\system32\shell32.dll,-12346"
```



## Provide Resources for Shell Verb Action Strings

Action strings for certain verbs, for example, "open" and "edit", are shown in the pop-up menu displayed when the user right-clicks a file in Windows Explorer. Your application does not have to specify strings for common shell verbs, as the shell has its own MUI-enabled defaults for these verbs. However, you should provide localizable string resources for strings representing uncommon verbs.

On pre-Windows XP operating systems, strings for shell verbs in the registry are rendered using the following syntax, where *verb* specifies the actual verb name:


```C++
HKCR\<progid>\shell\<verb>
@ = <friendly-name>
```



Here's an example:


```C++
HKCR\Sample.app\shell\Disc
@ = "Disconnect"
```



On Windows XP and later, you can use a level of indirection to make an action string depend on user interface language. These operating systems support a MUIVerb value for definition of a MUI-compatible string. Here's an example of a registry entry for an uncommon verb:


```C++
HKCR\Sample.app\shell\Disc
@ = "Disconnect"
"MUIVerb" = "@%systemroot%\system32\sample.exe,-9875"
```



Your MUI application should also be able to register the old default value as a localizable string, as shown below:


```C++
HKCR\Sample.app\shell\Disc
@ = "@%systemroot%\system32\sample.exe,-9875"
```



> [!Note]  
> Registration of the old default value is not recommended because it requires a different setup on Windows XP and later from the setup used on earlier operating systems.

 

## Create Resources for Verb, Protocol, and AuxUserType Strings

You should create localizable string resources for Verb, Protocol, and AuxUserType strings. Use the following registry settings:


```C++
HKCR\CLSID\{<Your_CLSID>}\Verb\<number> @="<Your Verb>, <menu_flag>, <verb_flag>"
"LocalizedString"="@<resDLLpath\resDLL.DLL>,-resStrID"
...

HKCR\CLSID\{<Your_CLSID>}\AuxUserType\<number>
@="<Your Short Name>"
"LocalizedString"="@<resDLLpath\resDLL.DLL>,-resStrID1"
...

HKCR\<Your_Name>\protocol\StdFileEditing\verb\<number>
@="<Your Verb>"
"LocalizedString"="@<resDLLpath\resDLL.DLL>,-resStrID"
...
```



The value specified for LocalizedString only contains or replaces the value for *Your Verb*, not the two flag values.

Here is a summary to help you ensure correct registry settings:

-   If CLSID has a HKCR\\CLSID\\{clsid}\\Insertable key, define the default CLSID value using HKCR\\CLSID\\{clsid}\\LocalizedString.
-   If CLSID has one or more subkeys under HKCR\\CLSID\\{clsid}\\Verb, define each individual Verb string using HKCR\\CLSID\\{clsid}\\Verb\\xxx\\LocalizedString.
-   If CLSID has one or more subkeys under HKCR\\{progid}\\Protocol\\Stdfileediting\\Verb, define each individual Verb string using HKCR\\{progid}\\Protocol\\Stdfileediting\\Verb\\xxx\\LocalizedString.
-   If CLSID has one or more listed AuxUserType subkeys under HKCR\\CLSID\\{clsid}\\AuxUserType, define each AuxUserType entry using HKCR\\CLSID\\{clsid}\\AuxUserType\\xxx\\LocalizedString.

## Create a Resource for the Uninstall Program

To register the uninstall program for the application, you can create registry values in the unique identifier subkey for the application under the registry key HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall. Values to set include: DisplayName, DisplayVersion, Publisher, ProductID, RegOwner, RegCompany, UrlInfoAbout, HelpTelephone, HelpLink, InstallLocation, InstallSource, InstallDate, Contact, Comments, DisplayIcon, Readme, UrlUpdateInfo.

> [!Note]  
> To enable MUI technology for each value, you can append "\_Localized" to the value name.

 

Operating system components are required to provide a value for DisplayName\_Localized in a MUI-specific way. You should place the display name in a DLL, such as Res.dll, as a string resource, assuming the identifier to be 1245. Then the application can register the display name as DisplayName\_Localized with value "@\\res.DLL,-1245". All the other registry settings should be retained as they are, including the original value for DisplayName.

## Create Resources for Sound Events

Windows associates certain events with sound files, for example, a New Mail Notification event or a Critical Battery Alarm event. The event names must be displayed by the user interface and must support globalization. Therefore, you should implement a localizable string resource for the description of each event description. Add a new registry value for each event name, in addition to the hard-coded default value.

Do the following to enable a sound event:

1.  Implement the description as a localizable string resource.
2.  Add a new registry value for the display name, in addition to the hard-coded default value. The associated registry layout is shown below:


```C++
HKCR\AppEvents\EventLabels
<event_name>
    (Default) REG_SZ "<description>"
    DispFileName REG_EXPAND_SZ "@<path>,-<resID>"
```



If the shell cannot find or retrieve the value of DispFileName, it uses the default description.

## Create Resources for Keyboard Layout Strings

If your application implements a keyboard layout, it requires a localizable string resource for the name of the layout for screen display, for example, in lists of keyboard layouts. Each keyboard layout has a registry key under `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Keyboard Layouts`.

Among the values for that key are `Layout Text`, a human-readable name for backward compatibility, and `Layout Display Name`. The data supplied for `Layout Display Name` should be a string reference of the form `@<path>,-resID`, referring to a localizable string resource associated with the keyboard layout.

Here is an example of a registry setting for the Spanish (Spain) keyboard layout:

`Layout Display Name=@%SystemRoot%\system32\input.dll,-5020`

## Represent OLE Insert Object Common Dialog Strings

You can implement the display name of an OLE insertable object as a localizable string resource associated with the code implementing that object. The [OLE Insert Object dialog box](/cpp/mfc/reference/coleinsertdialog-class) gets a display name from the registry key HKCR\\CLSID\\{*&lt;GUID&gt;*}, where *GUID* identifies the class identifier of an insertable OLE object. Windows Vista and later implement this type of object in a localizable way, using a MUI-compliant display name that allows customization to the user interface language. In contrast, pre-Windows Vista operating systems implement the display name for this type of object using the default value of the corresponding registry key. Typically this name is either an English (United States) name or a name in the system default UI language.

> [!Note]  
> Not all objects that correspond to subkeys of the registry key are insertable.

 

The default value of the HKCR\\CLSID\\{*&lt;GUID&gt;*} key should retain a human-readable name for backward compatibility. However, it should also define the LocalizedString value, in the format "`@<path>,-ResID`", where path identifies the executable file implementing the object. The ResID value specifies the resource identifier of the localizable string for the display name.

For example, the registration script for the insertable Media Clip object includes the following lines:


```C++
HKCR,"CLSID\%CLSID_Media_Clip%",,,"%default description%"
HKCR,"CLSID\%CLSID_Media_Clip%","LocalizedString",,"@%systemroot%\system32\mplay32.exe,-9217"
```



The first line provides backward compatibility by placing a simple text string in the registry as a default display name. The second line provides access to the MUI-compliant display name. It indicates the string identifier stored in Mplay32.exe. The string with identifier 9217 in Mplay32.exe can be associated with string resource values for any number of languages. Its English (United States) name is "Media Clip".

## Create String Resources for Microsoft Management Console Snap-Ins

You should create a localizable string resource for each Microsoft Management Console (MMC) snap-in used by your MUI application. Because a snap-in is part of a console, it has a user interface and must be globalized to operate in more than one language.

For the most part, MMC snap-ins raise the same globalization and localization issues as the MUI application itself. An MMC snap-in must reflect its name in the registry for display. The registry entry should include both an indirect reference to a localizable string resource and a literal string for backward compatibility.

Each MMC snap-in has a registry key under HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns. Among the values for that key are NameString, specifying a human-readable name for backward compatibility, and NameStringIndirect, specifying an indirect reference to a localizable string resource. For NameStringIndirect, you should provide a string reference of the form "`@<path>,-resID`", representing a localizable string resource.

For example, you might make the following setting for Mymmc.dll, where 12345 is the identifier of the corresponding string resource containing the localizable name of the snap-in:


```C++
NameStringIndirect=@%systemroot%@c:\windir\system32\mymmc.dll,-12345
```



Some snap-ins register other registry string values that MMC does not read from the registry. For more information about using these values, see Register Microsoft Management Console Snap-In Strings Not Read from the Registry in [Locating Redirected Strings](locating-redirected-strings.md).

## Create String Resources for a Windows Service

Although a Windows service typically has little or no user interface, it must display a MUI-compliant name and usually provides a MUI-compliant language-specific description. The registry key that describes a Windows service supports only the DisplayName value for the service name and the Description value for the service description.

Settings for the Windows service are made from the application, as described in Set the Display Name and Description for a Windows Service from the Registry in [Locating Redirected Strings](locating-redirected-strings.md). If your application does not set the registry values for the service user interface, values in the registry remain set to English, even if the user interface is in another language.

## Related topics

<dl> <dt>

[Preparing Resources](preparing-resources.md)
</dt> <dt>

[Locating Redirected Strings](locating-redirected-strings.md)
</dt> </dl>

 

 
