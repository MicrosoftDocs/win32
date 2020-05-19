---
title: Registry Keys and Entries for a Type 2 Online Store
description: Registry Keys and Entries for a Type 2 Online Store
ms.assetid: 17dff940-3884-488a-9016-29bb47c51caf
keywords:
- Windows Media Player online stores,registry
- online stores,registry
- type 2 online stores,registry
- registry,type 2 online stores
ms.topic: article
ms.date: 05/31/2018
---

# Registry Keys and Entries for a Type 2 Online Store

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

To make a type 2 online store available in Windows Media Player, the online store provider must create the following registry subkeys and entries on the user's computer.


```C++
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MediaPlayer\Subscriptions\keyName]
"Capabilities"=dword:flags
"SubscriptionObjectGUID"=clsid
"FriendlyName"=friendlyName

[HKEY_CLASSES_ROOT\CLSID\clsid]
@=className

[HKEY_CLASSES_ROOT\CLSID\clsid\InprocServer32]
@=moduleName
"ThreadingModel"="Apartment"
```



In the preceding registry syntax, the symbols in italic are placeholders for names and globally unique identifiers (GUIDs) that are specific to the online store. The following table describes those placeholders.



| Placeholder    | Description                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *keyName*      | A string agreed upon between Microsoft and the online store. This string uniquely identifies the online store.Example: "Proseware"<br/>                                                                                                                                                                                                                                                          |
| *flags*        | A bitwise **OR** of one or more plug-in capability flags These flags specify whether Windows Media Player should call particular methods of [IWMPSubscriptionService](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice) and [IWMPSubscriptionService2](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice2). For information about supported flags, see the table of plug-in capability flags that follows this table.Example: 00000037<br/> |
| *clsid*        | A GUID that is the class identifier (CLSID) for the class that implements **IWMPSubscriptionService** in the online store's plug-in. This GUID must be in registry format, complete with the curly braces.Format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}<br/>                                                                                                                                    |
| *friendlyname* | A friendly name for the online store.Example: "Proseware Music Service"<br/>                                                                                                                                                                                                                                                                                                                     |
| *pluginName*   | A name for the online store's plug-in.Example: "Proseware Service Plug-in"<br/>                                                                                                                                                                                                                                                                                                                  |
| *className*    | The name of the class that implements **IWMPSubscriptionService** in the online store's plug-in.Example: "CProsewareService"<br/>                                                                                                                                                                                                                                                                |
| *moduleName*   | The fully qualified path to the DLL that implements the online store's plug-in.Example: "C:\\Program Files\\Proseware\\ProsewareService.dll"<br/>                                                                                                                                                                                                                                                |



 

The following table describes the plug-in capability flags.



| Flag                                    | Value | Description                                                                                                                                                                                                                        |
|-----------------------------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBSCRIPTION\_CAP\_ALLOWPLAY            | 0X1   | Windows Media Player should call [IWMPSubscriptionService::allowPlay](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice-allowplay).                                                                                                                      |
| SUBSCRIPTION\_CAP\_ALLOWCDBURN          | 0X2   | Windows Media Player should call [IWMPSubscriptionService::allowCDBurn](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice-allowcdburn).                                                                                                                  |
| SUBSCRIPTION\_CAP\_ALLOWPDATRANSFER     | 0X4   | Windows Media Player should call [IWMPSubscriptionService::allowPDATransfer](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice-allowpdatransfer).                                                                                                        |
| SUBSCRIPTION\_CAP\_BACKGROUNDPROCESSING | 0X8   | Windows Media Player should call [IWMPSubscriptionService::startBackgroundProcessing](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice-startbackgroundprocessing).                                                                                      |
| SUBSCRIPTION\_CAP\_DEVICEAVAILABLE      | 0X10  | Windows Media Player should call [IWMPSubscriptionService2::deviceAvailable](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice2-deviceavailable).                                                                                                        |
| SUBSCRIPTION\_CAP\_PREPAREFORSYNC       | 0X20  | Windows Media Player should call [IWMPSubscriptionService2::prepareForSync](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice2-prepareforsync).                                                                                                          |
| SUBSCRIPTION\_V1\_CAPS                  | 0XF   | Default. This value is used if none is registered. This is equivalent to combining SUBSCRIPTION\_CAP\_ALLOWPLAY, SUBSCRIPTION\_CAP\_ALLOWCDBURN, SUBSCRIPTION\_CAP\_ALLOWPDATRANSFER, and SUBSCRIPTION\_CAP\_BACKGROUNDPROCESSING. |



 

**Registry Entries for Development and Testing**

When you begin developing your online store, Microsoft provides you with two keys: a test key and a production key. During the development and testing phase, your online store will appear in Windows Media Player only if your test key or your production key is in the registry on the user's computer. For more information about the test and production keys, see [Test and Production Keys for a Type 2 Online Store](test-and-production-keys-for-a-type-2-online-store.md).

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

[**Reference for Type 2 Online Stores**](reference-for-type-2-online-stores.md)
</dt> </dl>

 

 





