---
title: Default Tuning Spaces
description: This topic lists the default tuning spaces that were introduced in Windows 7.
ms.assetid: 627e8aaf-7638-4d17-97b5-0aeaad304b98
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Default Tuning Spaces

This topic lists the default tuning spaces that were introduced in Windows 7. These tuning spaces are persisted in the registry with the properties shown in the following tables. Use the [SystemTuningSpaces](systemtuningspaces-object.md) object to access or modify these tuning spaces, or to add a new tuning space.

The default country/region code in these tuning spaces is for the region that includes Canada, the United States, and parts of the Caribbean. The country/region code in the tuning space must correspond to the region setting in the host system. See [Frequency Tables](https://msdn.microsoft.com/library/windows/desktop/dd375810) for a list of country/region codes.

-   [ATSC Cable](#atsc-cable)
-   [ATSC Cable Default Locator](#atsc-cable-default-locator)
-   [Digital Cable](#digital-cable)
-   [Digital Cable Default Locator](#digital-cable-default-locator)
-   [DVB-S](#dvb-s-default-locator)
-   [DVB-S Default Locator](#dvb-s-default-locator)
-   [DVB-T](#dvb-t-default-locator)
-   [DVB-T Default Locator](#dvb-t-default-locator)
-   [FM Radio](#fm-radio)
-   [ISDB-S](#isdb-s-default-locator)
-   [ISDB-S Default Locator](#isdb-s-default-locator)
-   [ISDB-T](#isdb-t-default-locator)
-   [ISDB-T Default Locator](#isdb-t-default-locator)
-   [Related topics](#related-topics)

## ATSC Cable



| Property                 | Value                                  |
|--------------------------|----------------------------------------|
| CLSID                    | {A2E30750-6C3D-11D3-B653-00C04F79498E} |
| Country/region           | 0x00000000                             |
| Description              | Local ATSC Digital Cable               |
| Input type               | 0x00000000                             |
| Maximum channel          | 0x00000063                             |
| Maximum minor channel    | 0x000003e7                             |
| Maximum physical channel | 0x0000009e                             |
| Minimum channel          | 0x00000001                             |
| Minimum minor channel    | 0x00000000                             |
| Minimum physical channel | 0x00000001                             |
| Name                     | ATSCCable                              |
| Network type             | {0DAD2FDD-5FD7-11D3-8F50-00C04F7971E2} |



 

## ATSC Cable Default Locator



| Property            | Value                                  |
|---------------------|----------------------------------------|
| CLSID               | {8872FF1B-98FA-4D7A-8D93-C9F1055F85BB} |
| Frequency           | 0xFFFFFFFF                             |
| Inner FEC method    | 0xFFFFFFFF                             |
| Inner FEC rate      | 0xFFFFFFFF                             |
| Modulation type     | 0x00000007                             |
| Outer FEC method    | 0xFFFFFFFF                             |
| Outer FEC rate      | 0xFFFFFFFF                             |
| Physical channel    | 0xFFFFFFFF                             |
| Program number      | 0xFFFFFFFF                             |
| Symbol rate         | 0xFFFFFFFF                             |
| Transport stream ID | 0xFFFFFFFF                             |



 

## Digital Cable



| Property                 | Value                                  |
|--------------------------|----------------------------------------|
| CLSID                    | {D9BB4CEE-B87A-47F1-AC92-B08D9C7813FC} |
| Country/region           | 0x00000000                             |
| Description              | Local Digital Cable                    |
| Input type               | 0x00000000                             |
| Maximum channel          | 0x0000270f                             |
| Maximum major channel    | 0x00000063                             |
| Maximum minor channel    | 0x000003e7                             |
| Maximum physical channel | 0x0000009e                             |
| Maximum source ID        | 0x7FFFFFFF                             |
| Minimum channel          | 0x00000002                             |
| Minimum major channel    | 0x00000001                             |
| Minimum minor channel    | 0x00000000                             |
| Minimum physical channel | 0x00000002                             |
| Minimum source ID        | 0x00000000                             |
| Name                     | Digital Cable                          |
| Network type             | {143827AB-F77B-498d-81CA-5A007AEC28BF} |



 

## Digital Cable Default Locator



| Property            | Value                                  |
|---------------------|----------------------------------------|
| CLSID               | {03C06416-D127-407A-AB4C-FDD279ABBE5D} |
| Frequency           | 0xFFFFFFFF                             |
| Inner FEC method    | 0xFFFFFFFF                             |
| Inner FEC rate      | 0xFFFFFFFF                             |
| Modulation type     | 0xFFFFFFFF                             |
| Outer FEC method    | 0xFFFFFFFF                             |
| Outer FEC rate      | 0xFFFFFFFF                             |
| Symbol rate         | 0xFFFFFFFF                             |
| Transport stream ID | 0xFFFFFFFF                             |
| Physical Channel    | 0xFFFFFFFF                             |
| Program number      | 0xFFFFFFFF                             |



 

## DVB-S



| Property                  | Value                                  |
|---------------------------|----------------------------------------|
| CLSID                     | {B64016F3-C9A2-4066-96F0-BD9563314726} |
| Description               | Default Digital DVB-S Tuning Space     |
| High oscillator frequency | 0x00a1be40                             |
| LNB switch frequency      | 0x00b28720                             |
| Low oscillator frequency  | 0x0094c5f0                             |
| Name                      | DVB-S                                  |
| Network ID                | 0xFFFFFFFF                             |
| Network type              | {FA4B375A-45B4-4D45-8440-263957B11623} |
| Spectral inversion        | 0xFFFFFFFF                             |
| System type               | 0x00000002                             |



 

## DVB-S Default Locator



| Property         | Value                                  |
|------------------|----------------------------------------|
| Azimuth          | 0xFFFFFFFF                             |
| CLSID            | {1DF7D126-4050-47F0-A7CF-4C4CA9241333} |
| Elevation        | 0xFFFFFFFF                             |
| Frequency        | 0xFFFFFFFF                             |
| Inner FEC method | 0xFFFFFFFF                             |
| Inner FEC rate   | 0xFFFFFFFF                             |
| Modulation type  | 0xFFFFFFFF                             |
| Orbital position | 0xFFFFFFFF                             |
| Outer FEC method | 0xFFFFFFFF                             |
| Outer FEC rate   | 0xFFFFFFFF                             |
| Polarisation     | 0xFFFFFFFF                             |
| Symbol rate      | 0xFFFFFFFF                             |
| West position    | 0x00000000                             |



 

## DVB-T



| Property     | Value                                  |
|--------------|----------------------------------------|
| CLSID        | {C6B14B32-76AA-4A86-A7AC-5C79AAF58DA7} |
| Description  | Local DVB-T Digital Antenna            |
| Name         | DVB-T                                  |
| Network ID   | 0x00000000                             |
| Network type | {216C62DF-6D7F-4e9a-8571-05F14EDB766A} |
| System type  | 0x00000001                             |



 

## DVB-T Default Locator



| Property               | Value                                  |
|------------------------|----------------------------------------|
| Bandwidth              | 0xFFFFFFFF                             |
| CLSID                  | {EFE3FA02-45D7-4920-BE96-53FA7F35B0E6} |
| Frequency              | 0xFFFFFFFF                             |
| Guard interval         | 0xFFFFFFFF                             |
| Hierarchy alpha        | 0xFFFFFFFF                             |
| Inner FEC method       | 0xFFFFFFFF                             |
| Inner FEC rate         | 0xFFFFFFFF                             |
| LP inner FEC method    | 0xFFFFFFFF                             |
| LP inner FEC rate      | 0xFFFFFFFF                             |
| Modulation type        | 0xFFFFFFFF                             |
| Other frequency in use | 0xFFFFFFFF                             |
| Outer FEC method       | 0xFFFFFFFF                             |
| Outer FEC rate         | 0xFFFFFFFF                             |
| Physical layer pipe ID | 0xFFFFFFFF                             |
| Symbol rate            | 0xFFFFFFFF                             |
| Transmission mode      | 0xFFFFFFFF                             |



 

## FM Radio



| Property          | Value                                  |
|-------------------|----------------------------------------|
| CLSID             | {8A674B4C-1F63-11D3-B64C-00C04F79498E} |
| Country/region    | 0x00000001                             |
| Description       | Local Analog FM Radio                  |
| Maximum frequency | 0x066e6c60                             |
| Minimum frequency | 0x05404ca0                             |
| Name              | FM Radio                               |
| Network type      | {00000000-0000-0000-0000-000000000000} |
| Step              | 0x00030d40                             |



 

## ISDB-S



| Property                  | Value                                  |
|---------------------------|----------------------------------------|
| CLSID                     | {B64016F3-C9A2-4066-96F0-BD9563314726} |
| Description               | Default Digital ISDB-S Tuning Space    |
| High oscillator frequency | 0xFFFFFFFF                             |
| LNB switch frequency      | 0xFFFFFFFF                             |
| Low oscillator frequency  | 0xFFFFFFFF                             |
| Name                      | ISDB-S                                 |
| Network ID                | 0xFFFFFFFF                             |
| Network type              | {B0A4E6A0-6A1A-4B83-BB5B-903E1D90E6B6} |
| Spectral inversion        | 0xFFFFFFFF                             |
| System type               | 0x00000004                             |



 

## ISDB-S Default Locator



| Property         | Value                                  |
|------------------|----------------------------------------|
| Azimuth          | 0xFFFFFFFF                             |
| CLSID            | {6504AFED-A629-455C-A7F1-04964DEA5CC4} |
| Elevation        | 0xFFFFFFFF                             |
| Frequency        | 0xFFFFFFFF                             |
| Inner FEC method | 0xFFFFFFFF                             |
| Inner FEC rate   | 0xFFFFFFFF                             |
| Modulation type  | 0xFFFFFFFF                             |
| Orbital position | 0xFFFFFFFF                             |
| Outer FEC method | 0xFFFFFFFF                             |
| Outer FEC rate   | 0xFFFFFFFF                             |
| Polarisation     | 0xFFFFFFFF                             |
| Symbol rate      | 0xFFFFFFFF                             |
| West position    | 0xFFFFFFFF                             |



 

## ISDB-T



| Property     | Value                                  |
|--------------|----------------------------------------|
| CLSID        | {C6B14B32-76AA-4A86-A7AC-5C79AAF58DA7} |
| Description  | Local ISDB-T Digital Antenna           |
| Name         | ISDB-T                                 |
| Network ID   | 0xFFFFFFFF                             |
| Network type | {95037F6F-3AC7-4452-B6C4-45A9CE9292A2} |
| System type  | 0x00000003                             |



 

## ISDB-T Default Locator



| Property               | Value                                  |
|------------------------|----------------------------------------|
| Bandwidth              | 0xFFFFFFFF                             |
| CLSID                  | {9CD64701-BDF3-4D14-8E03-F12983D86664} |
| Frequency              | 0xFFFFFFFF                             |
| Guard interval         | 0xFFFFFFFF                             |
| Hierarchy alpha        | 0xFFFFFFFF                             |
| Inner FEC method       | 0xFFFFFFFF                             |
| Inner FEC rate         | 0xFFFFFFFF                             |
| LP inner FEC method    | 0xFFFFFFFF                             |
| LP inner FEC rate      | 0xFFFFFFFF                             |
| Modulation type        | 0xFFFFFFFF                             |
| Other frequency in use | 0xFFFFFFFF                             |
| Outer FEC method       | 0xFFFFFFFF                             |
| Outer FEC rate         | 0xFFFFFFFF                             |
| Symbol rate            | 0xFFFFFFFF                             |
| Transmission mode      | 0xFFFFFFFF                             |



 

## Related topics

<dl> <dt>

[Default Tuning Spaces (Legacy)](default-tuning-spaces--legacy-.md)
</dt> <dt>

[The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md)
</dt> </dl>

 

 




