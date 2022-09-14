---
description: Locating Non-Win32 PE Resources
ms.assetid: 12f0b78e-ca85-443a-94ea-6bec5aa40c06
title: Locating Non-Win32 PE Resources
ms.topic: article
ms.date: 05/31/2018
---

# Locating Non-Win32 PE Resources

To locate non-Win32 PE resources, your application should first call the [**GetFileMUIPath**](/windows/desktop/api/Winnls/nf-winnls-getfilemuipath) function to locate the language-specific resource file from which to load resources. If the application is following system language settings, it must call the function with MUI\_LANGUAGE\_NAME \| MUI\_USER\_PREFERRED\_UI\_LANGUAGES specified for *dwFlags* and **NULL** specified for *pwszLanguage*. If the application is following application-specific language settings, it uses **GetFileMUIPath** to determine if a language-specific file exists by specifying the language in the *pwszLanguage* parameter.

After the call to [**GetFileMUIPath**](/windows/desktop/api/Winnls/nf-winnls-getfilemuipath), the application must define custom functionality to load the resource module and load specific resources from it. For example, if you are using a .txt or .xml resource file, the application must use a TXT or XML parser to load the file and then parse the contents of the file for each required resource.

## Related topics

<dl> <dt>

[Using Multilingual User Interface](using-multilingual-user-interface.md)
</dt> <dt>

[**GetFileMUIPath**](/windows/desktop/api/Winnls/nf-winnls-getfilemuipath)
</dt> </dl>

 

 



