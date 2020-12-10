---
title: Microsoft Windows Media DRM Client Structures
description: Microsoft Windows Media DRM Client Structures
ms.assetid: 794de1b7-d60c-435e-9f77-c4df109b5372
keywords:
- Windows Media Format SDK,structures
- digital rights management (DRM),structures
- DRM (digital rights management),structures
- DRM Client Extended APIs,structures
- Client Extended APIs,structures
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Windows Media DRM Client Structures

The following structures are supported by the Windows Media DRM Client Extended APIs.



| Structure or Enumeration                                                                    | Description                                                                                                                                                 |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS**](drm-audio-output-protection-ids.md)              | Contains a list of audio output protection identifiers.                                                                                                     |
| [**DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS\_EX**](drm-audio-output-protection-ids-ex.md)       | Contains a list of audio output protection identifiers. This structure extends **DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS** by adding a version number.          |
| [**DRM\_COPY\_OPL**](drmdrm-copy-opl.md)                                                   | Holds information about the output protection levels specified in a license for copy actions.                                                               |
| [**DRM\_LICENSE\_STATE\_DATA**](drmdrm-license-state-data.md)                              | Contains information about the license restrictions for a DRM right.                                                                                        |
| [**DRM\_MINIMUM\_OUTPUT\_PROTECTION\_LEVELS**](drmdrm-minimum-output-protection-levels.md) | Holds the minimum output protection levels (OPLs) for playback of various types of content.                                                                 |
| [**DRM\_OPL\_OUTPUT\_IDS**](drmdrm-opl-output-ids.md)                                      | Holds a number of OPL output identifiers.                                                                                                                   |
| [**DRM\_OUTPUT\_PROTECTION**](drm-output-protection.md)                                    | Holds information about an output protection technology.                                                                                                    |
| [**DRM\_OUTPUT\_PROTECTION\_EX**](drm-output-protection-ex.md)                             | Holds information about an output protection technology. This structure extends **DRM\_OUTPUT\_PROTECTION** by adding a version number.                     |
| [**DRM\_PLAY\_OPL**](drmdrm-play-opl.md)                                                   | Holds information about the OPLs specified in a license for play actions.                                                                                   |
| [**DRM\_PLAY\_OPL\_EX**](drm-play-opl-ex.md)                                               | Holds extended information about the OPLs specified in a license for play actions.                                                                          |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS**](drmdrm-video-output-protection-ids.md)           | Holds an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures.                                                                                            |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS\_EX**](drm-video-output-protection-ids-ex.md)       | Holds an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures. This structure extends **DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS** by adding a version number. |
| [**WM\_BACKUP\_RESTORE\_STATUS**](wm-backup-restore-status.md)                             | Holds information about a pending license backup or restore operation.                                                                                      |
| [**WM\_INDIVIDUALIZE\_STATUS**](drmwm-individualize-status.md)                             | Holds information about a pending individualization process.                                                                                                |
| [**WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS**](wmdrm-analog-video-restrictions.md)               | Holds information about a restriction for playing back content as analog video.                                                                             |
| [**WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS\_EX**](wmdrm-analog-video-restrictions-ex.md)        | Holds extended information about a restriction for playing back content as analog video.                                                                    |
| [**WMDRM\_ENCRYPT\_SCATTER\_BLOCK**](wmdrm-encrypt-scatter-block.md)                       | Contains a block of data to be encrypted.                                                                                                                   |
| [**WMDRM\_ENCRYPT\_SCATTER\_INFO**](wmdrm-encrypt-scatter-info.md)                         | Contains information needed to configure the [**IWMDRMEncryptScatter**](iwmdrmencryptscatter.md) interface for use.                                        |
| [**WMDRM\_LICENSE\_FILTER**](wmdrm-license-filter.md)                                      | Contains filtering information for creating license enumerations.                                                                                           |
| [**WMDRM\_OUTPUT\_PROTECTION\_LEVELS**](wmdrm-output-protection-levels.md)                 | Contains the output protections levels required by a license to perform various actions.                                                                    |
| [**WMDRMCryptoData**](wmdrmcryptodata.md)                                                  | Contains information about the cryptographic algorithm used to encrypt and decrypt content.                                                                 |
| [**WMDRMNET\_POLICY**](wmdrmnet-policy.md)                                                 | Contains the policy to be used for Windows Media DRM for Network Devices operations.                                                                        |
| [**WMDRMNET\_POLICY\_GLOBAL\_REQUIREMENTS**](wmdrmnet-policy-global-requirements.md)       | Holds global requirements for Windows Media DRM for Network Devices.                                                                                        |
| [**WMDRMNET\_POLICY\_MINIMUM\_ENVIRONMENT**](wmdrmnet-policy-minimum-environment.md)       | Contains the minimum security requirements for Windows Media DRM for Network Devices.                                                                       |
| [**WMDRMNET\_POLICY\_TRANSCRYPTPLAY**](wmdrmnet-policy-transcryptplay.md)                  | Holds the policy information for playing content using Windows Media DRM for Network Devices.                                                               |



 

## Related topics

<dl> <dt>

[**Programming Reference**](drm-programming-reference.md)
</dt> </dl>

 

 




