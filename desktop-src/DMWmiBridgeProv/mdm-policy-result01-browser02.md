---
title: MDM_Policy_Result01_Browser02 class
description: The MDM\_Policy\_Result01\_Browser02 class represents the browser policies available.MDM\_Policy\_Result01\_Browser02 class represents the browser policies available.
ms.assetid: 06dc9f68-d9ea-4eec-93cb-1f26e8a6050d
keywords:
- MDM_Policy_Result01_Browser02 class
- MDM_Policy_Result01_Browser02 class, described
topic_type:
- apiref
api_name:
- MDM_Policy_Result01_Browser02
- MDM_Policy_Result01_Browser02.InstanceID
- MDM_Policy_Result01_Browser02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: article
ms.date: 05/31/2018
---

# MDM\_Policy\_Result01\_Browser02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_Policy\_Result01\_Browser02** class represents the browser policies available.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system", "local-user"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Result01_Browser02
{
  string InstanceID;
  string ParentID;
  sint32 AllowAddressBarDropdown;
  sint32 AllowAutofill;
  sint32 AllowCookies;
  sint32 AllowDeveloperTools;
  sint32 AllowInPrivate;
  sint32 AllowMicrosoftCompatibilityList;
  sint32 AllowDoNotTrack;
  sint32 AllowFlashClickToRun;
  sint32 AllowFlash;
  sint32 AllowExtensions;
  sint32 AllowPasswordManager;
  sint32 AllowPopups;
  sint32 AllowSearchEngineCustomization;
  sint32 AllowSearchSuggestionsinAddressBar;
  sint32 AllowSmartScreen;
  sint32 AlwaysEnableBooksLibrary;
  sint32 DisableLockdownOfStartPages;
  string ConfigureAdditionalSearchEngines;
  sint32 ClearBrowsingDataOnExit;
  string EnterpriseModeSiteList;
  string EnterpriseSiteListServiceUrl;
  string Homepages;
  sint32 LockdownFavorites;
  sint32 PreventAccessToAboutFlagsInMicrosoftEdge;
  sint32 PreventLiveTileDataCollection;
  sint32 PreventFirstRunPage;
  sint32 PreventSmartScreenPromptOverride;
  sint32 PreventSmartScreenPromptOverrideForFiles;
  sint32 PreventUsingLocalHostIPAddressForWebRTC;
  string ProvisionFavorites;
  sint32 SendIntranetTraffictoInternetExplorer;
  string SetDefaultSearchEngine;
  sint32 ShowMessageWhenOpeningSitesInInternetExplorer;
  sint32 SyncFavoritesBetweenIEAndMicrosoftEdge;
};
```

## Members

The **MDM\_Policy\_Result01\_Browser02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Result01\_Browser02** class has these properties.

<dl> <dt>

[AllowAddressBarDropdown](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowaddressbardropdown)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowAutofill](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowautofill)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowCookies](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowcookies)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowDeveloperTools](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowdevelopertools)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowDoNotTrack](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowdonottrack)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowExtensions](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowextensions)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowFlash](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowflash)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowFlashClickToRun](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowflashclicktorun)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowInPrivate](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowinprivate)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowMicrosoftCompatibilityList](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowmicrosoftcompatibilitylist)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPasswordManager](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowpasswordmanager)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPopups](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowpopups)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowSearchEngineCustomization](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowsearchenginecustomization)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowSearchSuggestionsinAddressBar](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowsearchsuggestionsinaddressbar)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowSmartScreen](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-allowsmartscreen)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AlwaysEnableBooksLibrary](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-alwaysenablebookslibrary)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ClearBrowsingDataOnExit](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-clearbrowsingdataonexit)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ConfigureAdditionalSearchEngines](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-configureadditionalsearchengines)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisableLockdownOfStartPages](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-disablelockdownofstartpages)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[EnterpriseModeSiteList](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-enterprisemodesitelist)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[EnterpriseSiteListServiceUrl](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-enterprisesitelistserviceurl)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Homepages](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-homepages)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://docs.microsoft.com/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "Browser".

</dd> <dt>

[LockdownFavorites](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-lockdownfavorites)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://docs.microsoft.com/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/Policy/Result"

</dd> <dt>

[PreventAccessToAboutFlagsInMicrosoftEdge](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-preventaccesstoaboutflagsinmicrosoftedge)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PreventFirstRunPage](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-preventfirstrunpage)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PreventLiveTileDataCollection](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-preventlivetiledatacollection)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PreventSmartScreenPromptOverride](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-preventsmartscreenpromptoverride)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PreventSmartScreenPromptOverrideForFiles](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-preventsmartscreenpromptoverrideforfiles)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PreventUsingLocalHostIPAddressForWebRTC](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-preventusinglocalhostipaddressforwebrtc)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ProvisionFavorites](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-provisionfavorites)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SendIntranetTraffictoInternetExplorer](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-sendintranettraffictointernetexplorer)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SetDefaultSearchEngine](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-setdefaultsearchengine)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ShowMessageWhenOpeningSitesInInternetExplorer](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-showmessagewhenopeningsitesininternetexplorer)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SyncFavoritesBetweenIEAndMicrosoftEdge](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-browser#browser-syncfavoritesbetweenieandmicrosoftedge)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM\\DMMap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](https://docs.microsoft.com/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

 





