---
description: As of Windows Vista, Control Panel items included with Windows are given a canonical name that can be used in an API call or a command-line instruction to programmatically launch that item.
ms.assetid: A02DFC9F-646D-40d8-901C-7239A820DE2C
title: Canonical Names of Control Panel Items
ms.topic: article
ms.date: 05/31/2018
---

# Canonical Names of Control Panel Items

As of Windows Vista, Control Panel items included with Windows are given a canonical name that can be used in an [API call or a command-line instruction](executing-control-panel-items.md) to programmatically launch that item. As of Windows 7 and Windows Server 2008 R2, canonical names can be used in a group policy to hide specific Control Panel items. This topic provides details for each Control Panel item: canonical name, GUID, module name, and the operating system versions that recognize the canonical name.

> [!Note]  
> Canonical names for Control Panel items are not supported prior to Windows Vista.

 

-   [Control Panel Canonical Names](#control-panel-canonical-names)
-   [Deprecated Control Panel Canonical Names](#deprecated-control-panel-canonical-names)
-   [Using Canonical Names in Group Policy](#using-canonical-names-in-local-group-policy)
-   [Remarks](#remarks)

## Control Panel Canonical Names

Points to remember when working with these values:

-   By definition, canonical names do not change based on the system language; they're always in English, even if the system's language is not.
-   Not all Control Panel items are present in all varieties of Windows.
-   Some Control Panel items only appear if the right hardware is detected on the system.
-   Third parties can also add Control Panel items. The canonical names listed here are only for Control Panel items that are included with Windows.

The following are the Control Panel items available in Windows 8.1:

-   [Action Center](#action-center)
-   [Administrative Tools](#administrative-tools)
-   [AutoPlay](#autoplay)
-   [Biometric Devices](#biometric-devices)
-   [BitLocker Drive Encryption](#bitlocker-drive-encryption)
-   [Color Management](#color-management)
-   [Credential Manager](#credential-manager)
-   [Date and Time](#date-and-time)
-   [Default Programs](#default-programs)
-   [Device Manager](#device-manager)
-   [Devices and Printers](#devices-and-printers)
-   [Display](#display)
-   [Ease of Access Center](#ease-of-access-center)
-   [Family Safety](#family-safety)
-   [File History](#file-history)
-   [Folder Options](#folder-options)
-   [Fonts](#fonts)
-   [HomeGroup](#homegroup)
-   [Indexing Options](#indexing-options)
-   [Infrared](#infrared)
-   [Internet Options](#internet-options)
-   [iSCSI Initiator](#iscsi-initiator)
-   [iSNS Server](#isns-server)
-   [Keyboard](#keyboard)
-   [Location Settings](#location-settings)
-   [Mouse](#mouse)
-   [MPIOConfiguration](#mpioconfiguration)
-   [Network and Sharing Center](#network-and-sharing-center)
-   [Notification Area Icons](#notification-area-icons)
-   [Pen and Touch](#pen-and-touch)
-   [Personalization](#personalization)
-   [Phone and Modem](#phone-and-modem)
-   [Power Options](#power-options)
-   [Programs and Features](#programs-and-features)
-   [Recovery](#recovery)
-   [Region](#region)
-   [RemoteApp and Desktop Connections](#remoteapp-and-desktop-connections)
-   [Sound](#sound)
-   [Speech Recognition](#speech-recognition)
-   [Storage Spaces](#storage-spaces)
-   [Sync Center](#sync-center)
-   [System](#system)
-   [Tablet PC Settings](#tablet-pc-settings)
-   [Taskbar and Navigation](#taskbar-and-navigation)
-   [Troubleshooting](#troubleshooting)
-   [TSAppInstall](#tsappinstall)
-   [User Accounts](#user-accounts)
-   [Windows Anytime Upgrade](#windows-anytime-upgrade)
-   [Windows Defender](#windows-defender)
-   [Windows Firewall](#windows-firewall)
-   [Windows Mobility Center](#windows-mobility-center)
-   [Windows To Go](#windows-to-go)
-   [Windows Update](#windows-update)
-   [Work Folders](#work-folders)

### Action Center

-   **Canonical name**: Microsoft.ActionCenter
-   **GUID**: {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\ActionCenterCPL.dll,-1
-   **Pages**

    | Page Name           | Opens                      |
    |---------------------|----------------------------|
    | MaintenanceSettings | Automatic Maintenance      |
    | pageProblems        | Problem Reports            |
    | pageReliabilityView | Reliability Monitor        |
    | pageResponseArchive | Archived Messages          |
    | pageSettings        | Problem Reporting Settings |

    

     

### Administrative Tools

-   **Canonical name**: Microsoft.AdministrativeTools
-   **GUID**: {D20EA4E1-3957-11d2-A40B-0C5020524153}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\system32\\shell32.dll,-22982

### AutoPlay

-   **Canonical name**: Microsoft.AutoPlay
-   **GUID**: {9C60DE1E-E5FC-40f4-A487-460851A8D915}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\autoplay.dll,-1

### Biometric Devices

-   **Canonical name**: Microsoft.BiometricDevices
-   **GUID**: {0142e4d0-fb7a-11dc-ba4a-000ffe7ab428}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\biocpl.dll,-1

### BitLocker Drive Encryption

-   **Canonical name**: Microsoft.BitLockerDriveEncryption
-   **GUID**: {D9EF8727-CAC2-4e60-809E-86F80A666C91}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\fvecpl.dll,-1

### Color Management

-   **Canonical name**: Microsoft.ColorManagement
-   **GUID**: {B2C761C6-29BC-4f19-9251-E6195265BAF1}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%systemroot%\\system32\\colorcpl.exe,-6

### Credential Manager

-   **Canonical name**: Microsoft.CredentialManager
-   **GUID**: {1206F5F1-0569-412C-8FEC-3204630DFB70}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\system32\\Vault.dll,-1
-   **Pages**

    | Page Name                   | Opens               |
    |-----------------------------|---------------------|
    | ?SelectedVault=CredmanVault | Windows Credentials |

    

     

### Date and Time

-   **Canonical name**: Microsoft.DateAndTime
-   **GUID**: {E2E7934B-DCE5-43C4-9576-7FE4F75E7480}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\timedate.cpl,-51
-   **Pages**

    | Page Name | Opens             |
    |-----------|-------------------|
    | 1         | Additional Clocks |

    

     

### Default Programs

-   **Canonical name**: Microsoft.DefaultPrograms
-   **GUID**: {17cd9488-1228-4b2f-88ce-4298e93e0966}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\sud.dll,-1
-   **Pages**

    | Page Name          | Opens                |
    |--------------------|----------------------|
    | pageDefaultProgram | Set Default Programs |
    | pageFileAssoc      | Set Associations     |

    

     

### Device Manager

-   **Canonical name**: Microsoft.DeviceManager
-   **GUID**: {74246bfc-4c96-11d0-abef-0020af6b0b7a}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\devmgr.dll,-4

### Devices and Printers

-   **Canonical name**: Microsoft.DevicesAndPrinters
-   **GUID**: {A8A91A66-3A7D-4424-8D24-04E180695C7A}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%systemroot%\\system32\\DeviceCenter.dll,-1000

### Display

-   **Canonical name**: Microsoft.Display
-   **GUID**: {C555438B-3C23-4769-A71F-B6D3D9B6053A}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\Display.dll,-1
-   **Pages**

    | Page Name | Opens             |
    |-----------|-------------------|
    | Settings  | Screen Resolution |

    

     

### Ease of Access Center

-   **Canonical name**: Microsoft.EaseOfAccessCenter
-   **GUID**: {D555645E-D4F8-4c29-A827-D93C859C4F2A}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\accessibilitycpl.dll,-10
-   **Pages**

    | Page Name               | Opens                                                               |
    |-------------------------|---------------------------------------------------------------------|
    | pageEasierToClick       | Make the mouse easier to use                                        |
    | pageEasierToSee         | Make the computer easier to see                                     |
    | pageEasierWithSounds    | Use text or visual alternatives for sounds                          |
    | pageFilterKeysSettings  | Set up Filter Keys                                                  |
    | pageKeyboardEasierToUse | Make the keyboard easier to use                                     |
    | pageNoMouseOrKeyboard   | Use the computer without a mouse or keyboard                        |
    | pageNoVisual            | Use the computer without a display                                  |
    | pageQuestionsCognitive  | Get recommendations to make your computer easier to use (cognitive) |
    | pageQuestionsEyesight   | Get recommendations to make your computer easier to use (eyesight)  |

    

     

### Family Safety

-   **Canonical name**: Microsoft.ParentalControls
-   **GUID**: {96AE8D84-A250-4520-95A5-A47A7E3C548B}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\wpccpl.dll,-100
-   **Pages**

    | Page Name   | Opens                                  |
    |-------------|----------------------------------------|
    | pageUserHub | Choose a user and set up Family Safety |

    

     

### File History

-   **Canonical name**: Microsoft.FileHistory
-   **GUID**: {F6B6E965-E9B2-444B-9286-10C9152EDBC5}
-   **Supported OS**: Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\fhcpl.dll,-52
-   File History includes a newer version of the Backup and Restore item, but that older item's canonical name does not remap to File History.

### Folder Options

-   **Canonical name**: Microsoft.FolderOptions
-   **GUID**: {6DFD7C5C-2451-11d3-A299-00C04F8EF6AF}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\system32\\shell32.dll,-22985

### Fonts

-   **Canonical name**: Microsoft.Fonts
-   **GUID**: {93412589-74D4-4E4E-AD0E-E0CB621440FD}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\FontExt.dll,-8007

### HomeGroup

-   **Canonical name**: Microsoft.HomeGroup
-   **GUID**: {67CA7650-96E6-4FDD-BB43-A8E774F73A57}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\hgcpl.dll,-1

### Indexing Options

-   **Canonical name**: Microsoft.IndexingOptions
-   **GUID**: {87D66A43-7B11-4A28-9811-C86EE395ACF7}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\srchadmin.dll,-601

### Infrared

-   **Canonical name**: Microsoft.Infrared
-   **GUID**: {A0275511-0E86-4ECA-97C2-ECD8F1221D08}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\irprops.cpl,-1

### Internet Options

-   **Canonical name**: Microsoft.InternetOptions
-   **GUID**: {A3DD4F92-658A-410F-84FD-6FBBBEF2FFFE}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @C:\\Windows\\System32\\inetcpl.cpl,-4312
-   **Pages**

    | Page Name | Opens       |
    |-----------|-------------|
    | 1         | Security    |
    | 2         | Privacy     |
    | 3         | Content     |
    | 4         | Connections |
    | 5         | Programs    |
    | 6         | Advanced    |

    

     

### iSCSI Initiator

-   **Canonical name**: Microsoft.iSCSIInitiator
-   **GUID**: {A304259D-52B8-4526-8B1A-A1D6CECC8243}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\iscsicpl.dll,-5001

### iSNS Server

-   **Canonical name**: Microsoft.iSNSServer
-   **GUID**: {0D2A3442-5181-4E3A-9BD4-83BD10AF3D76}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\isnssrv.dll,-5005
-   This Control Panel item will be seen only in server versions of Windows.

### Keyboard

-   **Canonical name**: Microsoft.Keyboard
-   **GUID**: {725BE8F7-668E-4C7B-8F90-46BDB0936430}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\main.cpl,-102

### Location Settings

-   **Canonical name**: Microsoft.LocationSettings
-   **GUID**: {E9950154-C418-419e-A90A-20C5287AE24B}
-   **Supported OS**: Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\SensorsCpl.dll,-1

### Mouse

-   **Canonical name**: Microsoft.Mouse
-   **GUID**: {6C8EEC18-8D75-41B2-A177-8831D59D2D50}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\main.cpl,-100
-   **Pages**

    | Page Name | Opens           |
    |-----------|-----------------|
    | 1         | Pointers        |
    | 2         | Pointer Options |
    | 3         | Wheel           |
    | 4         | Hardware        |

    

     

### MPIOConfiguration

-   **Canonical name**: Microsoft.MPIOConfiguration
-   **GUID**: {AB3BE6AA-7561-4838-AB77-ACF8427DF426}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\mpiocpl.dll,-1000
-   This Control Panel item will be seen only in server versions of Windows.

### Network and Sharing Center

-   **Canonical name**: Microsoft.NetworkAndSharingCenter
-   **GUID**: {8E908FC9-BECC-40f6-915B-F4CA0E70D03D}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\netcenter.dll,-1
-   **Pages**

    | Page Name  | Opens                     |
    |------------|---------------------------|
    | Advanced   | Advanced sharing settings |
    | ShareMedia | Media streaming options   |

    

     

### Notification Area Icons

-   **Canonical name**: Microsoft.NotificationAreaIcons
-   **GUID**: {05d7b0f4-2121-4eff-bf6b-ed3f69b894d9}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\taskbarcpl.dll,-1

### Pen and Touch

-   **Canonical name**: Microsoft.PenAndTouch
-   **GUID**: {F82DF8F7-8B9F-442E-A48C-818EA735FF9B}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\tabletpc.cpl,-10103
-   **Pages**

    | Page Name | Opens       |
    |-----------|-------------|
    | 1         | Flicks      |
    | 2         | Handwriting |

    

     

### Personalization

-   **Canonical name**: Microsoft.Personalization
-   **GUID**: {ED834ED6-4B5A-4bfe-8F11-A626DCB6A921}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\themecpl.dll,-1
-   **Pages**

    | Page Name        | Opens                |
    |------------------|----------------------|
    | pageColorization | Color and Appearance |
    | pageWallpaper    | Desktop Background   |

    

     

### Phone and Modem

-   **Canonical name**: Microsoft.PhoneAndModem
-   **GUID**: {40419485-C444-4567-851A-2DD7BFA1684D}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\telephon.cpl,-1
-   The window that this value launches is titled "Location Information" in versions of Windows prior to Windows 8. The item's UI is considerably changed as of Windows 8.

### Power Options

-   **Canonical name**: Microsoft.PowerOptions
-   **GUID**: {025A5937-A6BE-4686-A844-36FE4BEC8B6D}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\powercpl.dll,-1
-   **Pages**

    | Page Name          | Opens              |
    |--------------------|--------------------|
    | pageGlobalSettings | System Settings    |
    | pagePlanSettings   | Edit Plan Settings |

    

     

### Programs and Features

-   **Canonical name**: Microsoft.ProgramsAndFeatures
-   **GUID**: {7b81be6a-ce2b-4676-a29e-eb907a5126c5}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%systemroot%\\system32\\appwiz.cpl,-159
-   **Pages**

    | Page Name                                | Opens             |
    |------------------------------------------|-------------------|
    | ::{D450A8A1-9568-45C7-9C0E-B4F9FB4537BD} | Installed Updates |

    

     

### Recovery

-   **Canonical name**: Microsoft.Recovery
-   **GUID**: {9FE63AFD-59CF-4419-9775-ABCC3849F861}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\recovery.dll,-101

### Region

-   **Canonical name**: Microsoft.RegionAndLanguage
-   **GUID**: {62D8ED13-C9D0-4CE8-A914-47DD628FB1B0}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\intl.cpl,-1
-   The Region and Language item found in Windows 7 was split as of Windows 8. Microsoft.RegionAndLanguage now launches the Region item. To launch the Language item, use [Microsoft.Language](#location-settings).
-   **Pages**

    | Page Name | Opens          |
    |-----------|----------------|
    | 1         | Location       |
    | 2         | Administrative |

    

     

### RemoteApp and Desktop Connections

-   **Canonical name**: Microsoft.RemoteAppAndDesktopConnections
-   **GUID**: {241D7C96-F8BF-4F85-B01F-E2B043341A4B}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\tsworkspace.dll,-15300

### Sound

-   **Canonical name**: Microsoft.Sound
-   **GUID**: {F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\mmsys.cpl,-300

### Speech Recognition

-   **Canonical name**: Microsoft.SpeechRecognition
-   **GUID**: {58E3C745-D971-4081-9034-86E34B30836A}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\Speech\\SpeechUX\\speechuxcpl.dll,-1

### Storage Spaces

-   **Canonical name**: Microsoft.StorageSpaces
-   **GUID**: {F942C606-0914-47AB-BE56-1321B8035096}
-   **Supported OS**: Windows 8, Windows 8.1
-   **Module name**: @C:\\Windows\\System32\\SpaceControl.dll,-1

### Sync Center

-   **Canonical name**: Microsoft.SyncCenter
-   **GUID**: {9C73F5E5-7AE7-4E32-A8E8-8D23B85255BF}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\SyncCenter.dll,-3000

### System

-   **Canonical name**: Microsoft.System
-   **GUID**: {BB06C0E4-D293-4f75-8A90-CB05B6477EEE}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\systemcpl.dll,-1

### Tablet PC Settings

-   **Canonical name**: Microsoft.TabletPCSettings
-   **GUID**: {80F3F1D5-FECA-45F3-BC32-752C152E456E}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\tabletpc.cpl,-10100

### Taskbar and Navigation

-   **Canonical name**: Microsoft.Taskbar
-   **GUID**: {0DF44EAA-FF21-4412-828E-260A8728E7F1}
-   **Supported OS**: Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\system32\\shell32.dll,-32517

### Troubleshooting

-   **Canonical name**: Microsoft.Troubleshooting
-   **GUID**: {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\DiagCpl.dll,-1
-   **Pages**

    | Page Name   | Opens   |
    |-------------|---------|
    | HistoryPage | History |

    

     

### TSAppInstall

-   **Canonical name**: Microsoft.TSAppInstall
-   **GUID**: {BAA884F4-3432-48b8-AA72-9BF20EEF31D5}
-   **Supported OS**: Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%systemroot%\\system32\\tsappinstall.exe,-2001

### User Accounts

-   **Canonical name**: Microsoft.UserAccounts
-   **GUID**: {60632754-c523-4b62-b45c-4172da012619}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\usercpl.dll,-1

### Windows Anytime Upgrade

-   **Canonical name**: Microsoft.WindowsAnytimeUpgrade
-   **GUID**: {BE122A0E-4503-11DA-8BDE-F66BAD1E3F3A}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @$(resourceString.\_SYS\_MOD\_PATH),-1

### Windows Defender

-   **Canonical name**: Microsoft.WindowsDefender
-   **GUID**: {D8559EB9-20C0-410E-BEDA-7ED416AECC2A}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%ProgramFiles%\\Windows Defender\\MsMpRes.dll,-104

### Windows Firewall

-   **Canonical name**: Microsoft.WindowsFirewall
-   **GUID**: {4026492F-2F69-46B8-B9BF-5654FC07E423}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @C:\\Windows\\system32\\FirewallControlPanel.dll,-12122
-   **Pages**

    | Page Name         | Opens        |
    |-------------------|--------------|
    | pageConfigureApps | Allowed apps |

    

     

### Windows Mobility Center

-   **Canonical name**: Microsoft.MobilityCenter
-   **GUID**: {5ea4f148-308c-46d7-98a9-49041b1dd468}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\system32\\mblctr.exe,-1002

### Windows To Go

-   **Canonical name**: Microsoft.PortableWorkspaceCreator
-   **GUID**: {8E0C279D-0BD1-43C3-9EBD-31C3DC5B8A77}
-   **Supported OS**: Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\System32\\pwcreator.exe,-151

### Windows Update

-   **Canonical name**: Microsoft.WindowsUpdate
-   **GUID**: {36eef7db-88ad-4e81-ad49-0e313f0c35f8}
-   **Supported OS**: Windows Vista, Windows 7, Windows 8, Windows 8.1
-   **Module name**: @%SystemRoot%\\system32\\wucltux.dll,-1
-   **Pages**

    | Page Name         | Opens               |
    |-------------------|---------------------|
    | pageSettings      | Change settings     |
    | pageUpdateHistory | View update history |

    

     

### Work Folders

-   **Canonical name**: Microsoft.WorkFolders
-   **GUID**: {ECDB0924-4208-451E-8EE0-373C0956DE16}
-   **Supported OS**: Windows 8.1
-   **Module name**: @C:\\Windows\\System32\\WorkfoldersControl.dll,-1

## Deprecated Control Panel Canonical Names

The following are canonical names that are no longer in use as of Windows 8.1 or later. Some have been removed altogether. Others have been remapped in these situations:

-   A Control Panel item is renamed. The renamed item is given a new canonical name but keeps the same GUID. In this case, the old canonical name launches the renamed Control Panel item. Be aware that the item that's launched might not use the same UI as that item's older version.
-   The functionality of one or more Control Panel items is moved or consolidated into a new item. In this case, the old canonical name maps to the most appropriate new Control Panel item.

> [!Note]  
> Remappings exist for backward compatibility. You should not use deprecated values in new code.

 



| Deprecated canonical name                                   | Control Panel Item                | GUID                                   | Notes                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------|-----------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Microsoft.AddHardware                                       | Add Hardware                      | {7A979262-40CE-46ff-AEEE-7884AC3B6136} | Maps to [Microsoft.DevicesAndPrinters](#devices-and-printers) as of Windows 7.                                                                                                                                                                                                                                                                            |
| Microsoft.AudioDevicesAndSoundThemes                        | Sound                             | {F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D} | Maps to [Microsoft.Sound](#sound) as of Windows 7.                                                                                                                                                                                                                                                                                                        |
| Microsoft.BackupAndRestoreCenter/Microsoft.BackupAndRestore | Backup and Restore Center         | {B98A2BEA-7D42-4558-8BD1-832F41BAC6FD} | Microsoft.BackupAndRestoreCenter maps to Microsoft.BackupAndRestore in Windows 7. Both are removed as of Windows 8; use [Microsoft.FileHistory](#file-history) instead.                                                                                                                                                                                   |
| Microsoft.CardSpace                                         | Windows CardSpace                 | {78CB147A-98EA-4AA6-B0DF-C8681F69341C} | Removed as of Windows 8.                                                                                                                                                                                                                                                                                                                                  |
| Microsoft.DesktopGadgets                                    | Desktop Gadgets                   | {37efd44d-ef8d-41b1-940d-96973a50e9e0} | Removed as of Windows 8.                                                                                                                                                                                                                                                                                                                                  |
| Microsoft.GetProgramsOnline                                 | Windows Marketplace               | {3e7efb4c-faf1-453d-89eb-56026875ef90} | Removed as of Windows 7.                                                                                                                                                                                                                                                                                                                                  |
| Microsoft.InfraredOptions                                   | Infrared                          | {A0275511-0E86-4ECA-97C2-ECD8F1221D08} | Maps to [Microsoft.Infrared](#infrared) as of Windows 7.                                                                                                                                                                                                                                                                                                  |
| Microsoft.Language                                          | Language                          | {BF782CC9-5A52-4A17-806C-2A894FFEEAC5} | Removed as of Windows 10, version 1803                                                                                                                                                                                                                                                                                                                    |
| Microsoft.LocationAndOtherSensors                           | Location and Other Sensors        | {E9950154-C418-419e-A90A-20C5287AE24B} | Maps to [Microsoft.LocationSettings](#infrared) as of Windows 8.                                                                                                                                                                                                                                                                                          |
| Microsoft.PenAndInputDevices                                | Pen and Input Devices             | {F82DF8F7-8B9F-442E-A48C-818EA735FF9B} | Maps to [Microsoft.PenAndTouch](#pen-and-touch) as of Windows 7.                                                                                                                                                                                                                                                                                          |
| Microsoft.PeopleNearMe                                      | People Near Me                    | {5224F545-A443-4859-BA23-7B5A95BDC8EF} | Removed as of Windows 8.                                                                                                                                                                                                                                                                                                                                  |
| Microsoft.PerformanceInformationAndTools                    | Performance Information and Tools | {78F3955E-3B90-4184-BD14-5397C15F1EFC} | Removed as of Windows 8.1.                                                                                                                                                                                                                                                                                                                                |
| Microsoft.PhoneAndModemOptions                              | Phone and Modem                   | {40419485-C444-4567-851A-2DD7BFA1684D} | Maps to [Microsoft.PhoneAndModem](#phone-and-modem) as of Windows 7.                                                                                                                                                                                                                                                                                      |
| Microsoft.Printers                                          | Printers                          | {2227A280-3AEA-1069-A2DE-08002B30309D} | Maps to [Microsoft.DevicesAndPrinters](#devices-and-printers) as of Windows 7.                                                                                                                                                                                                                                                                            |
| Microsoft.ProblemReportsAndSolutions                        | Problem Reports and Solutions     | {FCFEECAE-EE1B-4849-AE50-685DCF7717EC} | Maps to [Microsoft.ActionCenter](#action-center) as of Windows 7.                                                                                                                                                                                                                                                                                         |
| Microsoft.RegionalAndLanguageOptions                        | Regional and Language Options     | {62D8ED13-C9D0-4CE8-A914-47DD628FB1B0} | Maps to [Microsoft.RegionAndLanguage](#region) as of Windows 7. Note that as of Windows 8, Region and Language were each given their own Control Panel item. Both Microsoft.RegionalAndLanguageOptions and Microsoft.RegionAndLanguage currently open the Region item. You must use [Microsoft.Language](#location-settings) to access the Language item. |
| Microsoft.SecurityCenter                                    | Windows Security Center           | {087DA31B-0DD3-4537-8E23-64A18591F88B} | Maps to [Microsoft.ActionCenter](#action-center) as of Windows 7.                                                                                                                                                                                                                                                                                         |
| Microsoft.SpeechRecognitionOptions                          | Speech Recognition Options        | {58E3C745-D971-4081-9034-86E34B30836A} | Maps to [Microsoft.SpeechRecognition](#speech-recognition) as of Windows 7.                                                                                                                                                                                                                                                                               |
| Microsoft.TaskbarAndStartMenu                               | Taskbar and Start Menu            | {0DF44EAA-FF21-4412-828E-260A8728E7F1} | Maps to [Microsoft.Taskbar](#speech-recognition) as of Windows 8.                                                                                                                                                                                                                                                                                         |
| Microsoft.WelcomeCenter                                     | Welcome Center                    | {CB1B7F8C-C50A-4176-B604-9E24DEE8D4D1} | Maps to Microsoft.GettingStarted in Windows 7. Launches the Control Panel home page as of Windows 8.                                                                                                                                                                                                                                                      |
| Microsoft.WindowsSidebarProperties                          | Windows Sidebar Properties        | {37efd44d-ef8d-41b1-940d-96973a50e9e0} | Maps to Microsoft.DesktopGadgets in Windows 7. Removed as of Windows 8.                                                                                                                                                                                                                                                                                   |
| Microsoft.WindowsSideShow                                   | Windows SideShow                  | {E95A4861-D57A-4be1-AD0F-35267E261739} | Feature deprecated in Windows 8, removed as of Windows 8.1.                                                                                                                                                                                                                                                                                               |



 

## Using Canonical Names in Local Group Policy

As of Windows 7, you can use canonical names to restrict access to individual Control Panel items through group policy. This same procedure can be used in Windows Vista, but you have to use the module name instead of the canonical name.

### Hiding individual Control Panel items

Use this method if you want to show more Control Panel items than you want to hide.

1.  Run the Gpedit.msc file to launch the Local Group Policy Editor. You can also type "group policy" at the Windows 8.1 Start screen and select **Edit group policy** from the search results.
2.  Select **User Configuration** > **Administrative Templates** > **Control Panel**.
3.  Select **Hide specified Control Panel items**.
4.  In the **Hide Specified Control Panel Items** window that opens, click **Enabled**.
5.  Click the **Show** button in the Options panel to show the list of disallowed Control Panel items.
6.  In the **Show Contents** window that opens, type a canonical name into the **Value** column. Repeat as necessary.
7.  Click **OK**.

### Showing individual Control Panel items

Use this method if you want to hide more Control Panel items than you want to show.

1.  Run the Gpedit.msc file to launch the Local Group Policy Editor. You can also type "group policy" at the Windows 8.1 Start screen and select **Edit group policy** from the search results.
2.  Select **User Configuration** > **Administrative Templates** > **Control Panel**.
3.  Select **Show only specified Control Panel items**.
4.  In the **Show Only Specified Control Panel Items** window that opens, click **Enabled**. This hides everything in the Control Panel.
5.  Click the **Show** button in the Options panel to show the list of allowed Control Panel items.
6.  In the **Show Contents** window that opens, type a canonical name into the **Value** column. Repeat as necessary.
7.  Click **OK**.

If you want to remove all of the entries that you've added to a Show or Hide Control Panel items list, return to the screen in step 4 and select **Not Configured** to clear the list. If you want to retain your entries but suspend the restrictions, select **Disabled**.

## Remarks

You might see items in your Control Panel that are not listed here. Those items are not part of Windows, but instead are added during the installation of various software and hardware, such as Microsoft Office or a video card. Non-Windows Control Panel items may or may not have a canonical name. To find the canonical name of a Control Panel item not listed here, look in the registry under these paths:

```
HKEY_CLASSES_ROOT
   CLSID
      {CLSID of the Control Panel item}
         System.ApplicationName
```

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Classes
         CLSID
            {CLSID of the Control Panel item}
               System.ApplicationName
```

For more information that can help you discover the necessary CLSIDs, see [How to Register Executable Control Panel Items](how-to-register-an-executable-control-panel-item-registration-.md) and [How to Register DLL Control Panel Items](how-to-register-dll-control-panel-item-registration-.md).

## Related topics

<dl> <dt>

[Executing Control Panel Items](executing-control-panel-items.md)
</dt> <dt>

[**IOpenControlPanel**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iopencontrolpanel)
</dt> </dl>

 

 



