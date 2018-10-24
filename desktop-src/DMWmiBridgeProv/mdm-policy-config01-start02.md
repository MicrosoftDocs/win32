---
title: MDM_Policy_Config01_Start02 class
description: The MDM\_Policy\_Config01\_Start02 class represents the start screen policies available.
ms.assetid: 2aef29c8-164a-4111-9c1a-e63eeec2531e
keywords:
- MDM_Policy_Config01_Start02 class
- MDM_Policy_Config01_Start02 class, described
topic_type:
- apiref
api_name:
- MDM_Policy_Config01_Start02
- MDM_Policy_Config01_Start02.InstanceID
- MDM_Policy_Config01_Start02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MDM\_Policy\_Config01\_Start02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_Policy\_Config01\_Start02** class represents the start screen policies available.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Config01_Start02
{
  string InstanceID;
  string ParentID;
  sint32 AllowPinnedFolderVideos;
  sint32 AllowPinnedFolderSettings;
  sint32 AllowPinnedFolderPictures;
  sint32 AllowPinnedFolderPersonalFolder;
  sint32 AllowPinnedFolderNetwork;
  sint32 AllowPinnedFolderMusic;
  sint32 AllowPinnedFolderHomeGroup;
  sint32 AllowPinnedFolderFileExplorer;
  sint32 AllowPinnedFolderDownloads;
  sint32 AllowPinnedFolderDocuments;
  sint32 ForceStartSize;
  string StartLayout;
  sint32 NoPinningToTaskbar;
  string ImportEdgeAssets;
  sint32 HideUserTile;
  sint32 HideSwitchAccount;
  sint32 HideSleep;
  sint32 HideSignOut;
  sint32 HideShutDown;
  sint32 HideRestart;
  sint32 HideRecentlyAddedApps;
  sint32 HideRecentJumplists;
  sint32 HidePowerButton;
  sint32 HideLock;
  sint32 HideHibernate;
  sint32 HideFrequentlyUsedApps;
  sint32 HideChangeAccountSettings;
  sint32 HideAppList;
};
```

## Members

The **MDM\_Policy\_Config01\_Start02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Config01\_Start02** class has these properties.

<dl> <dt>

[AllowPinnedFolderDocuments](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfolderdocuments)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderDownloads](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfolderdownloads)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderFileExplorer](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfolderfileexplorer)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderHomeGroup](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfolderhomegroup)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderMusic](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfoldermusic)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderNetwork](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfoldernetwork)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderPersonalFolder](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfolderpersonalfolder)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderPictures](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfolderpictures)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderSettings](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfoldersettings)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPinnedFolderVideos](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-allowpinnedfoldervideos)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ForceStartSize](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-forcestartsize)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideAppList](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hideapplist)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideChangeAccountSettings](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hidechangeaccountsettings)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideFrequentlyUsedApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hidefrequentlyusedapps)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideHibernate](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hidehibernate)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideLock](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hidelock)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HidePowerButton](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hidepowerbutton)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideRecentJumplists](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hiderecentjumplists)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideRecentlyAddedApps](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hiderecentlyaddedapps)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideRestart](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hiderestart)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideShutDown](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hideshutdown)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideSignOut](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hidesignout)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideSleep](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hidesleep)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideSwitchAccount](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hideswitchaccount)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HideUserTile](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-hideusertile)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ImportEdgeAssets](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-importedgeassets)
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

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "Start"

</dd> <dt>

[NoPinningToTaskbar](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-nopinningtotaskbar)
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

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/Policy/Config"

</dd> <dt>

[StartLayout](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-start#start-startlayout)
</dt> <dd> <dl> <dt>

Data type: **string**
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

[Using PowerShell scripting with the WMI Bridge Provider](https://msdn.microsoft.com/library/windows/hardware/mt614877)
</dt> </dl>

 

 





