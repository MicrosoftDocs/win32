---
title: DRM Properties
description: DRM Properties
ms.assetid: 862fc8bc-6e40-4496-862a-c12c8a382116
keywords:
- Windows Media Format SDK,DRM properties
- Advanced Systems Format (ASF),DRM properties
- ASF (Advanced Systems Format),DRM properties
- digital rights management (DRM),properties
- DRM (digital rights management),properties
ms.topic: article
ms.date: 05/31/2018
---

# DRM Properties

The following table lists DRM properties that applications can get or set when writing or reading protected files. These properties are not file attributes; they are not written to the ASF file header.



| DRM Property                                                                             | Global Identifier                               | Data Type             |
|------------------------------------------------------------------------------------------|-------------------------------------------------|-----------------------|
| [**DRM\_ActionAllowed**](drm-actionallowed.md)                                          | g\_wszWMDRM\_ActionAllowed                      | **WMT\_TYPE\_BOOL**   |
| [**DRM\_ActionAllowed\_Backup**](drm-actionallowed-backup.md)                           | g\_wszWMDRM\_ActionAllowed\_Backup              | **WMT\_TYPE\_BOOL**   |
| [**DRM\_ActionAllowed\_CollaborativePlay**](drm-actionallowed-collaborativeplay.md)     | g\_wszWMDRM\_ActionAllowed\_CollaborativePlay   | **WMT\_TYPE\_BOOL**   |
| [**DRM\_ActionAllowed\_Copy**](drm-actionallowed-copy.md)                               | g\_wszWMDRM\_ActionAllowed\_Copy                | **WMT\_TYPE\_BOOL**   |
| [**DRM\_ActionAllowed\_CopyToCD**](drm-actionallowed-copytocd.md)                       | g\_wszWMDRM\_ActionAllowed\_CopyToCD            | **WMT\_TYPE\_BOOL**   |
| [**DRM\_ActionAllowed\_CopyToNonSDMIDevice**](drm-actionallowed-copytononsdmidevice.md) | g\_wszWMDRM\_ActionAllowed\_CopyToNonSDMIDevice | **WMT\_TYPE\_BOOL**   |
| [**DRM\_ActionAllowed\_CopyToSDMIDevice**](drm-actionallowed-copytosdmidevice.md)       | g\_wszWMDRM\_ActionAllowed\_CopyToSDMIDevice    | **WMT\_TYPE\_BOOL**   |
| [**DRM\_ActionAllowed\_Playback**](drm-actionallowed-playback.md)                       | g\_wszWMDRM\_ActionAllowed\_Playback            | **WMT\_TYPE\_BOOL**   |
| [**DRM\_ActionAllowed\_PlaylistBurn**](drm-actionallowed-playlistburn.md)               | g\_wszWMDRM\_ActionAllowed\_PlaylistBurn        | **WMT\_TYPE\_BOOL**   |
| [**DRM\_BaseLicenseAcqURL**](drm-baselicenseacqurl.md)                                  | g\_wszWMDRM\_BaseLicenseAcqURL                  | **WMT\_TYPE\_STRING** |
| [**DRM\_Flags**](drm-flags.md)                                                          | g\_wszWMDRM\_Flags                              | **WMT\_TYPE\_DWORD**  |
| [**DRM\_HeaderSignPrivKey**](drm-headersignprivkey.md)                                  | g\_wszWMDRM\_HeaderSignPrivKey                  | **WMT\_TYPE\_STRING** |
| [**DRM\_IsDRM**](drm-isdrm.md)                                                          | g\_wszIsDRM                                     | **WMT\_TYPE\_BOOL**   |
| [**DRM\_IsDRMCached**](drm-isdrmcached.md)                                              | g\_wszIsDRMCached                               | **WMT\_TYPE\_BOOL**   |
| [**DRM\_KeySeed**](drm-keyseed.md)                                                      | g\_wszWMDRM\_KeySeed                            | **WMT\_TYPE\_STRING** |
| [**DRM\_Level**](drm-level.md)                                                          | g\_wszWMDRM\_Level                              | **WMT\_TYPE\_DWORD**  |
| [**DRM\_LicenseID**](drm-licenseid.md)                                                  | g\_wszWMDRM\_LicenseID                          | **WMT\_TYPE\_STRING** |
| [**DRM\_LicenseState**](drm-licensestate.md)                                            | g\_wszWMDRM\_LicenseState                       | **WMT\_TYPE\_DWORD**  |
| [**DRM\_LicenseState\_CollaborativePlay**](drm-licensestate-collaborativeplay.md)       | g\_wszWMDRM\_LicenseState\_CollaborativePlay    | **WMT\_TYPE\_BINARY** |
| [**DRM\_LicenseState\_Copy**](drm-licensestate-copy.md)                                 | g\_wszWMDRM\_LicenseState\_Copy                 | **WMT\_TYPE\_BINARY** |
| [**DRM\_LicenseState\_CopyToCD**](drm-licensestate-copytocd.md)                         | g\_wszWMDRM\_LicenseState\_CopyToCD             | **WMT\_TYPE\_BINARY** |
| [**DRM\_LicenseState\_CopyToSDMIDevice**](drm-licensestate-copytosdmidevice.md)         | g\_wszWMDRM\_LicenseState\_CopyToSDMIDevice     | **WMT\_TYPE\_BINARY** |
| [**DRM\_LicenseState\_CopyToNonSDMIDevice**](drm-licensestate-copytononsdmidevice.md)   | g\_wszWMDRM\_LicenseState\_CopyToNonSDMIDevice  | **WMT\_TYPE\_BINARY** |
| [**DRM\_LicenseState\_Playback**](drm-licensestate-playback.md)                         | g\_wszWMDRM\_LicenseState\_Playback             | **WMT\_TYPE\_BINARY** |
| [**DRM\_LicenseState\_PlaylistBurn**](drm-licensestate-playlistburn.md)                 | g\_wszWMDRM\_LicenseState\_PlaylistBurn         | **WMT\_TYPE\_BINARY** |
| [**DRM\_Rights**](drm-rights.md)                                                        | g\_wszWMDRM\_Rights                             | **WMT\_TYPE\_STRING** |
| [**DRM\_SAPLEVEL**](drm-saplevel--deprecated.md)                                        | g\_wszWMDRM\_SAPLEVEL                           | **WMT\_TYPE\_STRING** |
| [**Use\_Advanced\_DRM**](use-advanced-drm.md)                                           | g\_wszWMUse\_Advanced\_DRM                      | **WMT\_TYPE\_BOOL**   |
| [**Use\_DRM**](use-drm.md)                                                              | g\_wszWMUse\_DRM                                | **WMT\_TYPE\_BOOL**   |
| [**WMDRMNET\_Revocation**](wmdrmnet-revocation.md)                                      | g\_wszWMDRMNET\_Revocation                      | **WMT\_TYPE\_STRING** |



 

## Related topics

<dl> <dt>

[**DRM Attribute List**](drm-attribute-list.md)
</dt> </dl>

 

 




