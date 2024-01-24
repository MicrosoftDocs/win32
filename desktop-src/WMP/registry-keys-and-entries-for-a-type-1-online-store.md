---
title: Registry Keys and Entries for a Type 1 Online Store
description: Registry Keys and Entries for a Type 1 Online Store
ms.assetid: cf25a004-e0c3-407c-8704-54be3601528b
keywords:
- Windows Media Player online stores,registry
- online stores,registry
- type 1 online stores,registry
- registry,type 1 online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Registry Keys and Entries for a Type 1 Online Store

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To make a type 1 online store available in Windows Media Player, the online store provider must create the following registry subkeys and entries on the user's computer.


```C++
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MediaPlayer\Subscriptions\keyName]
"Capabilities"=dword:flags
"SubscriptionObjectGUID"=clsid
"FriendlyName"=friendlyName

[HKEY_CLASSES_ROOT\AppID\appid]
@=pluginName
"DllSurrogate"=""

[HKEY_CLASSES_ROOT\CLSID\clsid]
@=className
"AppID"="appid"

[HKEY_CLASSES_ROOT\CLSID\clsid\InprocServer32]
@=moduleName
"ThreadingModel"="threading"
```



> [!Note]  
> Setting the value of DllSurrogate to the empty string indicates that the COM runtime will load the online store's plug-in into the default DLL surrogate, dllhost.exe.

 

In the preceding registry syntax, the symbols in italic are placeholders for names and globally unique identifiers (GUIDs) that are specific to the online store. The following table describes those placeholders.



| Placeholder    | Description                                                                                                                                                                                                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *keyName*      | A string agreed upon between Microsoft and the online store. This string uniquely identifies the online store.Example: "Proseware"<br/>                                                                                                                                                                                   |
| *flags*        | A bitwise **OR** of one or more plug-in capability flags These flags specify whether Windows Media Player should call particular methods of [IWMPContentPartner](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartner). For information about supported flags, see the table of plug-in capability flags that follows this table.Example: 00000058<br/> |
| *clsid*        | A GUID that is the class identifier (CLSID) for the class that implements **IWMPContentPartner** in the online store's plug-in. This GUID must be in registry format, complete with the curly braces.Format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}<br/>                                                                  |
| *friendlyname* | A friendly name for the online store.Example: "Proseware Music Service"<br/>                                                                                                                                                                                                                                              |
| *appid*        | A GUID that is the application identifier (AppID) for the online store's plug-in. This GUID must be in registry format, complete with the curly braces.Format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}<br/>                                                                                                                |
| *pluginName*   | A name for the online store's plug-in.Example: "Proseware Content Partner Plug-in"<br/>                                                                                                                                                                                                                                   |
| *className*    | The name of the class that implements **IWMPContentpartner** in the online store's plug-in.Example: "CProsewarePartner"<br/>                                                                                                                                                                                              |
| *moduleName*   | The fully qualified path to the DLL that implements the online store's plug-in.Example: "C:\\Program Files\\Proseware\\ProsewarePartner.dll"<br/>                                                                                                                                                                         |
| *threading*    | The type of apartment the plug-in runs in. "ThreadingModel"="Apartment" indicates that the plug-in runs in a single-threaded apartment (STA). "ThreadingModel"="Free" indicates that the plug-in runs in the multithreaded apartment (MTA).                                                                                     |



 

The following table describes the plug-in capability flags.



| Flag                                    | Value | Description                                                                                                                                                                                                                                                                 |
|-----------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBSCRIPTION\_CAP\_BACKGROUNDPROCESSING | 0x8   | Windows Media Player should call [IWMPContentPartner::Notify](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-notify) to inform the plug-in when it should start and stop background processing.                                                                                                     |
| SUBSCRIPTION\_CAP\_DEVICEAVAILABLE      | 0x10  | Windows Media Player should call [IWMPContentPartner::UpdateDevice](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-updatedevice).                                                                                                                                                                   |
| SUBSCRIPTION\_CAP\_IS\_CONTENTPARTNER   | 0x40  | Informs Windows Media Player that the plug-in implements the **IWMPContentPartner** interface. All type 1 online store plug-ins must set this flag.                                                                                                                         |
| SUBSCRIPTION\_CAP\_ALTLOGIN             | 0x80  | Informs Windows Media Player that the plug-in supports an alternate login. If the plug-in supports an alternate login, Windows Media Player retrieves the alternate login URL and caption by calling [IWMPContentPartner::GetItemInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getiteminfo). |



 

**Registry Entries for Development and Testing**

When you begin developing your online store, Microsoft provides you with two keys: a test key and a production key. During the development and testing phase, your online store will appear in Windows Media Player only if your test key or your production key is in the registry on the user's computer. For more information about the test and production keys, see [Test and Production Keys for a Type 1 Online Store](test-and-production-keys-for-a-type-1-online-store.md).

Place your test or production key in the following location in the registry.


```C++
[HKEY_CURRENT_USER\Software\Microsoft\MediaPlayer\Services]
"TestParameter" = "key1;key2;...;keyN"
```



Note that the value of the TestParameter registry entry can specify multiple test or production keys. For example, suppose that Proseware has a test key of "1234" and Contoso has a test key of "2345". The following registry entry specifies that the test stores for Proseware and Contoso will appear in Windows Media Player.


```C++
[HKEY_CURRENT_USER\Software\Microsoft\MediaPlayer\Services]
"TestParameter" = "1234;2345"
```



**ActiveService Registry Entry**

When the user activates an online store, Windows Media Player writes information in the registry that identifies the active online store. Windows Media Player places the information in the following location in the registry on the user's computer.


```C++
[HKEY_CURRENT_USER\Software\Microsoft\MediaPlayer\Subscriptions]
"ActiveService"=serviceInfo
```



In the preceding registry syntax, *serviceInfo* is a placeholder for a string that contains descriptive information about the active online store.

## Related topics

<dl> <dt>

[**Reference for Type 1 Online Stores**](reference-for-type-1-online-stores.md)
</dt> </dl>

 

 





