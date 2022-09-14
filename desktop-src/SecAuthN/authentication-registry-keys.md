---
description: When it installs a network provider, your application should create the registry keys and values described in this topic.
ms.assetid: cc5a4a7b-02b5-4ecd-967c-de0656f00846
title: Authentication Registry Keys
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Registry Keys

When it installs a network provider, your application should create the registry keys and values described in this topic. These keys and values provide information to the MPR about the network providers installed on the system. The MPR checks these keys when it starts and loads the network provider DLLs that it finds.

Before you create a set of keys to hold information about your network provider, you should add the name of your network provider to the **order** key. This key is a subkey of the following key:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Control
            NetworkProvider
```

The **order** key contains a single value, **ProviderOrder**, which lists the installed providers and specifies the order in which they should be tried during operations that cycle through providers until an accepting provider is found.

The **ProviderOrder** value contains a comma-separated list of key names. Each key name in **ProviderOrder** identifies a network provider. When MPR cycles through the providers, it calls them in the order in which they appear in this list.

The provider name set in **ProviderOrder** should also be used as the name of the registry key that contains information about that provider. The provider-specific registry keys are created as subkeys of the following key:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Services
```

In other words, the provider names specified in **ProviderOrder** are the path to the registry of the network provider-specific keys, relative to the following path:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Services
```

When your network provider service is installed, the installation application should add a key as follows:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Services
            ProviderName
```

Where *ProviderName* is the name of the network provider as specified in the **ProviderOrder** value of the **order** key. The **Group** value under the *ProviderName* key should be set to "NetworkProvider". This identifies the service as being in the network provider group.

You must also create a subkey of *ProviderName*, **networkprovider**. This key contains the following values that describe the network provider.



| Value                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name**<br/>         | Contains the name of the provider. This name is displayed to the user as the name of the network in the browse dialog boxes and should match the **lpProvider** field returned in [**NETRESOURCE**](/windows/desktop/api/Winnetwk/ns-winnetwk-netresourcea) structures. This name should be some variation of the product name, preferably with some indication of the company as well, so that it is clear and unique. "MS-LanMan" for example is a good name, whereas "The Net" would be a poor choice.<br/> |
| **ProviderPath**<br/> | Contains the full path of the DLL that implements the network provider. MPR calls [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) on this path.<br/>                                                                                                                                                                                                                                                                                                                                |



 

The following values are used only by network providers that support the credential management functions, [**NPLogonNotify**](/windows/desktop/api/Npapi/nf-npapi-nplogonnotify) and [**NPPasswordChangeNotify**](/windows/desktop/api/Npapi/nf-npapi-nppasswordchangenotify).



| Value                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Class**<br/>               | A **DWORD** that identifies the class, or type, of provider functionality that this provider supports. Values may be joined by the **OR** operator when appropriate. Valid values for this are WN\_NETWORK\_CLASS, WN\_CREDENTIAL\_CLASS, WN\_PRIMARY\_AUTHENT\_CLASS, and WN\_SERVICE\_CLASS.<br/> Although a provider may support primary authenticator functionality, another means will be used to determine which authenticator is primary.<br/> **Windows XP/2000:** Switching primary authenticators is not supported, so this value is ignored. <br/> |
| **AuthentProviderPath**<br/> | This is the fully qualified file name for the DLL that exports the Credential Management Functions. This value is useful (but not required) only when the provider is identified as being a CREDENTIAL\_CLASS or PRIMARY\_AUTHENT\_CLASS provider. If this value is not present for a provider of this class, the credential management functions are expected to be exported from the DLL identified by the ProviderPath value. This value is used only if it is desirable to package the network functions and the credential manager functions in separate DLLs.<br/>  |



 

In addition to the values used to register network providers and credential managers, you can add a value to the registry to register a DLL to receive connection notifications. To do so, create a REG\_EXPAND\_SZ value under the following key:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Control
            NetworkProvider
               Notifyees
```

This value should specify the path to a DLL that implements the [Connection Notification API](connection-notification-api.md). The name of this value can be anything you want, as long as it does not conflict with preexisting value names.

## Example

The following example shows the registry keys for a system that has two network providers installed: LanmanWorkStation and AnotherNetSvc. AnotherNetSvc is also a credential manager. In the example, key names are bold and value names are italic.

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**NetworkProvider**\\**order**

*ProviderOrder* = "LanmanWorkStation,AnotherNetSvc"

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**NetworkProvider**\\**Notifyees**

*MyNotifyApp* = "c:\\connect\\connect.dll"

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**LanmanWorkStation**\\

*Group* = "NetworkProvider"

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**LanmanWorkStation**\\**NetworkProvider**

*Name* = "NT LanMan"*ProviderPath* = "ntlanman.dll"

*Class* = 0x00000001 (WN\_NETWORK\_CLASS)

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**AnotherNetSvc**\\

*Group* = "NetworkProvider"

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**AnotherNetSvc**\\**NetworkProvider**

*Name* = "Another Network"*ProviderPath* = "c:\\another\\anet.dll"

*Class* = 0x00000003 (WN\_NETWORK\_CLASS \| WN\_CREDENTIAL\_CLASS)

*AuthentProviderPath* = "c:\\another\\anetCM.dll"

 

