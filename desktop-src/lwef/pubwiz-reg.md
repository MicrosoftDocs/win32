---
title: Registering a Service
description: To add your service to the list of providers in either the Web Publishing Wizard or the Online Print Ordering Wizard, you must add the appropriate key and its values to the Windows registry.
ms.assetid: 4a6f6df8-f850-4a80-9cf9-e62f3350915f
keywords:
- register,services
- Web Publishing Wizard,registering
- Online Print Ordering Wizard,registering
- register,Web Publishing Wizard
- register,Online Print Ordering Wizard
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Service

To add your service to the list of providers in either the Web Publishing Wizard or the Online Print Ordering Wizard, you must add the appropriate key and its values to the Windows registry.

## Required Keys and Values

To add your service to the list of providers for the Web Publishing Wizard, add a key as shown below.

```
HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  PublishingWizard
                     PublishingWizard
                        Providers
                           MyProviderName
                              IconPath
                              DisplayName
                              Description
                              HREF
                              SupportedTypes
```

To add your service to the list of providers for the Online Print Ordering Wizard, add a key as shown below.

```
HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  PublishingWizard
                     InternetPhotoPrinting
                        Providers
                           MyProviderName
                              IconPath
                              DisplayName
                              Description
                              HREF
                              SupportedTypes
```

Each of the values is a string of type REG\_SZ. Provide its data as explained in the following table. 

| Value Name     | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IconPath       | The full path to the icon file, including the file name.                                                                                                                                                                                                                                                                                                                                                                        |
| DisplayName    | The name displayed for your service in the wizard's providers list.                                                                                                                                                                                                                                                                                                                                                             |
| Description    | A short description for your service. This description also displays in the wizard's providers list directly below the name of your service.                                                                                                                                                                                                                                                                                    |
| HREF           | The URL of the first page of your service.                                                                                                                                                                                                                                                                                                                                                                                      |
| SupportedTypes | The file types supported by your service. For instance, *\*.jpg*. By specifying only certain file types, your service only appears when those file types have been selected. If more than one file type has been selected, your service appears if any of those file types are supported by your service. If you want to specify multiple file types, separate them in the list with semicolons. For example, *\*.jpg; \*.bmp*. |



 

The following is a complete example for a photo processing service entitled "MyProvider."

```
HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  PublishingWizard
                     InternetPhotoPrinting
                        Providers
                           MyProvider
                              IconPath = C:\MyProviderFiles\MyIcon.ico
                              DisplayName = My Photo Processing Provider
                              Description = 24 hour processing guaranteed!
                              HREF = https://www.MyProvider.com/Intro.htm
                              SupportedTypes = *.jpg; *.gif; *.bmp
```

When the URL of your service is called, two values are added to the end of the URL—lcid and langid. For example, the URL string for the example above might be https:\//www.MyProvider.com/Intro.htm?lcid=1033&langid=1033. These variables are used for language and localization information.

-   **lcid** is used to inform the server of the client's country/region and language settings. It is not used to determine the language of the client's UI, but is used to determine the proper format for currency, date and time, and other region-specific data.
-   **langid** is used to inform the server of the client's default language setting so that it can use the proper language in the UI.

 

 




