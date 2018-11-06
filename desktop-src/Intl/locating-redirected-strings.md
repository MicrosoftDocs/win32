---
Description: This topic discusses programming instructions for locating redirected registry strings. For more information, see Using Registry String Redirection.
ms.assetid: 03d1512f-35a6-4b3a-9a0e-97e17bd9b126
title: Locating Redirected Strings
ms.topic: article
ms.date: 05/31/2018
---

# Locating Redirected Strings

This topic discusses programming instructions for locating redirected registry strings. For more information, see [Using Registry String Redirection](using-registry-string-redirection.md).

## Load a Language-Neutral Registry Value

On Windows Vista and later, the MUI application uses a language-neutral registry value to allow access to language-specific strings stored in a string resource table. For more information, see Create a Language-Neutral Resource in [Using Registry String Redirection](using-registry-string-redirection.md).

Application code that reads the language-neutral value from the registry should load the strings in the correct user interface language by calling [**RegLoadMUIStringW**](https://msdn.microsoft.com/en-us/library/ms724890(v=VS.85).aspx). If using this function, your application does not have to deal explicitly with resource loading.

If you are updating an existing application to the language-neutral use of the registry, you will typically keep the existing string values, localized to English or to some other single language in the registry, as fallbacks and for backward compatibility. Keeping a literal string in the registry allows the application to fall back to the literal string if a call to [**RegLoadMUIStringW**](https://msdn.microsoft.com/en-us/library/ms724890(v=VS.85).aspx) fails. You must decide how to implement such a fallback, as MUI provides no support for such an implementation.

## Use Shell API to Set Shortcut Strings from the Registry

Your application can use the shell API to create strings for shortcuts that link files or folders in the **Start** menu or on the desktop. For more information, see Create Resources for Shortcut Strings in [Using Registry String Redirection](using-registry-string-redirection.md).

The application can use [**SHSetLocalizedName**](https://msdn.microsoft.com/library/Bb762250(v=VS.85).aspx) to load the MUI-compliant display name for a shortcut. It should use [**IShellLink::SetDescription**](https://msdn.microsoft.com/en-us/library/Bb774955(v=VS.85).aspx) to set the associated InfoTip. The calls register the strings with the registry. Consider the following examples, for which "HKCR" represents the HKEY\_CLASSES\_ROOT registry key:


```C++
HKCR,"CLSID\%CLSID_AntiSpyware%",,,"Windows AntiSpyware"

HKCR,"CLSID\%CLSID_AntiSpyware%","LocalizedString",,"@%ProgramFiles%\Windows AntiSpyware\MSASCui.exe,-104"

HKCR,"CLSID\%CLSID_AntiSpyware%","InfoTip",,"@%ProgramFiles%\Windows AntiSpyware\MSASCui.exe,-208"
```



The first line provides an unlocalized literal string for fallback and backward compatibility. The second line shows the MUI-compliant way to register the display name. This line indicates the string identifier 104 stored in Msascui.exe (for Windows XP) or in its associated language-specific file (for Windows Vista). This string identifier corresponds to "My Network Places". The third line in the example handles InfoTip registration. %CLSID\_AntiSpyware% specifies an environment variable representing the GUID that matches the class identifier of this component.

For the example shown above, the application calls [**SHSetLocalizedName**](https://msdn.microsoft.com/library/Bb762250(v=VS.85).aspx) to specify the path of the executable for the first two parameters, and specify *idsRes* as "@%ProgramFiles%\\Windows AntiSpyware\\MSASCui.exe,104". A call to [**IShellLink::SetDescription**](https://msdn.microsoft.com/en-us/library/Bb774955(v=VS.85).aspx), specifies the path for the InfoTip as "@%ProgramFiles%\\Windows AntiSpyware\\MSASCui.exe,208".

## Query Friendly Document Type Names in the Registry

Resource creation for friendly document type names is discussed in Create Resources for Friendly Document Type Names in [Using Registry String Redirection](using-registry-string-redirection.md). To query a friendly document name, the application should use [**IQueryAssociations::Init**](https://msdn.microsoft.com/en-us/library/Bb761398(v=VS.85).aspx), followed by a call to [**IQueryAssociations::GetString**](https://msdn.microsoft.com/en-us/library/Bb761396(v=VS.85).aspx). The call to **IQueryAssociations::Init** specifies the document type, for example, ".txt". The call to **IQueryAssociations::GetString** must specify ASSOCSTR\_FRIENDLYDOCNAME as the string identifier.

## Register Microsoft Management Console Snap-in Strings Not Read from the Registry

Your application can use a Microsoft Management Console (MMC) snap-in to host its management tasks. Most strings are handled as resources using the registry settings described in Create String Resources for Microsoft Management Console Snap-Ins in [Using Registry String Redirection](using-registry-string-redirection.md). However, some snap-ins register registry string values that MMC cannot read from the registry. In this case, the snap-in must obtain the values using the [**ISnapinAbout**](https://msdn.microsoft.com/en-us/library/Aa814937(v=VS.85).aspx) interface, which is MUI-compatible.

## Set the Display Name and Description for a Windows Service from the Registry

If your MUI application is using a Windows service, it must display the service display name and description. The associated resources are discussed in "Create String Resources for a Windows Service" in [Using Registry String Redirection](using-registry-string-redirection.md).

To set the service display name, the MUI application calls [**CreateService**](https://msdn.microsoft.com/en-us/library/ms682450(v=VS.85).aspx) or [**ChangeServiceConfig**](https://msdn.microsoft.com/en-us/library/ms681987(v=VS.85).aspx). The name is a string of the form "`@<PE-path>,-<stringID>[;<comment>]`". For example, if your service is implemented by a .dll file with path %ProgramFiles%\\%MyPath%\\MyDll.dll, and the string identifier of the language-specific display name is 347, the parameter is specified as "`@%ProgramFiles%\\%MyPath%\\MyDll.dll,-347`". The double backslashes (\\\\) are necessary because C/C++ uses the backslash as an escape character in strings.

To set the language-specific service description, the MUI application should make the **lpDescription** member of a [**SERVICE\_DESCRIPTION**](https://msdn.microsoft.com/en-us/library/ms685156(v=VS.85).aspx) structure indicate a string of form "`@<PE-path>,-<stringID>[;<comment>]`", referencing the appropriate string identifier. Then the application calls [**ChangeServiceConfig2**](https://msdn.microsoft.com/en-us/library/ms681988(v=VS.85).aspx) with parameter *dwInfoLevel* specified as SERVICE\_CONFIG\_DESCRIPTION and parameter *lpInfo* specified as the **SERVICE\_DESCRIPTION** structure.

## Related topics

<dl> <dt>

[Locating Win32 PE Resources](locating-win32-pe-resources.md)
</dt> <dt>

[Using Registry String Redirection](using-registry-string-redirection.md)
</dt> </dl>

 

 



