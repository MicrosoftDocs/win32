---
title: Default Tuning Spaces (Legacy)
description: This topic lists the default tuning spaces that were introduced in Windows XP. The same tuning spaces are also provided with DirectX 9.0.
ms.assetid: '24e3c32f-50c6-4e45-aed6-1727c99a5dc2'
---

# Default Tuning Spaces (Legacy)

This topic lists the default tuning spaces that were introduced in Windows XP. The same tuning spaces are also provided with DirectX 9.0.

> [!Note]  
> Starting in Windows 7, a new set of default tuning spaces is provided. See [Default Tuning Spaces](default-tuning-spaces.md).

 

## Local Analog Cable



| Property            | Value                                                                       |
|---------------------|-----------------------------------------------------------------------------|
| CLSID               | CLSID\_AnalogTVTuningSpace{8A674B4D-1F63-11D3-B64C-00C04F79498E}<br/> |
| Unique Name         | Cable                                                                       |
| Friendly Name       | Local Analog Cable                                                          |
| Network Type        | ANALOG\_TV\_NETWORK\_TYPE{B820D87E-E0E3-478f-8A38-4E13F7B3DF42}<br/>  |
| Minimum Channel     | 0x01                                                                        |
| Maximum Channel     | 0x9E                                                                        |
| Input Type          | 0x0 (Cable)                                                                 |
| Country/Region Code | 0x01                                                                        |



 

## Local Analog Antenna



| Property            | Value                                                                       |
|---------------------|-----------------------------------------------------------------------------|
| CLSID               | CLSID\_AnalogTVTuningSpace{8A674B4D-1F63-11D3-B64C-00C04F79498E}<br/> |
| Unique Name         | Antenna                                                                     |
| Friendly Name       | Local Analog Antenna                                                        |
| Network Type        | ANALOG\_TV\_NETWORK\_TYPE{B820D87E-E0E3-478f-8A38-4E13F7B3DF42}<br/>  |
| Minimum Channel     | 0x02                                                                        |
| Maximum Channel     | 0x45                                                                        |
| Input Type          | 0x1 (Antenna)                                                               |
| Country/Region Code | 0x01                                                                        |



 

## ATSC Digital Antenna



| Property                 | Value                                                                       |
|--------------------------|-----------------------------------------------------------------------------|
| CLSID                    | CLSID\_ATSCTuningSpace{A2E30750-6C3D-11D3-B653-00C04F79498E}<br/>     |
| Unique Name              | ATSC                                                                        |
| Friendly Name            | Local ATSC Digital Antenna                                                  |
| Network Type             | CLSID\_ATSCNetworkProvider{0DAD2FDD-5FD7-11D3-8F50-00C04F7971E2}<br/> |
| Minimum Channel          | 0x01                                                                        |
| Maximum Channel          | 0x63                                                                        |
| Input Type               | 0x0 (Cable)                                                                 |
| Country/Region Code      | 0x00                                                                        |
| Minimum Minor Channel    | 0x00                                                                        |
| Maximum Minor Channel    | 0x03E7                                                                      |
| Minimum Physical Channel | 0x02                                                                        |
| Maximum Physical Channel | 0x9E                                                                        |



 

## Default Locator for ATSC Digital Antenna



| Property            | Value                                                               |
|---------------------|---------------------------------------------------------------------|
| CLSID               | CLSID\_ATSCLocator{8872FF1B-98FA-4D7A-8D93-C9F1055F85BB}<br/> |
| Frequency           | 0xFFFFFFFF (-1)                                                     |
| Inner FEC Method    | 0xFFFFFFFF (-1)                                                     |
| Inner FEC Rate      | 0xFFFFFFFF (-1)                                                     |
| Outer FEC Method    | 0xFFFFFFFF (-1)                                                     |
| Outer FEC Rate      | 0xFFFFFFFF (-1)                                                     |
| ModulationType      | 0x7                                                                 |
| Symbol Rate         | 0xFFFFFFFF (-1)                                                     |
| Physical Channel    | 0xFFFFFFFF (-1)                                                     |
| Transport Stream ID | 0xFFFFFFFF (-1)                                                     |
| Program Number      | 0xFFFFFFFF (-1)                                                     |



 

## Local ATSC-style Digital Cable

> [!Note]  
> Currently not supported.

 



| Property                 | Value                                                                          |
|--------------------------|--------------------------------------------------------------------------------|
| CLSID                    | CLSID\_ATSCTuningSpace{A2E30750-6C3D-11D3-B653-00C04F79498E}<br/>        |
| Unique Name              | Digital Cable                                                                  |
| Friendly Name            | Local ATSC-Style Digital Cable                                                 |
| Network Type             | DIGITAL\_CABLE\_NETWORK\_TYPE{143827AB-F77B-498d-81CA-5A007AEC28BF}<br/> |
| Minimum Channel          | 0x02                                                                           |
| MaximumChannel           | 0x3E7                                                                          |
| Input Type               | 0x0 (Cable)                                                                    |
| Country/Region Code      | 0x00                                                                           |
| Minimum Minor Channel    | 0x00                                                                           |
| Maximum Minor Channel    | 0x03E7                                                                         |
| Minimum Physical Channel | 0x02                                                                           |
| Maximum Physical Channel | 0x03E7                                                                         |



 

## Analog Auxiliary Input



| Property      | Value                                                                         |
|---------------|-------------------------------------------------------------------------------|
| CLSID         | CLSID\_AuxInTuningSpace{F9769A06-7ACA-4e39-9CFB-97BB35F0E77E}<br/>      |
| Unique Name   | AuxIn1                                                                        |
| Friendly Name | Analog Auxiliary Input \#1                                                    |
| Network Type  | ANALOG\_AUXIN\_NETWORK\_TYPE{742EF867-09E1-40A3-82D3-9669BA35325F}<br/> |



 

## Related topics

<dl> <dt>

[Default Tuning Spaces](default-tuning-spaces.md)
</dt> <dt>

[The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md)
</dt> </dl>

 

 





